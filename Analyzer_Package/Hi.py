import ROOT as ROOT
#import sys
from ROOT import gROOT, TH1F, TGraph, gStyle

class Hi(object):
	'''
	Class Histos which read the histos file and draw the histograms
	'''
	def __init__(self):
		'''
		Constructor: read the histograms from the both files
		'''
		self.file=ROOT.TFile("datafiles/histos.root","read")
		self.Gfile=ROOT.TFile("datafiles/goodHistos.root", "read")
		self.histogram= ROOT.TH1F()
		#self.ghisto = ROOT.TH1F()
		self.canvas = ROOT.TCanvas("", "", 800, 600)
		self.mytuple=tuple()

	def DrawHi( self, *args):
			'''
			Drawing function:
			Draw histograms of the main kinetics variables for all_muons, selected muons, and both in the same canvas
			args= 'h_pt','g_pt' (e.g)
			'''
			self.mylist=[]
			for i in args:
				if type(i) == str:
					if 'g_' in i:
						print 'g_'+i[2:]
						self.ghisto=self.Gfile.Get(i)
						self.ghisto.SetLineColor(2)                        
						self.mylist.append(self.ghisto)
						#self.canvas=self.CanvasCre(self.ghisto,i)                        
					elif 'h_' in i:
						self.histo=self.file.Get(i)
						self.mylist.append(self.histo)						
						#self.canvas=self.CanvasCre(self.histo, i)
					else:
						print ("This histogram does not exist")                        
				elif type(i) == tuple:
					self.mytuple=()                  
					for j in range(len(i)):
						if 'h_' in i[j]:
							self.histo=self.file.Get(i[j])
							self.mytuple+=(self.histo,)
						elif 'g_' in i[j]:
							self.ghisto=self.Gfile.Get(i[j])
							self.mytuple+=(self.ghisto,)
						else: 
							print ("This histogram does not exist")
					self.mylist.append(self.mytuple)

					#self.canvas=self.CanvasCre( self.mytuple, 'namess')                    
				else:
					print("This element type is not correct, try again!")
                
			self.canvas=self.CanvasCre(self.mylist, 'namess')
			return (self.histogram, self.canvas)

                
	def CanvasCre(self, mylist, name=None):
			'''
			Create and return a canvas. Set the legend configuration (because of Draw() function is returning self.histo or self.ghisto or 				both you can set the legend online )
			'''
			self.canvas = ROOT.TCanvas("", "", 800, 600)
			self.canvas.cd()
			for i in range(len(mylist)):
				print len(mylist), type(mylist), len(mylist[i]),mylist[i]                 
				if type(mylist[i]) != tuple:                   
					mylist[i].Draw()
					self.canvas.Draw()            
					self.canvas.SaveAs("../output_histograms/"+ name +".png")                   
				else: 
					print "coge tupla" 
					mylist[0].Draw()
					for j in range(1,len(mylist[i])):
						mylist[i][j].Draw("same")
						mylist[i][j].SetLineColor(5+j)
					self.canvas.Draw()            
					self.canvas.SaveAs("../output_histograms/"+ name +".png")              
			return self.canvas                


             
	def Setting(self, introvariable, saveName, **otros):
		'''
		scaleY /scaleX : string parameter. Must be 'LogY' to draw log y axis and/or to draw log x axix
		xmin,xmax,nbin,scaleY,scaleX,SetLegend
		'''
		retorno=self.DrawHi(introvariable)
		print retorno
		claves=otros.keys()    
		#for c in claves:
		if 'scale' in claves:
			s1=otros['scale']
			if s1 == 'LogY':
				retorno[1].SetLogy()
			elif s1 == 'LogX':
				retorno[1].SetLogx()
                    
		if 'legend' in claves and otros['legend'] == True:          
			legend =ROOT.TLegend(0.1,0.2,0.30,0.3)
			if type(retorno[0]) is not tuple:
				legend.AddEntry(retorno[0],"All muons","l")
			elif type(retorno[0]) == tuple:
				for j in range(len(retorno[0])):
					legend.AddEntry(retorno[0][j],"All muons","l")
					#legend.AddEntry(retorno[0][1],"Selected muons","l")
			legend.Draw()
        
		if 'xlimits' in claves:
			xmin=otros['xlimits'][0]
			xmax=otros['xlimits'][1]
			if type(retorno[0]) is not tuple:
				retorno[0].GetXaxis().SetRangeUser(xmin, xmax)
			elif type(retorno[0]) == tuple:
				for j in range(len(retorno[0])):
					retorno[0][j].GetXaxis().SetRangeUser(xmin, xmax)

		#if c == 'nbin':
		#		s5=otros[c]
		#		print s5
		#		histo.Rebin(s5)

		#else:
		#	print("The parameter that you introduced is not correct")
		print (retorno[0])
		self.CanvasCre(retorno[0], saveName)
        
        
        
### Fallan legend y scale.
### Anadir unidades y posibilidad de poner distintos ejes para distintas variables 
        
            

