# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 11 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer6.SetMinSize( wx.Size( 150,250 ) ) 
		
		fgSizer6.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )
		
		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,200 ), 0 )
		fgSizer6.Add( self.m_dataViewListCtrl1, 0, wx.ALL, 5 )
		
		
		fgSizer5.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		fgSizer7 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Ecuacion", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"No lineal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer7.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Ecuacion", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		fgSizer5.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	


class MyApp(wx.App):
	def OnInit(self):
		frame = MyFrame2(None)
		self.SetTopWindow(frame)
		frame.Show()
		return 1
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
