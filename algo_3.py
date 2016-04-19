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


def solve_h(user_m_cluster):
    """ 
        Used to solve for little Psi
    """
    

def solve_X_m(user_m_cluster, x_i_groups):
    #creates a unique X_m cluster 
    X_m = numpy.empty()
    for cluster in user_m_cluster:
	for item in cluster:
	    numpy.vstack(X_m, x_i_groups[int(item)])
    return X_m


def solve_H(user_m_cluster, x_i_groups):
    """
        Used to solve for big Psi
    """
    #we are under the assumption that each user gets a subset of items
    #so when we calculate X_m it will be different for each user
    X_m = solve_X_m(user_m_cluster, x_i_groups)
    
    for 
	


def solve_t_m(user_m_cluster):
    """
	t_m = (number of links for user m)/number of total possible pairs
    """
    total_item_count = 0
    link_count = 0

    for cluster_id in len(user_m_cluster):
	items = len(user_m_cluster[cluster_id])
	total_item_count += items
	link_count += math.factorial(items)

    #don't know if this is what they mean by total possible pairs        
    total_links = math.factorial(total_item_count)
    return (link_count*(1.0))/total_links


def solve_linked_sum_big_psi(user_m_cluster):


def solve_linked_sum_little_psi(user_m_cluster):



def algorithm_3(user_m_cluster, b, x_i_groups):
    # b is the global offset set in algorithm 1
    # Note: user_m_cluster is a list of lists

    global H, h
    H = solve_H(user_m_cluster)
    h = solve_h(user_m_cluster)
    
    s = 1
    t_m = solve_t_m(user_m_cluster)

    linked_sum_big_psi = solve_linked_sum_big_psi()
    linked_sum_little_psi = solve_linked_sum_little_psi()

    big_psi = (s-t_m)*linked_sum_big_psi + t_m*H
    little_psi = ((1-b)*s + (1+b)*t_m) * linked_sum_little_psi + (1-b)*t_m*h

    return (big_psi, little_psi)







