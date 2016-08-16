import numpy as np
import grafica
class Calculo ():
	def set_data( self ):
		self.vx= [0.1,0.17,0.27,0.35,0.39,0.42,0.43,0.44]
		self.vy = [10,20,30,40,50,60,70,80]
		self.vx_lineal = self.vx[0:4]
		self.vx_nolineal = self.vx[4:8]
		self.vy_lineal = self.vy[0:4]
		self.vy_nolineal = self.vy[4:8]
		self.c_ndata_lineal = len(self.vx_lineal)
		self.c_ndata_nolineal = len(self.vx_nolineal)
		print "X Lineales",self.vx_lineal
		print "X No Lineales",self.vx_nolineal
		print "Y Lineales",self.vy_lineal
		print "Y No Lineales",self.vy_nolineal
		print "Lineales Totales",self.c_ndata_lineal
		print "No Lineales Totales",self.c_ndata_nolineal
		
	def lineal ( self ):
		self.vx_total = sum(self.vx_lineal)
		self.vy_total = sum(self.vy_lineal)
		self.vx_media = self.vx_total / self.c_ndata_lineal
		self.vy_media = self.vy_total / self.c_ndata_lineal
		print "	Valores Lineales"
		print "Numero de datos = ", self.c_ndata_lineal
		print "Sumatoria de x = ", self.vx_total
		print "Sumatoria de y =", self.vy_total
		print "Media de x = ", self.vx_media
		print "Media de y = ", self.vy_media
		dividendo = 0.0
		divisor = 0.0
		c_ndata = self.c_ndata_lineal - 1
		while(c_ndata >= 0):
			dividendo = dividendo + ((self.vx_lineal[c_ndata] - self.vx_media)*(self.vy_lineal[c_ndata] - self.vy_media))
			divisor = divisor + ((self.vx_lineal[c_ndata] - self.vx_media) ** 2)
			c_ndata = c_ndata -1
		self.b1_lineal = dividendo / divisor
		self.b0_lineal = self.vy_media - (self.b1_lineal*self.vx_media)
		if(self.b0_lineal > 0):
			signo = " + "
		else:
			signo = " - "	
		self.ecuacion_lineal ="Ecuacion Lineal:  f(x) = "+ str(round(self.b1_lineal,6))+"x "+signo+" "+str(round(abs(self.b0_lineal),6))
		
	def no_lineal ( self ):
		self.e = 2.71828182846
		self.vx_log_y = []
		self.v_log_y = []
		self.v_x_x = []
		c_ndata = self.c_ndata_nolineal - 1
		while (c_ndata >= 0):
			self.vx_log_y.append(np.log(self.vy_nolineal[c_ndata])*self.vx_nolineal[c_ndata])
			self.v_log_y.append(np.log(self.vy_nolineal[c_ndata]))
			self.v_x_x.append(self.vx_nolineal[c_ndata] ** 2 )
			c_ndata = c_ndata -1
		self.vx_y_log = sum(self.vx_log_y)
		self.vy_log_y = sum(self.v_log_y)
		self.vx_x = sum(self.v_x_x)
		self.v_log_y_media = self.vy_log_y / self.c_ndata_nolineal
		self.vx_total_nl = sum(self.vx_nolineal)
		self.vx_media_nl = self.vx_total_nl / self.c_ndata_nolineal
		print "	Valores no lineales"
		print "Numero de datos = ", self.c_ndata_nolineal
		print "Sumatoria x = ", self.vx_total_nl
		print "Sumatoria x log(y) = ", self.vx_y_log
		print "Sumatoria log(y) = ", self.vy_log_y
		print "Sumatoria x^2 = ", self.vx_x
		print "Media log(y) = ", self.v_log_y_media	
		self.b1_nolineal = (self.vx_y_log - (self.v_log_y_media * self.vx_total_nl)) / (self.vx_x - (self.vx_media_nl * self.vx_total_nl))
		self.b0_nolineal = self.e ** (self.v_log_y_media - (self.b1_nolineal*self.vx_media_nl))
		self.ecuacion_nolineal ="Ecuacion no Lineal:  f(x) = "+ str(round(self.b0_nolineal,6))+"e^"+str(round(self.b1_nolineal,6))+"x"
		print self.ecuacion_lineal
		print self.ecuacion_nolineal
	def graficar( self ):
		val = True
		while(val):
			r = raw_input("Desea Generar la Grafica (G) / Salir (S) : ")
			if(r == "g" or r == "G"):
				grafico = grafica.Grafica()
				grafico.dibujar(self.b1_lineal, self.b0_lineal, self.b1_nolineal, self.b0_nolineal, self.vx, self.vy)
			elif(r == "S" or r == "s"):
				val = False
			else:
				print "Ingrese una Opcion Valida"
nuevo = Calculo()
nuevo.set_data()
nuevo.lineal()
nuevo.no_lineal()
nuevo.graficar()
