# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from __future__ import division
from PyGMO import problem
from PyGMO import algorithm
from PyGMO import island
from PyGMO import population
import math
%matplotlib inline  

class schaffer_function(problem.base):
    """ Schaffer Function With 2 objectives.
    Reference: http://en.wikipedia.org/wiki/Test_functions_for_optimization#Test_functions_for_single-objective_optimization_problems """
  
    def __init__(self):
        dim = 1 # n = 1 schaffer function 
        #Important: For multi objective optimisation, 
        #you need to pass number of objectives to the constructor of super class
        super(schaffer_function,self).__init__(dim,0,2)
        self.set_bounds(-10,10)
        self.__dim = dim
    
    def _objfun_impl(self, x): 
        f1 = x[0]**2
        f2 = (x[0] - 2)**2 
        return (f1,f2)
 
    def human_readable_extra(self):
        text = """\tProblem dimension: %s
        Implemented function: f1 = x^2, f2 = (x-2)^2 (Schaffer)""" % str(self.__dim)
        return text

class zdt_1(problem.base):
    def __init__(self):
        dim = 30 # n = 30 ZDT1 function 
        super(zdt_1,self).__init__(dim,0,2)
        self.set_bounds(0,1)
        self.__dim = dim
    
    def _objfun_impl(self, x):
        f1 = x[0]
        sum_2_to_n = 0
        for i in range(1,self.__dim):
            sum_2_to_n += x[i]   
        g = 1 + 9/(self.__dim - 1)*sum_2_to_n 
        f2 = g * ( 1 - math.sqrt(x[0]/g) ) 
        return (f1,f2)

    def human_readable_extra(self):
        text = """\tProblem dimension: %s
        Implemented function: f1 = x1, f2 = g * ( 1 - math.sqrt(x1/g) ) (ZDT1)""" % str(self.__dim)
        return text
    

# <codecell>

if __name__ == '__main__':

    print("############### NSGA-II ##########################")
    algo = algorithm.nsga_II(gen = 250)
    prob1 = schaffer_function()
    print(prob1)
    
    pop = population(prob1,100)
    isl = island(algo,pop)
    isl.evolve(1)
    
    isl.population.plot_pareto_fronts()

# <codecell>

    prob2 = zdt_1()
    print(prob2)
    
    pop2 = population(prob2,100)
    isl2 = island(algo,pop2)
    isl2.evolve(1)
    
    isl2.population.plot_pareto_fronts()

# <codecell>


