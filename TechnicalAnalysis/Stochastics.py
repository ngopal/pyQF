
# Need to run this function over as many days as possible, not just last few

def Run(data,days):
                """ Stochastics formula from here: http://www.ehow.com/how_5131646_calculate-stochastics-make-stochastic-oscillator.html """

                L = float(min(data['Low'][-days:]))
                H = float(max(data['High'][-days:]))
                pctK = list(data['Close'][-days:])
                K = [100*((float(i)-L)/(H-L)) for i in pctK]
                D = (sum(K[-3:])/3)

                return (K,D)
