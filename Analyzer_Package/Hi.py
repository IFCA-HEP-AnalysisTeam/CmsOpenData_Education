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
					for j in range(0,len(i)):
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
			return (self.mylist, self.canvas)

                
	def CanvasCre(self, mylist, name=None):
			'''
			Create and return a canvas. Set the legend configuration (because of Draw() function is returning self.histo or self.ghisto or 				both you can set the legend online )
			'''
			#self.canvas = ROOT.TCanvas("", "", 800, 600)
			#self.canvas.cd()
			for i in range(0,len(mylist)):
				if type(mylist[i]) != tuple:                   
					mylist[i].Draw()
					self.canvas.Draw()            
					self.canvas.SaveAs("../output_histograms/"+ name +".png")                   
				else: 
					print mylist[i][0] 
					mylist[i][0].Draw()
					for j in range(1,len(mylist[i])):
						mylist[i][j].Draw("same")
						mylist[i][j].SetLineColor(5+j)
					self.canvas.Draw()            
					self.canvas.SaveAs("../output_histograms/"+ name +".png")              
			return self.canvas                


             
	def Setting(self, histo_name, saveName, **otros):
		'''
		scaleY /scaleX : string parameter. Must be 'LogY' to draw log y axis and/or to draw log x axix
		xmin,xmax,nbin,scaleY,scaleX,SetLegend
		'''
		self.DrawHi(histo_name)
		claves=otros.keys()    
		for i in range(0,len(self.mylist)):
			#print "retorno[0]: ", retorno[0][0], "type:",type(retorno[0][0])
			if 'scale' in claves:
				s1=otros['scale']
				if s1 == 'LogY':
					self.canvas.SetLogy()
				elif s1 == 'LogX':
					self.canvas.SetLogx()
                    
			if 'legend' in claves and otros['legend'] == True:          
	
				print "Entra a leyenda"
				legend =ROOT.TLegend(0.1,0.2,0.30,0.3)
				print legend
				if type(self.mylist[i]) != tuple:
					legend.AddEntry(self.mylist[i],"All muons","l")
					print "Anade el primer histo a la leyenda"
				else:
					for j in range(0,len(self.mylist[i])):
						legend.AddEntry(self.mylist[i][j],"All muons","l")
						#legend.AddEntry(retorno[0][1],"Selected muons","l")
				legend.Draw()
        
			if 'xlimits' in claves:
				xmin=otros['xlimits'][0]
				xmax=otros['xlimits'][1]
				if type(self.mylist[i]) is not tuple:
					self.mylist[i].GetXaxis().SetRangeUser(xmin, xmax)
				else:
					for j in range(len(retorno[0][i])):
						self.mylist[i][j].GetXaxis().SetRangeUser(xmin, xmax)

			if 'nbin' in claves:
				s5=otros['xlimits']
				print s5
				histo.Rebin(s5)

			#else:
			#	print("The parameter that you introduced is not correct")
		self.CanvasCre(self.mylist, saveName)
        
        
        
### Fallan legend y scale.
### Anadir unidades y posibilidad de poner distintos ejes para distintas variables 
        
            

