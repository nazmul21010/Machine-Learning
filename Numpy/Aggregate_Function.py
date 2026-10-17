import numpy as np

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

#print(np.sum(arr))
#print(np.sum(arr,axis=0))
#print(np.sum(arr,axis=1))
#print(np.mean(arr))

# Standard Deviation Step 1: find the mean, 
# Step 2: find the difference of each element from the mean, 
# Step 3: square the differences, 
# Step 4: find the mean of the squared differences, 
# Step 5: take the square root of the mean of the squared differences 
#print(np.std(arr))

#print(np.var(arr))#standerd derivation=sqrt(variance)

#print(np.min(arr))
#print(np.max(arr))
#print(np.argmin(arr))#find the index of the minimum value in the array
print(np.argmax(arr))#find the index of the maximum value in the array

