from src.learnCPnet import *

modeForDatasetGeneration = 1 # 1 = read a file, 2 = generate a synthetic database
nameOfFile = ["databases/sushi_30Users_10000Comparisons.dat","databases/sushi_30Users_20000Comparisons.dat","databases/hotels_parsing_binarisation_10000.dat","databases/hotels_parsing_binarisation_20000.dat","databases/movieLensDataset_200000.dat"]
numberOfComparisons = -1 # -1 = all of the comparisons in file
percentageOfNoise = [0] # between 0 and 50
numberOfVariables = 12 # -1 = automatically choose from the number of comparisons
numberOfEdgesLambda = -1 # -1 = infinity
numberOfParentsForTargetCPNet = -1 # -1 = infinity
numberOfParentsForLearnedCPNet = -1 # -1 = infinity
numberOfRoundsForFileGeneration = 1
numberOfRoundsForLearningProcedure = 10 # = percentage taken in the dataset for the cross validation

decisionThresholdBis = 0.1 # delta for decisionMode = 1
epsilonThreshold = 0.05 # threshold for epsilon

convergence = False

online = False
offline = True
autorizedCycle = False

# 1 = McDiarmid for conditioned variable, 2 = McDiarmid for conditioned AND conditional variables
decisionMode = 2



fileTestHL = open("test-results/test_acc_sushi_10000_Offline.dat","w")
for numberOfParentsForLearnedCPNet in [0,1,2]:
	averageCycleSize2,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,sdANoiseOnline,sdANoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,sdANoiseOffline,sdANoiseOfflineLog,lenOfFold,numberOfAttributes,meanConvergenceAccuracyOnline,meanConvergenceAccuracyOnlineLog,sdConvergenceAccuracyOnline,sdConvergenceAccuracyOnlineLog,meanConvergenceAccuracyOffline,meanConvergenceAccuracyOfflineLog,sdConvergenceAccuracyOffline,sdConvergenceAccuracyOfflineLog = generalProcedure(modeForDatasetGeneration,nameOfFile[0],numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,epsilonThreshold,convergence,online,offline,decisionMode,None,autorizedCycle)
	fileTestHL.write(str(numberOfParentsForLearnedCPNet) + " " + str(aOffline[0]) + " " + str(sdAOffline[0]) + " " + str(aOfflineLog[0]) + " " + str(sdAOfflineLog[0]) + "\n")
fileTestHL.close()

fileTestHL = open("test-results/test_acc_sushi_20000_Offline.dat","w")
for numberOfParentsForLearnedCPNet in [0,1,2]:
	averageCycleSize2,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,sdANoiseOnline,sdANoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,sdANoiseOffline,sdANoiseOfflineLog,lenOfFold,numberOfAttributes,meanConvergenceAccuracyOnline,meanConvergenceAccuracyOnlineLog,sdConvergenceAccuracyOnline,sdConvergenceAccuracyOnlineLog,meanConvergenceAccuracyOffline,meanConvergenceAccuracyOfflineLog,sdConvergenceAccuracyOffline,sdConvergenceAccuracyOfflineLog = generalProcedure(modeForDatasetGeneration,nameOfFile[1],numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,epsilonThreshold,convergence,online,offline,decisionMode,None,autorizedCycle)
	fileTestHL.write(str(numberOfParentsForLearnedCPNet) + " " + str(aOffline[0]) + " " + str(sdAOffline[0]) + " " + str(aOfflineLog[0]) + " " + str(sdAOfflineLog[0]) + "\n")
fileTestHL.close()

fileTestHL = open("test-results/test_acc_hotels_10000_Offline.dat","w")
for numberOfParentsForLearnedCPNet in [0,1,2,3,4,5,6]:
	averageCycleSize2,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,sdANoiseOnline,sdANoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,sdANoiseOffline,sdANoiseOfflineLog,lenOfFold,numberOfAttributes,meanConvergenceAccuracyOnline,meanConvergenceAccuracyOnlineLog,sdConvergenceAccuracyOnline,sdConvergenceAccuracyOnlineLog,meanConvergenceAccuracyOffline,meanConvergenceAccuracyOfflineLog,sdConvergenceAccuracyOffline,sdConvergenceAccuracyOfflineLog = generalProcedure(modeForDatasetGeneration,nameOfFile[2],numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,epsilonThreshold,convergence,online,offline,decisionMode,None,autorizedCycle)
	fileTestHL.write(str(numberOfParentsForLearnedCPNet) + " " + str(aOffline[0]) + " " + str(sdAOffline[0]) + " " + str(aOfflineLog[0]) + " " + str(sdAOfflineLog[0]) + "\n")
fileTestHL.close()

fileTestHL = open("test-results/test_acc_hotels_20000_Offline.dat","w")
for numberOfParentsForLearnedCPNet in [0,1,2,3,4,5,6]:
	averageCycleSize2,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,sdANoiseOnline,sdANoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,sdANoiseOffline,sdANoiseOfflineLog,lenOfFold,numberOfAttributes,meanConvergenceAccuracyOnline,meanConvergenceAccuracyOnlineLog,sdConvergenceAccuracyOnline,sdConvergenceAccuracyOnlineLog,meanConvergenceAccuracyOffline,meanConvergenceAccuracyOfflineLog,sdConvergenceAccuracyOffline,sdConvergenceAccuracyOfflineLog = generalProcedure(modeForDatasetGeneration,nameOfFile[3],numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,epsilonThreshold,convergence,online,offline,decisionMode,None,autorizedCycle)
	fileTestHL.write(str(numberOfParentsForLearnedCPNet) + " " + str(aOffline[0]) + " " + str(sdAOffline[0]) + " " + str(aOfflineLog[0]) + " " + str(sdAOfflineLog[0]) + "\n")
fileTestHL.close()

fileTestHL = open("test-results/test_acc_movieLens_Offline.dat","w")
for numberOfParentsForLearnedCPNet in [0,1,4,7,10,13,16,18]:
	averageCycleSize2,aOnline,aOnlineLog,sdAOnline,sdAOnlineLog,aOffline,aOfflineLog,sdAOffline,sdAOfflineLog,tOnline,sdTOnline,meanIT,sdIT,tOffline,sdTOffline,meanAccNoiseOnline,meanAccNoiseOnlineLog,sdANoiseOnline,sdANoiseOnlineLog,meanAccNoiseOffline,meanAccNoiseOfflineLog,sdANoiseOffline,sdANoiseOfflineLog,lenOfFold,numberOfAttributes,meanConvergenceAccuracyOnline,meanConvergenceAccuracyOnlineLog,sdConvergenceAccuracyOnline,sdConvergenceAccuracyOnlineLog,meanConvergenceAccuracyOffline,meanConvergenceAccuracyOfflineLog,sdConvergenceAccuracyOffline,sdConvergenceAccuracyOfflineLog = generalProcedure(modeForDatasetGeneration,nameOfFile[4],numberOfComparisons,percentageOfNoise,numberOfVariables,numberOfEdgesLambda,numberOfParentsForTargetCPNet,numberOfParentsForLearnedCPNet,numberOfRoundsForFileGeneration,numberOfRoundsForLearningProcedure,decisionThresholdBis,epsilonThreshold,convergence,online,offline,decisionMode,None,autorizedCycle)
	fileTestHL.write(str(numberOfParentsForLearnedCPNet) + " " + str(aOffline[0]) + " " + str(sdAOffline[0]) + " " + str(aOfflineLog[0]) + " " + str(sdAOfflineLog[0]) + "\n")
fileTestHL.close()
