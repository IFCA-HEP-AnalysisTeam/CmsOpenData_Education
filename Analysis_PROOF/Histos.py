import ROOT as ROOT
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from ROOT import gROOT, TH1F, TGraph, gStyle
import matplotlib as plt
import numpy

class Histos(object):
	'''
	Class Histos which read the histos file and draw the histograms
	'''
	def __init__(self):
		'''
		Constructor: only read the histograms from the both files
		'''
		self.file=ROOT.TFile("../files/histos.root","read")
		self.Gfile=ROOT.TFile("../files/goodHistos.root", "read")
		
	#### bins and bounds?????

	def drawHisto(self, *args):
		'''
		DrawHisto function just prints the histograms for all muons 
		'''
                for i in args:
			self.histo=self.file.Get('h_'+i)
                        self.createCanvas(self.histo, 'h_'+i)

	def drawSelHisto(self, *args):
		'''
		DrawSelHisto function prints the histograms for the selected muons
		'''
                for i in args:
                        self.gHisto=self.Gfile.Get('g_'+i)
                        self.createCanvas(self.gHisto, 'g_'+ i)

	def drawTwoHistos(self, *args): 
		'''
		drawTwoHistos prints all and good muons in the same Histogram 
		The efficiency is the only variable which has one histogram
		'''
		for i in args:
			if i != 'efficiency':
				self.histo=self.file.Get('h_'+i)
                                self.gHisto=self.Gfile.Get('g_'+i)
                                self.createCanvas( self.histo, 'hg_'+i, self.gHisto)
			else:
				self.histo=self.Gfile.Get('h_'+i)
				self.createCanvas( self.histo, 'h_'+i)
		

	def GaussianFit(self, histo):
		'''
		Fit Histograms for Exercise 3. 
		### FALTA Fit Breit Wigner  
		'''
		self.gHisto=self.Gfile.Get('g_'+histo)
		self.gHisto.Fit("gaus")		
		#self.fit1 = self.gHisto.GetFunction("gaus")
		gStyle.SetOptFit()
		self.createCanvas(self.gHisto, 'fit_'+histo)

	def createCanvas(self, histo, i=None, gHisto=None):
		'''
		Create Canvas for only all muons histogram or both histograms: all and selected muons 
		'''
		# Create Canvas = canvas
		canvas = ROOT.TCanvas("", "", 1)
	
		canvas.cd()
		# Print histogram
		histo.Draw()
		# If we want to print both histograms in the same canvas:
		if gHisto is not None:
			gHisto.SetLineColor(2)
			gHisto.Draw("same")
		
		canvas.Update()
		canvas.Draw()		

		# Save Canvas in histos directory
		canvas.SaveAs("$HOME/CmsOpendata/histos/"+ i +".png")

    		# ONLY WAY found to display and keep the canvas on screen
		#ROOT.gApplication.Run()

#if __name__=="__main__":
#	main()
