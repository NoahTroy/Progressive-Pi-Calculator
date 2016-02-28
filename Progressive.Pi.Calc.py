from time import *
from decimal import *
getcontext().prec = 1000
import pickle , os , math
print('WELCOME TO THE PROGRESSIVE PI CALCULATOR!')
print('''This calculator will calculate the digits of pi for however long you
set it to calculate for, and remember its progress when you start
it up next time. With every iteration, it gets a slightly more
accurate calculation of pi.''')
print('''\nPLEASE NOTE: DO NOT END THE CALCULATOR PREMATURELY, AS
THIS WILL RESULT IN FAILURE TO SAVE DATA, OR WORSE.''')
LengthOfRuntime = input('''\nFor how many minutes would you like the calculator to run?
Please respond in whole numbers here:\t''')
LengthOfRuntime = int(LengthOfRuntime)
LengthOfRuntimeSecs = (LengthOfRuntime * 60)
StartTime = time()
EndTime = (StartTime + LengthOfRuntimeSecs)
CurrentTime = time()
NumberOfItsCompleted = 0
IsPos = True
TimeRemaining = ((EndTime - CurrentTime) / 60)
TimeSinceLastCountdownPrint = StartTime
if not os.path.isfile('CurrentABCterms.dat'):
     aTerm = Decimal(2)
     bTerm = Decimal(3)
     cTerm = Decimal(4)
     abcTermsList = [aTerm , bTerm , cTerm]
     abcTerms = open('CurrentABCterms.dat' , 'wb')
     pickle.dump(abcTermsList , abcTerms)
     abcTerms.close()
else:
     abcTerms = open('CurrentABCterms.dat' , 'rb')
     abcTermsList = pickle.load(abcTerms)
     aTerm = abcTermsList[0]
     bTerm = abcTermsList[1]
     cTerm = abcTermsList[2]
     abcTerms.close()
     
if not os.path.isfile('CurrentPiNum.dat'):
     CurrentPiNum = Decimal(3)
     CurrentPiNumFile = open('CurrentPiNum.dat' , 'wb')
     pickle.dump(CurrentPiNum , CurrentPiNumFile)
     CurrentPiNumFile.close()
else:
     CurrentPiNumFile = open('CurrentPiNum.dat' , 'rb')
     CurrentPiNum = pickle.load(CurrentPiNumFile)
     CurrentPiNumFile.close()

if not os.path.isfile('TotalTime.dat'):
     TotalTime = int(0)
     TotalTimeFile = open('TotalTime.dat' , 'wb')
     pickle.dump(TotalTime , TotalTimeFile)
     TotalTimeFile.close()
else:
     TotalTimeFile = open('TotalTime.dat' , 'rb')
     TotalTime = pickle.load(TotalTimeFile)
     TotalTimeFile.close()

if not os.path.isfile('TotalNumOfItsCompleted.dat'):
     TotalNumOfItsCompleted = int(0)
     TotalNumOfItsFile = open('TotalNumOfItsCompleted.dat' , 'wb')
     pickle.dump(TotalNumOfItsCompleted , TotalNumOfItsFile)
     TotalNumOfItsFile.close()
else:
     TotalNumOfItsFile = open('TotalNumOfItsCompleted.dat' , 'rb')
     TotalNumOfItsCompleted = pickle.load(TotalNumOfItsFile)
     TotalNumOfItsFile.close()

TotalTimeIncludingNow = (TotalTime + LengthOfRuntime)

while (CurrentTime < EndTime):
     MultipliedTerms = Decimal(aTerm*bTerm*cTerm)
     if IsPos:
          OperationPos = Decimal(4/MultipliedTerms)
          CurrentPiNum = Decimal(CurrentPiNum + OperationPos)
          print(OperationPos)
     else:
          OperationNeg = Decimal(-4/MultipliedTerms)
          CurrentPiNum = Decimal(CurrentPiNum + OperationNeg)
          print(OperationNeg)
     PrintCountdownYet = int(math.floor(CurrentTime - TimeSinceLastCountdownPrint))
     TimeRemaining = int(math.ceil((EndTime - CurrentTime) / 60))
     if TimeRemaining > 1:
          if PrintCountdownYet >= 60:
               print('\n***There Are About' , TimeRemaining , 'Minutes Remaining Until Finish.***')
               TimeSinceLastCountdownPrint = time()
     else:
          if PrintCountdownYet >= 60:
               print('\n***There Is About' , TimeRemaining , 'Minute Remaining Until Finish.***')
               TimeSinceLastCountdownPrint = time()
     aTerm += 2
     bTerm += 2
     cTerm += 2
     IsPos = not IsPos
     NumberOfItsCompleted += 1
     CurrentTime = time()

OperationPos = str(OperationPos)
OperationNeg = str(OperationNeg)
OperationPosForIntersect = {}
OperationNegForIntersect = {}
for i in OperationPos:
     OperationPosForIntersect.add(i)
for i in OperationNeg:
     OperationNegForIntersect.add(i)
CurrentPiNumRefined = OperationPosForIntersect.intersection(OperationNegForIntersect)     
print('\n\n\n\n\nTime\'s Up!')
print('''\nSo Far, This Is What We Have Calculated Of Pi (Note: The
Longer You Let Me Run, And The More I Calculate, The More
Accurate This Number Will Become):\n''' , CurrentPiNumRefined , sep='')
print('\nThe Number Of Iterations Completed Today Is:\t' , NumberOfItsCompleted)
TotalNumOfItsCompleted = (NumberOfItsCompleted + TotalNumOfItsCompleted)
print('\nThe Number Of Iterations Completed In Total Is:\t' , TotalNumOfItsCompleted)
print('''\nIn Total, You Have Ordered Your Computer To Calculate Pi
For Around''' , TotalTimeIncludingNow , 'minute(s)!')
print('''\n\nPlease wait while we clean up and save our progress; we will inform
you when we have finished...''')
#Update TotalTime, abcTerms, TotalNumOfItsCompleted, and CurrentPiNum
TotalTimeFile = open('TotalTime.dat' , 'wb')
pickle.dump(TotalTimeIncludingNow , TotalTimeFile)
TotalTimeFile.close()

abcTermsList = [aTerm , bTerm , cTerm]
abcTerms = open('CurrentABCterms.dat' , 'wb')
pickle.dump(abcTermsList , abcTerms)
abcTerms.close()

TotalNumOfItsFile = open('TotalNumOfItsCompleted.dat' , 'wb')
pickle.dump(TotalNumOfItsCompleted , TotalNumOfItsFile)
TotalNumOfItsFile.close()

CurrentPiNumFile = open('CurrentPiNum.dat' , 'wb')
pickle.dump(CurrentPiNum , CurrentPiNumFile)
CurrentPiNumFile.close()

print('\n\nWe have finished saving our progress! Goodbye!')
