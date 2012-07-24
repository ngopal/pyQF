import urllib2

class Data:
	def __init__(self, ticker, start, end):
		self.data = self.csvToDict(self.fromYahoo(ticker,start,end))
	def fromYahoo(self,sym, start, end):
		url = 'http://ichart.finance.yahoo.com/table.csv?d=6&e=1&f='+str(end)+'&g=d&a=7&b=19&c='+str(start)+'&ignore=.csv&s='+sym
		response = urllib2.urlopen(url)
		csv = response.read()
		return csv
	def csvToDict(self,csvfile):
		new = []
		for i in csvfile.strip('\n').split('\n'):
			print i.split(',')

if __name__ == "__main__":
	print "hello"
	DD = Data('ilmn',2004,2009)
	print DD.data
