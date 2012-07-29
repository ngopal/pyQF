from Data import Present
from Data import Historical
from TechnicalAnalysis import *

print Present.get_all('GOOG')
H = Historical.Quotes('GOOG',2004,2010)
print H.data
