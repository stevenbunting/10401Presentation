import random

# holdout 25% of each cluster

allData = text_processing("feature1_svd", "feature2", "clustering_data", "attraction_mapping", "attraction_information", "feature2_keywords")

def holdout25(allData):
	trainData = {}
	testData = {}
	testLabels = {}
	for user in range(allData.num_user):
		train, test, labels = holdout25User(allData.get_user_cluster(user))
		trainData[user] = train
		testLabels[user] = labels
		testData[user] = test 
	return(trainData, testData, testLabels)


def holdout25User(userClusts):
	test = []
	labels = []
	train = []
	for i in range(len(userClusts)):
		if 0 < len(userClusts[i]) <= 3:
			nout = 1
		else:
			nout = int(.25 * len(userClusts[i]))
		indexes = random.sample(xrange(len(userClusts[i])), nout)
		testItems = []
		testLabels = []
		clustTrain = []
		for index in range(len(userClusts[i])):
			if index in indexes:
				testItems.append(userClusts[i][index])
				testLabels.append(i)
				userClusts[i].remove(userClusts[i][index])
		test += testItems
		labels += testLabels
		train.append(userClusts[i])
	return(train, test, labels)



