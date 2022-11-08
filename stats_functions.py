from scipy import stats

# ----- =+= -----#
# Determine the statistical significance & validity of a 
# null and/or alternative hypothesis
#   nullHyp = null hypothesis
#   altHyp = alternate hypothesis
#   g1 = data from group 1
#   g2 = data from group 2
#   confidence = confidence level [ideally between 0.80 and 0.99]

def statSig(nullHyp:str, altHyp:str, g1:list, g2:list, confidence:float):
    
    t, p = round(stats.ttest_ind(g1,g2), 4)
    
    if confidence > 1: 
        print('Error: Confidence level is greater than 1. Try a lower threshold.')
    print(f'T-Test result: {t}')
    print(f'p-value: {p}')
    
    print('\nResults: ')
    a = 1-confidence
    if p <= a:
        print(f'Since the p-value = {p} is less than the alpha value = {a}, we reject the null hypothesis.\
                We therefore accept the alternate hypothesis and conclude that {altHyp} with a confidence level of {confidence*100}%.')
    else: 
        print(f'Since the p-value = {p} is higher than the alpha value = {a}, we accept the null hypothesis.\
                We conclude that {nullHyp} with a confidence level of {confidence*100}%.')
             

def weightedMean(x:list[float],w:list[float]):
    pass