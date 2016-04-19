import random 


#holdout one cluster at random

allData = text_processing("feature1_svd", "feature2", "clustering_data", "attraction_mapping", "attraction_information", "feature2_keywords")

def holdout1(allData):
	trainData = {}
	testData = {}
	for user in range(allData.num_user):
		train, test = holdout1User(allData.get_user_cluster(user))
		trainData[user] = train
		testData[user] = test 
	return(trainData, testData)


def holdout1User(userClusts):
	total = len(userClusts)
	index = random.sample(xrange(total), 1)
	testData = userClusts[index]
	trainData = userClusts[:index] + userClusts[index:]
	return(trainData, testData)