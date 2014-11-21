# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from __future__ import division
from PyGMO import problem
from PyGMO import algorithm
from PyGMO import island
import math
from misc_library import *

class schaffer_function_n2(problem.base):
    """ Schaffer Function N.2
    Reference: http://en.wikipedia.org/wiki/Test_functions_for_optimization#Test_functions_for_single-objective_optimization_problems """
  
    def __init__(self):
        #First we call the constructor of the base class telling
        #essentially to PyGMO what kind of problem to expect (1 objective, 0 contraints etc.)
        dim = 2 #This is schaffer_function with 2 dimensions
        super(schaffer_function_n2,self).__init__(dim)
        #then we set the problem bounds (in this case equal for all components)
        self.set_bounds(-100,100)
        #define instance variable dim
        self.__dim = dim
    
    #We reimplement the virtual method that defines the objective function.
    def _objfun_impl(self, candidate):
        x = candidate[0]
        y = candidate[1]
        f = 0.5 + (math.sin(x**2 - y**2)**2 - 0.5) / ( 1 + 0.001*(x**2 + y**2) )**2
        return (f,)
    
    #Finally we also reimplement a virtual method that adds some output to the __repr__ method
    def human_readable_extra(self):
        text = """\tProblem dimension: %s
        Implemented function: 
            f = 0.5 + (math.sin(x**2 - y**2)**2 - 0.5) / ( 1 + 0.001*(x**2 + y**2) )**2 """ % str(self.__dim)
        return text

class sphere_function(problem.base):
    """ Sphere Function N dimension
    Reference: http://en.wikipedia.org/wiki/Test_functions_for_optimization#Test_functions_for_single-objective_optimization_problems """
  
    def __init__(self, dim = 10):
        super(sphere_function,self).__init__(dim)
        self.set_bounds(-100,100)
        self.__dim = dim
    
    def _objfun_impl(self, x):
        f = 0
        for i in range(self.__dim):
            f += x[i]**2
        return (f,)
    
    def human_readable_extra(self):
        text = """\tProblem dimension: %s 
        Implemented function: f = x^2""" % str(self.__dim)
        return text

# <codecell>

if __name__ == '__main__':

    print("############### Differential Evolution ##########################") 
    algo = algorithm.de(gen = 500)
    results_de_schaffer = []
    results_de_sphere = []
    
    for i in range(30):
        prob = schaffer_function_n2()
        #print("\nSchaffer Function")
        #print(prob)
        isl = island(algo,prob,50)
        #print("Before optimisation: " +  str(isl.population.champion.f[0]) )
        isl.evolve(10)
        results_de_schaffer.append( isl.population.champion.f[0] )
        #print("After optimisation: " + str( isl.population.champion.f[0]) + '\n')
        #print("="*70 + '\n')
        #print("Sphere Function")
        prob2 = sphere_function(dim=100)
        #print(prob2)
        isl2 = island(algo,prob2,50)
        #print("Before optimisation: " + str(isl2.population.champion.f[0]))
        isl2.evolve(10)
        results_de_sphere.append( isl2.population.champion.f[0] )
        #print("After optimisation: " + str(isl2.population.champion.f[0]))
    print("\nSchaffer Function:\n")
    print(xtile(results_de_schaffer, hi = max(results_de_schaffer), lo=min(results_de_schaffer), show="%.10f") )
    print("\nSphere Function:\n")
    print( xtile(results_de_sphere, hi = max(results_de_sphere), lo=min(results_de_sphere), show="%.10f") )

# <codecell>

    print("############### Simulated Anealing ##########################")
    algo3 = algorithm.sa_corana()
    results_sae_schaffer = []
    results_sae_sphere = []
    
    for i in range(30):        
        isl3 = island(algo3,prob,50)
        #print(prob)
        #print("Before optimisation: " + str(isl3.population.champion.f[0]) )
        isl3.evolve(10)
        results_sae_schaffer.append( round(isl3.population.champion.f[0], 5) )
        #print("After optimisation: " + str(isl3.population.champion.f[0]) ) 
        #print('\n' + "="*70 + '\n')     
        #print(prob2)
        isl4 = island(algo3,prob2,50)
        #print("Before optimisation: " + str(isl4.population.champion.f[0]) )
        isl4.evolve(10)
        results_sae_sphere.append( round(isl4.population.champion.f[0], 5) )
        #print("After optimisation: " + str(isl4.population.champion.f[0]))
    print("\nSchaffer Function:\n")   
    print(xtile(results_sae_schaffer))
    print("\nSphere Function:\n")
    print(xtile(results_sae_sphere))
    

# <codecell>


