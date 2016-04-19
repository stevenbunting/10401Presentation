# algorithm for computing phi
# inputs: i is the item, m is the user
# assumes feature is a dataset of feature representations for the items, 
# and feature[i] is the row vector for the feature representation of 
#feature i
# assumes clusterGroups is the preclustered groups by user m, where each row is a cluster


import numpy as np

global Gm
global gm


#literally copied this from algo_3.py
def transform_X_m(user_m_cluster, x_i_groups):
    """
        This function takes all the transformed values of x_i
        and creates an array X_m that has each transformed vector
        as a column vector. We can then call on each column vector
        when we need to do calculations later
    """
    X_m = np.empty()
    for cluster in user_m_cluster:
        for item in cluster:
            np.hstack(X_m, np.transpose(x_i_groups[int[item]]))
    return X_m
    

def algo2(item_i_index, Um, b, clusterGroups, t_m, x_i_groups):
    global Gm
    global gm

    s = 1
    #i_group = NULL	

    X_m = transform_X_m(clusterGroups, x_i_groups) 
    (rows, cols) = X_m.shape

    Gm = 0
    gm = np.zeros((rows, 1), dtype = np.float)    

    #this is the cluster that x_i is in
    x_i_cluster = []
    #clusterGroups is a list of lists
    for cluster in xrange(len(clusterGroups)):
	if (item_i_index in cluster):
            x_i_cluster = cluster
	for item in cluster:
            x_j = X_m[:,int(item)]
            Gm += x_j.dot(np.transpose(x_j))
            gm += x_j

    x_i = X_m[:, item_i_index]
    big_phi_sum = 0
    kappa_1_sum = np.zeros((rows, 1), dtype = np.float)
    for item in x_i_cluster:
        x_j = X_m[:,int(item)]
        kappa_1_sum += x_j
        big_phi_sum += x_j.dot(np.transpose(x_j)) + t_m*(Gm-(x_i.dot(np.transpose(x_i))))
    
    bigPhi = Um.dot(((s-t_m)*big_phi_sum) * Um)
    
    #kappa_1 is 217x1
    kappa_1 = ((1-b)*s + (1+b)*t_m)*kappa_1_sum
    #kappa_2 is also 217x1
    kappa_2 = (1 + b)*t_m*(gm-x_i)

    littlePhi = Um.dot(kappa_1 - kappa_2)    

    return(bigPhi, littlePhi)

