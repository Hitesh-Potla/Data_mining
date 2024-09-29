# 1)Assign the closest cluster to each and every data points
# 2)update the centriods of each clusters
# 3)repeat step 1 and 2
import numpy as np 
def initialize_cluster(clusters):
    clusters.clear()
    for i in range(k):
        clusters.append([])
def find_cluster(number,centriods):
    if(type(number)=='list'):#works for 2 and 3 dimensional points
        pass
    else:#works for one dimensional points
        dist=float('inf')
        for i in range(k):
            if(dist>np.abs(number-centriods[i])):
                temp_cluster=i
                dist=np.abs(number-centriods[i])
        clusters[temp_cluster].append(number)
def update_centriods(centriods):
    for i in range(k):
        centriods[i]=sum(clusters[i])/len(clusters[i])
    return centriods



points=[5,11,19,27,23,25,6,18,2,8,10,12,31,29,4]#list containing list of x,y,z of points
centriods=[0,7,20]#list containing list of x,y,z of clusters
n=len(points)
k=len(centriods)
clusters=[]
for i in range(5):
    initialize_cluster(clusters)
    for i in range(n):
        find_cluster(points[i],centriods)
    centriods=update_centriods(centriods)
print(clusters)