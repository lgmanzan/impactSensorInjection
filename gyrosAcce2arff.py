# Script for the analysis of injection attacks on sensor-based continuous authentication for smartphones
# This script makes use of Sherlock dataset (http://bigdata.ise.bgu.ac.il/sherlock/#/)
# This script focuses on converting gyroscope and accelerometer CSV data to ARFF data
# AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
# Version: 2020-06-15

import csv
import sys
############
listnull=[]
for i in range(93):
	listnull.append(0)
############
def createline(lineAux2):
	idUser = 1
	idString= lineAux2.split(",")[0].strip()
	idUser=abs(hash(idString))				
	#In this case the first is the UserId but converted to a number regarding position in listUsers
	nullVar=0
	lineAux=''

	for x in range(4, 97):
		if lineAux2.split(",")[x].strip()== 'NULL' or lineAux2.split(",")[x].strip()== 'null':
			#This fields usually have NULL values
			if x != 49 and x != 50 and x != 51:
				nullVar=1
			############
			aux =listnull[x-4]
			listnull[x-4] = aux +1
			############
	if nullVar==0:
		lineAux = str(idUser)
		for x in range(4, 97):
			if x != 49 and x != 50 and x != 51:
				lineAux = lineAux + ","+lineAux2.split(",")[x].strip()
			if x ==96:
				lineAux = lineAux +"\n"
	return nullVar, lineAux, idUser
	
	
	
dir = sys.argv[1]
dircsvT1 = dir + '/T2.csv'
dirarff = dir + '/gyrosAcce2arff.arff'

with open(dircsvT1) as infile:
    with open(dirarff,'wb') as outfile:
		outfile.write("@RELATION acceGyros\n")
		outfile.write("@ATTRIBUTE UserId real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_dc_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_first_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_first_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_fourth_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_fourth_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_mean real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_mean_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_median real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_median_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_second_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_second_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_third_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_third_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_var real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_x_var_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_dc_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_first_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_first_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_fourth_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_fourth_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_mean real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_mean_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_median real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_median_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_second_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_second_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_third_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_third_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_var real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_y_var_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_dc_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_first_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_first_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_fourth_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_fourth_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_mean real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_mean_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_median real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_median_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_second_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_second_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_third_idx_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_third_val_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_var real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_z_var_fft real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_cov_y_x real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_cov_z_x real\n")
		outfile.write("@ATTRIBUTE accelerometerstat_cov_z_y real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_fourth_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_fourth_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_mean real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_mean_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_median real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_median_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_second_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_second_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_third_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_third_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_var real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_x_var_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_dc_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_first_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_first_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_fourth_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_fourth_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_mean real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_mean_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_median real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_median_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_second_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_second_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_third_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_third_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_var real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_y_var_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_dc_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_first_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_first_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_fourth_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_fourth_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_mean real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_mean_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_median real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_median_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_second_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_second_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_third_idx_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_third_val_fft real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_var real\n")
		outfile.write("@ATTRIBUTE gyroscopestat_z_var_fft real\n")
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
		print 'pos', i, 'value', listnull
				

					
