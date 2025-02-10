import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import Averaging_Process
import Graphs

def test_time(graph,xi,low,high,t,p,l):
    # measures the L^p(pi) norm for a graph G_n for different values of n at time t(n)
    # graph(n) is a function that takes as input n and return the networkx graph G_n, G_n has n vertices
    # xi(n) is the starting value for eta in the averaging process of G_n
    # low and high are the lower and upper bounds for the values of n
    # t(n) is the time at which we evaluate L^p(pi)
    # l is the number of simulations of each n between low and high
    L_p_n = np.zeros(high-low+1)
    for n in range(low,high+1):
        n_l = np.zeros(l)
        for i in range(l):
            G_n = graph(n)
            xi_n = xi(n)
            avg_n = Averaging_Process.Averaging_Process(G_n,xi_n)
            t_n = t(n)
            avg_n.update(t_n)
            n_l[i] = avg_n.L_p(p)
        L_p_n[n-low] = np.mean(n_l)
    return(L_p_n)
def test_value(graph,xi,low,high,threshold,inc,p):
    # measures the time it takes for the L^p norm to reach a threshold value as a function of n
    # graph(n) is a function that takes as input n and return the networkx graph G_n, G_n has n vertices
    # xi(n) is the starting value for eta in the averaging process of G_n
    # low and high are the lower and upper bounds for the values of n
    threshold_n = np.zeros(high-low+1)
    for n in range(low,high+1):
        G_n = graph(n)
        xi_n = xi(n)
        avg_n = Averaging_Process.Averaging_Process(G_n,xi_n)
        while avg_n.L_p(p) > threshold:
            avg_n.inc(inc)
        threshold_n[n-low] = avg_n.t
    return(threshold_n)
if __name__ == '__main__':
    #K_n
    def xi(n):
        x = np.zeros(n)
        x[0] = 1
        return(x)
    def t(n):
        return(2*np.log(n)/n)
    low = 10
    high = 100
    p = 2
    l = 10
    complete_n = test_time(Graphs.K_n,xi,low,high,t,p,l)
    plt.plot(np.arange(low,high+1),complete_n)
    plt.show()
    threshold = 0.1
    inc = 1
    complete_n = test_value(Graphs.K_n,xi,low,high,threshold,inc,p)
    plt.plot(np.arange(low,high+1),complete_n)
    plt.show()