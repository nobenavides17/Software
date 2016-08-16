# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 11 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import numpy as np
import grafica

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 450,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer5.AddSpacer( ( 80, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Ecuacion Lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Ecuacion Exponencial", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"K = ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.AddSpacer( ( 120, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Calcular", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Y = ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer6 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer6.AddSpacer( ( 120, 0), 1, wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Graficar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.calcular )
		self.m_button4.Bind( wx.EVT_BUTTON, self.graficar )
		self.m_button5.Bind( wx.EVT_BUTTON, self.salir )
		self.ver_data()
		self.y =0.0
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def val_lineal( self ):
		self.y = self.b1_lineal*self.x + self.b0_lineal
		print "Valor de fx ", self.y
		
	def val_nolineal( self ):
		self.y = self.b0_nolineal*(self.e ** (self.b1_nolineal * self.x))
		print "Valor de fx ",self.y
	
	def calcular ( self, event ):
		if(self.m_textCtrl2.GetValue != ""):
			if(self.m_textCtrl2.GetValue().isdigit() == True and int(self.m_textCtrl2.GetValue()) > 0):
				self.x = float(self.m_textCtrl2.GetValue())
				print "Valor de x", self.x
				if self.x >= 40:
					self.val_nolineal()
				else:	
					self.val_lineal()
				label  = "Y = "+ str(self.y)	
				self.m_staticText7.SetLabel(label)
			else:
				print "No es un numero Valido"
		else:
			print "No ingreso nada"		
	def ver_data( self ):
		self.vy= [0.1,0.17,0.27,0.35,0.39,0.42,0.43,0.44]
		self.vx = [10,20,30,40,50,60,70,80]
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
		self.lineal()
		self.no_lineal()
		self.m_staticText1.SetLabel(self.ecuacion_lineal)
		self.m_staticText2.SetLabel(self.ecuacion_nolineal)
		k = "K lineal = "+str(round(self.b1_lineal,6))+",  K no lineal = "+str(round(self.b1_nolineal,6))
		self.m_staticText3.SetLabel(k)
		
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
	
	def graficar( self, event ):
		grafico = grafica.Grafica()
		grafico.dibujar(self.b1_lineal, self.b0_lineal, self.b1_nolineal, self.b0_nolineal, self.vx, self.vy)
	
	def salir( self, event ):
		self.Close()
	
class MyApp(wx.App):
	def OnInit(self):
		frame = MyFrame1(None)
		self.SetTopWindow(frame)
		frame.Show()
		return 1
		
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
