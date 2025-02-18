#!/Users/Matt/.pyenv/versions/3.10.2/envs/WebsiteHelpers/bin/python3.10
import pathlib
import sqlite3
import itertools
import json
import sys
import re

import networkx as nx
import networkx.algorithms.link_analysis.pagerank_alg as pag
import networkx.algorithms.community as com
from networkx.drawing.nx_pydot import read_dot
from networkx.readwrite import json_graph


def to_rellink(inp: str) -> str:
    return pathlib.Path(inp).stem


def to_rellink_with_subnote(note_file: str, title: str, properties: str) -> str:
    mtch = re.search("\(\"ROAM_REFS\" \. \"cite:([a-zA-Z0-9]+)\"\)", properties)
    lnk = ""
    if mtch is not None:
        lnk += mtch.groups()[0]
    else:
        lnk += pathlib.Path(note_file).stem
        lnk += "#" + title.replace(' ', '-').replace('"', '').lower()
    return lnk


def get_sqlite_conn():
    home = pathlib.Path.home()
    conn = sqlite3.connect(home / ".emacs.d" / "org-roam.db")
    return conn


def get_nodes_from_conn(conn):
    nodes = conn.execute("SELECT file, id, title, properties FROM nodes "
                         "ORDER BY title ASC;")
    nds = [n for n in nodes]
    return nds


def create_node_div(n):

    lnk = to_rellink_with_subnote(n[0], n[2], n[3]).lower()
    
    label = n[2].strip("\"")
    html_str = "<li class=notes-item id=\"" + label.lower().replace(' ', '_')
    html_str += "\"> <a href=\"" + lnk + "\" title=\"" + label + "\">"
    html_str += "<div data-name=\"" + label
    html_str += "\" class=node-link>\n"

    html_str += "\t<h3>" + label + "</h3>"

    md_path = "content/braindump/" + pathlib.Path(n[0]).stem + ".md"

    category = regex_roam_category(n[3])
    add_tag = category != label.lower().replace(' ', '_') and category is not None

    html_str += "<div class=note-item-content>"
    if pathlib.Path(md_path).exists():
        with open(md_path, 'r') as file:
            lines = file.readlines()

            tags = []
            if 'tags\n' in lines:
                idx = lines.index('tags\n')
                tags = [tag.replace('[', '').replace(']', '')
                        for tag in re.findall("\[[a-zA-Z\s]*\]",
                                              lines[idx + 1])]
            if add_tag:
                tags.append(category.replace('_', ' ').title())
            if len(tags) > 0:
                html_str += ("<div class=note-tags-wrapper>"
                             "<h4>Tags: </h4> "
                             "<ul class=note-tags>")
                for t in tags:
                    html_str += "<li data-name=\"" + t + "\">" + t + "</li>"
                if html_str[-2:] == ", ":
                    html_str = html_str[0:-2]
                html_str += "</ul> </div>"

    aliases = regex_roam_aliases(n[3])
    if aliases is not None:
        html_str += ("\n"
                     "<div class=note-aliases-wrapper>"
                     "<h4>Aliases:</h4>"
                     "\n"
                     "\t<ul class=note-aliases>\n")
        for alias in aliases:
            html_str += "\t\t<li data-name=\"" + alias + "\">"
            html_str += alias + "</li>\n"
        html_str += "\t</ul> </div>\n"
    return html_str + "</div> </div> </a> </li>"


def regex_roam_category(nde_str):
    mtch = re.search("\(\"CATEGORY\" \. (\"[a-zA-Z_\"]+)\)",
                     nde_str.replace("\\", "").replace("\"\"", "\""))
    if mtch is None:
        return None
    return mtch.groups()[0].replace("\"", "")


def regex_roam_aliases(nde_str):
    mtch = re.search("\(\"ROAM_ALIASES\" \. (\"[a-zA-Z\s\"]+)\)",
                     nde_str.replace("\\", "").replace("\"\"", "\""))
    if mtch is None:
        return None
    aliases = mtch.groups()[0].split('" "')
    return [a.replace('"', '').replace('`', '').replace('\'', '') for a in aliases]


def build_list():
    conn = get_sqlite_conn()
    nds = get_nodes_from_conn(conn)

    nds_div = [create_node_div(n) for n in nds]

    conn.close()

    ret_str = "<ul id=notes-list>"
    for nds in nds_div:
        ret_str += nds + "\n"
    return ret_str


def build_graph() -> nx.DiGraph:
    """Build a graph from the org-roam database."""
    graph = nx.DiGraph()
    conn = get_sqlite_conn()

    # Query all nodes first
    nodes = conn.execute("SELECT file, id, title, properties FROM nodes;")
    # A double JOIN to get all nodes that are connected by a link
    links = conn.execute("SELECT n1.id, nodes.id FROM ((nodes AS n1) "
                         "JOIN links ON n1.id = links.source) "
                         "JOIN (nodes AS n2) ON links.dest = nodes.id "
                         "WHERE links.type = '\"id\"';")

    # Populate the graph
    graph.add_nodes_from((n[1], {
        "label": n[2].strip("\""),
        "tooltip": n[2].strip("\""),
        "lnk": to_rellink_with_subnote(n[0], n[2], n[3]).lower(),
        "id": n[1].strip("\"")
    }) for n in nodes)
    graph.add_edges_from(n for n in links if (n[0] in graph.nodes and
                                              n[1] in graph.nodes))

    nodes_2 = conn.execute("SELECT file, id, title, level FROM nodes;")
    for n in nodes_2:
        if n[3] != 0:
            nodes_3 = conn.execute("SELECT file, id, title, level "
                                   "FROM nodes "
                                   "WHERE file='{}' AND level=0;".format(n[0]))
            parent = [nd for nd in nodes_3][0]
            graph.add_edge(parent[1], n[1])
            graph.add_edge(n[1], parent[1])

    conn.close()
    return graph


N_COM = 7  # Desired number of communities
N_MISSING = 20  # Number of predicted missing links
MAX_NODES = 200  # Number of nodes in the final graph


def compute_centrality(dot_graph: nx.DiGraph) -> None:
    """Add a `centrality` attribute to each node with its PageRank score.
    """
    simp_graph = nx.Graph(dot_graph)
    central = pag.pagerank(simp_graph)
    min_cent = min(central.values())
    central = {i: central[i] - min_cent for i in central}
    max_cent = max(central.values())
    central = {i: central[i] / max_cent for i in central}
    nx.set_node_attributes(dot_graph, central, "centrality")
    sorted_cent = sorted(dot_graph,
                         key=lambda x: dot_graph.nodes[x]["centrality"])
    for n in sorted_cent[:-MAX_NODES]:
        dot_graph.remove_node(n)


def compute_communities(dot_graph: nx.DiGraph, n_com: int) -> None:
    """Add a `communityLabel` attribute to each node according to their
    computed community.
    """
    simp_graph = nx.Graph(dot_graph)
    communities = com.girvan_newman(simp_graph)
    labels = [tuple(sorted(c) for c in unities) for unities in
              itertools.islice(communities, n_com - 1, n_com)][0]
    label_dict = {l_key: i for i in range(len(labels)) for l_key in labels[i]}
    nx.set_node_attributes(dot_graph, label_dict, "communityLabel")


def add_missing_links(dot_graph: nx.DiGraph, n_missing: int) -> None:
    """Add some missing links to the graph by using top ranking inexisting
    links by ressource allocation index.
    """
    simp_graph = nx.Graph(dot_graph)
    preds = nx.ra_index_soundarajan_hopcroft(simp_graph,
                                             community="communityLabel")
    new = sorted(preds, key=lambda x: -x[2])[:n_missing]
    for link in new:
        sys.stderr.write(f"Predicted edge {link[0]} {link[1]}\n")
        dot_graph.add_edge(link[0], link[1], predicted=link[2])


if __name__ == "__main__":
    sys.stderr.write("Re-creating notes-list page\n")
    lst = build_list()
    with open("layouts/partials/notes_list.html", "w") as file:
        file.write(lst)
    sys.stderr.write("Re-creating notes-graph\n")
    DOT_GRAPH = build_graph()
    compute_centrality(DOT_GRAPH)
    compute_communities(DOT_GRAPH, N_COM)
    add_missing_links(DOT_GRAPH, N_MISSING)
    JS_GRAPH = json_graph.node_link_data(DOT_GRAPH)
    with open("static/js/notes_graph.json", "w") as file:
        file.write(json.dumps(JS_GRAPH))

# if __name__ == "__main__":
#     sys.stderr.write("Reading graph...")
#     DOT_GRAPH = build_graph()
#     compute_centrality(DOT_GRAPH)
#     compute_communities(DOT_GRAPH, N_COM)
#     add_missing_links(DOT_GRAPH, N_MISSING)
#     sys.stderr.write("Done\n")
#     JS_GRAPH = json_graph.node_link_data(DOT_GRAPH)
#     sys.stdout.write(json.dumps(JS_GRAPH))
