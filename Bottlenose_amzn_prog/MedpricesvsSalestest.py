import csv
import bottlenose as BN
import lxml
import os
from bs4 import BeautifulSoup
import numpy
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pylab
from datetime import datetime
import pandas as pd

#This is the graphing code for use with the base program.
#It will create a series of graphs onto a single figure containing relevant data 
#time series data from the base program.
#The first section sets up the data read in.
#The second section sets up the graph outputs.


#Initialise Counter Variable
j = 0
##starttime = time.time()
########FIRST SECTION#######
isbns = open('AmznIds.txt', 'r')
for line in isbns:
    isbnclean = line.strip()
    ##Read Datafile
    datafile = ('%s.txt' % isbnclean)
    months = dates.MonthLocator()
    timefmt = '%Y/%m/%d:%H:%M:%S'
    
    
    pddata=pd.read_csv(datafile, header=0, delimiter = r'\s+')
    #Assign Variables value from data array using col header names.
    
    UsedMedian = pddata["Lowest-Used-Price:"].median()
    SalesAvg = pddata['Sales-Rank'].mean()
    outfile = open('MedPricevsSales.txt', 'a')
    if SalesAvg == 0:
        continue
      
    if os.stat('MedPricevsSales.txt').st_size==0:
        outfile.write('{0} {1}\n'.format('UsedMedian:', 'SalesAvg:'))
        outfile.write('{0} {1}\n'.format(UsedMedian, SalesAvg))
        outfile.close()
    else:
        outfile.write('{0} {1}\n'.format(UsedMedian, SalesAvg))
        outfile.close()
        
print 'Done'

names = ['UsedPrice', 'SalesRank']
## Read data from file to array 'data'.
data = np.genfromtxt('MedPricevsSales.txt', skip_header=1, names = ['UsedPrice', 'SalesRank'])

#Assign Variables value from data array using col header names.
CollabMedPrice = data[names[0]]
CollabSalesRank = data[names[1]]

#######Second Section#########
    #Create figure, specify arguments size etc.
fig = plt.figure(figsize=(5,5),dpi=150,edgecolor='k')
fig.set_tight_layout(True)

# Sales Rank and Used Price vs Time graph
ax1 = plt.subplot2grid((3,3), (0,0), colspan = 3, rowspan = 3, axisbg='#A9A9A9')
ax1.plot(CollabSalesRank, CollabMedPrice, color='#4682B4', marker='.', linestyle ='None')
ax1.set_ylabel('Median Price', color = '#4682B4')
ax1.set_xlabel('SalesRank Avg.')
ax1.set_title('MedianPrice VS SalesRank Avg')
ax1.set_xscale('log')
ax1.set_ylim(0,10000)
#Rotation of axis markers.
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=25)


#Save to file of ISBN + pdf
plt.savefig('MedPricevsSales.pdf')
#Show plt, don't use when running full isbn list.
plt.show()
#Close All
plt.close(fig)
print ' Finished'