# Script for the analysis of injection attacks on sensor-based continuous authentication for smartphones
# This script makes use of Sherlock dataset (http://bigdata.ise.bgu.ac.il/sherlock/#/)
# This script focuses on doing Slogger injection in location or gyroscope and accelerometer data
# AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
# Version: 2020-06-15
import csv

import os
import csv
import sys
from random import randint
import random
from math import ceil

dirOutput = sys.argv[1]
dir = sys.argv[2]
#posUserId-last column (it starts in 0 which means that it should be equal to the number of columns -1)
posUserId=int(sys.argv[3])
#Percentage of lines after which the injection should start
percentageLinesBeforeInjection=int(sys.argv[4])
#0 means percentage is used
linesBeforeInjection=int(sys.argv[5])
#The input parameter corresponds to the width in MAO
#max value of lines in file = width of MOA + injectedLines + 1
width=int(sys.argv[6])
maxLines=width+linesBeforeInjection+1
#0 means location and 1 acc+gyr --this is done to avoid negative numbers in data for using MOA
locGyrAcc=int(sys.argv[7])
#Version number of the file
version=int(sys.argv[8])
#Percentage of lines of the file to start creating the file
numLineToStart=int(sys.argv[9])

#From this array the location of UserId will become the new UserId
newUsersId=['1748983473209579185','306193130034809840','8313018476638449002','3793829844934448386','9044225701106794722','6245263230078180165','2455493504656501937','119380033406075185','3539446876354904424','4388285494707702938','8465639903493332598','1990926470709207990','7869173497522369978','518434444251012418','3243216915828208788','2938296691114749316','4173126100837443136','1737024320145262954','4024518201050142590','3118288676166938491','811079331256169673','4641149986913005989','5241054485802581732','8779805405089906071','1866493943235912077','2809965213377465278','4079581754161090327','1870420528426696311','5002548063396967234','1953337345189472787','7243738075555796600','512788887580404098','3337883177501524743','3749623868996067505','4227057480449898351','8143617850034579599','6088915139589626654','2020470922631136966','734380131189539113','4976623810289972435','7328663297982158881','8865556362572198700','8098747179428131431','4588546231200288501','7169570410058253847','8898141746165244982','4065738735294812525','2455850638851156506','223648709045563645','2775889206720328473','7351849348157164257','6140493896276004934']

for file in os.listdir(dir):

	fileOpen = dir + file
	#---------------------
	countTotalLines = 0
	with open(fileOpen, 'r') as f:
		for line in f:
			countTotalLines += 1
	#This is to discount hearders
	if locGyrAcc==1:
		countTotalLines = countTotalLines-28
	else:
		countTotalLines = countTotalLines-8		

	numLineToStartAux = numLineToStart
	
	numLineToStartAux = int(ceil((numLineToStartAux * countTotalLines)/100))
	#-----------------
	contLinesFile =0
	if linesBeforeInjection==0:
		with open(fileOpen) as infile:
			for line in infile:
				if line.find("@DATA")==-1 or line.find("@ATTRIBUTE")==-1 or line.find("@RELATION")==-1:
					contLinesFile = contLinesFile+1
		linesBeforeInjection = contLinesFile*percentageLinesBeforeInjection/100

	
	userIdNameIndex= file.find('.')
	newuserIdNameIndex= newUsersId.index(file[0:userIdNameIndex])	
	dirarffInjected = dirOutput+ str(newuserIdNameIndex)+'_'+str(posUserId)+'_'+str(percentageLinesBeforeInjection)+'_'+str(linesBeforeInjection)+'_'+str(width)+'_'+str(version)+'_'+str(numLineToStart)+'.arff'
	
	with open(fileOpen) as infile:
		with open(dirarffInjected,'wb') as outfile:
			#The max and min per feature (column) should be stored to add random noice between such values afterwards.
			elementLineMax=[]
			elementLinesMin=[]
			contFirstLine=0
		
			exit=2
			linesBeforeInjectionCont=linesBeforeInjection
			
			contLinesFileAux=0
			for line in infile:
				if exit != 0 and exit!=1:	
					#write all lines except for @ATTRIBUTE UserId and @ATTRIBUTE UserI
					if line.find("@DATA")!=-1:
						exit=0
					elif line.find("@ATTRIBUTE UserId")==-1:
						outfile.write(line)
				
				#Here lines of data starts
				else:
					#This is just to write the classes of the file, which is the userId and the UserId+1, simulating the class of the injection
					#Though it is not really needed
					if exit==0:
						exit=1
						#For MOA it should be stored in this way "@ATTRIBUTE UserId real"
						outfile.write("@ATTRIBUTE UserId real\n")
						outfile.write("@DATA\n")
					
					#The file should be created from a particular line on
					if numLineToStartAux<=0:
						
						#To inject data in the expected line
						if linesBeforeInjectionCont<=0:
							#If the mix and max are analogous, the max is incremented in 0,5 just to get random numbers close to the target number
							
							for x in range(0,len(elementLine)):
								if float(elementLineMax[x])==float(elementLinesMin[x]):
									elementLineMax[x]=str(float(elementLineMax[x])+0.5)
							
							lineInjected = ''
							cont=0
							for num in line.strip().split(','):
								
								if cont==posUserId:
									newIdUser= newUsersId.index(num)
									lineInjected=lineInjected+str(newIdUser)+'1'
								else:	
									lineInjected=lineInjected+str("%.4f" %(random.uniform(float(elementLinesMin[cont]), float(elementLineMax[cont]))))+','
								cont= cont +1

							lineInjected = lineInjected + "\n"
							outfile.write(lineInjected)
							
						else:
							#The first element is included in the list to do comparison in pairs with the remaining lines
							if contFirstLine==0:
								#Collect the line except for the UserId
								elementLineMaxAux=line.strip().split(',')[0:len(line)-1]
								elementLineMax = elementLineMaxAux[0:len(elementLineMaxAux)-1]
								elementLinesMinAux=line.strip().split(',')[0:len(line)-1]
								elementLinesMin = elementLinesMinAux[0:len(elementLinesMinAux)-1]
								contFirstLine=contFirstLine+1
							else:
								#Collect the line except for the UserId
								elementLineAux = line.strip().split(',')
								elementLine=elementLineAux[0:len(elementLineAux)-1]
								if locGyrAcc==0:
									for x in range(0,len(elementLine)):
										if float(elementLineMax[x])<float(elementLine[x]):
											elementLineMax[x]=elementLine[x]
										if float(elementLinesMin[x])>float(elementLine[x]):
											elementLinesMin[x]=elementLine[x]
								else:
									for x in range(0,len(elementLine)):
										if float(elementLineMax[x])<float(elementLine[x]):
											elementLineMax[x]=str(float(elementLine[x])+10)
										if float(elementLinesMin[x])>float(elementLine[x]):
											elementLinesMin[x]=str(float(elementLine[x])+10)

							UserId= line.strip().split(',')[posUserId]
							newIdUser= newUsersId.index(UserId)
							lengthLine=len(line)

							if locGyrAcc==0:
								newLine=''
								for num in line.strip().split(','):
									if num!=UserId:
										newLine=newLine+str(float(num))+','
								newLine=newLine+str(newIdUser)+'\n'
								outfile.write(newLine)
							else:
								newLine=''
								for num in line.strip().split(','):
									if num!=UserId:
										newLine=newLine+str(float(num)+10)+','
								newLine=newLine+str(newIdUser)+'\n'
								outfile.write(newLine)
						linesBeforeInjectionCont=linesBeforeInjectionCont-1

						contLinesFileAux=contLinesFileAux+1
					else:
						numLineToStartAux=numLineToStartAux-1
				#Stop the loop is lines corresponds to maxLines 
				if maxLines==contLinesFileAux:
					break 
														

			