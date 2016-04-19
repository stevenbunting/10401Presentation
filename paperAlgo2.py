# algorithm for computing phi
# inputs: i is the item, m is the user
# assumes feature is a dataset of feature representations for the items, 
# and feature[i] is the row vector for the feature representation of 
#feature i
# assumes groups is the preclustered groups by user m, where each row is a cluster


import numpy

Gm = 0
gm = np.zeros(len(feature[0]))

def algo2(i, m, Um, b, groups, feature):
	global Gm
	global gm

	s = 1
	links = 0
	total = 0
	i_group = NULL
	for group in range(nrow(groups)):
		links += (len(groups[group])-1)*len(groups[group])
		total += len(groups[group])
		for item in groups[group]:
			if item == i: 
				i_group = group
			feat = feature[item]
			Gm += np.dot(feat.transpose(),feat)
			gm += feat
	tm = float(links) / (total * (total-1))
	sameSum = 0
	featureSum = np.zeros(len(feature[0]))
	for elem in groups[i_group]:
		sameSum += np.dot(feature[elem].tranpose(), feature[elem])
		featureSum += feature[elem]
	Phi = np.dot(np.dot(Um,(((s-tm)*sameSum) + (tm*(Gm-np.dot(feature[i].transpose(),feature[i]))))),Um)	
	kappa1 = ((1-b)*s + (1-b)*tm)*featureSum
	kappa2 = (1+b)*tm*(gm-feature[i])
	phi = Um*(kappa1-kappa2)
	return(Phi, phi)

