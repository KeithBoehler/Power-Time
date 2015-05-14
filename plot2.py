import numpy as np
import scipy as spy
import astropy as aspy
import matplotlib.pyplot as plt
import lofasm 
from astropy.time import Time
from lofasm import parse_data as pdat #Gathers the data 


#Data Input ####################################################
fileName = '20150323_033624.lofasm'

#Get the corrolation.
Corrolation = raw_input('Enter the disired corolation. Ex) AA, BB, CC, DD ')
print Corrolation
timeArray = [] #creates empty array to be filled later

def Times():
	timeArray = [] #creates empty array to be filled later
	
	crawler = pdat.LoFASMFileCrawler(fileName, start_loc=96)#create cralwer object with our file

	for i in range(0, 5): 
		#This would be equivalent to the first time stamp in your code
		currentTime = crawler.time.datetime.strftime('%Y-%m-%dT%H:%M:%-s.00')#Year Month Day : Hour Minute Second
		print currentTime
		currentTime = Time(currentTime,format = 'isot', scale='utc').mjd
#		currentTime = currentTime.time.datetime.mjd
		timeArray.append(currentTime) #1st time stamp is written to zero index of array. In the second comming of the array the timestamp that has move in time is written into index 1. 
		crawler.forward()#we go foward in time by one.
	print 'Time'
	#print timeArray
	
	return timeArray


#print Times()#Invoking the function that will procces the time. 

#Def for power
def Power():
	powerTimeS = []#Array to be filled with power integrations
	crawler = pdat.LoFASMFileCrawler(fileName, start_loc=96)#create cralwer object
	for i in range(0, 5):
		Power = crawler.autos['AA']
		powerTimeS.append(Power)
		crawler.forward()
	print 'power'
	print powerTimeS
	return powerTimeS

x = Power()
y = Times()

plt.plot(x, y, '-')
plt.show()
#Def for plotting power vs time































