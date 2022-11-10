import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, stdev
from themes import *
from scipy.stats import norm

class NormalDist:
    
    def __init__(self, data):  
        self.data = data
        
    def render(self, theme):
        m = mean(self.data)
        sd = stdev(self.data)
        
        fig, ax = plt.subplots()
        plt.plot(self.data, norm.pdf(self.data, m, sd))
        
        d=checkTheme(theme)
        
        fig.set(facecolor=d.get('axes.facecolor'))
        ax.set_facecolor(d.get('axis.facecolor'))
        ax.axes.grid(which='major', color=d.get('axis.bordercolor'))
        ax.spines[['left', 'right', 'top','bottom']].set_color(d.get('axis.spinecolor')) 
        ax.axes.set_axisbelow(True)
        
        plt.title(f'N{round(mean(self.data),2), round(stdev(self.data),2)}', 
                  horizontalalignment='center', 
                  color=d.get('titlecolor'), 
                  fontsize=16, 
                  fontfamily=d.get('fontfamily'))
        
        plt.show()




testData = np.random.normal(20,0.45,200)
testData.sort()

print(testData)
NormalDist(testData).render('dark')
    