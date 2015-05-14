import numpy as np
import scipy as spy
import astropy as aspy
import matplotlib.pyplot as plt
import lofasm 
from astropy.time import Time
from lofasm import parse_data as pdat #Gathers the data 

fileName = '20150323_033624.lofasm'
f = open('20150323_033624.lofasm','rb')


#create crawler object with data starting at location 96
#
crawler = pdat.LoFASMFileCrawler(fileName, start_loc=96)
#Dictrionary with info about header. fstart print spesific header. fspet has a decimal first 'digit' . 
hdr_dict = pdat.parse_file_header(f)
numberOfIntegrations = pdat.get_number_of_integrations(f)
print hdr_dict
print 'numberOfIntegrations'
print numberOfIntegrations

powerArray = []
timeArray = []
#MHz = raw_input('Enter the needed frequency in MHZ ')
 
#powerTimeS.append(Power)

while True:

	Corrolation = raw_input('Enter the disired corolation. Ex) AA, BB, CC, DD ')
	for t in range(0, 100):
		#
		powerSpectrum = crawler.autos[Corrolation]
		#
		bin = 500
		powerArray.append(powerSpectrum[bin])#500 is the 500th bin(spot on the array) 
		crawler.forward()

	n = raw_input("Would you like to plot another Corrolation? Y / N:")
	if n.strip() == 'N':
		break
	

plt.plot(10*np.log10(powerArray))
plt.ylabel('Power')
plt.xlabel('Time')
plt.title('Power vs Time')
plt.show()