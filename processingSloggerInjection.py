# Script for the analysis of injection attacks on sensor-based continuous authentication for smartphones
# This script makes use of Sherlock dataset (http://bigdata.ise.bgu.ac.il/sherlock/#/)
# This script focuses on processing MOA results in accelerometer and gyroscope and location data after Slogger injection
# AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
# Version: 2020-06-15

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors as mcolors
import sys
import csv
import os
dir = str(sys.argv[1])

#These for alg KNN
data1 = [0 for j in xrange(4)]
data2 = [0 for j in xrange(4)]

#These for alg HAT
data3 = [0 for j in xrange(4)]
data4 = [0 for j in xrange(4)]
storeInType=0
for file in os.listdir(dir):
	lineLen=0
	uselessName,locGyr,typeInj,typeW,typePercentag,typeAlg = file.strip().split('_')
	typeAlgo=typeAlg[0:len(typeAlg)-4]
	
	if typeW=='w1000' and locGyr=='T2':
		storeInType=0
	elif typeW=='w10000' and locGyr=='T2':
		storeInType=1
	elif typeW=='w1000' and locGyr=='T1':
		storeInType=2
	elif typeW=='w10000' and locGyr=='T1':
		storeInType=3
		
	fileOpen=dir+file
	valueLine=0
	with open(fileOpen) as infile:
		for line in infile:
			lineElements= line.strip().split(' ')
			if lineElements[0]=='10000' or lineElements[0]=='1000':
				if typeAlgo=='KNN':
				#3=TN & 5=FP
					if float(lineElements[3]) > 100.0:
						data1[storeInType]=140
					else:
						data1[storeInType]=float(lineElements[3])
					data2[storeInType]=float(lineElements[5])
				else:
					if float(lineElements[3]) > 100.0:
						data3[storeInType]=140
					else: 
						data3[storeInType]=float(lineElements[3])
					data4[storeInType]=float(lineElements[5])
		


		
fig, ax = plt.subplots()
n_groups = 4
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8



rects1 = plt.bar(index, data1, bar_width,alpha=opacity,color='#00796B',label='FITN - KNN')
 
rects2 = plt.bar(index + bar_width, data2, bar_width,alpha=opacity,color='#48C9B0',label='FIFP - KNN')

rects3 = plt.bar(index + (bar_width*2), data3, bar_width,alpha=opacity,color='#CD5C5C',label='FITN - HAT')
 
rects4 = plt.bar(index + (bar_width*3), data4, bar_width,alpha=opacity,color='#FFA07A',label='FIFP - HAT')

print data1
print data2
print data3
print data4
plt.ylabel('Time (min)')

plt.xticks(index + bar_width, ('Gyr+Acc w10^3','Gyr+Acc w10^4','Loc w10^3','Loc w10^4'),rotation=0)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
 
plt.tight_layout()
plt.axhline(y=120, color='r', linestyle='-')
plt.show()