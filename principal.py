# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 11 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import grafica

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 430,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer4.AddSpacer( ( 100, 25), 1, wx.EXPAND, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 40), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Regresion lineal y no lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 25), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Numero de pares", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer1.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.AddSpacer( ( 100, 60), 1, wx.EXPAND, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Graficar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 12, 70, 93, 90, False, "Century Schoolbook L" ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer( ( 50, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Desplazamiento (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Fuerza (10^4N)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 150, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 60), 1, wx.EXPAND, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer3.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 12, 70, 93, 90, False, "Century Schoolbook L" ) )
		self.m_staticText11.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
	
		fgSizer6.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer6.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		fgSizer6.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )
	
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer6.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer5.AddSpacer( ( 120, 0), 1, wx.EXPAND, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Continuar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Resetear", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrl1.Bind( wx.EVT_TEXT, self.display )
		self.m_textCtrl1.Bind( wx.EVT_TEXT_ENTER, self.num_pares )
		self.m_button1.Bind( wx.EVT_BUTTON, self.num_pares )
		self.m_textCtrl2.Bind( wx.EVT_TEXT, self.display )
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.display )
		self.m_button2.Bind( wx.EVT_BUTTON, self.add_pares )
		self.m_button3.Bind( wx.EVT_BUTTON, self.continuar )
		self.m_button4.Bind( wx.EVT_BUTTON, self.resetear )	
		self.m_button2.Enable(False)
		self.m_button3.Enable(False)
		self.m_textCtrl2.Enable(False)
		self.m_textCtrl3.Enable(False)
		self.x_data = []
		self.y_data = []
		self.x_media = 0.0
		self.y_media = 0.0
		self.b1 = 0.0
		self.b0 = 0.0
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def num_pares( self, event ):
		if(self.m_textCtrl1.GetValue() != ""):
			if (self.m_textCtrl1.GetValue().isdigit() == True and int(self.m_textCtrl1.GetValue()) > 0):
				self.n_datos = self.m_textCtrl1.GetValue()
				self.m_button1.Enable(False)
				self.m_textCtrl1.Enable(False)
				self.m_button2.Enable(True)
				self.m_textCtrl2.Enable(True)
				self.m_textCtrl3.Enable(True)
				self.m_textCtrl1.SetValue("")
				print "Valido"
				
			else:
				self.m_textCtrl1.SetValue("")
				print "No es un nuero valido"
				self.m_staticText10.SetLabel("El dato ingresado es Invalido")	
		else:		
			print "No escribio nada"
			self.m_staticText10.SetLabel("No ingreso ningun dato")
			
	def add_pares( self, event ):
		if(self.m_textCtrl2.GetValue() != "" and self.m_textCtrl3.GetValue() != ""):
			try:
				x_unit = float(self.m_textCtrl2.GetValue())
				y_unit = float(self.m_textCtrl3.GetValue())
				coun = 1
			except ValueError:
				coun = 0
			if(coun):
				self.x_data.append(x_unit)
				self.x_media = self.x_media + x_unit
				self.y_data.append(y_unit)
				self.y_media = self.y_media + y_unit
				self.n_datos = int(self.n_datos) - 1;
				self.m_textCtrl2.SetValue("")
				self.m_textCtrl3.SetValue("")
			else:
				self.m_textCtrl2.SetValue("")
				self.m_textCtrl3.SetValue("")
				print "Uno o ambos no son numeros validos"
				self.m_staticText11.SetLabel("Uno o ambos no son numeros validos")
		else:
			print "uno o ambos estan vacios"
			self.m_staticText11.SetLabel("Uno o ambos estan vacios")
			self.m_textCtrl2.SetValue("")
			self.m_textCtrl3.SetValue("")
			
		if int(self.n_datos) >= 1:
			print " faltan "
		else:
			self.m_textCtrl2.Enable(False)
			self.m_textCtrl3.Enable(False)
			self.m_button2.Enable(False)
			self.m_button3.Enable(True)
			self.m_textCtrl2.SetValue("")
			self.m_textCtrl3.SetValue("")
			print "completos"
			self.calcular()
		print "x = ",self.x_data, " y = ", self.y_data
		
	def continuar( self, event ):
		grafico = grafica.Grafica()
		grafico.dibujar(self.b1, self.b0, self.x_data, self.y_data, self)

	def resetear(self, event):
		self.m_textCtrl1.Enable(True)
		self.m_textCtrl2.Enable(False)
		self.m_textCtrl3.Enable(False)
		self.m_button1.Enable(True)
		self.m_button2.Enable(False)
		self.m_button3.Enable(False)
		self.m_textCtrl1.SetValue("")
		self.m_textCtrl2.SetValue("")
		self.m_textCtrl3.SetValue("")
		self.x_data = []	
		self.y_data = []	
		self.x_media = 0.0	
		self.y_media = 0.0	
		self.n_data = 0
	def display ( self, event ):
		self.m_staticText11.SetLabel("")
		self.m_staticText10.SetLabel("")
	def calcular ( self ):
		print "media x ",self.x_media," media y", self.y_media
		print "total x ",len(self.x_data)," total y", len(self.y_data)
		sumatoria = 0.0
		sumaa = 0.0
		flag = len(self.x_data) - 1
		self.x_media = self.x_media / len(self.x_data)	  
		self.y_media = self.y_media / len(self.y_data)	  
		print "X_media = ",self.x_media, "  Y_media = ", self.y_media	
		while(flag >= 0):
			sumatoria = sumatoria + ((self.x_data[flag] - self.x_media)*(self.y_data[flag] - self.y_media))
			sumaa = sumaa + ((self.x_data[flag] - self.x_media)*(self.x_data[flag] - self.x_media))
			print "iteracion ", self.x_data[flag] , self.y_data[flag]
			flag = flag -1
		self.b1 = sumatoria / sumaa
		self.b0 = self.y_media - (self.b1*self.x_media)
		ecuacion ="Ecuacion Lineal:  f(x) = "+ str(self.b1)+"x +"+str(self.b0)
		self.m_staticText8.SetLabel(ecuacion)
		self.m_staticText9.SetLabel(ecuacion)
		print "Valor de b1 = ",self.b1,"  Valor de b0 = ",self.b0," dividendo = ", sumatoria, " divisor = ", sumaa
		
class MyApp(wx.App):
	def OnInit(self):
		frame = MyFrame1(None)
		self.SetTopWindow(frame)
		frame.Show()
		return 1
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
