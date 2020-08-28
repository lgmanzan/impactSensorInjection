# Script for the analysis of injection attacks on sensor-based continuous authentication for smartphones
# This script makes use of Sherlock dataset (http://bigdata.ise.bgu.ac.il/sherlock/#/)
# This script focuses on selecting features either for gyroscope and accelerometer or for location
# AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
# Version: 2020-06-15
import os
import sys

dir = sys.argv[1]
locGyrosAcc=int(sys.argv[2])
listAttSelect=[]
#Attributes to be keeped in the file, the remaining ones will be removed
#0 means location and 1 accelerometer and gyroscope

if locGyrosAcc==0:
	#This is for location
	listAttSelectNames=['location_spatio_25means','location_spatio_50means','location_spatio_10means','location_spatio_100means','location_spatio_5means']
else:
	#This is for gyroscope and accelerometer
	listAttSelectNames=['gyroscopestat_x_median','gyroscopestat_x_mean','gyroscopestat_y_median','gyroscopestat_y_mean','accelerometerstat_z_dc_fft','accelerometerstat_z_mean','accelerometerstat_z_mean_fft','accelerometerstat_z_var_fft','accelerometerstat_cov_y_x','gyroscopestat_y_dc_fft','gyroscopestat_z_median','gyroscopestat_z_mean','accelerometerstat_z_median_fft','gyroscopestat_z_dc_fft','accelerometerstat_z_fourth_idx_fft','accelerometerstat_y_fourth_idx_fft','accelerometerstat_z_third_idx_fft','accelerometerstat_x_fourth_idx_fft','accelerometerstat_y_var_fft','accelerometerstat_z_second_idx_fft','accelerometerstat_z_fourth_val_fft','accelerometerstat_y_second_idx_fft','accelerometerstat_y_mean_fft','accelerometerstat_y_third_idx_fft','accelerometerstat_y_first_idx_fft']

# Main loop for reading and writing files
for file in os.listdir(dir):
	#print file
	fileOpen = dir + file
	cont=0
	contNames=0
	ContUserId=0
	fileNew = dir + file.replace(".arff","reduced.arff")
	with open(fileOpen, "r") as infile:
		with open(fileNew, "w") as outfile:
			for line in infile:
				cont = 1
				newLine=""
				if line.find("@")!=-1:
					if line.find("@ATTRIBUTE")!=-1:
						contNames=contNames+1
						getAtt=line.split(' ')[1]
						if getAtt in listAttSelectNames:
							listAttSelect.append(contNames)
							newLine = line
						#This is to add the userId
						if line.find("@ATTRIBUTE UserId")!=-1:
							newLine=line
					elif line.find("@RELATION")!=-1 or line.find("@DATA")!=-1:
						newLine = line
				else:
					if ContUserId==0:
						#This is just to add the number of the column of the userId
						listAttSelect.append(contNames)
						ContUserId=ContUserId+1
					for value in line.split(','):
						value = value.strip()
						if cont in listAttSelect:
							if newLine=='':
								newLine= value
							else:
								newLine = newLine + ','+value
						cont = cont +1
					newLine = newLine + '\n'
				if len(line)>0:
					outfile.write(newLine)

	