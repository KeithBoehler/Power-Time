import numpy as np
import scipy as spy
import astropy as aspy
import matplotlib.pyplot as plt
import lofasm 
import astropy.time
from lofasm import parse_data as pdat #Gathers the data 


#text_file = open("20150323_033624.lofasm", "r")#opens the text file with variable name text_file and the r stands for read. Must be in quaotes 
#print text_file.read()#reads the whole file
#text_file.close()#closes the file that we are working with. 

#Data Input ####################################################
fileName = '20150323_033624.lofasm'

#Get the corrolation.
Corrolation = raw_input('Enter the disired corolation. Ex) AA, BB, CC, DD ')


filterBank= []

crawler = pdat.LoFASMFileCrawler(fileName, scan_file=True)#create cralwer object with our file

x = (10)*np.log10(crawler.autos[Corrolation])

plt.ylabel('Power')
plt.xlabel('Frequency')
plt.title('PowerVsFrequency')

plt.plot(x)

plt.show()
####################################################################











#creat new array, from channels of next integration. plot how htis changes in time. Take data, acumilate data avg and fit to a model. 

#next step load many integrations and plot power of a single channel over time. ex. plot at 50MHz show it from one integration to the next. One point from each array, load next integration save it to an array and plot this in a neew array., 

#think about ploting a group of channels. Make it flexabile to other channels. 



#time. >>http://astropy.readthedocs.org/en/latest/time/ This is the link for time stuff
#UTCtime = pdat.parse_filename(fileName) #Something does not exist of needs to be imported expliciedly. Probably does not excist. I am attempting to get UTC time stamp to convert to siderial. This is a string so be sure to convert into something that can be worked with as time.  
#print UTCtime
#Siderial = Time('UTCtime')
#Siderial = UTCtime.sidereal_time('apparent','greenwich')
#print Siderial
