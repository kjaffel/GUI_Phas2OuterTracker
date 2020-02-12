"""
first try to pass the modules coordinates to pygtgraph
plotting for: 
        - PS module
        - odd Assemblay 
        - TEDD1, surface 1
work in progress...

Qt Documentation: https://doc.qt.io/
"""
import json
import subprocess
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
#from QGraphicsDeeItem import DeeObject

sys.path.append("/home/jaffel/Phas2OuterTracker/GUI_Phase2OuterTracker")

## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see QGraphicsItem documentation)


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

data = json.loads(getProcessOutput("python DataEvenAssemblyPSModule.py"))
#data = json.loads(sys.argv[1])

class CustomiseDeeItems(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  
        self.generatePicture()

    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly, 
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        #p.TextItem('PS Module',anchor=(0.5,0))
        
        # ___ more options for style ___
        #   mkPen('y', width=3, style=QtCore.Qt.DashLine)          ## Make a dashed yellow line 2px wide
        #   mkPen(0.5)                                             ## solid grey line 1px wide
        #   mkPen(color=(200, 200, 255), style=QtCore.Qt.DotLine)  ## Dotted pale-blue line
        #module_footprint.setPen(pg.mkPen(0.5)) 

        for (id, ringNbr, radius, phi, opt, pwr, moduletype, surface) in self.data:
        ## frame node:
            
            # sensor length:
            pssensorx = 49.2 # width (mm)
            pssensory = 98.7 # height (mm)
            
            # Angle:
            angle =(phi if surface== 1 else 180-phi)
            
            # Transform to cartesian and plot
            x = radius * np.cos(phi)
            y = radius * np.sin(phi)
            
            #p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            p.setBrush(pg.mkBrush('g'))    # TODO : set pwr colour diff from opt 
            
            # Draw module 
            #p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
            p.drawRect(QtCore.QRectF(x, y, pssensorx, pssensory))
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())

# for quick test !
#data = [
        ## fields are :
        #Module_DetId, Module_RingL, Module_RingR, Module_phi_deg, OPT_Services_Channel, PWR_Services_Channel, type_/C, surface
#        (411571240,     1,         259.78,         171,                "7B",               "7A",               "PS",       2),    
#        (411571236,     1,         259.78,         153,                "6B",               "5C",               "PS",       1),     
#    ]

item = CustomiseDeeItems(data)
plt = pg.plot()
plt.showGrid(x=True, y=True)
plt.addItem(item)
plt.setWindowTitle('TEDD1, surface1 \n Full-mockup \n UCLouvain 2020')



# TODO: add the ring of the dee !
#item = CustomiseDeeItems(data)
#plot = pg.plot()
#plot.setAspectLocked()
# Add polar grid lines
#plot.addLine(x=0, pen=0.2)
#plot.addLine(y=0, pen=0.2)
#for r in range(2, 20, 2):
#    circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, r * 2, r * 2)
#    circle.setPen(pg.mkPen(0.2))
#    plot.addItem(circle)
#plot.setWindowTitle('TEDD1, surface1 \n Full-mockup \n UCLouvain 2020')

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
