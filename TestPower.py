from lofasm import parse_data as pdat
import numpy as np
fileName = '20150323_033624.lofasm'

#create crawler object with data starting at location 96
crawler = pdat.LoFASMFileCrawler(fileName, start_loc=96)

#Print the first power integration 
#x = (10)*np.log10(crawler.autos['AA']) #Error. Divide by zero. [-inf -inf.... -inf]
x = crawler.autos['AA']

crawler.forward()

x = crawler.autos['AA'] 





