import subprocess
import re
import json

###
# Represents an output of the ab command
###
class ABResult:

	def extractString(self, pattern):
		return re.search(pattern, output).group(1).strip()

	def __init__(self, output):
		self.output = output
		self.hostname = self.extractString('Server Hostname:(.+?)\n')
		self.port = self.extractString('Server Port:(.+?)\n')
		self.requestPerSecond = self.extractString('Requests per second:(.+?)\n')
		self.ninetyPercent = int(self.extractString('  90%(.+?)\n'))     

class ServerData:

	def __init__(self, url, datas):
		self.url = url
		self.datas = datas

	def json(self):
		return json.dumps(
			{
				"label": "nginx",
				"url": self.url,
				"data": self.datas
			}
		)

xValues = range(1,10)
numberOfRequests = 10
urls = [
	"http://localhost:81/", 
	"http://localhost:82/", 
	"http://myrba.net/", 
	"http://lequipe.fr/",
	"http://google.fr/",
	"http://lamontagne.fr/",
]

data = []

for url in urls:
	urlResults = []
	for x in xValues:
		proc = subprocess.Popen([
			  "ab",
			  "-c " + str(x),
			  "-n " + str(numberOfRequests),
			  url
		], stdout=subprocess.PIPE)
		output = proc.stdout.read()
		urlResults.append(ABResult(output))

	times = []
	for result in urlResults:
		times.append(result.ninetyPercent)

	data.append(ServerData(url, times))	



d = {
		"xValues": xValues,
		"datas": []
	}
for dataForUrl in data:
	d["datas"].append({"url": dataForUrl.url, "data": dataForUrl.datas})

f = open ('results/results.json', 'w')
j = json.dumps(d, indent=4)
print >> f, j
f.close()


