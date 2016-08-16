from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Grafica():
	def lineal(self, x):
		y = self.b1_lineal*x + self.b0_lineal
		return y
		
	def nolineal(self, x):
		y = self.b0_nolineal*(self.e ** (self.b1_nolineal * x))
		return y
		
	def dibujar(self, b1_lineal, b0_lineal, b1_nolineal, b0_nolineal, xp ,yp):
		self.b1_lineal = b1_lineal
		self.b0_lineal = b0_lineal
		self.b1_nolineal = b1_nolineal
		self.b0_nolineal = b0_nolineal
		xl=[0.1,0.12,0.13,0.14,0.15,0.16, 0.17,0.18,0.19, 0.27,0.28,0.29, 0.35,0.36,0.37,0.38,0.43]
		xnl=[0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.40,0.41,0.42,0.43,0.44,0.45,0.46,0.47]
		self.e = 2.71828182846
		yp = yp
		xp= xp
		plt.figure()
		plt.plot(xl,[self.lineal(i) for i in xl], 'k', linewidth = 1, label = 'Lineal')
		plt.plot(xnl,[self.nolineal(i) for i in xnl], 'r', linewidth = 1, label = 'Exponencial')
		plt.scatter(xp,yp, label="", color='b', marker=".", s=100)
		plt.hold(True)
		plt.legend(loc = 2)
		plt.xlabel(r"$Desplazamiento (m)$", fontsize = 16, color = (1,0,0))
		plt.ylabel(r"$Fuerza (N)$", fontsize = 16, color = (0,0,1))
		plt.grid(True)
		plt.grid(color = '0.5', linestyle = ':', linewidth = 0.5)
		plt.axis('tight')
		plt.title('Grafica', fontsize = 28, color = '0.75', verticalalignment = 'baseline', horizontalalignment = 'center')
		
		
		plt.show()
	def __del__( self ):
		pass
