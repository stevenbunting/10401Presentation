"""
This file contains the code for algorithm 3 (solving for upper/lower-case psi)

Also, need to import text_processing to call user m's cluster

Remember to declare global H and h when calling function in another file
"""

import numpy
import math
from paperAlgo2 import *


global H
global h


def solve_h(user_m_cluster, X_m):
    """ 
        Used to solve for little Psi
    """
    (rows, cols) = X_m.shape

    starting_array_1 = numpy.zeros((rows, 1), dtype=numpy.float)
    starting_array_2 = numpy.zeros((rows, 1), dtype=numpy.float)
    for col in xrange(cols):
	starting_array_1 += col
        starting_array_2 += (col * col)

    return ((starting_array_1 * starting_array_1) - starting_array_2)    


def solve_X_m(user_m_cluster, x_i_groups):
    #creates a unique X_m cluster that is tranposed from given X_m
    X_m = numpy.empty()
    for cluster in user_m_cluster:
	for item in cluster:
	    # this will create a 217 x num_items_in_cluster array
	    numpy.hstack(X_m, numpy.transpose(x_i_groups[int(item)]))
    return X_m


def solve_H(user_m_cluster, X_m):
    """
        Used to solve for big Psi
    """
    #we are under the assumption that each user gets a subset of items
    #so when we calculate X_m it will be different for each user
    (rows, cols) = X_m.shape
    
    starting_array = numpy.zeros((rows, rows), dtype=numpy.float)i
    for col in xrange(cols):
        x_j = X_m[:,col]
	summand_1 = (x_j.dot(numpy.transpose(x_j)))
	summ = summand_1 * summand_1
	starting_array += summ

    X_m_calc_1 = (X_m.dot(numpy.transpose(X_m)))
    X_m_calc = X_m_calc_1 * X_m_calc_1
    return (X_m_calc - starting_array)
	
"""
def solve_t_m(user_m_cluster):
    total_item_count = 0
    link_count = 0

    for cluster_id in len(user_m_cluster):
	items = len(user_m_cluster[cluster_id])
	total_item_count += items
	link_count += math.factorial(items)

    #don't know if this is what they mean by total possible pairs        
    total_links = math.factorial(total_item_count)
    return (link_count*(1.0))/total_links
"""

def solve_linked_sum_for_psi(user_m_cluster, X_m, big=True):
    # basically sum over all linked pairs
    num_clusters = len(user_m_cluster)
    total_items_so_far = 0

    (rows, cols) = X_m.shape

    if(big == True):
        starting_array = numpy.zeros((rows, rows), dtype=numpy.float)
    else:
        starting_array = numpy.zeros((rows, 1), dtype=numpy.float)    

    for cluster in xrange(num_clusters):
        #each item corresponds to a column in X_m
        num_items = len(cluster)
	for item_1 in xrange(num_items):
	    x_i = item_1 + total_items_so_far
	    for item_2 in xrange(1, num_items):
		x_j = item_2 + total_items_so_far
                if(big == True):
		    calc = X_m[:,x_i]*X_m[:,x_j]
		    starting_array += calc.dot(numpy.transpose(calc))
                else:
                    calc = X_m[:,x_i]*X_m[:,x_j]
                    starting_array += calc
	total_items_so_far += num_items

    # Final array should be 217x217 and should match with H
    # OR
    # Final array should be 217x1 and should match with h
    return starting_array



def algorithm_3(user_m_cluster, b, x_i_groups, t_m):
    # b is the global offset set in algorithm 1
    # Note: user_m_cluster is a list of lists

    global H, h
    X_m = solve_X_m(user_m_cluster, x_i_groups)

    H = solve_H(user_m_cluster, X_m)
    h = solve_h(user_m_cluster, X_m)
    
    s = 1

    linked_sum_big_psi = solve_linked_sum_for_psi(user_m_cluster,X_m)
    linked_sum_little_psi = solve_linked_sum_for_psi(user_m_cluster,X_m,big=False)

    big_psi = (s-t_m)*linked_sum_big_psi + t_m*H
    little_psi = ((1-b)*s + (1+b)*t_m) * linked_sum_little_psi + (1-b)*t_m*h

    return (big_psi, little_psi)







