#creation of the heap
import math
import igraph

from map_to_graph.main import map_to_graph


def node (n) :

    length = math.ceil(math.sqrt(n))
    size = length**2
    deg2 = size-n
    probadeg2 = (deg2/size)
    center = length/2
    position(length, n)



def position (length, n) :

    tab =[]
    for i in range (n) :

        row = math.floor(i/length)
        column = i%(length)
        tab.append((row, column))
    return tab



map_to_graph()


