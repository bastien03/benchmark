import subprocess
import re

###
# Represents an output of the ab command
###
class ABResult:

	def extractString(self, pattern):
		return re.search(pattern, output).group(1)

	def __init__(self, output):
		self.output = output
		self.hostname = self.extractString('Server Hostname:        (.+?)\n')
		self.port = self.extractString('Server Port:            (.+?)\n')
		self.requestPerSecond = self.extractString('Requests per second:    (.+?)\n')

xValues = [1]
numberOfRequests = 10
abResults = []

for x in xValues:
	proc = subprocess.Popen([
		  "ab",
		  "-c " + str(x),
		  "-n " + str(numberOfRequests),
		  "http://localhost:81/"
	], stdout=subprocess.PIPE)
	output = proc.stdout.read()
	abResults.append(ABResult(output))

print "http://" + abResults[0].hostname + ":" + abResults[0].port + " - " + abResults[0].requestPerSecond