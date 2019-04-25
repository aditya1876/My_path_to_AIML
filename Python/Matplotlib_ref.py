print("====================")
print("=======Matplotlib=======")
print("====================")
print("=======Importing=======")
import matplotlib.pyplot as plt
#if matlplotlib is not available, use 'pip install matplotlib' (pip will have to be installed first if not present)

import numpy as np
print("====================")
print("=======Plotting=======")

#plt.plot([1,2,3,4]) #this only providing the y-axis values. x-axis is auto generated if not provided(based on the index values). of course this is not useful without x-axis
#plt.show() #plot is shown in a different figure.

#x_values = [1,2,3,4]
#y_values = [i**2 for i in x_values]
#plt.plot(x_values, y_values)
#plt.show()

x=np.arange(0,5,0.01) #all values form 0 to 5(not included) with step 0.01
#plt.plot(x,[i**2 for i in x])
##plt.show() #smoother graph than before. 

print("====================")
print("=======Multiline Plots=======")

# x = range(10)
# plt.plot(x,[i+10 for i in x],label = "linear")
# plt.plot(x,[i**2 for i in x],label="square")
# plt.plot(x,[i**3 for i in x],label="cubes")
# plt.grid(True)  # to show grids on the graph.
# plt.axis([0,5, 0,130]) # to only show x-axis from 0 to 5 and y-axis from 0 to 130. but use the below 2 lines. it does the same thing but better to understand.
# plt.xlim(0,5)
# plt.ylim(0,130)

#adding lables 
# plt.xlabel("X-axis")
# plt.ylabel("My results")

# #adding title
# plt.title("My fisrt graphs")

# #adding legend
# plt.legend() #also add the lables to the plot() function call above.

#Showing the plot to user
# plt.show()

#saving the plot
# plt.savefig("Myplot1.png")

# import os
# os.remove("Myplot1.png")

#above 3 lines for plot can also be written as plt.plot(x,[i+10 for i in x], x,[i**2 for i in x],x,[i**3 for i in x]) and it would plot the same graph


print("====================")
print("=======Histogram=======")

# y = np.random.randn(100,100) #generates random values as per gaussian distribution with 100 rows and 100 columns.
# # print(y)

# plt.hist(y)
# plt.show() #please note the graphs is not a bar graph it is a histogram.

print("====================")
print("=======Bar graph=======")

# plt.bar([1,2,3,4,6],[10,20,30,40,60])
# plt.show()

# dict1 = {'A':10,'B':20,'C':30,'D':45}
# for i,k in enumerate(dict1):
#     plt.bar(k,i)  #need to enumerate and key value pair is plotted individuall because dictionaries are not iteratable

# plt.show() 


print("====================")
print("=======Pie Chart=======")

# plt.figure(figsize=(3,3))  #give size of pie chart in inches
# plt.pie([10,20,40], labels=['A','B','C'])
# plt.show()


print("====================")
print("=======Scatter Plot=======")

# x=np.random.rand(1000)
# y=np.random.rand(1000)

# plt.scatter(x,y) # prints 2 gaussian points
# plt.show()


print("====================")
print("=======Styling the plot=======")

x=np.arange(1,10)
#Colours in graph
# plt.plot(x, 'y') #y,r,b are the colours for the plot lines in the graph.
# plt.plot(x+5,'r') #colour codes are provided by matplotlib. Google to get the colour codes.
# plt.plot(x+10,'b') 
# plt.show()

#Stying the plot lines
# plt.plot(x,'-',x+5,':', x+10,'--') # '-' = solid line, '--' = dashed line, '-.' = dashdot line, ':'=dotted line
# plt.plot(x,'*',x+5,'o',x+10,'D',x+15,'^',x+20,'s') #to show the data points on the plot
# plt.show() 



