import numpy as np
import matplotlib.pyplot as plt
import pylab
import datetime as datetime
with open(datafile) as f:
	data=f.read()
datafile = '0230723217.txt'
plotfile = '0230723217.png'

convertfunc = datetime.datetime.strftime('%Y/%m/%d:%H:%M:%S')

col_headers = ["Time", "ISBN", "Retail", "NewPrice", "LowPrice", "Rank"]

dd = [(a, 'd') for a in col_headers[:-1]] + [(col_headers[-1], 'object')]

datalist = np.genfromtxt(datafile, skip_header=1, dtype='i8')

plt.plotfile(datafile, cols=(5,6), names=('UsedPrice', 'Rank'), marker='o')

for data in datalist:
    print data
    pylab.plot(data[:,4], data[:,5])


plt.xlabel('Time')
plt.ylabel('Rank')
plt.title('Rank over Time')
plt.grid(True)
plt.savefig('rankvstime.png')
plt.show()
