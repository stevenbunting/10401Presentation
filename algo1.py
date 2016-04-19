from text_processing import text_processing
from paperAlgo2 import algo2
import numpy

t = text_processing("feature1_svd", "feature2", "clustering_data", "attraction_mapping", "attraction_information", "feature2_keywords")
M = t.num_users

def algo1(lx, lu, su, D):
  converged = False
  N = 250
  allU = numpy.zeros((M, D, D))

  T = numpy.zeros(M)
  for m in range(0,M):
    actual = 0
    total = 0
    for cluster in t.get_user_clusters(m):
      size = len(cluster)
      actual = actual + size*(size-1)/2
      total = total+size
    T[m] = (actual*1.)/(total*1.)
  
  B = numpy.zeros((M,N,N))
  y = numpy.zeros((M,N,N))
  for m in range(0,M):
    clusters = t.get_user_clusters(m)
    for cluster in clusters:
      for i in cluster:
        for j in range(0,N):
          y[m,i,j] = 1 if j in cluster else -1
          B[m,i,j] = 1 if j in cluster else T[m]

  for i in range (0,M):
    allU[i] = numpy.identity(D)
  
  allX = numpy.zeros ((250, D)) #SHOULD THIS BE ALL 0s?????
  while not converged:
    total = 0
    for m in range(0,M):
      clusters = t.get_user_clusters(m)
      clusters = [item for sublist in clusters for item in sublist]
      Um = allU[m]
      for i in clusters:
        for j in clusters:
          i = int(i)
          j = int(j)
          xi = allX[i]
          xj = numpy.transpose(allX[j])
          temp = numpy.dot(numpy.dot(xi,Um),xj)
          total = total + B[m,i,j]*(y[m,i,j] - temp)
    b = (total*1.)/(M*1.)

    
    phi = numpy.zeros((M,N,D,D))  
    phi2 = numpy.zeros((M,N,D,D))
    for x in range(0,M):
      clusters = t.get_user_clusters(x)
      clusters = [item for sublist in clusters for item in sublist]
      print(len(clusters))
      for y in range(0,len(clusters)):
        (p,p2) = algo2(y,allU[x],b,t.get_user_clusters(x),T[x],allX)
        phi[m,i] = p
        phi2[m,i] = p2

    for i in range(0,N):
      sm = numpy.zeros((D,D))
      sm2 = numpy.zeros((D,D))
      for m in range(0,M):
        sm = sm+p[m,i]
        sm2 = sm+p2[m,i]
      pre=lx*numpy.identity(D) + (1./2.)*sm
      allX[i] = numpy.dot(numpy.linalg.inv(pre),(1./2.)*sm2)

    for i in range(0,M):
      p = 0.01
      theta = numpy.zeros(D)
      a = numpy.zeros(D)
      (psi1, psi2) = algo3(t.get_user_clusters(m), b, allX, T[i])
      A = (lu + p)*numpy.identity(D) + (1./2.)*psi1
      c = lu*su*numpy.ones(D)+ (1./2.)*psi2 + p(theta-a)
      um = numpy.dot(numpy.linalg.inv(A),c)
      while (um > 0).sum() > 0:
        theta = max(um+a, 0)
        a = a +um - theta
        p = 1.1*p
        A = (lu + p)*numpy.identity(D) + (1./2.)*psi1
        c = lu*su*numpy.ones(D)+ (1./2.)*psi2 + p(theta-a)
        um = numpy.dot(numpy.linalg.inv(A),c)
      allU[m] = numpy.diag(um)
    converged = True



algo1(0.1,0.1,0.1,217)
