import numpy as np
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class CustomiseDeeItems(pg.GraphicsObject):
    ## Create a subclass of GraphicsObject.
    ## The only required methods are paint() and boundingRect()
    ## (see QGraphicsItem documentation)

    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()

    #         for rect in data:
    #             self.drawrect(rect)

    def generatePicture(self):

        def big_square(p, colors=[1, 0]):

            w1, h1, w2, h2 = [2, 2, 2.2, 2.2]
            epsilon = w1 * 0.1

            p.rotate(-90)  # rotate to put empty part to the left
            # Exterior square
            p.setBrush(pg.mkBrush(colors[1]))
            p.setPen(0)

            xoff = - w2 / 2
            yoff = - h2 / 2

            p.translate(xoff, yoff)  # translate from center to low-x, low-y position.
            w = (w2 - w1) * 0.5
            h = h2
            rectangle = QtCore.QRectF(0, 0, w + epsilon, h)
            p.drawRoundedRect(rectangle, 0.0, 0.5)

            p.translate(w + w1 - epsilon, 0)
            w = (w2 - w1) * 0.5
            h = h2
            rectangle = QtCore.QRectF(0, 0, w + epsilon, h)
            p.drawRoundedRect(rectangle, 0.0, 0.05)

            p.translate(- w - w1 + epsilon, (h2 - h1) * 0.5 + h1)
            w = w2
            h = (h2 - h1) * 0.5
            rectangle = QtCore.QRectF(0, 0, w, h)
            p.drawRoundedRect(rectangle, 0.05, 0.0)
            p.translate(0, -epsilon)
            p.drawRect(rectangle)
            p.translate(0, epsilon)

            # Interior square
            p.setBrush(pg.mkBrush(colors[0]))
            p.setPen(pg.mkPen('k'))

            p.translate((w2 - w1) * 0.5, - h1)

            rectangle = QtCore.QRectF(0, 0, w1, h1)
            p.drawRoundedRect(rectangle, 0.05, 0.05)

            p.translate(w1 * 0.5, h1 * 0.5)  # go back to center position
            p.rotate(90)  # rotate to put empty part to the left

        def small_square(p, colors=['w', 0], linecolor='g'):

            w1, h1, w2, h2 = [2.5, 1.5, 2, 1]

            # Exterior square
            p.setBrush(pg.mkBrush(colors[1]))
            p.setPen(pg.mkPen('k'))

            p.translate(- w1 / 2, - h1 / 2)  # translate from center to low-x, low-y position.
            rectangle = QtCore.QRectF(0, 0, w1, h1)
            p.drawRoundedRect(rectangle, 0.05, 0.05)
            p.translate(w1 / 2, h1 / 2)  # go back to center positio

            # Interior square
            p.setBrush(pg.mkBrush(colors[0]))
            p.setPen(pg.mkPen(linecolor))

            p.translate(-w2 / 2, -h2 / 2)
            rectangle = QtCore.QRectF(0, 0, w2, h2)
            p.drawRoundedRect(rectangle, 0.05, 0.05)
            p.translate(w2 / 2, h2 / 2)  # go back to center positio

            # Inter-Internal
            p.setPen(pg.mkPen('k'))
            w = w2 * 0.8
            h = h2 * 0.5
            p.translate(-w / 2, -h / 2)
            rectangle = QtCore.QRectF(0, 0, w, h)
            p.drawRoundedRect(rectangle, 0.5, 0.5)

            p.translate(w / 2, h / 2)  # go back to center position

        ## pre-computing a QPicture object allows paint() to run much more quickly,
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        # p.TextItem('PS Module',anchor=(0.5,0))

        rectangle = QtCore.QRectF(-30, -5, 60, 35)
        p.drawRoundedRect(rectangle, 0., 0.)

        for (m_id, m_ringL, m_ringR, m_phi_deg, OPT_Services_Channel, PWR_Services_Channel, type_C, surf) in self.data:

            rad = m_ringR
            angle = m_phi_deg

            xin = rad * np.cos(np.radians(angle))
            yin = rad * np.sin(np.radians(angle))
            rot = angle - 90

            #         for (xin, yin, w, h , rot, color) in self.data:  # for testing

            p.translate(xin, yin)
            p.rotate(rot)

            if m_id > 5:
                big_square(p)
            else:
                small_square(p)

            p.rotate(-rot)
            p.translate(-xin, -yin)

        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())


######################################

w = 1.618  # wide
h = 1  # height

## for test                                                         # colors:   3: green, 1: orange , 0: red,
data = [  ## m_id, m_ringL, m_ringR, m_phi_deg, OPT_Services_Channel, PWR_Services_Channel, type_C, surf
    (1., 0, 10, 0, 0, 0, 0, 0),
    (2., 0, 10, 25, 0, 0, 0, 0),
    (3., 0, 10, 50, 0, 0, 0, 0),
    (4., 0, 10, 90, 0, 0, 0, 0),

    (6., 0, 20, 0, 0, 0, 0, 0),
    (7., 0, 20, 25, 0, 0, 0, 0),
    (8., 0, 20, 50, 0, 0, 0, 0),
    (8., 0, 20, 90, 0, 0, 0, 0),

]

item = CustomiseDeeItems(data)
plt = pg.plot()
plt.showGrid(x=True, y=True)
plt.addItem(item)
plt.setWindowTitle('TEDD1, surface1 \n Full-mockup \n UCLouvain 2020')


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
