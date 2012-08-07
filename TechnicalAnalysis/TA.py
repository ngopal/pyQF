import PivotPoints

class Analyze:
	def __init__(self,dataObj):
		print 'This will be the master class to drive the use of the analysis classes'
		self.data = dataObj

	def pivotPoint(self):
		print PivotPoints.Run(self.data)
		return 0


