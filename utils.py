from pyqtgraph import QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

"""
optional: you can pass hexcolor 
https://www.colorhexa.com/

"""

# check available colors! 
print("\n".join(QtGui.QColor.colorNames()))


# sensors
def GetOpticalColor(optchannel):
    if optchannel == "1B":
        color ='r'#'red'  
    elif optchannel == "2B":
        color = 'g'#'green'
    elif optchannel == "3B":
        color = 'o'#'orange'
    elif optchannel == "4B":
        color = 'y'#'yellow'
    elif optchannel == "5B":
        color = 'l'#'bleu'
    elif optchannel == "6B":
        color = '#833549'#'red'
    elif optchannel == "7B":
        color ='b'#"black"
    else:
        raise RuntimeError("{0} optical channel not in the list !".format(optchannel))
    return color 

# frames
def GetPowerColor(pwrchannel):
    if pwrchannel == "1C":
        color = 'y'#'yellow'
    elif pwrchannel == "1A":
        color = 'r'#'red'
    elif pwrchannel == "2A":
        color = 'p'#"purple"
    elif pwrchannel == "3A":
        color = 'o'#'orange'
    elif pwrchannel == "3C":
        color ='b'#'brown'
    elif pwrchannel == "4A":
        color = 'w'#'white' 
    elif pwrchannel == "5A":
        color = 'b'#'bleu'
    elif pwrchannel == "5C":
        color = 'g'#'green'
    elif pwrchannel == "6A":
        color = 'r'#'red'
    elif pwrchannel == "7A":
        color = 'g'#'grey'
    else:
        raise RuntimeError("{0} PWR channel not in the list !".format(pwrchannel))
    return color

