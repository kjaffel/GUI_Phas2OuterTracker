from pyqtgraph import QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

"""
optional: you can pass hexcolor 
https://www.colorhexa.com/

"""

# check available colors! 
#print("\n".join(QtGui.QColor.colorNames()))


# edge of the sensor
def GetOpticalColor(optchannel):
    if optchannel == "1B":
        color ='r' #'red'  
    elif optchannel == "2B":
        color = '#195D19' # green
    elif optchannel == "3B":
        color = '#E53900' #'orange'
    elif optchannel == "4B":
        color = 'y'#'yellow'
    elif optchannel == "5B":
        color = '1329d0'
    elif optchannel == "6B":
        color = '#92333E' 
    elif optchannel == "7B":
        color = '#000000' 
    else:
        raise RuntimeError("{0} optical channel not in the list !".format(optchannel))
    return color 

# fill module frame 
def GetPowerColor(pwrchannel):
    if pwrchannel == "1A":
        color = '#8E0047'
    elif pwrchannel == "1C":
        color = 'y'
    elif pwrchannel == "2A":
        color = '#660066'#"purple"
    elif pwrchannel == "3A":
        color = '#FFA508'
    elif pwrchannel == "3C":
        color ='#542727'#'brown'
    elif pwrchannel == "4A":
        color = 'w'#'white' 
    elif pwrchannel == "5A":
        color = '#1B108C'#'bleu'
    elif pwrchannel == "5C":
        color = '#195D19'#'green'
    elif pwrchannel == "6A":
        color = 'r'#'red'
    elif pwrchannel == "7A":
        color = '#404040'
    else:
        raise RuntimeError("{0} PWR channel not in the list !".format(pwrchannel))
    return color

