from subprocess import call
import os

xValues = [1,2,3,4]
numberOfRequests = 10
currentDir = os.path.dirname(os.path.realpath(__file__))
print currentDir + "/results/nginx-" + str(1) + ".csv"

for x in xValues:
	call(["ab",
		  "-c " + str(x),
		  "-n " + str(numberOfRequests),
		  "-e  " + currentDir + "/results/nginx-" + str(x) + ".csv",
		  "http://localhost:81/"
	])