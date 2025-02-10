import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import Averaging_Process

#Vertices and nodes are the same thing

def C_n(n):
    #returns a Cycle graph of size n
    return(nx.cycle_graph(n))
def C_n_xi(n):
    #returns a Cycle graph of size n and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    xi[0] = 1
    return(nx.cycle_graph(n),xi)

def K_n(n):
    #returns a complete graph of size n
    return(nx.complete_graph(n))
def K_n_xi(n):
    #returns a complete graph of size n and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    xi[0] = 1
    return(nx.complete_graph(n),xi)

def K_n_m(n,m):
    #returns a complete bipartite graph of size n
    return(nx.complete_multipartite_graph(n,m))
def K_n_m_xi(n,m):
    #returns a complete bipartite graph of size n and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    # you pick a vertex which has more edges connected to it that is belonging to the smaller group
    if n > m:
        xi[0] = 1
    else:
        xi[n] = 1
    return(nx.complete_multipartite_graph(n,m),xi)

def P_n(n):
    #returns a Path graph of size n
    return(nx.path_graph(n))
def P_n_xi(n):
    #returns a Path graph of size n and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    # the two nodes at either end are the worst
    xi[0] = 1
    return(nx.path_graph(n),xi)

def star_n(n):
    #returns a star graph of size n,nx.star_graph(n) has size n+1
    return(nx.star_graph(n-1))
def star_n_xi(n):
    #returns a star graph of size n and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    # 0 vertex is in the center
    if n>1:
        xi[1] = 1
    else:
        xi[0] = 1
    return(nx.star_graph(n-1),xi)

def wheel_n(n):
    #returns a wheel graph of size n
    return(nx.wheel_graph(n))
def wheel_n_xi(n):
    #returns a wheel graph of size n and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    # 0 vertex is in the center
    if n>1:
        xi[1] = 1
    else:
        xi[0] = 1
    return(nx.wheel_graph(n),xi)

def barbell_n_m(n,m):
    #returns a barbell graph of size 2*n+m
    #n is the size of the two complete graphs
    #m is the size of the path between the two complete graphs
    return(nx.barbell_graph(n,m))
def barbell_n_m_xi(n,m):
    #returns a barbell graph of size 2*n+m and worst possible starting value xi
    size = 2*n + m
    xi = np.zeros(size)
    # the middle of the path between the two complete graphs is the worst
    worst = n + m//2+1
    xi[worst] = 1
    return(nx.barbell_graph(n,m),xi)

def turan_n_r(n,r):
    #returns a turan graph of size n and groups r
    #a turan graph is a complete multipartite graph with n vertices and
    return(nx.turan_graph(n,r))
def turan_n_r_xi(n,r):
    #returns a turan graph of size n and groups r and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    xi[0] = 1
    return(nx.turan_graph(n,r),xi)

def lollipop_n_m(n,m):
    #returns a lollipop graph of size n+m
    return(nx.lollipop_graph(n,m))
def lollipop_n_m_xi(n,m):
    #returns a lollipop graph of size n+m and worst possible starting value xi
    size = n+m
    xi = np.zeros(size)
    # the vertex at the end of the path graph not connected to the complete graph is the worst
    xi[size-1] = 1
    return(nx.lollipop_graph(n,m),xi)

def ladder_n(n):
    #returns a ladder graph of size 2n
    return(nx.ladder_graph(n))
def ladder_n_xi(n):
    #returns a ladder graph of size 2n and worst possible starting value xi
    size = 2*n
    xi = np.zeros(size)
    # the vertices at the bottom or top of the ladder is the worst
    xi[0] = 1
    return(nx.ladder_graph(n),xi)

def full_rary_tree_n_r(n,r):
    #returns a Cycle graph of size n
    return(nx.full_rary_tree_graph(r,n))
def full_rary_tree_n_r_xi(n,r):
    #returns a Cycle graph of size n and worst possible starting value xi
    size = n
    xi = np.zeros(size)
    xi[0] = 1
    return(nx.full_rary_tree_graph(r,n),xi)

if __name__ == '__main__':
    n = 5
    k = 2

    KG = nx.kneser_graph(n,k)
    print(KG.nodes)
    print(KG.edges)