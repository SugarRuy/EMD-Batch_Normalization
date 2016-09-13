import numpy as np
import scipy.optimize
import test
import emd

N = 4
for epoch in range(10)
    withBN = np.load('withBN_%d.npz'%epoch);
    withoutBN = np.load('withoutBN_%d.npz'%epoch)

    with_index = ["arr_0", "arr_1","arr_2","arr_3","arr_4","arr_5"]
    without_index = ["arr_0", "arr_1","arr_2","arr_3","arr_4","arr_5","arr_6"]
    with_name = ["input","conv1","pool1","conv2","pool2","conv3"]
    without_name = ["input","conv1","pool1","drop1","conv2","pool2","conv3"]

    for i in range(5):
	with_front = withBN[with_index[i]]
	with_back = withBN[with_index[i+1]]
	with_front_value = test.getRepresentValue(with_front, N)
	with_back_value = test.getRepresentValue(with_back, N)
	with_front_count = test.getNsplitCount(with_front, N)
	with_back_count = test.getNsplitCount(with_back, N)
	print "with BN(%s-%s)"%( with_name[i], with_name[i+1])
	for j in range(1):
	    #print "Sample %d"%(j) 
	    print emd.emd(with_front_value[j].tolist(), with_back_value[j].tolist(), with_front_count[j].tolist(), with_back_count[j].tolist())

    for i in range(6):
	without_front = withoutBN[without_index[i]]
	without_back = withoutBN[without_index[i+1]]
	without_front_value = test.getRepresentValue(without_front, N)
	without_back_value = test.getRepresentValue(without_back, N)
	without_front_count = test.getNsplitCount(without_front, N)
	without_back_count = test.getNsplitCount(without_back, N)
	print "without BN(%s-%s)"%( without_name[i], without_name[i+1])
	for j in range(1):
	    #print "Sample %d"%(j)
	    print emd.emd(without_front_value[j].tolist(), without_back_value[j].tolist(), without_front_count[j].tolist(), without_back_count[j].tolist())


"""
with_in = withBN['arr_0']
with_c1 = withBN['arr_1']
with_p1 = withBN['arr_2']
with_c2 = withBN['arr_3']
with_p2 = withBN['arr_4']
with_c3 = withBN['arr_5']


without_in = withoutBN['arr_0']
without_c1 = withoutBN['arr_1']
without_p1 = withoutBN['arr_2']
without_d1 = withoutBN['arr_3']
without_c2 = withoutBN['arr_4']
without_p2 = withoutBN['arr_5']
without_c3 = withoutBN['arr_6']

weights1 = np.array(50*[1/50])
weights2 = np.array(50*[1/50])

#input and conv1
with_in_value = test.getRepresentValue(with_in, 4)
with_c1_value = test.getRepresentValue(with_c1, 4)
with_p1_value = test.getRepresentValue(with_p1, 4)
with_c2_value = test.getRepresentValue(with_c2, 4)
with_p2_value = test.getRepresentValue(with_p2, 4)
with_c3_value = test.getRepresentValue(with_c3, 4)

with_in_count = test.getNsplitCount(with_in, 4)
with_c1_count = test.getNsplitCount(with_c1, 4)
with_p1_count = test.getNsplitCount(with_p1, 4)
with_c2_count = test.getNsplitCount(with_c2, 4)
with_p2_count = test.getNsplitCount(with_p2, 4)
with_c3_count = test.getNsplitCount(with_c3, 4)




without_in_value = test.getRepresentValue(without_in, 4)
without_c1_value = test.getRepresentValue(without_c1, 4)
without_p1_value = test.getRepresentValue(without_p1, 4)
without_d1_value = test.getRepresentValue(without_d1, 4)
without_c2_value = test.getRepresentValue(without_c2, 4)
without_p2_value = test.getRepresentValue(without_p2, 4)
without_c3_value = test.getRepresentValue(without_c3, 4)

without_in_count = test.getNsplitCount(without_in, 4)
without_c1_count = test.getNsplitCount(without_c1, 4)
without_p1_count = test.getNsplitCount(without_p1, 4)
without_d1_count = test.getNsplitCount(without_d1, 4)
without_c2_count = test.getNsplitCount(without_c2, 4)
without_p2_count = test.getNsplitCount(without_p2, 4)
without_c3_count = test.getNsplitCount(without_c3, 4)




print 'with BN(input-conv1):'
print emd.emd(with_in_value[0].tolist(), with_c1_value[0].tolist(), with_in_count[0].tolist(), with_c1_count[0].tolist())
print 'without BN(input-conv1):'
print emd.emd(without_in_value[0].tolist(), without_c1_value[0].tolist(), without_in_count[0].tolist(), without_c1_count[0].tolist())
print 'with BN(conv1-pool1):'
print emd.emd(with_c1_value[0].tolist(), with_p1_value[0].tolist(), with_c1_count[0].tolist(), with_p1_count[0].tolist())
"""






