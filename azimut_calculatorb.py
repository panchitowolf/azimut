#!/usr/bin/python
# coding=utf-8

from obspy.core import read
import time
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *
from decimal import *
from scipy import signal






#************************************GRAFICO
#getcontext().prec = 6
canaluno = read('C.GO01..BHN.M.2014.091.234612.SAC')
canaldos = read('C.GO01..BHE.M.2014.091.234612.SAC')
canaltres = read('C.GO01..BHZ.M.2014.091.234612.SAC')

xx = canaluno[0]
yy = canaldos[0]
zz = canaltres[0]






#print xx.stats
#ntx = mlab.detrend(xx.data[0:len(xx)-1], key='linear')
#ntz = mlab.detrend(zz.data[0:len(xx)-1], key='linear')
#nty = mlab.detrend(yy.data[0:len(xx)-1], key='linear')




cx = np.array(xx.data)
cy = np.array(yy.data)
cz = np.array(zz.data)

#============= Remover Tend ===========
ntx= signal.detrend(cx)
nty= signal.detrend(cy)
ntz= signal.detrend(cz)

#============ Diferencia ===============

#fd=np.diff(cx)
#fd1=np.diff(cy)
#fd2=np.diff(cz)

#============ PLOTEAR =================

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.set_title('SIGNAL')
ax1.plot(ntx)

ax2 = fig.add_subplot(312)
ax2.plot(xx, 'g')

ax3 = fig.add_subplot(313)
ax3.plot(xx - ntx, 'y')

plt.show()