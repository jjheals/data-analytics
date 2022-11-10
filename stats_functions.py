from scipy import stats

x = [0,2,5,2,6,3,4.5,7.3,7.5,7.8,9.2,11,12.4,16.33,
     3,4,5,6,7,8]
w = [0.2,0.3,0.7,0.5,0.7,0.2,0.4,0.6,0.7,0.8,0.2,0.1,0.4,
     0.2,0.21,0.34,0.43,0.63,0.5,0.6]
     
# ----- =+= -----#
# Determine the statistical significance & validity of a 
# null and/or alternative hypothesis
#   nullHyp = null hypothesis (No, x does NOT have an effect on Y)
#   altHyp = alternate hypothesis (Yes, x DOES have an effect on Y)
#   g1 = data from group 1
#   g2 = data from group 2
#   confidence = confidence level [ideally between 0.80 and 0.99]. Note that the complement of the confidence level is alpha (significance level)

def statSig(nullHyp:str, altHyp:str, g1:list, g2:list, confidence:float):
    
    t, p = stats.ttest_ind(g1,g2)
    round(t, 4)
    round(p,4)
    
    if confidence > 1: 
        print('Error: Confidence level is greater than 1. Try a lower threshold.')
    print(f'T-Test result: {t}')
    print(f'p-value: {p}')
    
    print('\nResults: ')
    a = 1-confidence
    if p <= a:
        print(f'Since the p-value = {p} is less than the alpha value = {a}, we reject the null hypothesis.\
                We therefore accept the alternate hypothesis and conclude that {altHyp.lower()} with a confidence level of {confidence*100}%.')
    else: 
        print(f'Since the p-value = {p} is higher than the alpha value = {a}, we fail to reject the null hypothesis.\
                We conclude that {nullHyp.lower()} with a confidence level of {confidence*100}%.')
             

def weightedMean(X:list[float], W:list[float]):
    mean = 0
    for x, w in zip(X,W):
        mean += x*w
    return mean / len(X)

print(weightedMean(x,w))
