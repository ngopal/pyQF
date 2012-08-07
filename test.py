from Data import Present
from Data import Historical
from TechnicalAnalysis import TA

print Present.get_all('GOOG')
H = Historical.Quotes('GOOG',2004,2010)
print H.data
T = TA.Analyze(H.data)
T.pivotPoint()
