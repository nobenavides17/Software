from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Grafica():
	def lineal(self, x):
		y = self.b1_lineal*x + self.b0_lineal
		return y
		
	def nolineal(self, x):
		y = self.b0_nolineal*(self.padre.e ** (self.b1_nolineal * x))
		return y
		
	def dibujar(self, b1_lineal, b0_lineal, b1_nolineal, b0_nolineal, xp ,yp, parent):
		self.b1_lineal = b1_lineal
		self.b0_lineal = b0_lineal
		self.b1_nolineal = b1_nolineal
		self.b0_nolineal = b0_nolineal
		self.padre = parent
		x=range(-10,10)
		yp =yp
		xp =xp
		plt.figure()
		plt.plot(x,[self.lineal(i) for i in x], 'k', linewidth = 1, label = 'Lineal')
		plt.plot(x,[self.nolineal(i) for i in x], 'r', linewidth = 1, label = 'Exponencial')
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
		"""self.padre.m_textCtrl1.Enable(True)
		self.padre.m_button1.Enable(True)
		self.padre.m_button2.Enable(False)
		self.padre.m_button3.Enable(False)
		self.padre.x_data = []
		self.padre.y_data = []
		self.padre.x_media = 0.0
		self.padre.x_total = 0.0
		self.padre.x_cuadrado = 0.0
		self.padre.y_media = 0.0
		self.padre.y_total = 0.0
		self.padre.y_log = 0.0
		self.padre.x_y_log = 0.0
		self.padre.b1_lineal = 0.0
		self.padre.b0_lineal = 0.0
		self.padre.b1_nolineal = 0.0
		self.padre.b0_nolineal = 0.0
		self.padre.m_staticText8.SetLabel("")
		self.padre.m_staticText9.SetLabel("")
		self.padre.n_data = 0.0"""
