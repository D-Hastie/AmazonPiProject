import csv
import bottlenose as BN
import lxml
import datetime
import os
from bs4 import BeautifulSoup
import numpy
import time
import Gnuplot

amazon = BN.Amazon('AMZNPASSWORD','AMZNSECRETKEY','AMZNUSER',Region='UK',MaxQPS=0.8)

i = 0
##starttime = time.time()
isbns = open('Book1.txt', 'r')
print "Number", "ISBN:"
for line in isbns:
    isbnclean = line.strip()
    response = amazon.ItemLookup(ItemId=isbnclean, ResponseGroup="Large")
    soup = BeautifulSoup(response, "xml")
    try:
        itmisbn=soup.find('ISBN').contents[-1].strip()
    except AttributeError:
        itmisbn =0
    AmznIds = open('amznids.txt', 'a')
    AmznIds.write('{0}\n'.format(itmisbn))
    AmznIds.close()

    i = i + 1
    print i, itmisbn

##endtime = time.time()
##progtime =endtime-starttime
##
##print 'RUN TIME:', progtime
