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

pd.set_option('display.mpl_style', 'default')

#Counter variable set.
j = 0
##Iterative initialising section. Comment out for testing on single file. 
isbns = open('amznids.txt', 'r')
for line in isbns:
    isbnclean = line.strip()
#Read Datafile
    
    datafile = ('%s.txt' % isbnclean)
    


    #Read data file in using pandas.
    #For reference, the .txt files headers are:
    # Time: ISBN: Retail-Price: Lowest-New-Price: Lowest-Used-Price: Sales-Rank
    # include the colons and dashes.
    pddata=pd.read_csv(datafile, header=0, delimiter = r'\s+')
    # The complete last row of data.
    # last = pd.DataFrame.tail(pddata, n=1,)

    #The last data entries (most current) in the data file.
    CurrentUsed= pddata.iloc[-1, pddata.columns.get_loc('Lowest-Used-Price:')]
    CurrentTime= pddata.iloc[-1, pddata.columns.get_loc('Time:')]
    CurrentRetail= pddata.iloc[-1, pddata.columns.get_loc('Retail-Price:')]
    CurrentNew= pddata.iloc[-1, pddata.columns.get_loc('Lowest-New-Price:')]
    CurrentSalesRank= pddata.iloc[-1, pddata.columns.get_loc('Sales-Rank')]

    #Print the last data (current) data entries. Only for testing/checking really.
    # print CurrentUsed
    # print CurrentTime
    # print CurrentRetail
    # print CurrentSalesRank
    # print CurrentNew

   
    #Evaluating different column data with panda analysis tools (mean, median etc.)
    # Used Price stats.
    UsedMean = pddata["Lowest-Used-Price:"].mean()
    RollingUsedAvg = pd.rolling_mean(pddata['Lowest-Used-Price:'], window = 10)
    UsedMed = pddata["Lowest-Used-Price:"].median()
    
    
    #New Price stats.
    NewMean = pddata['Lowest-New-Price:'].mean()
    RollingNewAvg= pd.rolling_mean(pddata ['Lowest-New-Price:'], window = 10)
    NewMed = pddata['Lowest-New-Price:'].median()
    
    #Retail box stats.
    RetailMean = pddata['Retail-Price:'].mean()
    RollingRetailAvg = pd.rolling_mean(pddata['Retail-Price:'], window = 10)
    RetailMed = pddata['Retail-Price:'].median()
    
    #Counter incremental increase with each item on list.
    j = j + 1
    #print j
    
    #####Used Price Evaluaion.#####
    ##Profit calculation for Used prices if used costs less than new or retail price.
    #15pcnt referral fee, 4.18 item fee and variable closing (postage) fee, + postage of buying it.
    if CurrentUsed<CurrentNew and CurrentUsed<CurrentRetail and CurrentUsed != 0:
        if UsedMed<NewMed:
            ProfitUsed = (UsedMed*0.85)-443-(CurrentUsed)
            # print 'Potential Used Profit:', ProfitUsed
            ProfitabilityUsed = (ProfitUsed/(CurrentUsed))*100
        if UsedMed>NewMed:
            ProfitUsed = (NewMed*0.80)-443-(CurrentUsed)
            # print 'Potential Used Profit:', ProfitUsed
            ProfitabilityUsed = (ProfitUsed/(CurrentUsed))*100
        if (ProfitUsed > 0):
            print 'Potential Profitable Item:', j
            print 'ISBN:', isbnclean,' Condition = Used - 1' 
            print 'Current Profit Value:', ProfitUsed, ' Approx. Profitability:', ProfitabilityUsed,'%'
            print ' '
            if CurrentUsed > NewMed:
                print 'Check graphing for viability.'
                print ' '
            if (CurrentUsed*1.15)>CurrentNew:
                print 'Potential conflict with New items'
                print 'Will either have to wait to sell, or drop price.'
    if CurrentUsed>CurrentNew and CurrentNew !=0:
    # As current used is greater than new, it won't sell. So calculate the sell price at 15%
    # lower than the New Median price.
        ProfitUsed = ((NewMed*0.85)*0.85)-443-(CurrentUsed)
        ProfitabilityUsed = (ProfitUsed/CurrentUsed)*100
        if ProfitUsed>0:
            print 'Potential Profitable Item:', j
            print 'ISBN:', isbnclean,' Condition = Used - 2' 
            print 'Current Profit Value:', ProfitUsed, ' Approx. Profitability:', ProfitabilityUsed,'%'
            print ' '
    
    #####New Price Evaluation#####
    #15pcnt referral fee, 1.38 item fee and variable closing (postage) fee.
    #2.80 on top of used price for postage costs.
    if CurrentNew<CurrentRetail and CurrentNew !=0:
        ProfitNew = (NewMed*0.85)-443-(CurrentNew)
        ProfitabilityNew = (ProfitNew/(CurrentNew))*100
        if (ProfitNew>0):
            print 'Potential Profitable Item:', j
            print 'ISBN:', isbnclean, ' Condition = New'
            print 'Current Profit Value:', ProfitNew, ' Approx. Profitability:', ProfitabilityNew,'%'
            print ' '
    #Retail Price Evaluation
    #This section differs in pattern from the others.
    #Retail can be purchased, but not sold in the retail box, only sold as 3rd party new.
    if CurrentRetail<CurrentNew and CurrentRetail != 0:
        ProfitRetail = (NewMed*0.85)-443-(CurrentRetail)
        ProfitabilityRetail = (ProfitRetail/CurrentRetail)*100
        if (ProfitRetai>0):
            print 'Potential Profitable Item:', j
            print 'ISBN:', isbnclean, ' Condition = Retai'
            print 'Current Profit Value', ProfitRetail, ' Approx. Profitability:', ProfitabilityRetail, '%'
            print ' '
    
        
