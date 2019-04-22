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

#cont from https://www.youtube.com/watch?v=vaysJAMDaZw&t=782s  4:50 hrs
# https://elitedatascience.com/learn-python-for-data-science
# https://github.com/aditya1876/My_path_to_AIML
# https://www.google.co.nz/search?q=escape+char+in+python&oq=escape+char+in+python&aqs=chrome..69i57j0l3.7772j0j7&client=ubuntu&sourceid=chrome&ie=UTF-8


