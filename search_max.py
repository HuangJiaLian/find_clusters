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




def find_Largest_cluster(contact_matrix, N_ring):
    for k in range(0, N_ring):
        for j in range(0, N_ring):
            contacts = np.where(contact_matrix[j] == 1)
            for contact in contacts[0]:
                a = contact_matrix[j]
                b = contact_matrix[contact]
                contact_matrix[j] = np.logical_or(a,b).astype(int)
    return np.max(contact_matrix.sum(1))


def find_Max(contact_matrix):
    contact_matrix = np.tril(contact_matrix,0)
    return np.max(contact_matrix.sum(1))


print("Your answer:")
print(find_Largest_cluster(data2, n))
print("My answer:")
print(find_Max(data2))
