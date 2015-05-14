# Python scrip to fill array with the needed time stamps insted of ploting with integrations 

import numpy as np
import scipy as spy
import astropy as aspy
import matplotlib.pyplot as plt
import lofasm 
from astropy.time import Time
from lofasm import parse_data as pdat #Gathers the data 

from Tkinter import *
from datetime import datetime
from datetime import timedelta
import math

fileName = '20150323_033624.lofasm'

crawler = pdat.LoFASMFileCrawler(fileName, start_loc=96)

timeArray = [] 

for i in range(0, 20):
	#We dropped the date and now we just have time
	timeStamp = crawler.time.datetime.strftime('%H:%M:%S')
	#Change the time into a float. 
	secondsTimeStamp = timeStamp.total_seconds()
	timeArray.append(secondsTimeStamp)
	#Change the time into a float. 

print timeArray
