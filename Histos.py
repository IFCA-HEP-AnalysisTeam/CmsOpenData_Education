import ROOT as ROOT
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from Muon import Muon
from readTTree import readTTree
#from Selector import Selector

from ROOT import gROOT, TH1F, TGraph, gStyle
import matplotlib as plt
import numpy

#def main():
#class Histos(object)
#	"""
#	Draw Histograms
#	"""
#
class Histos(object):

	def __init__(self):

		self.file=ROOT.TFile("histos.root","read")
		self.Gfile=ROOT.TFile("histos_good.root", "read")
		
	#### bins and bounds?????

	def drawHisto(self, *args):

                for i in args:
			self.histo=self.file.Get('h_'+i)
                        self.createCanvas(self.histo, i)

	def drawSelHisto(self, *args):

                for i in args:
                        self.gHisto=self.Gfile.Get('g_'+i)
                        self.createCanvas(self.gHisto, i)



	def drawTwoHistos(self, *args): 

		for i in args:
			if i != 'efficiency' and i!='mass':
				self.histo=self.file.Get('h_'+i)
                                self.gHisto=self.Gfile.Get('g_'+i)
                                self.createCanvas( self.histo, i, self.gHisto)
			else:

				self.histo=self.Gfile.Get('g_'+i)
				self.createCanvas( self.histo, i)
		

	def GaussianFit(self, histo):
		self.gHisto=self.Gfile.Get('g_'+histo)
		self.gHisto.Fit("gaus")		
		#self.fit1 = self.gHisto.GetFunction("gaus")
		gStyle.SetOptFit()
		self.createCanvas(self.gHisto, histo)

	def createCanvas(self, histo, i=None, gHisto=None):
				
		canvas = ROOT.TCanvas("", "", 1)
	
		canvas.cd()
		
		histo.Draw()
		if gHisto is not None:
			gHisto.SetLineColor(2)
			gHisto.Draw("same")
		
		canvas.Update()
		canvas.Draw()		

		canvas.SaveAs("$HOME/CmsOpendata/histos/"+ i +".png")

    		
		ROOT.gApplication.Run()

#if __name__=="__main__":
#	main()
