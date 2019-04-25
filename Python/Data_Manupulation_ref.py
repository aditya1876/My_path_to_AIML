print("===============================")
print("=======Data Manupulation=======")
print("===============================")

import pandas as pd
import numpy as np

#Ndim() returns the dimentiionality of the data.
t=pd.Series(np.arange(1,10)) #series of numbers from 1 to 100
# print(t.ndim) # 1
t1 = pd.DataFrame({'a':pd.Series(np.arange(1,10)),'b':pd.Series(np.arange(1,12))})
# print(t1)
# print(t1.ndim)

#axes provides info about the data.
# print(t)
# print(t.axes)
# print(t1)
# print(t1.axes)

#Values prints the data
# print(t)
# print(t.values)
# print(t1)
# print(t1.values)

#head gives the first 5 rows of data from the dataset
# # print(t)
# print(t.head())
# # print(t1)
# print(t1.head())
#to print more rows, pass it a value like head(10)

#head gives the last 5 rows of data from the dataset
# print(t)
#print(t.tail())
# print(t1)
# print(t1.tail())
#to print more rows, pass it a value like tail(10)

print("===============================")
print("=======Sum,std=======")

# t=pd.DataFrame({'odd':pd.Series(np.arange(1,100,2)), 'even':pd.Series(np.arange(0,100,2))})
# print(t['odd'].head())
# print(t['even'].head())
# #print sum
# print(t.sum())

# #get standard deviation
# print(t.std())

print("===============================")
print("=======Iterating a dataFrame=======")
# d=pd.DataFrame(np.random.rand(5,4) ,columns=('c1','c2','c3','c4')) #creates a matrix of 5rowsX4 cols of random values
# print(d)

# for k,v in d.iteritems():  #iteritems iterates over the columns
#     print(k,v)

# for k,v in d.iterrows():  #iterrows iterates over the rows
#     print(k,v)   

# for row in d.itertuples(): #prints tuple for each row of data
#     print(row) 


print("===============================")
print("=======Group By=======")
world_cup={'team': ['a','a','b','c','d','e','c','c','c','b','c'],
            'rank':[7,7,2,1,6,4,1,1,1,2,1],
            'year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df = pd.DataFrame(world_cup)
# print(df)
# print(df.groupby('team').groups)  #getting groups based on 'team'
# print(df.groupby(['team','rank']).groups)  #grouping on multiple items.

# for name, group in df.groupby('team'):
#     print ('Group name : '+ name)
#     print (group)
#     print ("===========================")

# df1 = df.groupby('team')
# print(df1.get_group('a')) # to get data of a single group item

print("===============================")
print("=======Concatination and Append=======")

# l = pd.DataFrame({'keys':['K0','K1','K2','K3'],
#                 'A':[1,2,3,4],
#                 'B':[10,20,30,40],
#                 'C':[11,21,31,41]})
# r = pd.DataFrame({'keys':['K0','K1','K2','K3'],
#                 'D':[12,22,32,42],
#                 'E':[13,23,33,43]})

# print(pd.concat([l,r])) #the 'keys' column is just to understand what is happening it is not required for
# #the code to run.

# print(pd.concat([l,r], axis=0)) #concatinates along the rows (default value)
# print(pd.concat([l,r], axis=1)) #contatinates along the columns


# print(l.append(r)) # Appending.....
# print(r.append(l))

print("===============================")
print("=======Merging=======")
l = pd.DataFrame({'keys':['K0','K1','K2','K3','K4'],
                'A':[1,2,3,4,5],
                'B':[10,20,30,40,50],
                'C':[11,21,31,41,51]})
r = pd.DataFrame({'keys':['K0','K1','K2','K3','K6'],
                'D':[12,22,32,42,62],
                'E':[13,23,33,43,63]})

print(pd.merge(l,r, on='keys')) # merging on a column

print(pd.merge(l,r, on='keys', how='left')) # left join - joins the 2 objects based on the key from 
#left object.
print(pd.merge(l,r, on='keys', how='right')) #right join - joins the objects based on the key from right
#object

print(pd.merge(l,r, on='keys', how='outer')) # outer join - based on full union of the 'keys'columns.

print(pd.merge(l,r, on='keys', how='inner')) # inner join - based on AND/intersection of 'keys' columns
