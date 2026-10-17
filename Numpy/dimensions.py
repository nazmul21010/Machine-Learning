import numpy as np

arr=np.array([1,5,8,4,6,9])#1D array
arr2=np.array([[1,8,5,6,8,4,2],[4,9,5,3,3,5,9]])#2D array
arr3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])#3D array
arr4=np.array(89)
print("Print the dimensions of the arrays")
print(arr4)
print("\n")
print(arr)
print("\n")
print(arr2)
print("\n")
print(arr3)

print("check Dimensions \n")
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)