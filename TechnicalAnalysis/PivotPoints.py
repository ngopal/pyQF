
def Run(data):
                """ Formula from investopedia: http://www.investopedia.com/articles/technical/04/041404.asp#axzz21qPfzx5O
                R2 = P+(H-L)
                R1 = (P*2)-L
                P = (H+L+C)/3
                S1 = (P*2)-H
                S2 = P-(H-L) """

                H = float(data['High'][-1])
                L = float(data['Low'][-1])
                C = float(data['Close'][-1])
                P = (H+L+C)/3
                R2 = P+(H-L)
                R1 = (P*2)-L
                S1 = (P*2)-H
                S2 = P-(H-L)

                return (R2,R1,P,S1,S2)

