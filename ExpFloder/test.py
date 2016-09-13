import  cPickle as p
import  numpy as np


withBN = np.load('withBN.npz');
withoutBN = np.load('withoutBN.npz')

with_in = withBN['arr_0']
with_c1 = withBN['arr_1']

without_in = withoutBN['arr_0']
without_c1 = withoutBN['arr_1']

def getNsplitCount(mat, N):
#mat: The whole input sample mat
#N: How many segments the sample will be seperated
    num_count = mat.shape[0]
    #print num_count
    result_mat = np.zeros([num_count, N] ,dtype=np.float32)
    for i in range(num_count):
        mat_max =  mat[i,:].max()
        mat_min =  mat[i,:].min()
        _range = mat[i,:].max() - mat[i,:].min()
        for j in range(N) :
            #Assumpt that all number between -100 and 100
            floor = mat_min + _range * j / N if j>0 else -100
            ceiling = mat_min + _range * (j+1) / N if j<N-1 else 100
            #result_mat[i, j] = mat[i][np.where()]
            #result_mat[i, j] = (mat[i][mat[i]>floor])[mat[i][mat[i]>floor]<=ceiling].shape[0]
            result_mat[i, j] = getBetween(mat[i], floor, ceiling)  / mat[i].shape[1] / mat[i].shape[2]
    return result_mat

def getRepresentValue(mat, N):
#mat: The whole input sample mat
#N: How many segments the sample will be seperated
    num_count = mat.shape[0]
    result_value = np.zeros([num_count, N] ,dtype=np.float32)
    for i in range(num_count):
        mat_max =  mat[i,:].max()
        mat_min =  mat[i,:].min()
        _range = mat[i,:].max() - mat[i,:].min()
        for j in range(N) :
            #Assumpt that all number between -100 and 100
            floor = mat_min + _range * j / N 
            ceiling = mat_min + _range * (j+1) / N 
            result_value[i ,j] = ( floor + ceiling ) / 2
    return result_value

def getBetween(sub_mat ,floor, ceiling):
    count = 0
    for i in range(sub_mat.shape[1]):
        for j in range (sub_mat.shape[2]):
            for k in range (sub_mat.shape[0]):
                if sub_mat[k][i][j] >= floor:
                    if sub_mat[k][i][j] <= ceiling:
                        count += 1
    return float(count)

      

def getAll(sub_mat):
    count = 0
    for i in range(sub_mat.shape[1]):
        for j in range (sub_mat.shape[2]):
            count += 1
    return count

  
#with_in[0]
"""
with_in_value = getRepresentValue(with_in, 8)
print with_in_value

with_in_count = getNsplitCount(with_in, 8)
print np.sum(with_in_count[0:10])

print with_in_count[0]

with_c1_count = getNsplitCount(with_c1, 8)
print np.sum(with_c1_count[0:10])

print with_c1_count[0]

#print getAll(with_in[0])


without_in_count = getNsplitCount(without_in, 8)
print np.sum(without_in_count[0:10])

print without_in_count[0]


without_c1_count = getNsplitCount(without_c1, 8)
print np.sum(without_c1_count[0:10])

print without_c1_count[0]


"""
