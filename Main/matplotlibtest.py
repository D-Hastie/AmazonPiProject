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
    #Col Headers
    names = ['Time', 'ISBN', 'Retail', 'NewPrice', 'UsedPrice', 'SalesRank']
    ## Read data from file to array 'data'.
    data = np.genfromtxt(datafile, skip_header=1, dtype="O,S11,i8,i8,i8,i8", names = ['Timestamp', 'ISBN', 'Retail', 'NewPrice', 'UsedPrice', 'SalesRank'])
    
    #Assign Variables value from data array using col header names.
    Time = [datetime.strptime(i, timefmt) for i in data['Timestamp']]
    Retail = data[names[2]]
    NewPrice = data[names[3]]
    UsedPrice = data[names[4]]
    SalesRank  = data[names[5]]
    ISBN = data[names[1]]
    
#######Second Section#########    
    #Create figure, specify arguments size etc.
    fig = plt.figure(figsize=(15,15),dpi=150,edgecolor='k')
    fig.set_tight_layout(True)

    # Sales Rank and Used Price vs Time graph
    ax1 = plt.subplot2grid((9,3), (0,0), colspan = 3, rowspan = 3, axisbg='#A9A9A9')
    ax1.plot(Time, SalesRank, color='#4682B4')
    ax1.set_ylabel('SalesRank', color = '#4682B4')
    ax1.set_title('Rank vs Time, Used Price vs Time')
    ax2 = ax1.twinx()
    ax2.plot(Time, UsedPrice, color ='#B22222')
    ax2.set_ylabel('Used Price', color = '#B22222')
    ax2.set_ylim(0,10000)

    # Sales Rank and New Price vs Time graph
    ax3 = plt.subplot2grid((9,3), (3,0), colspan = 3, rowspan = 3, axisbg='#A9A9A9')
    ax3.plot(Time, SalesRank, color='#4682B4')
    ax3.set_ylabel('SalesRank', color = '#4682B4')
    ax3.set_title('Rank vs Time, New Price vs Time')
    ax4 = ax3.twinx()
    ax4.plot(Time, NewPrice, color ='#FFD700')
    ax4.set_ylabel('New Price', color = '#FFD700')
    ax4.set_ylim(0,10000)

    # Sales Rank and Retail Price vs Time graph
    ax5 = plt.subplot2grid((9,3), (6,0), colspan = 3, rowspan = 3, axisbg ='#A9A9A9')
    ax5.plot(Time, SalesRank, color='#4682B4')
    ax5.set_ylabel('SalesRank', color = '#4682B4')
    ax5.set_title('Rank vs Time, Retail vs Time')
    ax6 = ax5.twinx()
    ax6.plot(Time, Retail, color ='#008000')
    ax6.set_ylabel('Retail ', color = '#008000')
    ax6.set_ylim(0,10000)

    #Rotation of axis markers.
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=25)
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=25)
    plt.setp(ax5.xaxis.get_majorticklabels(), rotation=25)

    #Counter
    j = j + 1
    print 'Number:', j
    #Save to file of ISBN + pdf
    plt.savefig('./PDFS/%s.pdf' % isbnclean)
    #Show plt, don't use when running full isbn list.
    #plt.show()
    #Close All
    plt.close(fig)
