import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Averaging_Process:
    def __init__(self,G,xi):
        self.G = G
        self.n = G.number_of_nodes()
        self.E = [e for e in G.edges]
        self.E_n = G.size
        self.t = 0
        self.eta = np.zeros(self.n)
        for i in range(self.n):
            self.eta[i] = xi[i]
    def poisson_clock(self,E,t):
        #returns the poisson clock rings of each edge in order that they ring
        #min(X_i) = Exp(n*lambda) for X_1,...,X_n = Exp(lambda)
        #sum_0^n X_i = Gamma(n,lambda)
        #k*X_i = Exp(lambda/k)
        def exponential_array(k,lamb=1):
            x = np.random.exponential(1/lamb,int(k*lamb)+1)
            arr = np.cumsum(x)
            x_n = len(arr)
            ind = np.searchsorted(arr,k)
            ind_arr = ind
            arr_sum = arr[x_n-1]
            k = k-arr_sum
            while ind >= x_n:
                x = np.random.exponential(1/lamb,int(k*lamb)+1)
                x = np.cumsum(x)
                x_n = len(x)
                x_sum = x[x_n-1]
                arr = np.append(arr,x+arr_sum)
                arr_sum += x_sum
                ind = np.searchsorted(x,k)
                ind_arr += ind
            return(list(arr[:ind_arr]))
        
        n = len(E)
        exp_arr = exponential_array(t,lamb = n)
        exp_arr_n = len(exp_arr)
        edge_arr = np.random.randint(n,size=exp_arr_n)
        edge_arr = [E[x] for x in edge_arr]
        return(exp_arr,edge_arr)
    def average(self,e):
        #e is edge to be averaged
        e_1 = e[0]
        e_2 = e[1]
        val = (self.eta[e_1]+ self.eta[e_2])/2
        self.eta[e_1] = val
        self.eta[e_2] = val
        return()
    def L_p(self,p):
        vect = self.n*self.eta-1
        vect = np.abs(vect)
        vect = vect**p
        L_sum = np.sum(vect)/self.n
        return(L_sum)
    def update(self,inc):
        self.t += inc
        exp_arr,edge_arr = self.poisson_clock(self.E,inc)
        n = len(edge_arr)
        for i in range(n):
            e = edge_arr[i]
            self.average(e)
        return()