#NumPy
#=================

print("=======DATA ANALYSIS=======")
#RAW data > Transform into desired format > Clean the transformed data > prepare a model > Analyse trends and make decisions

print("=======NumPy=======")

print("=======Installation=======") 
#In terminal - pip install numpy 
#if you need pip installed first - sudo apt install python-pip


print("==========================")
print("=======NumPy Array=======") 
#ndarry is a multi-dimentional array oject consisting of 2 parts - actual data + metadata about the data.
#works like a sequence in python, starting from 0

#Each element of numPy array is an object of data-type called 'dtype'
#whenever an element is extracted from the array, the data type of the array gets linked with the element as well.

import numpy as np

arr = [1,2,3]
a=np.array(arr)

print(arr) #[1,2,3]
print(a) #[1 2 3]  notice the o/p of the np array a
print(type(a)) #<type 'numpy.ndarray'>

b= np.array([[1,2],[3,4]])
print(b) # notice the way o/p is dispalyed. If both sub-arrays are not same length, then entire array is treated like a single dimentional array

print(np.arange(0,5)) # [0 1 2 3 4]

b=np.zeros((5,5)) # creates a 5X5 array of '0'
print(b)

b=np.linspace(0, 20, 5)  #linspace - lenierly spaced vector  -- syntax linspace(<start>,<stop>,<no of steps>) note the last arg is 'number of steps and not the 
#value of each step 
print(b)

b=[1,2,3]
c=np.asarray(b) #converts python list into ndarrays
print(c) # [1 2 3]

d=np.zeros(8)
print(d)
print(d.reshape(2,2,2))
print(d.reshape(2,4))
print(d.reshape(4,2))
print(d.reshape(8,1))
print(d.reshape(1,8))
#print(d.reshape(4,4)) # this will throw error as 4x4 array requires 16 elements and we only have 8

c=d.reshape(2,2,2)
print(c)
print(c.ravel()) # flattens the array back to single line.

e=np.empty([3,5], dtype=int) #creates an uninitialized array of the dimension provided. Elements are set to random values.
print(e)

print("==========================")
print("=======NumPy Array - Accessing the elements=======") 

a=np.arange(0,10) #indexing starts from zero
print(a)
print(a[2]) #3rd element
print(type(a[2]))
print(a[2]+5) #allows added elements even though a[2] and 5 are not same data type. This is handeled by python
print(type(a[2]+5)) # python converts 5 into the np data type and then adds.

print("==========================")
print("=======NumPy Array - Slicing=======") 

a=np.arange(20)
print(a)
sli = slice(1,10,2) #start, stop, step. The slice object is created here (sli) by providing the parameters to slice()

print(a[sli]) #[1 3 5 7 9]
print(a[3:5]) #note normal list slicing and sequensing also work [3 4]
print(a[17:]) #[17 18 19]
print(a[:3]) # [0 1 2]
print(a[-4:]) #[16 17 18 19]
print(a[:-17]) #[0 1 2]

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[0:2,0:2])
print(b[0:1,0:2])
print(b[0:2,0:1])
print(b[0:3,:-1])
print(b[0:5,1:7]) #does not error out. prints the max possible

print("=======Attributes=======")

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)

print(b.shape) # prints teh rowsxcol value of array
print(b.ndim) # no of array dimensions. Here it is a 2-d array
print(b.itemsize) #length of each element of array in bytes

print("==========================")
print("=======Reading and writing from txt files=======")

#a = np.arange(20)
a = np.array([[1,2],[3,4]])
print(a)
np.savetxt('text1.txt', a) #saves the array arr data into the text1 file.
arr = np.loadtxt('text1.txt') #loads data from txt file into the ndarray arr automatically
print(arr)

#to save as .csv delimited with comma do the following
np.savetxt('text2.csv', a, delimiter=',') #saves value of a into a csv file.
arr2 = np.genfromtxt('text2.csv',delimiter=',') #loadtxt does not work here.
print(arr2)

import os

os.remove('text1.txt')
os.remove('text2.csv')
