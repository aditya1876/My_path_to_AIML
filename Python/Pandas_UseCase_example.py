print("===============================")
print("=======PandasUseCase=======")
#What to do when you get the data loaded into python?
dataset = pd.read_csv('<filePath>') # load the data

#Number of rows and cols of the data
print(dataset.shape)

# check the shape of data (what kind of data it is? text based of mathematical ect)
print(dataset.dtypes)
#check the first few rows to understand the data better.
print(dataset.head) 

#Describe the data (very useful to get a statistical summary...gives mean, median, mode etc.)
print(dataset.describe())

#Now try to get useful information out of the data.
#Questions like - 
#Write a program to get the list of all countries with a size larger than 2000KMsquare from
#the data provided.
#Is there any correlation between a country's GDP and birth-rates?



#Library to do web scraping - BeautifulSoup, requests

#Library to do datavisualization on browser - Bokeh

#Computer vision using OpenCV
#to install  - pip install opencv-python (huge file)
#import cv2
#img = cv2.imread('<img_path>',0) #0 for grascale image, 1 is for colour image

# Cont from projects - https://elitedatascience.com/learn-python-for-data-science
