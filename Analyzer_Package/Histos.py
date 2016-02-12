import ROOT as ROOT
#import sys
from ROOT import gROOT, TH1F,TF1, TGraph, gStyle

class Histos(object):
	'''
	Class Histos which read the histos file and draw the histograms
	'''
	def __init__(self):
		'''
		Constructor: read the histograms from the both files
		'''
		self.file=ROOT.TFile("datafiles/histos.root","read")
		self.Gfile=ROOT.TFile("datafiles/goodHistos.root", "read")
		#self.histogram= ROOT.TH1F()
		#self.ghisto = ROOT.TH1F()
		self.canvas = ROOT.TCanvas("", "", 800, 600)
		self.mytuple=tuple()
		self.legend =ROOT.TLegend(0.1,0.2,0.30,0.3)

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
			print mylist
			if type(mylist) is not list:
				mylist.Draw()
				self.canvas.Draw()
                                self.canvas.SaveAs("../output_histograms/"+ mylist.GetName() +".png")
			else:
				for i in range(0,len(mylist)):
					if type(mylist[i]) != tuple:                   
						mylist[i].Draw()
						self.canvas.Draw()            
						self.canvas.SaveAs("../output_histograms/"+ name +".png")                   
					else:                     
						mylist[i][0].Draw()
						for j in range(1,len(mylist[i])):
							## Poner nuestro titulo para mas de un histo en el mismo canvas 
							## mylist[i][0].GetName().SetTitle(pt/eta/distance Comparation")
							mylist[i][j].Draw("same")
							mylist[i][j].SetLineColor(5+j)
						self.canvas.Draw()
						self.canvas.SaveAs("../output_histograms/"+ name +".png")              
				return self.canvas                


             
	def Setting(self, saveName, *histo_name,**otros):
		'''
		scaleY /scaleX : string parameter. Must be 'LogY' to draw log y axis and/or to draw log x axix
		xmin,xmax,nbin,scaleY,scaleX,SetLegend
		'''
		self.DrawHi(*histo_name)
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
				#self.legend =ROOT.TLegend(0.1,0.2,0.30,0.3)
				if type(self.mylist[i]) != tuple:
					legend =ROOT.TLegend(0.1,0.2,0.30,0.3);
					legend.SetHeader("The Legend Title");
					self.legend.AddEntry(self.mylist[i],"All muons","l")
				else:
					for j in range(0,len(self.mylist[i])):
						legend =ROOT.TLegend(0.1,0.2,0.30,0.3);
						legend.SetHeader("The Legend Title");                        
						self.legend.AddEntry(self.mylist[i][j],"All muons","l")
						#legend.AddEntry(retorno[0][1],"Selected muons","l")
				self.legend.Draw()
			if 'xlimits' in claves:
				xmin=otros['xlimits'][0]
				xmax=otros['xlimits'][1]
				if type(self.mylist[i]) is not tuple:
					self.mylist[i].GetXaxis().SetRangeUser(xmin, xmax)
				else:
					for j in range(len(self.mylist[i])):
						self.mylist[i][j].GetXaxis().SetRangeUser(xmin, xmax)
			if 'nbin' in claves:
				s5=otros['nbin']
				#print s5
				self.mylist[i].Rebin(s5)

			#else:
			#	print("The parameter that you introduced is not correct")
		self.CanvasCre(self.mylist, saveName)
        
        
        
### Fallan legend y scale.
### Anadir unidades y posibilidad de poner distintos ejes para distintas variables 
        ##################################################################
	### 		              FIT     			       ###
	##################################################################
	def GaussianFit(self, histo):
                self.gHisto=self.Gfile.Get('g_'+histo)
                self.gHisto.Fit("gaus")
                #self.fit1 = self.gHisto.GetFunction("gaus")
                gStyle.SetOptFit()
                self.CanvasCre(self.gHisto, histo)

	def BreitWignerFit(self, histo):
		self.gHisto=self.Gfile.Get('g_'+histo)
		division = self.gHisto.GetNbinsX()
            	massMIN = self.gHisto.GetBinLowEdge(1)
            	massMAX = self.gHisto.GetBinLowEdge(division+1)
            	BIN_SIZE = self.gHisto.GetBinWidth(1)

		# Create a TF1 object called func 
		func = TF1("mybw",self.mybw,massMIN, massMAX,3)
		
		# Set parameter start values for the function
		func.SetParameter(0, 1)
            	func.SetParameter(2, 5)
            	func.SetParameter(1, 95)
		
		self.gHisto.Fit("mybw","QR")

		gStyle.SetOptFit()
                self.CanvasCre(self.gHisto, histo)

	# Breit-Wigner function
	def mybw(self, x, par):
		arg1 = 14.0/22.0 # 2 over pi
  		arg2 = par[1]*par[1]*par[2]*par[2] #Gamma=par[1]  M=par[2] 
 		arg3 = ((x[0]*x[0]) - (par[2]*par[2]))*((x[0]*x[0]) - (par[2]*par[2]))
  		arg4 = x[0]*x[0]*x[0]*x[0]*((par[1]*par[1])/(par[2]*par[2]))
  		return par[0]*arg1*arg2/(arg3 + arg4)

