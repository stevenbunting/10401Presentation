
import random

# holdout 50% of each cluster

allData = text_processing("feature1_svd", "feature2", "clustering_data", "attraction_mapping", "attraction_information", "feature2_keywords")

def holdout50(allData):
	trainData = {}
	testData = {}
	testLabels = {}
	for user in range(allData.num_user):
		train, test, labels = holdoutUser(allData.get_user_cluster(user))
		trainData[user] = train
		testLabels[user] = labels
		testData[user] = test 
	return(trainData, testData, testLabels)


def holdoutUser(userClusts):
	total = 0
	for cluster in userClusts:
		total += len(cluster)
	nout = int(.5 * total)
	indexes = random.sample(xrange(total),nout)
	testItems = []
	testlabels = []
	train = []
	count = 0
	for i in range(len(userClusts)):
		for j in userClusts[i]:
			if count in indexes:
				testItems.append(j)
				testLabels.append(i)
				userClusts[i].remove(j)
		    count += 1
		train.append(userClusts[i])
	return(train, testItems, testLabels)




