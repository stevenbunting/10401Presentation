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
    (r,c) = x_i_groups.shape
    #print(x_i_groups.shape)
    clusters = [item for sublist in user_m_cluster for item in sublist]
     
    X_m = None
    for cluster in user_m_cluster:
        for i in range(len(cluster)):
            if X_m == None:
              X_m = x_i_groups[int(item)].reshape(c,1)
            else:
              X_m = np.concatenate((X_m, x_i_groups[int(item)].reshape(c,1)),axis=1)
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
    x_i_index = 0
    #clusterGroups is a list of lists

    track_index = 0
    x_i_cluster_index = 0
    x_i_cluster_start = 0

    for cluster in clusterGroups:
        for item in xrange(len(cluster)):
            if(int(cluster[item]) == item_i_index):
                x_i_cluster = cluster            #store cluster x_i is in
                x_i_index = item + track_index   #store what index x_i is in in X_m
		x_i_cluster_start = track_index  #store where cluster starts in X_m

            x_j = X_m[:,(item + track_index)]
            Gm += np.dot(x_j,np.transpose(x_j))
            gm = gm + x_j 
        track_index = track_index + len(cluster)
            #gm += x_j
    #print(item_i_index)
    x_i = X_m[:, x_i_index]
    big_phi_sum = 0
    kappa_1_sum = np.zeros((rows, 1), dtype = np.float)
    for index in xrange(x_i_cluster_start, (x_i_cluster_start+len(x_i_cluster))):
        if(index == x_i_index):
            # this is x_i
            pass
        x_j = X_m[:,index]
        kappa_1_sum = kappa_1_sum + x_j
        big_phi_sum += x_j.dot(np.transpose(x_j)) + t_m*(Gm-(x_i.dot(np.transpose(x_i))))
    
    bigPhi = Um.dot(((s-t_m)*big_phi_sum) * Um)
    
    #kappa_1 is 217x1
    kappa_1 = ((1-b)*s + (1+b)*t_m)*kappa_1_sum
    #kappa_2 is also 217x1
    kappa_2 = (1 + b)*t_m*(gm-x_i)

    littlePhi = Um.dot(kappa_1 - kappa_2)    

    return(bigPhi, littlePhi)

