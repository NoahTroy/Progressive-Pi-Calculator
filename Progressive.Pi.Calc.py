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
if not os.path.isfile('ActualPiNum.dat'):
     ActualPiNum=''''3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865
     13282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786
     78316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036
     00113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912
     279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271
     452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136
     297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378
     387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959
     092164201989'''
     ActualPiNumFile = open('ActualPiNum.dat' , 'wb')
     pickle.dump(ActualPiNum , ActualPiNumFile)
     ActualPiNumFile.close()
else:
     ActualPiNumFile = open('ActualPiNum.dat' , 'rb')
     ActualPiNum = pickle.load(ActualPiNumFile)
     ActualPiNumFile.close()
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
     else:
          OperationNeg = Decimal(-4/MultipliedTerms)
          CurrentPiNum = Decimal(CurrentPiNum + OperationNeg)
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

IntTwoForIntersect = CurrentPiNum
IntOneForIntersect = str(IntOneForIntersect)
IntTwoForIntersect = str(IntTwoForIntersect)
def IntersectsInStrings(string1 , string2):
     global CurrentPiNumRefined
     CurrentPiNumRefined = ''
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
          shorterstringord = ord(shorterstring[i])
          longerstringord = ord(longerstring[i])
          aresame = (shorterstringord == longerstringord)
          if aresame:
               CurrentPiNumRefined += shorterstring[i]
print(IntOneForIntersect , IntTwoForIntersect)
IntersectsInStrings(ActualPiNum , IntTwoForIntersect)
   
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
