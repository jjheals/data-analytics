# ---------- + ---------- #
# Themes to be used with graphs 
# ---------- + ---------- #

# ---------- + ---------- #
# Converts a string into the dictionary 
# NOTE: Must be updated when new dictionaries are added
def checkTheme(t:str):
        if t == 'light':
                dict=lightDict
        elif t == 'dark':
                dict=darkDict
        return dict
        
# ---------- + ---------- #
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
# ---------- + ---------- #

# ---------- + ---------- #
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
# ---------- + ---------- #