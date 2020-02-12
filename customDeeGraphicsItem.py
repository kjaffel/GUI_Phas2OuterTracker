"""
first try to pass the modules coordinates  for PS module
work in progress...

"""
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see QGraphicsItem documentation)

class CustomiseDeeItems(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()

    def GetAngle (s):
        if s == 1:
            x = 30 # TODO  ask Maksym !
            module_angle= x
        else:
            module_angle= 180 - x
        return

    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly, 
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        #p.TextItem('PS Module',anchor=(0.5,0))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        
        # ___ more options for style ___
        #   mkPen('y', width=3, style=QtCore.Qt.DashLine)          ## Make a dashed yellow line 2px wide
        #   mkPen(0.5)                                             ## solid grey line 1px wide
        #   mkPen(color=(200, 200, 255), style=QtCore.Qt.DotLine)  ## Dotted pale-blue line
        #module_footprint.setPen(pg.mkPen(0.5)) 

        for (t, open, close, min, max) in self.data:  # for testing
        ## frame node:
        ## TODO converted from latex to python
        #\node[preaction={fill=\pwrcolour, fill}, align=center, rotate=\angle, chamfered rectangle, chamfered rectangle ysep=5mm, module_footprint, frame_pattern, inner sep=0pt, minimum height=130mm] (framenode) at (\angle:#2mm) {\hspace{69.6mm}};
         
            # sensor length:
            pssensorx = 49.2 # mm
            pssensory = 98.7 # mm


            #p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            p.setBrush(pg.mkBrush('g'))    # TODO  set pwr opt colour 
            p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())


## for test
data = [  ## fields are (t, open, close, min, max).
    (1., 10, 13, 5, 15),
    (2., 13, 17, 9, 20),
    (3., 17, 14, 11, 23),
    (4., 14, 15, 5, 19),
    (5., 15, 9, 8, 22),
    (6., 9, 15, 8, 16),
]

datav1 = [
        ## fields are :
        #Module_DetId, Module_RingL, Module_RingR, Module_phi_deg, OPT_Services_Channel, PWR_Services_Channel, type_/C, surface,    latexformula
        (411571240,     1,      259.78, 171,    "7B",   "7A",   "PS",   2),     # \psmodule{171}{259.78}{411571240}{7B}{7A}
        (411571236,     1,      259.78, 153,    "6B",   "5C",   "PS",   1),     # \psmodule{153}{259.78}{411571236}{6B}{5C}
    ]

item = CustomiseDeeItems(data)
plt = pg.plot()
plt.showGrid(x=True, y=True)
plt.addItem(item)
plt.setWindowTitle('pyqtgraph example: customGraphicsItem')

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
