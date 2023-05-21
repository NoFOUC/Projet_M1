import map_to_graph as m2g
from Generation import graph_generation_np_array
from plot_generation import plot_generation_ratio
import time
start_time = time.time()

usa = False

#choose the parameters of the graph
G = graph_generation_np_array.graph_generation(color=False)

#G= m2g.map_to_graph_from_point([35.7521, 139.8781, 3000], plot=True)

color = ["purple", "red", "green", "yellow", "orange", "blue"]
tot = [e for e in m2g.get_degree_sequence(G) if e != 2 and e != 1]
degree = [tot]

if usa == True:
    style = "USA"
else:
    style = "Classic"

txt = "Graph generation with a number of nodes equal to " + str(len(degree[0])) + \
      ". \nThe style is " + style + "."

for e in range(1, max(tot)):

    if e != 2:
        txt = txt + "\nThe number of node of degree " + str(e) + " is equal to " + str(tot.count(e)) + ". " + \
              "The ratio is equal to " + str(round(tot.count(e) / len(tot), 2)) + ". "
        if e < 5:
            txt = txt + "The color of the node is " + color[e] + ". "
        else:
            txt = txt + "The color of the node is " + color[5] + ". "

print(txt)

plot_generation_ratio(degree, ["test"])

print("--- %s seconds ---" % (time.time() - start_time))

