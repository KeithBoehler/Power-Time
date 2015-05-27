# Python scrip to fill array with the needed time stamps insted of ploting with integrations 
#Here I am putting the arrays together 
import numpy as np
import scipy as spy
import astropy as aspy
import matplotlib.pyplot as plt
import lofasm 
from astropy.time import Time
from lofasm import parse_data as pdat #Gathers the data 

fileName = '20150323_033624.lofasm'
crawler = pdat.LoFASMFileCrawler(fileName, start_loc=96)
hoursArray = []
minutesArray = []
secondsArray = []
totalSeconds = []
start = int(raw_input('What is the starting point of time?(integrations) '))
end = int(raw_input('what is the ending point in time?(integrations) '))
#fill hoursArray
for i in range(start, end):
	#we use the time format and drop everyting that is not hours
	hoursTimeStamp = crawler.time.datetime.strftime('%H')
	#change the time into a integer 
	hours2seconds = (int(hoursTimeStamp))*3600 #convert hours to seconds 
	hoursArray.append(hours2seconds)
	crawler.forward()
#Fill minutesArray
for i in range(start, end):
	#format the time so that we only have minutes 
	minutesTimeStamp = crawler.time.datetime.strftime('%M')
	minutes2seconds = (int(minutesTimeStamp))*60
	minutesArray.append(minutes2seconds)
#Fill Seconds Array 
for i in range(start, end):
	secondsTimeStamp = crawler.time.datetime.strftime('%S')
	seconds = int(secondsTimeStamp)
	secondsArray.append(seconds)
#put all time arrays together 
for i in range(start, end):
	sHours = hoursArray[i]
	sMinutes = minutesArray[i]
	seconds = secondsArray[i]
	Seconds = sHours + sMinutes + seconds
	totalSeconds.append(Seconds)
print totalSeconds







































