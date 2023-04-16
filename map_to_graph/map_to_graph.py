import inspect
import math
import os

import networkx as nx
import osmnx as ox
import grinpy as gp


def map_to_graph_from_point(lst, key=None, plot=False, dist=None):
    x = lst[0]
    y = lst[1]
    if dist is not None:
        dist = dist
    else:
        dist = lst[2]

    ox.config(use_cache=True, log_console=False)

    if key is not None:
        filepath = "graph_" + key + "_" + str(dist)
    else:
        filepath = "graph_" + str(x) + "_" + str(y) + "_" + str(dist)

    if os.path.exists("./map/" + filepath):

        G = ox.load_graphml("./map/" + filepath)

    else:

        G = ox.graph_from_point((x, y), dist=dist, network_type="drive", retain_all=False)
        ox.save_graphml(G, filepath="./map/" + filepath)

    if plot == True:
        plotting_graph(G)

    return G


def map_to_graph_from_bbox(lst, key=None, plot=False):
    dist = lst[3]
    ox.config(use_cache=True, log_console=False)

    if key is not None:
        filepath = "graph_" + key + "_" + str(dist)
    else:
        filepath = "graph_" + str(lst[0]) + "_" + str(lst[1]) + "_" + str(lst[2]) + "_" + str(dist)

    if os.path.exists("./map/" + filepath):

        G = ox.load_graphml("./map/" + filepath)
    else:

        G = ox.graph_from_bbox(lst[0], lst[1], lst[2], lst[3], network_type="drive", retain_all=False)

        ox.save_graphml(G, filepath="./map/" + filepath)

    if plot == True:
        plotting_graph(G)
    return G


def plotting_graph(G):
    fig, ax = ox.plot_graph(G, bgcolor="k", node_color="#FFFFFF", edge_color="#333333", node_size=20, edge_linewidth=2)


def get_adjacency_matrix(G):
    G_un = G.to_undirected()
    a = nx.adjacency_matrix(G_un)
    print(a.todense())


def get_diameter(G):
    G_un = G.to_undirected()
    diam = nx.diameter(G_un)
    print(diam)
    return diam


def get_radius(G):
    G_un = G.to_undirected()
    rad = nx.radius(G_un)
    print(rad)
    return rad


def get_average_shortest_path_length(G):
    G_un = G.to_undirected()
    avg = nx.average_shortest_path_length(G_un)
    print(avg)
    return avg


def get_independence_number(G):
    G_un = G.to_undirected()
    ind = len(nx.maximal_independent_set(G_un))
    return ind


def get_average_degree(G):
    G_un = G.to_undirected()
    deg = nx.average_degree_connectivity(G_un)
    print(deg)
    return deg


def get_irregularity(G):
    G_un = G.to_undirected()
    irr = gp.irregularity(G_un)
    print(irr)
    return irr


def get_degree_sequence(G):
    G_un = G.to_undirected()
    deg = sorted([val for (node, val) in G_un.degree()])
    return deg

def get_surface(G):
    min_x = +1000000000
    max_x = -1000000000
    min_y = +1000000000
    max_y = -1000000000
    for e in list(G.nodes(data=True)):

        if e[1]["x"] < min_x:
            min_x = e[1]["x"]
        if e[1]["x"] > max_x:
            max_x = e[1]["x"]
        if e[1]["y"] < min_y:
            min_y = e[1]["y"]
        if e[1]["y"] > max_y:
            max_y = e[1]["y"]

    latitude = max_y - min_y
    longitude = max_x - min_x

    # latitude in km = 111 * latitude
    latitude_km = 111 * latitude

    # longitude in km = 111 * cos(latitude) * longitude
    longitude_km = 111 * math.cos(latitude) * longitude

    surface = latitude_km * longitude_km

    return surface



def find_angle(Ax, Ay, Bx, By, Cx, Cy):


    AB = math.sqrt(math.pow(Bx - Ax, 2) + math.pow(By - Ay, 2))

    BC = math.sqrt(math.pow(Bx - Cx, 2) + math.pow(By - Cy, 2))

    AC = math.sqrt(math.pow(Cx - Ax, 2) + math.pow(Cy - Ay, 2))

    if (BC * BC + AB * AB - AC * AC) / (2 * BC * AB) > 1 :
        return math.cos(1)
    if (BC * BC + AB * AB - AC * AC) / (2 * BC * AB) < -1 :
        return math.cos(-1)
    return math.acos((BC * BC + AB * AB - AC * AC) / (2 * BC * AB));
