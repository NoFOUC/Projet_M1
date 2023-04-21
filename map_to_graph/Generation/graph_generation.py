import random
from dataclasses import dataclass
from typing import Annotated, List, Tuple

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def fct(x, a, b):
    """
    Function exponential to fit the degree distribution of the graph between 3 and +inf
    """

    return a * np.exp(-b * x)


def cumul(x, a, b):
    """
    Cumulative function of the exponential function fct
    """

    return 1 - fct(x, a, b)


def inverse(r, a, b):
    """
    Inverse of the cumulative function of the exponential function fct
    """

    return int(-np.log(-(r - 1) / a) / b)


def is_corner(i, j, side):
    """
    Check if the node is a corner
    """

    if i == 0 and j == 0:
        return [0, 0]
    elif i == 0 and j == side - 1:
        return [0, side - 1]
    elif i == side - 1 and j == 0:
        return [side - 1, 0]
    elif i == side - 1 and j == side - 1:
        return [side - 1, side - 1]
    else:
        return False


def is_border(i, j, side):
    """
    Check if the node is a border
    """

    if i == 0:
        return [0, j]
    elif i == side - 1:
        return [side - 1, j]
    elif j == 0:
        return [i, 0]
    elif j == side - 1:
        return [i, side - 1]
    else:
        return False


def position_in_adj(pos, side):
    """
    give the position of the node in the adjacency matrix in function of the position of the node in the graph

    Return
    ------
    :return the position of the node in the adjacency matrix
    """

    return pos[0] * side + pos[1]


def position_from_adj(pos, side):
    """
    give the position of the node in the graph in function of the position of the node in the adjacency matrix
    """

    i = pos // side
    j = pos % side
    return [i, j]


def get_up_left(i, j):
    """
    give the position of up-left node
    """

    return [i - 1, j - 1]


def get_up(i, j):
    """
    give the position of up node
    """

    return [i - 1, j]


def get_up_right(i, j):
    """
    give the position of up-right node
    """

    return [i - 1, j + 1]


def get_right(i, j):
    """
    give the position of right node
    """

    return [i, j + 1]


def get_down_right(i, j):
    """
    give the position of down-right node
    """
    return [i + 1, j + 1]


def get_down(i, j):
    """
    give the position of down node
    """

    return [i + 1, j]


def get_down_left(i, j):
    """
    give the position of down-left node
    """

    return [i + 1, j - 1]


def get_left(i, j):
    """
    give the position of left node
    """

    return [i, j - 1]


def add_edge(tab_adj, i, j, side, nbr_edge=2, usa=False):
    """

    Main Function to generate the graph
    Add a random number of edges for each node in the graph

    Parameters
    ----------
    :param tab_adj: matrix of adjacency
    :param i: position in abscisse of the node in the graph
    :param j: position in ordinate of the node in the graph
    :param side: size of the graph in number of nodes
    :param nbr_edge: number of edges to add for the node (i, j)
    :param usa: if True, the graph is a USA graph

    Returns
    -------
    :return: matrix of adjacency with the new edges

    """

    # dict with all the possible positions of edge for a node
    # up is not considered because it is already done in the previous node (i-1,j)
    possible_position = {"up-left": False, "up": False,
                         "up-right": False,
                         "right": get_right(i, j), "down-right": get_down_right(i, j),
                         "down": get_down(i, j),
                         "down-left": get_down_left(i, j), "left": get_left(i, j)}

    # number of possible position for the node (8 for a node in the middle of the graph) but 5 in reality
    # because the 3 up positions are already done in the previous node (i-1,j)
    poss_pos = {key for key in possible_position.keys() if possible_position[key]}

    # check if the node is on the up border of the graph (i=0)
    # if yes, remove the up-left, up and up-right positions
    # not necessary because the 3 up positions are already done in the previous node (i-1,j)
    # but it is a security to avoid errors
    if i == 0:
        if possible_position["up-left"]:
            possible_position["up-left"] = False
            poss_pos.remove("up-left")
        else:
            possible_position["up-left"] = False

        if possible_position["up"]:
            possible_position["up"] = False
            poss_pos.remove("up")
        else:
            possible_position["up"] = False

        if possible_position["up-right"]:
            possible_position["up-right"] = False
            poss_pos.remove("up-right")
        else:
            possible_position["up-right"] = False

    # check if the node is on the left border of the graph (j=0)
    # if yes, remove the up-left, left and down-left positions
    if j == 0:
        if possible_position["up-left"]:
            possible_position["up-left"] = False
            poss_pos.remove("up-left")
        else:
            possible_position["up-left"] = False

        if possible_position["left"]:
            possible_position["left"] = False
            poss_pos.remove("left")
        else:
            possible_position["left"] = False

        if possible_position["down-left"]:
            possible_position["down-left"] = False
            poss_pos.remove("down-left")
        else:
            possible_position["down-left"] = False

    # check if the node is on the down border of the graph (i=side-1)
    # if yes, remove the down-left, down and down-right positions
    if i == side - 1:

        if possible_position["down-left"]:
            possible_position["down-left"] = False
            poss_pos.remove("down-left")
        else:
            possible_position["down-left"] = False

        if possible_position["down"]:
            possible_position["down"] = False
            poss_pos.remove("down")
        else:
            possible_position["down"] = False

        if possible_position["down-right"]:
            possible_position["down-right"] = False
            poss_pos.remove("down-right")
        else:
            possible_position["down-right"] = False

    # check if the node is on the right border of the graph (j=side-1)
    # if yes, remove the up-right, right and down-right positions
    if j == side - 1:
        if possible_position["up-right"]:
            possible_position["up-right"] = False
            poss_pos.remove("up-right")
        else:
            possible_position["up-right"] = False

        if possible_position["right"]:
            possible_position["right"] = False
            poss_pos.remove("right")
        else:
            possible_position["right"] = False

        if possible_position["down-right"]:
            possible_position["down-right"] = False
            poss_pos.remove("down-right")
        else:
            possible_position["down-right"] = False

    # check all the possible positions still available
    # if the position is available, check if there is already an edge crossing the edge
    # if yes, remove the position from the possible positions to keep planarity
    for k in list(poss_pos):

        """
        If the possible position of the second node of the edge is (i-1,j-1), check if there is already 
        an edge crossing the edge (i-1,j) and (i,j-1)
        
        Our node is A and the edge we can have is AB but we can't have AB if there is already an edge YX
        |B| |Y|
           X
        |Z| |A|
        """
        if k == "up-left":
            if tab_adj[position_in_adj(possible_position["up"], side)][
                position_in_adj(possible_position["left"], side)] == 1:
                possible_position[k] = False
                poss_pos.remove(k)

        """
        If the possible position of the second node of the edge is (i-1,j+1), check if there is already
        an edge crossing the edge (i+1,j) and (i,j-1)
        
        Our node is A and the edge we can have is AB but we can't have AB if there is already an edge YX
        |Y| |B|
           X
        |A| |Z|
        """

        if k == "up-right":
            if tab_adj[position_in_adj(possible_position["up"], side)][
                position_in_adj(possible_position["right"], side)] == 1:
                possible_position[k] = False
                poss_pos.remove(k)

        """
        If the possible position of the second node of the edge is (i-1,j+1), check if there is already
        an edge crossing the edge (i-1,j) and (i,j+1)
        
        Our node is A and the edge we can have is AB but we can't have AB if there is already an edge YX
        |Z| |A|
           X
        |B| |Y|
        """
        if k == "down-left":
            if tab_adj[position_in_adj(possible_position["down"], side)][
                position_in_adj(possible_position["left"], side)] == 1:
                possible_position[k] = False
                poss_pos.remove(k)

        """
        If the possible position of the second node of the edge is (i+1,j+1), check if there is already
        an edge crossing the edge (i+1,j) and (i,j+1)
        
        Our node is A and the edge we can have is AB but we can't have AB if there is already an edge YX
        |A| |Z|
           X
        |Y| |B|
        """
        if k == "down-right":
            if tab_adj[position_in_adj(possible_position["down"], side)][
                position_in_adj(possible_position["right"], side)] == 1:
                possible_position[k] = False
                poss_pos.remove(k)

    # check if parameter usa is True
    # if yes, remove the down-left and down-right possible positions with 0.9% of probability
    # and add up position
    if usa == True:
        if np.random.rand(1)[0] < 0.9:

            if possible_position["down-left"]:
                possible_position["down-left"] = False
                poss_pos.remove("down-left")
            if possible_position["down-right"]:
                possible_position["down-right"] = False
                poss_pos.remove("down-right")

        if np.random.rand(1)[0] < 0.5:
            if get_up(i, j)[0] >= 0:
                if possible_position["up"] == False:
                    possible_position["up"] = get_up(i, j)
                    poss_pos.add("up")

            if get_down(i, j)[0] < side:
                if possible_position["down"] == False:
                    possible_position["down"] = get_down(i, j)
                    poss_pos.add("down")

    # check if there is already some edges to the node (i, j)
    # and substract the number of edges already present to the number of edges we want to add
    # if the number of edges we want to add is negative, set it to 0 (we have the number of edges we want)
    tot = nbr_edge
    if tab_adj[position_in_adj([i, j], side)].count(1) != 0:
        if nbr_edge - tab_adj[position_in_adj([i, j], side)].count(1) < 0:
            nbr_edge = 0
        else:
            nbr_edge = nbr_edge - tab_adj[position_in_adj([i, j], side)].count(1)

    # if the number of possible positions is lower than the number of edges we want to add
    # add all the possible positions to the graph
    if len(poss_pos) <= nbr_edge:
        for k in poss_pos:
            if possible_position[k]:
                tab_adj[position_in_adj(possible_position[k], side)][position_in_adj([i, j], side)] = 1
                tab_adj[position_in_adj([i, j], side)][position_in_adj(possible_position[k], side)] = 1

    # if the number of possible positions is higher than the number of edges we want to add and
    # the number of edges we want to add is not 0
    elif nbr_edge != 0:

        """
        COMPLEXITY PROBLEM HERE
        rand = list(mit.random_combination(range(len(poss_pos)), nbr_edge))
        corrected by changing poss_pos_count by poss_pos 
        """

        # create a copy of the possible positions set
        copy = poss_pos.copy()
        rand = []

        # use random choice to select the edges we want to add
        # not random.choices because we can have the same edge twice
        for w in range(nbr_edge):
            f = random.choice(list(copy))
            rand.append(f)
            copy.remove(f)

        # add the edges to the graph in the adjacency matrix in the 2 position (i,j) and (j,i)
        # because our graph is undirected

        for k in rand:
            if possible_position[k]:
                tab_adj[position_in_adj(possible_position[k], side)][position_in_adj([i, j], side)] = 1
                tab_adj[position_in_adj([i, j], side)][position_in_adj(possible_position[k], side)] = 1

        ## OLD CODE
        """temp = 0
        for k in possible_position.keys():
            if possible_position[k] != False:
                if len(rand) == 0:
                    break
                else:
                    if rand[0] == temp:
                        tab_adj[position_in_adj(possible_position[k], side)][position_in_adj([i, j], side)] = 1
                        tab_adj[position_in_adj([i, j], side)][position_in_adj(possible_position[k], side)] = 1

                        temp += 1
                        rand.pop(0)

                    else:
                        temp += 1
        """

    return tab_adj


def node_generation(tab_graph, tab_adj, side, funct_deg, pourc_2, pourc_0, usa=False):
    """

    Function that generate the graph with the right number of edges for each node

    Parameters
    ----------

    :param tab_graph: random number generated for each node
    :param tab_adj: matrix of adjacency
    :param side: size of the graph in number of nodes
    :param funct_deg: distribution of the degree of the nodes starting from 3
    :param pourc_2: pourcentage of edges with 2 degree
    :param pourc_0: pourcentage of edges with 0 degree
    :param usa: if True, the graph is a USA map

    Return
    ------

    :return: the adjacency matrix of the graph
    """

    temp = tab_adj

    # for each node in the graph add the edges we want and call add_edge function
    # use to have the right pourcentage of edges with 2 and 0 degree in the graph in accordance with the
    # value of the parameter pourc_2 and pourc_0
    for length in range(side):
        for width in range(side):

            print (str(length*side+width) + "/" + str(side*side))
            random_2 = np.random.rand(1)

            # if the random number is lower than the pourcentage of edges with 2 degree
            if random_2 < pourc_2:
                temp = add_edge(temp, length, width, side, nbr_edge=2, usa=usa)

            else:
                random_0 = np.random.rand(1)

                if random_0 < pourc_0:
                    continue  # no edge to add => no call to add_edge function

                # follow the distribution of the degree of the nodes
                else:
                    temp = add_edge(temp, length, width, side,
                                    nbr_edge=inverse(tab_graph[length][width], funct_deg[0], funct_deg[1]), usa=usa)

    return temp


@dataclass
class ValueRange:
    min: float
    max: float


def graph_generation(nbr_node: int = 4000,
                     funct_deg: Tuple[float, float] = [12.01009375101943, 0.9631486813699162],
                     pourc_2: Annotated[float, ValueRange(0.0, 1.0)] = 0.65,
                     pourc_0: Annotated[float, ValueRange(0.0, 1.0)] = 0.6,
                     noise: Annotated[float, ValueRange(0.0, 1.0)] = 1,
                     reduce_deg_1: int = 0,
                     usa: bool = False,
                     color: bool = True):
    """

    Generate the graph with the right number of nodes and edges

    Parameters
    ----------

    :param nbr_node: number of nodes in the graph
    :param funct_deg: distribution of the degree of the nodes starting from 3
    :param pourc_2: pourcentage of edges with 2 degree
    :param pourc_0: pourcentage of edges with 0 degree
    :param noise: noise to add to the position of the nodes
    :param reduce_deg_1: number of reduction of nodes of degree 1
    :param usa: if True, the graph is a USA map
    :param color: if True, the graph is colored

    Return
    ------

    :return: the graph with the right number of nodes and edges
    """

    """
    # real number of nodes in the graph is higher than the number of nodes we write in the parameter
    # because we want nodes of degree 2 (fake node) and nodes of degree 0 (no node)
    # we also want to have a square graph
    """

    # nbr of node with fake nodes and nodes of degree 0
    nbr_node = int((nbr_node * (1 + pourc_2)) * (1 + pourc_0)) * 2

    # nbr of nodes to have a square graph
    side = int(np.sqrt(nbr_node)) + 1

    # real number of nodes in the graph
    nbr_node = side * side

    print ("tab graph")
    # create a random tab of number between 0 and 1 to check the degree of the nodes in inverse function distribution
    tab_graph = np.random.rand(side, side)

    print ("done")

    print ("tab adj")
    # create the adjacency matrix
    tab_adj = [[0 for y in range(nbr_node)] for x in range(nbr_node)]


    print ("done")

    print ("test")
    test = np.zeros((nbr_node, nbr_node), int)
    print ("done")
    # create the graph

    print ("node gen")
    adj_mat = node_generation(tab_graph, tab_adj, side, funct_deg=funct_deg, pourc_2=pourc_2, pourc_0=pourc_0, usa=usa)

    print ("done")
    # create the dictionary of position of the nodes for networkx
    # if usa == True => no random position
    # else add noise to the position of the nodes

    print ("pos")
    dict_pos = {}
    for i in range(nbr_node):
        pos = position_from_adj(i, side)
        print (i + "/" + str(len(nbr_node)))
        if usa == True and noise == 1:
            dict_pos[i] = [pos[0] * 100, pos[1] * 100]
        else:
            dict_pos[i] = [(pos[0] + (np.random.rand(1)[0] - 0.5)) * 10000 * noise,
                           (pos[1] + (np.random.rand(1)[0] - 0.5)) * 10000 * noise]

    print ("done")
    """
    A FAIRE : 
    
    double dfs de gauche et droite pour chaque noeuds si degré = 2 , 
    on continue jusqu'à un noeuds de degré > 2 ou = 1 
    si les 2 sont >2 alors on relit le noeuds au noeuds à l'autre extrémité 
    si l'un des deux = 1 alors on supprime tout le segment car c'est un chemin sans issu
    si les 2 sont de degré 1 on supprime tout car ça veut dire que c'est une route sans issus des 2 cote donc 
    impossible d'y entrer 
    
    SI on retombe sur le meme noeuds de départ, alors on à une boucle = un circuit et on supprime aussi 
    
    ATTENTION il faut créer des segment avec des LINESTRIGHT avec type "geometry" 
    
    ça pourrait aussi detecter la plus grand composante connexe 
    
    """
    # ici code
    """for i in range(nbr_node):
        if adj_mat[i].count(1) == 2:

            segment = []
            i_1 = adj_mat[i].index(1)
            i_2 = adj_mat[i].index(1, i_1 + 1)

            adj_mat[i_1][i_2] = 1
            adj_mat[i_2][i_1] = 1

            adj_mat[i][i_1] = 0
            adj_mat[i][i_2] = 0

            print(i_1, i_2)"""

    print ("create graph")
    # create the graph with networkx from the adjacency matrix
    G = nx.from_numpy_array(np.array(adj_mat))

    print ("done")

    print ("remove node 1")
    for i in range(reduce_deg_1):
        for s in range(1):
            a = []
            for e in G.degree():
                if e[1] == 1:
                    a.append(e[0])

            G.remove_nodes_from(a)

    print ("done")
    # hide the fake nodes and the nodes of degree 0 from the graph with a size set to 0
    size_map = []
    color_map = []



    # check the bigger connected component of the graph and remove the nodes that are not in this component
    """
    COMPLEXITY PROBLEM HERE 
    """
    # a is all the nodes that are not in the biggest connected component
    # dict_pos are all the nodes in the graph
    # max(nx.connected_components(G), key=len) are the nodes in the biggest connected component
    print ("calcul connected component")

    not_in_graph = dict_pos.keys() - max(nx.connected_components(G), key=len)

    print ("done")

    print("supp node 2 and 0")
    # for all the nodes in the graph
    for i, e in enumerate(adj_mat):

        # if the node is in the biggest connected component
        if i not in not_in_graph:

            # if the node is a fake node or a node of degree 0 => size set to 0
            if e.count(1) == 2 or e.count(1) == 0:

                size_map.append(0)

                if color == True:
                    color_map.append("blue")

            # else => size set to 1
            else:
                size_map.append(4)

                if color == True:
                    if e.count(1) == 3:

                        color_map.append("red")

                    elif e.count(1) == 1:

                        color_map.append("purple")

                    elif e.count(1) == 4:

                        color_map.append("green")

                    elif e.count(1) == 5:

                        color_map.append("yellow")

                    elif e.count(1) == 6:

                        color_map.append("orange")

                    else:
                        color_map.append("blue")
    print ("done")
    G.remove_nodes_from(not_in_graph)


    if color == True:
        nx.draw(G, dict_pos, node_size=size_map, node_color=color_map)
    else:
        ax = plt.gca()
        ax.set_facecolor('black')
        nx.draw_networkx(G, dict_pos, node_size=size_map, node_color="#FFFFFF", edge_color="#333333", with_labels=False)


    plt.show()

    return G
