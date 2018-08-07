#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:51:40 2018

@author: huang
"""
"""
1. randomly generate a 5 times 5 matrix with element 0 or 1
"""
import numpy as np

"""Generate the data for testing"""
#n: the dimension
n = input("Input the number of beads you want calculate (positive integer):\n")
n= int(n)

data = np.random.rand(n,n)
data = np.floor(data + 0.2)

# generate a simplified map (use the symmetry of the map)
data2 = np.zeros([n,n])
for i in range(n):
    for j in range(i+1):
    # for j in range(n):
        if j == i:
            data2[i][j] = 1
        else:
            data2[i][j] = data[i][j]
            data2[j][i] = data[i][j]

print("Map:")
print(data2)


# search connected pairs
def generate_pair_list():
    li = []
    for i in range(n):
        for j in range(i+1):
            if data2[i][j] == 1:
                tmp_set ={i,j}
                li.append(tmp_set)
    return li


def clusters(li):
    for x in li:
        for y in li:
            if x != y:
                if x.issubset(y):
                    li.remove(x)
                    break
                if x.intersection(y) != set():
                    if x.union(y) not in li:
                        li.append(x.union(y))
                        break
    return li

            
"""Check if there is in-relation in a list"""
def in_relation(li):
    for x in li:
        for y in li:
            if x !=y and x.issubset(y):
                return True
            
def intersection_relation(li):
    for x in li:
        for y in li:
            if x!=y and x.intersection(y) != set():
                return True

# li = generate_pair_list()          
# while in_relation(li) or intersection_relation(li):
#     clusters(li)

#print("The cluster list:",clusters(li))



###############################################
def find_Largest_cluster(contact_matrix, N_ring):
    for k in range(0, N_ring):
        for j in range(0, N_ring):
            contacts = np.where(contact_matrix[j] == 1)
            for contact in contacts[0]:
                a = contact_matrix[j]
                b = contact_matrix[contact]
                contact_matrix[j] = np.logical_or(a,b).astype(int)
    return np.max(contact_matrix.sum(1)), contact_matrix.sum(1), contact_matrix


def find_Max(contact_matrix):
    contact_matrix = np.tril(contact_matrix,0)
    return np.max(contact_matrix.sum(1))

a,b,c = find_Largest_cluster(data2, n)
print("Your answer:")
print(a)
print("My answer:")
print(find_Max(data2))
# print(b)
print(c)

print("The cluster list:",clusters(li))



