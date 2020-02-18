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

"""
## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see the link to QGraphicsItem documentation above !)

"""
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


def drawLine(qPainter, color, x1, y1, x2, y2, width=0):
    pen = QtGui.QPen(QtGui.QColor(*color))
 
    pen.setWidth(width)
    qPainter.setPen(pen)
    qPainter.drawLine(x1, y1, x2, y2)


class CustomiseDeeItems(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  
        self.generatePicture()

    def generatePicture(self):
        def SSModule(self, opt, pwr, p):
            # lengths 
            framessx=144.1
            framessy=125
            crossx =41.4
            crossy =30.8
            sssensorx = 102.7
            sssensory = 94.2
            epsilon = sssensorx* 0.1
            w = crossx * 0.5

            BLACK = (0, 0, 0)
            BLUE = (0, 0, 255)
            CYAN = (0, 255, 255)
            GREEN = (0, 255, 0)
            YELLOW = (255, 255, 0)
            RED = (255, 0, 0)
            MAGENTA = (255, 0, 255)
            WHITE = (255, 255, 255)



            print (opt, pwr)
            
            # frame |_|  
            p.setBrush(pg.mkBrush(GetPowerColor(pwr)))
            p.setPen(0)
            frame1 = QtCore.QRectF(0., 0., w + epsilon, framessy)
            p.drawRect(frame1)
            p.translate(w + sssensorx - epsilon, 0.)

            frame2 = QtCore.QRectF(0., 0., w + epsilon, framessy)
            p.drawRect(frame2)
            p.translate(- w - sssensorx + epsilon, crossy * 0.5 + sssensory)

            frame3 = QtCore.QRectF(0, 0, framessx, crossy*0.5)
            p.drawRect(frame3)

            # sensor
            p.setBrush(pg.mkBrush(GetOpticalColor(opt)))
            #p.setBrush(pg.mkBrush('g'))
            p.setPen(pg.mkPen(0))
            p.translate(crossx * 0.5, - sssensory)
            sensor = QtCore.QRectF(0, 0, sssensorx, sssensory)
            p.drawRect(sensor)
            
            # centre
            #p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            #drawLine(p, BLUE,    10, 10, 160, 20)
        
        def PSModule(self, opt, pwr, p):
            # lengths:
            pssensorx = 98.7 
            pssensory = 49.2 
            framepsx = 130
            framepsy = 69.6
            # frame
            p.setBrush(pg.mkBrush(0))
            p.setPen(pg.mkPen('k'))

            p.translate(- framepsx / 2, - framepsy / 2)
            psframe = QtCore.QRectF(0, 0, framepsx, framepsy)
            p.drawRoundedRect(psframe, 5, 5)
            p.translate(framepsx / 2, framepsy / 2)
              
            # sensor 
            p.setBrush(pg.mkBrush(1))
            p.setPen(pg.mkPen('g'))
            p.translate(-pssensorx / 2, -pssensory / 2)
            pssensor = QtCore.QRectF(0, 0, pssensorx, pssensory)
            p.drawRect(pssensor)
            p.drawLine
            p.translate(pssensorx / 2, pssensory / 2)
            
            p.setPen(pg.mkPen('k'))
            p.translate(-pssensorx*0.8 / 2, -pssensory*0.5 / 2)
            pssensor = QtCore.QRectF(0., 0., pssensorx*0.8, pssensory*0.5)
            p.drawRoundedRect(pssensor, 20., 20.)

        
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
        
        val = None
        for (id, ringnbr, radius, phi, opt, pwr, type, surface) in self.data:
        
            # Ring updates :
            if ringnbr == val:
                print ("{0} raw".format(val))
            else:        
                DEE(self, radius, p)
            val = ringnbr

            # Angle:
            angle =(phi if surface== 1 else 180-phi)
            
            # Transform to cartesian 
            x = radius * np.cos(np.radians(angle))
            y = radius * np.sin(np.radians(angle))
            rot = angle - 90

            print("{0}Module ID: {1}".format(type, id))
            print("Cartesian coordinate: x =", x, ',y =', y, "\nPolar coordinate: r =", radius,', phi =', phi,'°')
            print("*****************************")
            #print(type(opt), type(pwr))
            p.translate(x, y)
            p.rotate(rot)
            
            if type =="2S":
                SSModule(self, opt, pwr, p)
            elif type =="PS":
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


# for fast test !
data = [
        ## fields are :
        #Module_Id, Module_RingL, Module_RingR, Module_phi_deg, OPT_Services_Channel, PWR_Services_Channel, type_/C, surface
#(411571240,     1,      259.78, 171,    "7B",   "7A",   "PS",   2),
(411571236,     1,      259.78, 153,    "6B",   "5C",   "PS",   1),
#(411571232,     1,      259.78, 135,    "6B",   "5C",   "PS",   2),
(411571228,     1,      259.78, 117,    "5B",   "4A",   "PS",   1),
#(411571224,     1,      259.78, 99,     "5B",   "4A",   "PS",   2),
(411571220,     1,      259.78, 81,     "5B",   "4A",   "PS",   1),
#(411571216,     1,      259.78, 63,     "3B",   "3A",   "PS",   2),
(411571212,     1,      259.78, 45,     "3B",   "3A",   "PS",   1),
#(411571208,     1,      259.78, 27,     "2B",   "1C",   "PS",   2),
(411571204,     1,      259.78, 9,      "2B",   "1C",   "PS",   1),
#(411612264,	11,	689.39,	176.538462,     "6B",	"6A",	"2S",	2),
(411612260,	11,	689.39,	169.615385,	"6B",	"6A",	"2S",	1),
    ]


# set axis limit 
plt = pg.plot()
# resizing the window
#plt = pg.GraphicsWindow(title="TEDD1 Plotter")
plt.resize(1000,600)
#plt.setAspectLocked()

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
