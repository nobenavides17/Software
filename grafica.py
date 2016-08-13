from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Grafica():
	def f_x(self, x):
		y = self.b1*x + self.b0
		return y
	def dibujar(self, b1, b0, xp ,yp, parent):
		self.b1 = b1
		self.b0 = b0
		self.padre = parent
		x=range(-10,10)
		yp =yp
		xp =xp
		plt.figure()
		plt.plot(x,[self.f_x(i) for i in x], 'b', linewidth = 1, label = 'Grafica Lineal')
		plt.scatter(xp,yp, label="", color='b', marker=".", s=100)
		plt.hold(True)
		plt.legend(loc = 2)
		plt.xlabel(r"$Desplazamiento (m)$", fontsize = 16, color = (1,0,0))
		plt.ylabel(r"$Fuerza (N)$", fontsize = 16, color = (0,0,1))
		#plt.grid(True)
		#plt.grid(color = '0.5', linestyle = '-', linewidth = 1)
		plt.axis('tight')
		plt.title('Grafica', fontsize = 28, color = '0.75', verticalalignment = 'baseline', horizontalalignment = 'center')
		plt.show()
	def __del__( self ):
		self.padre.m_textCtrl1.Enable(True)
		self.padre.m_button1.Enable(True)
		self.padre.m_button2.Enable(False)
		self.padre.m_button3.Enable(False)
		self.padre.x_data = []
		self.padre.y_data = []
		self.padre.m_staticText8.SetLabel("")
		self.padre.m_staticText9.SetLabel("")
		self.padre.n_data = 0
