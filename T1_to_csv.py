# Script for the analysis of injection attacks on sensor-based continuous authentication for smartphones
# This script makes use of Sherlock dataset (http://bigdata.ise.bgu.ac.il/sherlock/#/)
# This script focuses on converting location data from Sherlock dataset to CSV
# AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
# Version: 2020-06-15
import csv
import os
import csv
import sys


#csv.field_size_limit(sys.maxsize)

dir = sys.argv[1]
dircsvT1 = dir + '/T1.csv'
dirOriginal = dir + '/T1.tsv'

file = file(dircsvT1, 'wb')

fieldnames = ['userid', 'uuid', 'version', 'googleplayloc_speed', 'googleplayloc_maccuracy', 'googleplayloc_timestamp', 'celltower_cid', 'celltower_lac', 'celltower_psc', 'celltower_timestamp', 'celltower_type', 'status_alarmvol', 'status_brightnessmode', 'status_brightness_file', 'status_brightness_settings', 'status_dtmfvol', 'status_musicvol', 'status_notificationvol', 'status_orientation', 'status_ringermode', 'status_ringtonevol', 'status_systemvol', 'status_voicecallvol', 'status_timestamp', 'location_spatio_5means', 'location_spatio_10means', 'location_spatio_25means', 'location_spatio_50means', 'location_spatio_75means', 'location_spatio_100means', 'location_spatioTemporal_day_5means', 'location_spatioTemporal_day_25means', 'location_spatioTemporal_day_100means', 'location_spatioTemporal_week_5means', 'location_spatioTemporal_week_25means', 'location_spatioTemporal_week_100means']
csv.writer(file).writerow(fieldnames)

csv.writer(file).writerows(csv.reader(open(dirOriginal), delimiter="\t"))

file.close()

