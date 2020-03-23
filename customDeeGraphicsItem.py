"""
first try to pass the modules coordinates to pyqtgraph
plotting for: 
        - PS module
        - odd Assemblay 
        - TEDD1, surface 1
work in progress...

pyqtgraph user guide:  http://www.pyqtgraph.org/documentation/introduction.html
Qt Documentation:      https://doc.qt.io/

more links: 
https://likegeeks.com/pyqt5-drawing-tutorial/
https://www.tutorialspoint.com/pyqt/pyqt_layout_management.htm

"""
import json
import subprocess
import sys
import numpy as np

import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

from utils import GetOpticalColor, GetPowerColor

sys.path.append("/home/jaffel/Phas2OuterTracker/GUI_Phase2OuterTracker")
from DataOddAssemblyPS2SModule import OddAssemblyPS2SModule as data
"""
## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see the link to QGraphicsItem documentation above !)

"""
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)

def getProcessOutput(cmd):
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE)
    process.wait()
    data, err = process.communicate()
    if process.returncode is 0:
        return data.decode('utf-8')
    else:
        print("Error:", err)
    return ""

#data = json.loads(getProcessOutput("python DataEvenAssemblyPS2SModule.py"))
#data = json.loads(sys.argv[1])


pg.setConfigOptions(imageAxisOrder='row-major')

class CustomiseDeeItems(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        Win = pg.GraphicsWindow(size=(1000,800), border=True)
        #Win.resize(1000,1000, border=True)
        Win.setWindowTitle("TEDD1 Plotter")
        View = Win.addViewBox(col=0, row=0, lockAspect=True)
        View.disableAutoRange('xy')
        View.autoRange()
        self.data = data  
        self.generatePicture()
        pg.setConfigOptions(antialias=True)

    def generatePicture(self):
#        def drawLine(qPainter, color, x1, y1, x2, y2, width=0):
#            pen = QtGui.QPen(QtGui.QColor(*color))
#    
#            pen.setWidth(width)
#            qPainter.setPen(pen)
#            qPainter.drawLine(x1, y1, x2, y2)
#
        def SSModule(self, opt, pwr, p):
            print (opt, pwr)
            # lengths
            framessx = 144.1
            framessy = 125
            sssensorx = 102.7
            sssensory = 94.2
            epsilon = sssensorx * 0.1


            w1, h1, w2, h2 = [sssensorx, sssensory, framessx, framessy]

            p.rotate(-90)  # rotate to put empty part to the left
            # Exterior square
            p.setBrush(pg.mkBrush(GetPowerColor(pwr)))
            p.setPen(0)

            xoff = - w2 / 2
            yoff = - h2 / 2

            p.translate(xoff, yoff)  # translate from center to low-x, low-y position.
            w = (w2 - w1) * 0.5
            h = h2
            rectangle = QtCore.QRectF(0, 0, w + epsilon, h)
            p.drawRect(rectangle)

            p.translate(w + w1 - epsilon, 0)
            w = (w2 - w1) * 0.5
            h = h2
            rectangle = QtCore.QRectF(0, 0, w + epsilon, h)
            p.drawRect(rectangle)

            p.translate(- w - w1 + epsilon, (h2 - h1) * 0.5 + h1)
            w = w2
            h = (h2 - h1) * 0.5
            rectangle = QtCore.QRectF(0, 0, w, h)
            p.drawRect(rectangle)
            p.translate(0, -epsilon)
            p.drawRect(rectangle)
            p.translate(0, epsilon)

            # Interior square
            p.setBrush(pg.mkBrush('#778899'))
            p.setPen(pg.mkPen(GetOpticalColor(opt)))

            p.translate((w2 - w1) * 0.5, - h1)

            rectangle = QtCore.QRectF(0, 0, w1, h1)
            p.drawRect(rectangle)

            p.translate(w1 * 0.5, h1 * 0.5)  # go back to center position
            p.rotate(90)  # rotate to put empty part to the left


        def PSModule(self, opt, pwr, p):
            # lengths:
            pssensorx = 98.7 
            pssensory = 49.2 
            framepsx = 130
            framepsy = 69.6

            # Exterior square
            p.setBrush(pg.mkBrush(GetPowerColor(pwr)))
            p.setPen(pg.mkPen('k'))

            w1 =  framepsx
            h1 =  framepsy
            p.translate(- w1 / 2, - h1 / 2)  # translate from center to low-x, low-y position.
            rectangle = QtCore.QRectF(0, 0, w1, h1)
            p.drawRoundedRect(rectangle, 5, 5)
            p.translate(w1 / 2, h1 / 2)  # go back to center positio

            # Interior square
            p.setBrush(pg.mkBrush('#778899'))
            p.setPen(pg.mkPen(GetOpticalColor(opt)))

            w2 = pssensorx
            h2 = pssensory
            p.translate(-w2 / 2, -h2 / 2)
            rectangle = QtCore.QRectF(0, 0, w2, h2)
            p.drawRoundedRect(rectangle, 5, 5)
            p.translate(w2 / 2, h2 / 2)  # go back to center positio

            # Inter-Internal
            p.setPen(pg.mkPen('k'))
            w = w2 * 0.8
            h = h2 * 0.5
            p.translate(-w / 2, -h / 2)
            rectangle = QtCore.QRectF(0, 0, w, h)
            p.drawRoundedRect(rectangle, 20, 20)

            p.translate(w / 2, h / 2)  # go back to center position

        
        def DEE(self, radius, p):
            deeoutr =1098
            deeinr = 222
            p.setPen(pg.mkPen(0.2))
            #p.setBrush(CrossPattern)
            p.drawArc(-radius, -radius/2, radius*1.5 , radius, 0 , -180 * 16)

        ## pre-computing a QPicture object allows paint() to run much more quickly, 
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        
        # ___ more options for style ___
        #   mkPen('y', width=3, style=QtCore.Qt.DashLine)          ## Make a dashed yellow line 2px wide
        #   mkPen(0.5)                                             ## solid grey line 1px wide
        #   mkPen(color=(200, 200, 255), style=QtCore.Qt.DotLine)  ## Dotted pale-blue line
        #module_footprint.setPen(pg.mkPen(0.5)) 

        #rectangle = QtCore.QRectF(-800, 0, 800, 800)
        #p.drawRoundedRect(rectangle, 0., 0.)

        # rectangle = QtCore.QRectF(-2000, -200, 4000, 2000)
        # p.drawRoundedRect(rectangle, 0., 0.)

        for (id, ring, radius, phi, opt, pwr, type, surface) in self.data:

            # Angle:
            angle =(phi if surface== 1 else 180 - phi)

            # Transform to cartesian
            x = radius * np.cos(np.radians(angle))
            y = radius * np.sin(np.radians(angle))
            rot = angle - 90

            print("{0}Module ID: {1}".format(type, id))
            print("Cartesian coordinate: x =", x, ',y =', y, "\nPolar coordinate: r =", radius,', phi =', phi,'°')
            print("*****************************")
            p.translate(x, y)
            print( "initial:", x, y)
            p.rotate(rot)

            if type =="2S":
                if surface==1:
                    SSModule(self, opt, pwr, p)
            elif type =="PS":
                if surface ==1:
                    PSModule(self, opt, pwr, p)
            else:
                raise RuntimeError ("{0} __ Unkown type of module !".format(type))

            # go back to back to centre
            p.rotate(-rot) # N.B: rotate 1st then translate
            p.translate(-x, -y)
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())

# set axis limit 
plt = pg.plot()
#plt.setAspectLocked()
plt.resize(1000,1000)
#Add polar grid lines
y = range(0, 1000)
x = range(0, 1000)
plt.addLine(x=0, pen=0.2)
plt.addLine(y=0, pen=0.2)

# full TEDD1 !
#for r in range(2, 680, 40):
#    circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, r*2 , r*2)
#    circle.setStartAngle(180) # usless !
#    circle.setPen(pg.mkPen(0.2))
#    plt.addItem(circle)

# plot the modules :
item = CustomiseDeeItems(data)
plt.addItem(item)
plt.showGrid(x=True, y=True)
plt.setWindowTitle('TEDD1, surface1 \n Full-mockup \n UCLouvain 2020')


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
