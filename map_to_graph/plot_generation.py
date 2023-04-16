import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

"""
Repartition of the degree between 3 and +inf
"""
def fct(x, a, b):
    return a * np.exp(-b * x)

"""
Plot the ratio of a list of degree sequence
"""
def plot_generation_ratio(lst, keys, fit=False):
    x_tot = []
    y_tot = []

    for element in lst:
        y = []
        for val in range(min(element), max(element)+1):
            y.append(element.count(val) / len(element))


        x = list(range(min(element), max(element)+1))

        for e in y:
            y_tot.append(e)

        for e in x:
            x_tot.append(e)

        plt.scatter(x, y)
        plt.plot(x, y, label=keys[lst.index(element)])

        for i, txt in enumerate(y):
            plt.annotate(round(txt, 2), (x[i], y[i]))

    if fit:
        popt, pcov = curve_fit(fct, x_tot, y_tot)
        a = popt[0]
        b = popt[1]

        y_fitted = []
        for e in x:
            y_fitted.append(fct(e, a, b))

        print(str(a) + "* e^(-" + str(b) + "x)")

        plt.plot(x, y_fitted, label="fit")

        plt.legend()
        plt.show()
        return a, b

    else:
        plt.legend()
        plt.show()


"""
give the mean of the probability of each degree
"""
def get_mean_proba(lst, keys, fit=False):
    x_tot = []
    y_tot = []
    for element in lst:

        y = []
        for val in range(min(element), max(element)):
            y.append(element.count(val) / len(element))

        x = list(range(min(element), max(element)))

        y_tot.append(y)
        x_tot.append(x)

    print(y_tot)
    print(x_tot)
    print(max(x_tot))

    y_mean = [0] * len(max(x_tot))

    for e in y_tot:

        for i in range(len(e)):
            print(e[i])
            print(y_mean[i])
            y_mean[i] += e[i]

    for i in range(len(y_mean)):
        y_mean[i] = y_mean[i] / len(y_tot)

    print(y_mean)
    print(sum(y_mean))
