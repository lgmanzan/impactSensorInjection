# Script for the analysis of injection attacks on sensor-based continuous authentication for smartphones
# This script makes use of Sherlock dataset (http://bigdata.ise.bgu.ac.il/sherlock/#/)
# This script focuses on converting location CSV data to ARFF data
# AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
# Version: 2020-06-15
import csv
import sys

def createline(lineAux2):
	idString= lineAux2.split(",")[0].strip()

	idUser=abs(hash(idString))
	#In this case the first is the UserId but converted to a number regarding position in listUsers
	nullVar=0
	lineAux=''
	for x in range(24, 36):
		if lineAux2.split(",")[x].strip()== 'NULL' or lineAux2.split(",")[x].strip()== 'null':
			nullVar=1
	if nullVar==0:
		lineAux = str(idUser)
		for x in range(24, 36):
			lineAux = lineAux + ","+lineAux2.split(",")[x].strip()
			if x ==35:
				lineAux = lineAux +"\n"
	return nullVar, lineAux, idUser
	
	
	
dir = sys.argv[1]
dircsvT1 = dir + '/T1.csv'
dirarff = dir + '/location.arff'

with open(dircsvT1) as infile:
    with open(dirarff,'wb') as outfile:
		outfile.write("@RELATION location\n")
		outfile.write("@ATTRIBUTE UserId real\n")
		outfile.write("@ATTRIBUTE location_spatio_5means real\n")
		outfile.write("@ATTRIBUTE location_spatio_10means real\n")
		outfile.write("@ATTRIBUTE location_spatio_25means real\n")
		outfile.write("@ATTRIBUTE location_spatio_50means real\n")
		outfile.write("@ATTRIBUTE location_spatio_75means real\n")
		outfile.write("@ATTRIBUTE location_spatio_100means real\n")
		outfile.write("@ATTRIBUTE location_spatioTemporal_day_5means real\n")
		outfile.write("@ATTRIBUTE location_spatioTemporal_day_25means real\n")
		outfile.write("@ATTRIBUTE location_spatioTemporal_day_100means real\n")
		outfile.write("@ATTRIBUTE location_spatioTemporal_week_5means real\n")
		outfile.write("@ATTRIBUTE location_spatioTemporal_week_25means real\n")
		outfile.write("@ATTRIBUTE location_spatioTemporal_week_100means real\n")
		outfile.write("@DATA\n")
		#This is used to not include headers
		first_line = infile.readline()
		listUsers=[]
		contLine=0
		for line in infile:
			contLine=contLine+1
			lineCreated= createline(line)
			if int(lineCreated[0]) ==0:
				outfile.write(lineCreated[1])					
				#For all users...
				if line.split(",")[0].strip() not in listUsers:
					listUsers.extend([line.split(",")[0].strip(),lineCreated[2]])				
					
		print 'numUsers', len(listUsers)
		print 'numUsers', listUsers
		print 'numLines', contLine
				

					
