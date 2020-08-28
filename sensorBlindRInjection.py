# Script for the analysis of injection attacks on sensor-based continuous authentication for smartphones
# This script makes use of Sherlock dataset (http://bigdata.ise.bgu.ac.il/sherlock/#/)
# This script focuses on doing Blind rate injection in location, accelerometer and gyroscope data
# AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
# Version: 2020-06-15

import csv
import os
import csv
import sys
from math import ceil
dirOutput = sys.argv[1]
dir = sys.argv[2]
percentageIncrease= sys.argv[3]
#posUserId-last column (it starts in 0 which means that it should be equal to the number of columns -1)
posUserId=int(sys.argv[4])
#1 means addition, 0 means subtraction
operation=int(sys.argv[5])
#Percentage of lines after which the injection should start. 
percentageLinesBeforeInjection=int(sys.argv[6])
#0 means percentage is used
linesBeforeInjection=int(sys.argv[7])
#The input parameter corresponds to the width in MOA
#max value of lines in file = width of MOA + injectedLines + 1
width=int(sys.argv[8])
maxLines=width+linesBeforeInjection+1
#Lines from which start the file creation
numLineToStart=int(sys.argv[9])
#0 for location and 1 for gyroscope and accelerometer
locGyracc=int(sys.argv[10])

#From this array the location of UserId will become the new UserId
#It should be changed if ID identifiers of Sherlock dataset have been managed in some way
newUsersId=['1748983473209579185','306193130034809840','8313018476638449002','3793829844934448386','9044225701106794722','6245263230078180165','2455493504656501937','119380033406075185','3539446876354904424','4388285494707702938','8465639903493332598','1990926470709207990','7869173497522369978','518434444251012418','3243216915828208788','2938296691114749316','4173126100837443136','1737024320145262954','4024518201050142590','3118288676166938491','811079331256169673','4641149986913005989','5241054485802581732','8779805405089906071','1866493943235912077','2809965213377465278','4079581754161090327','1870420528426696311','5002548063396967234','1953337345189472787','7243738075555796600','512788887580404098','3337883177501524743','3749623868996067505','4227057480449898351','8143617850034579599','6088915139589626654','2020470922631136966','734380131189539113','4976623810289972435','7328663297982158881','8865556362572198700','8098747179428131431','4588546231200288501','7169570410058253847','8898141746165244982','4065738735294812525','2455850638851156506','223648709045563645','2775889206720328473','7351849348157164257','6140493896276004934']

for file in os.listdir(dir):
	
	fileOpen = dir + file
	#---------------------
	countTotalLines = 0
	with open(fileOpen, 'r') as f:
		for line in f:
			countTotalLines += 1
	#This is to discount hearders
	if locGyracc==0:
		countTotalLines = countTotalLines-8		
	else:
		countTotalLines = countTotalLines-28

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
	dirarffInjected = dirOutput + str(newuserIdNameIndex)+'_'+percentageIncrease+'_'+str(operation)+'_'+str(linesBeforeInjection)+'_'+str(percentageLinesBeforeInjection)+'_'+str(width)+'_'+str(numLineToStart)+'.arff'
	newIdUser=''
	with open(fileOpen) as infile:
		with open(dirarffInjected,'wb') as outfile:
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
					if exit==0:
						exit=1
						#For MOA it should be stored in this way "@ATTRIBUTE UserId real"
						outfile.write("@ATTRIBUTE UserId real\n")
						outfile.write("@DATA\n")
					#The file should be created from a particular line on
					if numLineToStartAux<=0:
						#To inject data in the expected line
						if linesBeforeInjectionCont<=0:
							lineInjected = ''
							cont=0
							for num in line.strip().split(','):
								
								if cont==posUserId:
									newIdUser= newUsersId.index(num)
									lineInjected=lineInjected+str(newIdUser)+'1'
								else:	
									if operation==1:
										if float(num)!=0.0:
											if locGyracc==0:
												lineInjected=lineInjected+str((float(num)+(float(num)* float(percentageIncrease)/100)))+','
											else:
												lineInjected=lineInjected+str((10+float(num)+(float(num)* float(percentageIncrease)/100)))+','
										else:
											if locGyracc==0:
												lineInjected=lineInjected+str((float(percentageIncrease)/100))+','
											else:
												lineInjected=lineInjected+str((float(percentageIncrease)/100)+10)+','
									else:
										if float(num)!=0.0:
											if locGyracc==0:
												lineInjected=lineInjected+ str((float(num)-(float(num)* float(percentageIncrease)/100)))+','
											else:
												lineInjected=lineInjected+str((10+float(num)-(float(num)* float(percentageIncrease)/100)))+','										
										else:
											if locGyracc==0:
												lineInjected=lineInjected+str((float(percentageIncrease)/100))+','
											else:
												lineInjected=lineInjected+str((float(percentageIncrease)/100)+10)+','												
								cont= cont +1
							lineInjected = lineInjected + "\n"
							outfile.write(lineInjected)
							
						else:
							newLine=''
							UserId= line.strip().split(',')[posUserId]
							newIdUser= newUsersId.index(UserId)
							lengthLine=len(line)
							for num in line.strip().split(','):
								if num!=UserId:
									if locGyracc==0:
										newLine=newLine+str(float(num))+','
									else:
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
			