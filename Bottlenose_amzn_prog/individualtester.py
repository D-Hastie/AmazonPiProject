import csv
import bottlenose as BN
import lxml
import datetime
import os
from bs4 import BeautifulSoup
import numpy
import time
import Gnuplot

amazon = BN.Amazon('AKIAIXTJSYDX4JO47FZQ','Jkucw6DFwIHDAjhE8f2XujjGZc65gmA40i/vxZ2U','davihasti-21',Region='UK',MaxQPS=0.8)

i = 0
##starttime = time.time()
# isbns = open('isbns.txt', 'r')
print "Number", "ISBN:","Retail:","New Price:","Used Price:", "Sales Rank:"
# for line in isbns:
isbnclean = '0521880327'
response = amazon.ItemLookup(ItemId=isbnclean, ResponseGroup="Large")
soup = BeautifulSoup(response, "xml")

try:
    newprice=soup.LowestNewPrice.Amount.string
except AttributeError:
    newprice=0
try:
    usedprice=soup.LowestUsedPrice.Amount.string
except AttributeError:
    usedprice=0
try:
    itmisbn =soup.find('ISBN').contents[-1].strip()
except AttributeError:
    itmisbn =0
try:
    retailprice=soup.Price.Amount.string
except AttributeError:
    retailprice= 0
try:
    salesrank=soup.find('SalesRank').contents[-1].strip()
except AttributeError:
    salesrank=0
print itmisbn
#
# time = datetime.datetime.now().strftime("%Y/%m/%d:%H:%M:%S")
# outfile = open('%s.txt' % itmisbn, 'a')
# AmznIds = open('amznids.txt', 'a')
# if os.stat('%s.txt' % itmisbn).st_size==0:
#     outfile.write('{0} {1} {2} {3} {4} {5}\n'.format('Time:', 'ISBN:', 'Retail-Price:', 'Lowest-New-Price:', 'Lowest-Used-Price:','Sales-Rank'))
#     outfile.write('{0} {1} {2} {3} {4} {5}\n'.format(time, itmisbn, retailprice,newprice,usedprice,salesrank))
#     outfile.close()
#     AmznIds.write('{0}\n'.format(itmisbn))
#     AmznIds.close()
# else:
#     outfile.write('{0} {1} {2} {3} {4} {5}\n'.format(time, itmisbn, retailprice,newprice,usedprice,salesrank))
#     outfile.close()
# i = i + 1
# print i, time, itmisbn, retailprice, newprice, usedprice, salesrank

##endtime = time.time()
##progtime =endtime-starttime
##
##print 'RUN TIME:', progtime









