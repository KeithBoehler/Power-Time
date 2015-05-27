# Python scrip to fill array with the needed time stamps insted of ploting with integrations 
#Here I am putting the time arrays together
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
end = int(raw_input('what is the ending point in time?(integrations) '))
for i in range(0, end):
	# Gathering time stamps 
	hoursTimeStamp = crawler.time.datetime.strftime('%H')
	minutesTimeStamp = crawler.time.datetime.strftime('%M')
	secondsTimeStamp = crawler.time.datetime.strftime('%S')
	# Convert time stamps into seconds 
	hours2seconds = (int(hoursTimeStamp))*3600
	minutes2seconds = (int(minutesTimeStamp))*60
	seconds = int(secondsTimeStamp)
	# Fill the arrays 
	hoursArray.append(hours2seconds)
	minutesArray.append(minutes2seconds)
	secondsArray.append(seconds)
	# Combine arrays into one complete array
	sHours = hoursArray[i]
	sMinutes = minutesArray[i]
	seconds = secondsArray[i]
	Seconds = sHours + sMinutes + seconds
	totalSeconds.append(Seconds)
	# Gather the next integration
	crawler.forward()
print totalSeconds

