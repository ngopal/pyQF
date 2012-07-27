import urllib2

class Data:
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

class TA:
	def __init__(self, dataObj):
		print 'technical analysis class'
		self.data_dict = dataObj.data
	def pivotPoints(self):
		""" Formula from investopedia: http://www.investopedia.com/articles/technical/04/041404.asp#axzz21qPfzx5O
		R2 = P+(H-L)
		R1 = (P*2)-L
		P = (H+L+C)/3
		S1 = (P*2)-H
		S2 = P-(H-L) """

		H = float(self.data_dict['High'][-1])
		L = float(self.data_dict['Low'][-1])
		C = float(self.data_dict['Close'][-1])
		P = (H+L+C)/3
		R2 = P+(H-L)
                R1 = (P*2)-L
		S1 = (P*2)-H
                S2 = P-(H-L)

		print (R2,R1,P,S1,S2)

		return 0

	def stochastics(self,days):
		""" Stochastics formula from here: http://www.ehow.com/how_5131646_calculate-stochastics-make-stochastic-oscillator.html """ 

		L = float(min(self.data_dict['Low'][-days:]))
		H = float(max(self.data_dict['High'][-days:]))
		pctK = list(self.data_dict['Close'][-days:])
		K = [100*((float(i)-L)/(H-L)) for i in pctK]
                D = (sum(K[-3:])/3)
		print K, D

		return (K,D)

	def parabolicSAR(self):
		""" Parabolic SAR formula from here: http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:parabolic_sar """
		return 0

if __name__ == "__main__":
	DD = Data('ilmn',2004,2009)
	T = TA(DD)
	T.pivotPoints()
	T.stochastics(14)
