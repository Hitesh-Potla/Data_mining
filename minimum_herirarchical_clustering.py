import pandas as pd
import numpy as np
def find_min_element(dist_matrix):
    min=float('inf')
    min_ind=()
    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix[0])):
            if(i==j):
                continue
            else:
                if(min > dist_matrix[i][j]):
                    min=dist_matrix[i][j]
                    min_ind=(j,i)
    return min_ind

def update_dist_matrix(dist_matrix,min_element):
    for i in range(len(dist_matrix)):
        dist_matrix[i].remove(dist_matrix[i][min_element[0]])
    for i in range(len(dist_matrix[0])):
        dist_matrix[min_element[1]][i]=min(dist_matrix[min_element[1]][i],dist_matrix[min_element[0]][i])
    dist_matrix.remove(dist_matrix[min_element[0]])

def print_matrix(dist_matrix):
    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix[0])):
            print(dist_matrix[i][j],end="\t")
        print('\n')

labels=[18,22,25,27,42,43]
dist_matrix = [
    [0,4,7,9,24,25],
    [4,0,3,5,20,21],
    [7,3,0,2,17,18],
    [9,5,2,0,15,16],
    [24,20,17,15,0,1],
    [25,21,18,16,1,0]
]

print("original matrix:\n",end="")
print_matrix(dist_matrix)

for i in range(5):
    print(f"{i+1}:\n")
    min_element=find_min_element(dist_matrix)
    update_dist_matrix(dist_matrix,min_element)
    print_matrix(dist_matrix)