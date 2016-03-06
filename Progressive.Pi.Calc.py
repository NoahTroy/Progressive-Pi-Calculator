'''#import "time", for understanding how long to run the program
import "decimal" for working with more accurate decimals with a virtually unlimited number of positions after the decimal
import "pickle" to allow us to store our data/progress
import "os" to allow us to search for our pickled files and/or create a new file if not found
import "math" to allow us to use the math "rounding" modules.'''
from time import *
from decimal import *
import pickle , os , math

#Set the decimal to be accurate up to 1000 places after the decimal:
getcontext().prec = 1000


def LoadFiles():
	#Initialize global variables:
	global aTerm , bTerm , cTerm
	global CurrentPiNum
	global TotalTime
	global TotalNumOfItsCompleted
	

	#Find The Path Of Our Main File:
	filepath = os.path.abspath('PiCalc.py')
	#Modify The Path To Get Rid Of Our Main File's Name:
	filepathlisttemp = []
	for chr in filepath:
		filepathlisttemp += chr
	lengthoffilepathlist = len(filepathlisttemp)
	lengthofourfilename = 9
	indextostartat = (lengthoffilepathlist - lengthofourfilename)
	for i in range(indextostartat , lengthoffilepathlist):
		filepathlisttemp.pop(indextostartat)
	#Rewrite The filepath To Contain The Path Of The Directory Containing Our Main File:
	filepath = ''
	for chr in filepathlisttemp:
		filepath += chr
	#Add Our Folder Name To The filepath, Creating The Correct folderpath:
	folderpath = filepath + 'Delete Me To Reset Calculator/'

	#Determine Whether Or Not The Folder Exists, And Create It If It Does Not:
	if not os.path.exists('Delete Me To Reset Calculator/'):
		os.makedirs(folderpath)

	#Check For And Create/Load Currently Saved a, b, and c Terms:
	if not os.path.isfile('Delete Me To Reset Calculator/CurrentABCterms.dat'):
		aTerm = Decimal(2)
		bTerm = Decimal(3)
		cTerm = Decimal(4)
		abcTermsList = [aTerm , bTerm , cTerm]
		abcTerms = open('Delete Me To Reset Calculator/CurrentABCterms.dat' , 'wb')
		pickle.dump(abcTermsList , abcTerms)
		abcTerms.close()
	else:
		abcTerms = open('Delete Me To Reset Calculator/CurrentABCterms.dat' , 'rb')
		abcTermsList = pickle.load(abcTerms)
		aTerm = abcTermsList[0]
		bTerm = abcTermsList[1]
		cTerm = abcTermsList[2]
		abcTerms.close()
	     
	#Check For And Create/Load Currently Saved/Calculated Pi Number:
	if not os.path.isfile('Delete Me To Reset Calculator/CurrentPiNum.dat'):
		CurrentPiNum = Decimal(3)
		CurrentPiNumFile = open('Delete Me To Reset Calculator/CurrentPiNum.dat' , 'wb')
		pickle.dump(CurrentPiNum , CurrentPiNumFile)
		CurrentPiNumFile.close()
	else:
		CurrentPiNumFile = open('Delete Me To Reset Calculator/CurrentPiNum.dat' , 'rb')
		CurrentPiNum = pickle.load(CurrentPiNumFile)
		CurrentPiNumFile.close()
	
	#Check For And Create/Load The Total Amount Of Time Ordered To Be Spent Calculating:
	if not os.path.isfile('Delete Me To Reset Calculator/TotalTime.dat'):
		TotalTime = int(0)
		TotalTimeFile = open('Delete Me To Reset Calculator/TotalTime.dat' , 'wb')
		pickle.dump(TotalTime , TotalTimeFile)
		TotalTimeFile.close()
	else:
		TotalTimeFile = open('Delete Me To Reset Calculator/TotalTime.dat' , 'rb')
		TotalTime = pickle.load(TotalTimeFile)
		TotalTimeFile.close()

	#Check For And Create/Load The Total Number Of Iterations Completed:
	if not os.path.isfile('Delete Me To Reset Calculator/TotalNumOfItsCompleted.dat'):
		TotalNumOfItsCompleted = int(0)
		TotalNumOfItsFile = open('Delete Me To Reset Calculator/TotalNumOfItsCompleted.dat' , 'wb')
		pickle.dump(TotalNumOfItsCompleted , TotalNumOfItsFile)
		TotalNumOfItsFile.close()
	else:
		TotalNumOfItsFile = open('Delete Me To Reset Calculator/TotalNumOfItsCompleted.dat' , 'rb')
		TotalNumOfItsCompleted = pickle.load(TotalNumOfItsFile)
		TotalNumOfItsFile.close()


#Opening Explanatory Messages:
def Startup():
	#Initialize Variables As Global:
	global LengthOfRuntime , LengthOfRuntimeSecs
	print('WELCOME TO THE PROGRESSIVE PI CALCULATOR!')
	print('''This calculator will calculate the digits of pi for however long you
set it, and remember its progress when you start it back up.
With every iteration, it gets a slightly more accurate calculation of pi.''')
	print('''\nPLEASE NOTE: DO NOT END THE CALCULATOR PREMATURELY, AS
THIS WILL RESULT IN FAILURE TO SAVE DATA, OR WORSE.''')
	LengthOfRuntime = input('''\nFor how many minutes would you like the calculator to run?
Please respond in a whole number here:\t''')
	#Convert Inputted Runtime To More Easily Calculated Seconds:
	LengthOfRuntime = int(LengthOfRuntime)
	LengthOfRuntimeSecs = (LengthOfRuntime * 60)


def MainCalculation():
	#Initialize Needed Variables As global:
	global TotalTimeIncludingNow
	global NumberOfItsCompleted
	global IntOneForIntersect , IntTwoForIntersect

	#Load global Variables:
	global LengthOfRuntime , LengthOfRuntimeSecs , aTerm , bTerm , cTerm , CurrentPiNum , TotalTime

	#Define A Starting, Ending, Remaining, And Total Time For The Program:
	CurrentTime = time()
	StartTime = time()
	EndTime = (StartTime + LengthOfRuntimeSecs)
	TimeRemaining = ((EndTime - CurrentTime) / 60)
	TotalTimeIncludingNow = (TotalTime + LengthOfRuntime)

	'''#Initialize Variables To Record How Many Iterations Have Been Completed, Whether It Is A Positive Or Negative Iteration,
	And How Much Time Has Passed To Determine When To Print How Much Time Is Left In The Program:'''
	NumberOfItsCompleted = 0
	IsPos = True
	TimeSinceLastCountdownPrint = StartTime

	#Start A Loop To Run The Program Until The Designated Time Period Is Up:
	while (CurrentTime < EndTime):
		#Set The Product For The Terms Multiplied Together:
		MultipliedTerms = Decimal(aTerm*bTerm*cTerm)

		#Branch Depending On Whether It Is Currently A Negative Or A Positive Iteration:
		if IsPos:
			#Calculate The Number To Be Added, Then Add It To Get The New Version Of Calculated Pi:
			OperationPos = Decimal(4/MultipliedTerms)
			CurrentPiNum = Decimal(CurrentPiNum + OperationPos)
			#Get The Current Pi Number (Converted Into A String) For Calculating Which Digits Of Pi Are Correct So Far:
			IntOneForIntersect = str(CurrentPiNum)
		else:
			#Calculate The Number To Be Subtracted, Then Subtract It To Get The New Version Of Calculated Pi:
			OperationNeg = Decimal(-4/MultipliedTerms)
			CurrentPiNum = Decimal(CurrentPiNum + OperationNeg)
			#Get The Current Pi Number (Converted Into A String) For Calculating Which Digits Of Pi Are Correct So Far:
			IntTwoForIntersect = str(CurrentPiNum)

		#Determine Whether More Than A Minute Is Remaining, In Order To Print The Grammatically Correct Countdown Sentence:
		TimeRemaining = int(math.ceil((EndTime - CurrentTime) / 60))
		#Determine Whether Or Not It Has Been At Least A Minute Since The Last Countdown Printed:
		PrintCountdownYet = int(math.floor(CurrentTime - TimeSinceLastCountdownPrint))
		
		#If Conditions Are Met, Print How Much Time Is Remaining In The Calculation Period:
		if TimeRemaining > 1:
			if PrintCountdownYet >= 60:
				#Calculate Percentage Complete:
				PercentageRemaining = int(math.floor((TimeRemaining / LengthOfRuntime) * 100))
				PercentageComplete = (100 - PercentageRemaining)
				print('\n***' , PercentageComplete , '%' , ' Complete!***' , sep = '')
				print('***There Are About' , TimeRemaining , 'Minutes Remaining Until Finish.***')
				#Reset The Countdown Timer:
				TimeSinceLastCountdownPrint = time()
		else:
			if PrintCountdownYet >= 60:
				#Calculate Percentage Complete:
				PercentageRemaining = int(math.floor((TimeRemaining / LengthOfRuntime) * 100))
				PercentageComplete = (100 - PercentageRemaining)
				print('\n***' , PercentageComplete , '%' , ' Complete!***' , sep = '')
				print('***There Is About' , TimeRemaining , 'Minute Remaining Until Finish.***')
				#Reset (Unnecessarily) The Countdown Timer:
				TimeSinceLastCountdownPrint = time()
		#Update The Counters, Terms, Etc. That Changer Per Iteration, In Preparation For The Next Iteration:
		aTerm += 2
		bTerm += 2
		cTerm += 2
		IsPos = not IsPos
		NumberOfItsCompleted += 1
		CurrentTime = time()


#Define A Function For Finding The Same Characters In The Same Position Between Two Strings, To Determine Which Digits Of Pi Are Accurrate:
def IntersectsInStrings(string1 , string2):
     global StringIntersection
     StringIntersection = ''
     string1len = len(string1)
     string2len = len(string2)
     if string1len <= string2len:
          shorterstring = string1
          longerstring = string2
     else:
          shorterstring = string2
          longerstring = string1
     lenshorterstring = len(shorterstring)
     for i in range(0 , lenshorterstring):
          currentshorterstringchr = shorterstring[i]
          currentlongerstringchr = longerstring[i]
          if (currentshorterstringchr == currentlongerstringchr):
               StringIntersection += currentshorterstringchr
          else:
               break


#Save Progress For Next Time By Writing The New Updated Values To The Data Files:
def SaveProgress():
	print('''\n\n\n\n\n\n\n\n\nPlease wait while we clean up and save our progress; we will inform
you when we have finished...''')

	#Load global Variables:
	global CurrentPiNum , TotalNumOfItsCompleted , TotalTimeIncludingNow , NumberOfItsCompleted

	TotalTimeFile = open('Delete Me To Reset Calculator/TotalTime.dat' , 'wb')
	pickle.dump(TotalTimeIncludingNow , TotalTimeFile)
	TotalTimeFile.close()

	abcTermsList = [aTerm , bTerm , cTerm]
	abcTerms = open('Delete Me To Reset Calculator/CurrentABCterms.dat' , 'wb')
	pickle.dump(abcTermsList , abcTerms)
	abcTerms.close()

	#Determine The Total Number Of Iterations Completed, To Save And Later Display:
	TotalNumOfItsCompleted += NumberOfItsCompleted

	TotalNumOfItsFile = open('Delete Me To Reset Calculator/TotalNumOfItsCompleted.dat' , 'wb')
	pickle.dump(TotalNumOfItsCompleted , TotalNumOfItsFile)
	TotalNumOfItsFile.close()

	CurrentPiNumFile = open('Delete Me To Reset Calculator/CurrentPiNum.dat' , 'wb')
	pickle.dump(CurrentPiNum , CurrentPiNumFile)
	CurrentPiNumFile.close()

	print('\n\nWe have finished saving our progress! Now Let\'s See The Results!')


#Display The Results And Statistics:
def ResultsAndStatistics():
	#Load global Variables:
	global TotalNumOfItsCompleted , TotalTimeIncludingNow , NumberOfItsCompleted , StringIntersection
	
	print('''\n\n\n\n\n\n\n\n\n\n\n\nSo Far, This Is What We Have Calculated Of Pi (Note: The
Longer You Let Me Run, And The More I Calculate, The More
Accurate This Number Will Become):\n''' , StringIntersection , sep='')

	print('\nThe Number Of Iterations Completed Today Is:\t' , NumberOfItsCompleted)

	print('\nThe Number Of Iterations Completed In Total Is:\t' , TotalNumOfItsCompleted)

	print('''\nIn Total, You Have Ordered Your Computer To Calculate Pi
For Around''' , TotalTimeIncludingNow , 'minute(s)!')

	print('\n\n\n\nThat\'s All! Goodbye!')

	exit()




##################################################################################################
#Run Through The Program:
LoadFiles()
Startup()
MainCalculation()
IntersectsInStrings(IntOneForIntersect , IntTwoForIntersect)
SaveProgress()
ResultsAndStatistics()
##################################################################################################
