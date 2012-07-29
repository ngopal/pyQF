import urllib2

class Quotes:
	def __init__(self, ticker, start, end):
		self.data = self.csvToDict(self.fromYahoo(ticker,start,end))
		self.properties = self.getProperties() #prints automatically
	def fromYahoo(self,sym, start, end):
		url = 'http://ichart.finance.yahoo.com/table.csv?d=6&e=1&f='+str(end)+'&g=d&a=7&b=19&c='+str(start)+'&ignore=.csv&s='+sym
		response = urllib2.urlopen(url)
		csv = response.read()
		return csv
	def csvToDict(self,csvfile):
		temp = []
		new_dict = {}
		for i in csvfile.strip('\n').split('\n'):
			temp.append(i.split(','))
		for i in zip(*temp):
			new_dict[i[0]] = list(i[1:])
		return new_dict
	def getProperties(self):
		print [(i,len(self.data[i])) for i in self.data]
		return 0

