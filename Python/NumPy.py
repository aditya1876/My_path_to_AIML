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

a=np.array([1,2,3])

print(a)
