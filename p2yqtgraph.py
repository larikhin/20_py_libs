import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

app = pg.mkQApp("Plotting Example")
#mw = QtWidgets.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(600,400)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

data = [1,2,54,45,76,99,34,9,3,34,5,6,]
data2 = [12,24,34,32,32,33,24,12,34,]
p1 = win.addPlot(title="Basic array plotting", y=data)
p2 = win.addPlot(title="Basic array plotting", y=data2)


if __name__ == '__main__':
    pg.exec()
 
