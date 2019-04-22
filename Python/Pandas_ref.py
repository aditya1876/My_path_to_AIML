print("=======PANDAS=======")
print("====================")

print("====================")
print("=======Importing pandas=======")
import pandas as pa
import numpy as np
#if not available, then install pandas by running the following command in the terminal
#pip install pandas    (must have pip installed)

print("====================")
print("=======Data Structures=======")
#Series --> Labled, homogenous array , size immutable(cant change data size after creation), value mutable (can change the value of data after creation) -- 1-D array
#DataFrames --> Labled, Heterogenous , size mutable tabular data, value mutable -- 2-D array
#Panels --> Labled, size mutable, value mutable -- 3-D array

print("====================")
print("=======Series=======")
#it is a 1-d array of single data type.
#value -mutable (values can be changed after creation)
#size immutable (size of array cannot be changed)
#Data type can be anything (ndarray, lists, constants, series, dicts etc)
#Indexes must be unique hashble and have the same length as data.(defaults to np.arrange(n) if nothing passed)
#Data type of each column is inferred if not provided
#Shallow copies by default (but can be set to deep copy) 

ser = pa.Series() #series function creates a new series.
print(ser) #Series([], dtype: float64)

a = np.array([10,20,30,40,50])
ser1 = pa.Series(a)
print(ser1)

dict1 = {'a':1,'b':2,'c':3}
ser2 = pa.Series(dict1)
print(ser2)

#slicing works as usual
print(ser1[:2])
print(ser2[1:2])
print(ser1[-1:])
print(ser1[:-2])

print("====================")
print("=======DataFrames=======")
#it is a 2-d array with data alligned in rows and cols.
#value -mutable 
#size mutable 
#called using the following constructor
#pandas.DataFrame(data, index, dtype, copy)
#Data can be of multiple data types (ndarray, lists, constants, series, dicts etc)
#Indexes are the row col references.(defaults to np.arrange(n) if nothing passed)
#Data type of each column is inferred if not provided
#Shallow copies by default (but can be set to deep copy) 

a=[10,20,30,40]
print(a)
df = pa.DataFrame(a)
print (df)

dict1 = [{'a':10,'b':20,'c':30,'d':40},{'a':11, 'b':21, 'c':31,'d':41},{'a':12, 'b':22, 'c':32,'e':52}] #notice that d value is not provided and e is provided
df = pa.DataFrame(dict1)
print(df)

a=[[1,2],[3,4],[5,6,7]]
df=pa.DataFrame(a)
print(df)

dict2=[{'a':10,'b':20},{'a':11,'b':21,'c':31}]
df=pa.DataFrame(dict2,index=['first','second'])
print(df)

#converitng a dictionary of pandas.Series() into panda.DataFrame()
data = {
    'stu1':pa.Series([10,20,30],index=['maths','physics','chem']),
    'stu2':pa.Series([11,21,31,41],index=['maths','physics','chem','bio'])
}
df= pa.DataFrame(data)
print(df)

#adding a new column of data to the same dataframe
df['stu3']=pa.Series([12,22,32,42], index=['maths','physics','chem','bio']) #adding 1 more data point i.e 51 with 'eng' will be ignored. see append() below
print(df)

#deleting data
#del df['three']
#print(df)

#get the removed data only
#df1 = df.pop('three')
#print(df1)

#get specific data
print(df.loc['maths'])
print(df.loc['physics'])

print(df.iloc[2])  #iloc[] can be used if row no is to be provided otherwise the row label/index need to be provided

#adding a new row to the DataFrame
df = df.append(pa.DataFrame([[35,36,37]],columns=['stu1','stu2','stu3'])) #notice new keyword columms
print(df)

#drop can be used to drop a row
#df = df.drop('maths')
#print (df)

print("====================")
print("=======Importing and Exporting Data=======")

#reading CSV
table = pa.read_csv("test.csv")
print(table)

#writinng to CSV
df.to_csv("test.csv")

#import os
#os.remove("test.csv")

#similarly for excel as well
#to read - table = pa.read_excel("<path to excel>")
#to write - df.to_excel("<path to exce")


print("====================")
print("=======PANDAS=======")

