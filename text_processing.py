"""
Text processing class

~~ README ~~
Relevant attributes:
    self.f1_item_array	-> Contains an array of everything in feature1_svd
    self.f2_item_array 	-> Contains an array of everything in feature2

Relevant functions:
    self.get_user_clusters(user_index)		-> returns cluster for user with index given
    self.get_item_vector(index, f1 = true) 	-> returns vector from f1_item_array or f2_item_array
    self.get_item_info(index)			-> returns [name, url] for item
    self.get_category_info(index)		-> returns category name for that index (used in feature2)
 
When instantiating a new instance use this line:
text_processing("feature1_svd", "feature2", "clustering_data", "attraction_mapping", "attraction_information", "feature2_keywords")

"""

import numpy

class text_processing():
    def __init__(self, f1_filename, f2_filename, cluster_filename, mapping_filename, attraction_filename, categories_filename):
	self.f1_item_array = self.feature1_text_cleanup(f1_filename)
	self.f2_item_array = self.feature2_text_cleanup(f2_filename)
	
	self.num_users = 0
	self.cluster_dict = self.clustering_text_cleanup(cluster_filename)

	self.mapping_dict = {}
	self.attraction_dict = {}
	self.categories_dict = {}	

	#initialize attraction and mapping dicts
	self.load_attractions(mapping_filename, attraction_filename)
	self.load_categories(categories_filename)

    #####	INTERNAL INITIALIZATION FUNCTIONS	#####
    def feature1_text_cleanup(self, filename): 
        """ return a numpy array, (# items) x (# features)
            shape = (250, 217)
            Note: when certain attractions were empty or didn't have
	    all 217 features, I filled their respective vector in 
	    the matrix with 0.0s
        """
        lineList = []

        feature1_text = open (filename, 'rb')
        for line in feature1_text:
	    toAppend = [float((x.split(':'))[1]) for x in line.split()]
	
	    x = len(toAppend)	

	    if (x < 217):
	        lineList.append(toAppend + [0.0]*(217 - x))
	    else:
	  	lineList.append(toAppend)
	feature1_text.close()
    	return numpy.asarray(lineList)


    def feature2_text_cleanup(self, filename):
	""" return a numpy array, (# items) x (# categories)
	    shape = (250, 39)
	
	    Note: this is directly copying what was given in 
	    the file
	"""
	lineList = []

	feature2_text = open (filename, 'rb')
	for line in feature2_text:
	    toAppend = [0.0]*39
	    
	    new_line = line.split()
	    for item in new_line:
		toAppend[int(item.split(':')[0])] = 1.0
	
	    lineList.append(toAppend)

	feature2_text.close()    		
	return numpy.asarray(lineList)


    def clustering_text_cleanup(self, filename):
	""" returns a dictionary mapping each user from 0 -> m
	    to their respective clusters (repr as list of lists)
	"""
	clustering_text = open (filename, 'rb')
        clustering_dict = {}
	index = 0
	
	for line in clustering_text:
	    clustering_dict[index] = [x.split() for x in line.split(':')]
	    index += 1

	self.num_users = index - 1
	return clustering_dict	


    def load_attractions(self, mapping_filename, attraction_filename):
	""" store a dictionary of mapping to attractions where
	    key = index in the feature1_svd
	    value = [id]

	    store another dictionary of mappings to attraction info
	    key = id
	    value = [name, url]
	"""
	mapping_text = open (mapping_filename, 'rb')
	
	index = 0
	for line in mapping_text:
	    self.mapping_dict[index] = line[0:-1]
	    index += 1
	mapping_text.close()

	
	attraction_text = open(attraction_filename, 'rb')
	for line in attraction_text:
	    net_info = line.split('\t', 1)
	    print net_info[1][0:-1].split('\t')
            self.attraction_dict[net_info[0]] = net_info[1][0:-1].split('\t')

	attraction_text.close()
	return

    
    def load_categories(self, categories_filename):
	""" store a dictionary mapping each index to its
	    relevant category
	"""
	categories_text = open (categories_filename, 'rb')
	index = 0
	for line in categories_text:
	    print line[:-1]
	    self.categories_dict[index] = line[:-1]
	    index += 1
	return


    #####	EXTERNAL FUNCTIONS	 #####
    def get_user_clusters(self, user_index):
	# return the relevant user's clusterings as list of lists
	if (-1 < user_index and user_index < self.num_users):
	    return self.cluster_dict[user_index]
	else:
	    print "User Index out of range"

    def get_item_vector(self, index, f1 = True):
	# return the relevant vector to the item
	if f1:
	    try:
	    	return self.f1_item_array[index, :]
	    except IndexError:
		print "Index out of range"
	else:
	    try:
	    	return self.f2_item_array[index, :]
	    except IndexError:
		print "Index out of range"
	

    def get_item_info(self, index):
	# return the relevant item's name and url
	x = self.mapping_dict[index] 
	if (x == None):
	    print "Index out of range"
	    return
	else:
	    return self.attraction_dict[x]

    def get_category_info(self, index):
	# return the category of the relevant index
	if (-1 < index and index < 39):
	    return self.categories_dict[index]
	else:
	    print "Category index out of range"





"""
Some Test Functions

t = text_processing("feature1_svd", "feature2", "clustering_data", "attraction_mapping", "attraction_information", "feature2_keywords")

print t.get_item_vector(2)
print t.get_item_vector(900)
print t.get_item_vector(4, f1 = False)
print t.get_item_info(3)
print t.get_user_clusters(5)
print t.get_user_clusters(9000)
print t.get_category_info(16)
print t.get_category_info(-1)
print t.get_category_info(-100)
"""
















