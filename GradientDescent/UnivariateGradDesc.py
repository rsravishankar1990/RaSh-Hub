import csv
import math
import numpy
import matplotlib.pyplot as plt

#Initialize variables that might be required:
learningrate = 0.000001
w0 = 0.0
w1 = 0.0
tempw0 = 0.0
tempw1 = 0.0
Cost = 0.0 #Any high value
Diff = 1000.0 #Any high value

#Get the training data file location from the user

print 'Univariate Classification - Bayesian Theory \n\n Enter the location of the training data'
filename = input(' ')

#Create reader object for the csv file
fileobj = open(filename)
csv_fileobj = csv.reader(fileobj)

#Get the column names from the file into a list
colnames = []
colnames = csv_fileobj.next()
colnum = len(colnames)

print 'The column names of the training data are:\n'
for i in range(len(colnames)):
	print colnames[i]

#Choose the input variable and outcome variable in the training set
inputvar = input('Enter the independent variable name:\n')
outputvar = input('Enter the outcome variable name:\n')
inputindex = -100
outputindex = -100

for i in range(colnum):
	if colnames[i] == inputvar:
		inputindex = i
	if colnames[i] == outputvar:
		outputindex = i

#Check if the mentioned variables are in the training dataset
if inputindex == -100:
	print 'Error Message: The input variable mentioned is not in the training data. Exiting system.'
	exit()

if outputindex == -100:
	print 'Error Message: The output variable mentioned is not in the training data. Exitting system.'
	exit()




#Get the required variables into different lists for easy processing
inputlist = []
outputlist = []



for row in csv_fileobj:
	inputlist.append(row[inputindex])
	outputlist.append(row[outputindex])

plt.scatter(inputlist,outputlist)
plt.show()

#GRADIENT DESCENT ALGORITHM -
loopCount = 0
loopContinue = 'y'
tempCost = 0.0
m = len(inputlist)
#Construct the loop for iterative checking of the 
while (Diff >= 0.001 and loopContinue == 'y'):
	#{
	#Assign the w0 and w1 values and the cost
	w0 = tempw0
	w1 = tempw1
	Cost = tempCost
	tempCost = 0.0
	derivw0 = 0.0
	derivw1 = 0.0
	#Calculate the new Cost with w0 and w1 and the derivative comp
	for i in range(len(inputlist)):
		#{
		tempCost = tempCost + (float(outputlist[i]) - float(w0+ w1*float(inputlist[i])))**2
		#Derivative Component
		derivw0 = derivw0 + float(w0+ w1*float(inputlist[i])) - float(outputlist[i])
		derivw1 = derivw1 + (float(w0+ w1*float(inputlist[i])) - float(outputlist[i]))*float(inputlist[i])
		#}
	derivw0 = derivw0/m
	derivw1 = derivw1/m
	tempCost = float(tempCost/(2*m))
	Diff = abs(Cost - tempCost)

	#Calculate the tempw0 and tempw1
	tempw0 = w0 - (learningrate*derivw0)
	tempw1 = w1 - (learningrate*derivw1)

	print 'tempCost = ',tempCost,'Cost = ',Cost
	print 'tempw0 =',tempw0,'w0 = ',w0
	print 'tempw1 =',tempw1,'w1=',w1
	print 'derivw0 = ',derivw0,'derivw1=',derivw1
	print 'Diff = ',Diff
	
	#increment LoopCounter
	loopCount = loopCount + 1
	if loopCount%1000000 ==0:
		loopContinue=input('Loop still not converged. Do you want to continue? (y/n)')
	
	#}

#Create the Predicted array and plot the predicted and observed
predicted =[]
plotX = []
maxInput = float(max(inputlist))
l = 0.0
#maxInput = int(max(inputlist))
while l <= maxInput:
	predicted.append (float( w0 + w1 * l))
	plotX.append(l)
	l = l+ 0.01
	

plt.scatter(plotX,predicted)
plt.scatter(inputlist,outputlist)
plt.show()

W = []


