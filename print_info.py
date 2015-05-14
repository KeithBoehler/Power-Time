#!/usr/local/bin/python

#python script to print time info on LoFASM test data

from lofasm import parse_data as pdat

fname = '20150323_033624.lofasm'

#create crawler object with data starting at location 96
crawler = pdat.LoFASMFileCrawler(fname, start_loc=96)

#print timestamp for first integration
print crawler.time.datetime.strftime('%Y/%d/%m %H:%M:%S')

#move lofasm crawler forward by 25 integrations
crawler.forward(25)

#print new timestamp.
print crawler.time.datetime.strftime('%Y/%d/%m %H:%M:%S')
