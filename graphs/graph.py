
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import axes


class Graph:

    darkDict = {    'titlecolor':'white',

                    'xtick.color':'white', 
                    'xtick.labelcolor':'white',
                    'xtick.labelsize':8,

                    'ytick.color':'white', 
                    'ytick.labelcolor':'white',
                    'ytick.labelsize':8,

                    'axes.facecolor':'black',
                    'axis.facecolor':'black',
                    'axis.bordercolor':'#575757',
                    'axis.labelcolor':'#909191',
                    'axis.spinecolor':'#575757',

                    'trendline.color':'#c7005a',
                    'markerfacecolor':'#850000',

                    'fontsize':12, 
                    'horizontalalignment':'center',
                    'fontfamily':'serif'
                    }
    lightDict = {   'titlecolor':'black',

                    'xtick.color':'black', 
                    'xtick.labelcolor':'#0a0a0a',
                    'xtick.labelsize':8,

                    'ytick.color':'black', 
                    'ytick.labelcolor':'#0a0a0a',
                    'ytick.labelsize':8,

                    'axes.facecolor':'white',
                    'axis.facecolor':'white',
                    'axis.bordercolor':'#a6a6a6',
                    'axis.labelcolor':'#0a0a0a',
                    'axis.spinecolor':'#0a0a0a',

                    'trendline.color':'#8400ff',
                    'markerfacecolor':'#ca99ff',

                    'fontsize':12, 
                    'horizontalalignment':'center',
                    'fontfamily':'serif'
                    }

    def __init__(self, x=list, y=list, xvar=str, yvar=str):
            self.x = x
            self.y = y
            self.xvar = xvar
            self.yvar = yvar
    
    # ----- =+= -----#
    # Helper to check the theme
    # **Called by all plot*() methods
    @staticmethod
    def checkTheme(t=str):
            if t == 'light':
                    dict=Graph.lightDict
            elif t == 'dark':
                    dict=Graph.darkDict
            return dict

    # ----- =+= -----#
    # Helper to format the ticks 
    # **Called by formatGraph()
    @staticmethod
    def formatTicks(a=axes, axisToSet=str, dict=dict):
            if axisToSet == 'x':
                    colorKey = 'xtick.color'
                    labelcolorKey = 'xtick.labelcolor'
                    labelsizeKey = 'xtick.labelsize'
            else:
                    colorKey = 'ytick.color'
                    labelcolorKey = 'ytick.labelcolor'
                    labelsizeKey = 'ytick.labelsize'

            a.tick_params(axis=axisToSet,
                            which='both',
                            color=dict.get(colorKey), 
                            labelcolor=dict.get(labelcolorKey),
                            labelsize=dict.get(labelsizeKey))

    # ----- =+= -----#
    # Helper to format the graph 
    # **Universal to all graph types
    @staticmethod
    def formatGraph(s,a=axes,f=plt.Figure,d=dict, h=bool):
            f.set(facecolor=d.get('axes.facecolor'))
            a.set_facecolor(d.get('axis.facecolor'))

            # Formatting the grid
            a.axes.grid(which='major', color=d.get('axis.bordercolor'))
            if h:
                a.minorticks_off()
            else: a.minorticks_on() # Toggle minorticks, minorticks_off() is the reverse

            # Format the axis ticks - specify which={'major', 'minor', 'both'} if needed
            Graph.formatTicks(a,'x',d)
            Graph.formatTicks(a,'y',d) 


            a.spines['top'].set_visible(False) # Remove the top border 
            a.spines['right'].set_visible(False) # Remove the right border
            a.spines[['left','bottom']].set_color(d.get('axis.spinecolor')) # Change the colors of the left and bottom borders

            a.axes.set_axisbelow(True) # Makes the markers and axis ABOVE the axes 

            # Formatting for the title
            # Note: use color='white' to override darkFontDict if you want the title color
            #       to be diff than the labels 
            plt.title(f'{s.xvar} vs. {s.yvar}', horizontalalignment='center', color=d.get('titlecolor'), fontsize=16, fontfamily=d.get('fontfamily'))

            # Setting & formatting the labels
            plt.xlabel(s.xvar, color=d.get('axis.labelcolor'), fontfamily=d.get('fontfamily'), labelpad=15)
            plt.ylabel(s.yvar, color=d.get('axis.labelcolor'), fontfamily=d.get('fontfamily'), labelpad=15)




    # ----- =+= -----#
    # Method to create a scatter plot of self 
    #       theme=str() one of ['dark', 'light']
    #       marker=str() a valid marker type for scatter plots
    def plotScatter(self, theme=str, marker='o',trendline=True):

            # Check the theme and get the according dictionary 
            dict=Graph.checkTheme(theme)

            # Create the figure & axes
            fig, ax = plt.subplots()

            # Plot x vs y as scatter
            ax.scatter(self.x,self.y,marker=marker,c=dict.get('markerfacecolor'))

            # Format the graph using outside helper
            Graph.formatGraph(self,ax,fig,dict)

            # Trendline 
            if trendline:
                    z = np.polyfit(self.x,self.y,1)
                    p = np.poly1d(z)
                    ax.plot(self.x,p(self.x), color=dict.get('trendline.color'))


    # ----- =+= -----#
    # Method to create a bar graph of self
    #       theme=str() one of ['dark', 'light']
    #       align=str() one of ['left', 'right', 'mid']
    def plotBar(self, theme=str, horiz=False, customTitle=''):

            # Check the theme and get the according dictionary
            dict=Graph.checkTheme(theme)

            # Create the figure & axes
            fig, ax = plt.subplots()

            # Plot x vs y as hist
            if horiz: 
                ax.barh(y=self.x, width=self.y, color=dict.get('markerfacecolor'))
            else: 
                ax.bar(x=self.x, height=self.y,color=dict.get('markerfacecolor'))
                ax.tick_params(axis='x', labelrotation=45)

            # Format the graph using outside helper
            Graph.formatGraph(self,ax,fig,dict,horiz)

            if not horiz:
                ax.tick_params(axis='x', which='minor', color=dict.get('axes.facecolor'))
            if customTitle:
                plt.title(f'{customTitle}', horizontalalignment='center', color=dict.get('titlecolor'), fontsize=16, fontfamily=dict.get('fontfamily'))
