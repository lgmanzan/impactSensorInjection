# IMPACT OF INJECTION ATTACKS ON SENSOR-BASED CONTINUOUS AUTHENTICATION FOR SMARTPHONES

Scripts for the analysis of injection attacks on sensor-based continuous authentication for smartphones are included. Based on paper "L. González-Manzano, U. Mahbub, J. M de Fuentes, R. Chellappa “Impact of injection attacks on sensor-based continuous authentication for smartphones”. Computer Communications, 2020", the process is the following:

1)DATA PROCESSING
In Sherlock dataset T1 (location) and T2 (gyroscope+accelerometer) should be processed. T1 and T2 are composed of folders from different years and months. All these folders should be processed to generate a single file per user, one for location and other for gyroscope+accelerometer. 

There are many ways to do the processing. For instance, using scripts "T1_to_csv.py" and "T2_to_csv.py" data from Sherlock dataset is converted into CVS and from then, into ARFF using scripts "gyrosAcce2arff.py" and "location2arff.py". For example:

$python ".../T1_to_csv.py" "/folderT1location_sherlockData" 

$python ".../T2_to_csv.py" "/folderT2GyrosAcc_sherlockData" 

$python ".../gyrosAcce2arff.py" "/folderGyrosAcc_CSVdata" 

$python ".../location2arff.py" "/folderLocation_CSVdata" 


Afterwards Weka is used for doing feature selection. Examples of the use of Weka with applied algorithms are the following:

$java -Xmx8g -cp .../weka.jar weka.filters.supervised.attribute.AttributeSelection -E weka.attributeSelection.CorrelationAttributeEval -S "weka.attributeSelection.Ranker -T -1.7976931348623157E308 -N -1"  -i ".../locationAllusers.arff"  -o ".../locationAllusers_CorrelationAttEval.arff"


$java -Xmx12g -cp .../weka.jar weka.filters.supervised.attribute.AttributeSelection -E weka.attributeSelection.CfsSubsetEval -S 'weka.attributeSelection.BestFirst -D 1 -N 5'  -i ".../locationAllusers.arff"  -o ".../locationAllusers_CFS.arff"

Script "featureSelection.py" is used for doing the feature selection process for T1 and T2. It is executed to generate files with just required features. The names of the attributes to be kept should be specified at the beginning of this script. Input parameters: folder with ARFF files to process; 2) 0 for location and 1 for accelerometer and gyroscope
$python ".../featureSelection.py" "/folderFilesToReduced/" 1

Note that selected features for T1 and T2 are presented in Appendix 1 of the paper [REF-TO BE PUBLISHED]


2)DATA INJECTION
Blind rate injection is carried out using script "sensorBlindRInjection.py" for both, location and accelerometer and gyroscope data. Input parameters: 1)directory to locate output files; 2)directory of files to do the injection; 3)percentage of injection; 4) column of the UserId (it starts in 0); 5)operation, 1 means addition, 0 means subtraction; 6)percentage of lines (regarding the lines of the whole file) after which the injection should start (leg); 7) lines before injection (leg), it should take value 0 if the percentage is applied; 8)w to be used; 9)percentage of file lines to start creating the injected file (percentage in %); 10) 0 for location and 1 for gyroscope and accelerometer.

For instance:
$python ".../sensorBlindRInjection.py" "/OutputFiles/" "/dirFilesToInject/" 10 25 0 0 250 1000 20 1

$python ".../sensorBlindRInjection.py" "/OutputFiles/" "/dirFilesToInject/" 10 5 0 0 500 1000 20 0

Slogger injection is executed using script "sensorSloggerInjection.py" for both accelerometer and gyroscope, and location. Input parameters: 1)directory to locate output files; 2)directory of files to do the injection;  3)column of the UserId #(it starts in 0); 4)percentage of injection (leg); 5)lines before injection (leg), it should take value 0 if the percentage is applied; 6)w to be used; 7)if location or gyros and acc files; 8)version of the files (just to be included in the name); 9)percentage of file lines to start creating the injected file (percentage in %).

For instance:
$python "...sensorSloggerInjection.py" "/OutputFiles/" "/dirFilesToInject/" 5 0 750 1000 0 1 80

3)MOA EXECUTION
After all injected files are developed, MOA is applied for authentication purposes. Examples of the use of MOA, applying chosen algorithms, are the following:

$java -cp .../moa.jar moa.DoTask "EvaluatePrequential -l (lazy.kNN -k 3  -w 1000 ) -s (ArffFileStream -f ( sourceFile) -c 26) -i -1 -o ( outputPredKNN)"

$java -cp /home/lgmanzan/moa-release-2017.06b/moa.jar moa.DoTask "EvaluatePrequential -l trees.HoeffdingAdaptiveTree -e (WindowClassificationPerformanceEvaluator -w 1000) -s (ArffFileStream -f (sourceFile) -c 26) -o (outputPredSVM )"

4)DATA ANALYSIS
Once MOA output is achieved, there are assorted ways to carry out the processing. For instance, script "processsingSloggerInjection.py" generates a plot with FirstIntervalFP and FirstIntervalTN per algorithm (KNN/HAT) and size of w. Input parameter: folder with MOA output of all processed slogger injection files. 

$python.exe "...\processingSloggerInjection.py" folderSloggerInjectionResults\

AUTHORS: Lorena Gonzalez (lgmanzan at inf.uc3m.es), Jose Maria de Fuentes (jfuentes at inf.uc3m.es)
