#
# author : ajay dsouza
# desc :  A non recursive merge sort with out of place sorting
# O(n log n)
# storage 2N 
#  we could make it efficient to use less than 2N storage
#   but would complicate a simple program
#
#

import numpy as np
import math

# routing to merge two sorted lists in O(N)
def merge(A,B,b,m,e):
   
    # for the last set we can have less than m or e 
    if m > N:
        m = N

    if e > N:
        e = N

    # merge the two lists into B
    i = b
    j = m
    k = b
    while( k < e ):
        if ( j < e and ( i >=m or (A[i]>A[j]) ) ):
            B[k] = A[j]
            j += 1
        else:
            B[k] = A[i]
            i += 1
        k += 1

    return



#list to be sorted
A = np.arange(16,0,-1)
N = len(A)
print('Original List')
print(A)

# out of place sorting - additional space
B = np.empty(len(A))
    
# take the log(N) sets, starting with the smallest set of 1
for i in range(0,math.ceil(math.log(N,2))):
    k = int(math.pow(2,i))
    
    # take every 2 sets of adjacent k elements and merge them
    for j in range(0,N,2*k):
        #merge the two sets our of place
        merge(A,B,j,j+k,j+2*k)

    # copy back the out of place sorted array back to A
    A=list(B)

# print the sorted list
print('Sorted List')
print(A)

