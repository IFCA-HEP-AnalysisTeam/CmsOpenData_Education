import ROOT as ROOT
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from Muon import Muon
from readTTree import readTTree
from Selector import Selector

from ROOT import gROOT, TH1F, TGraph
import matplotlib as plt
import numpy

def main():
#class Histos(object)
#	"""
#	Draw Histograms
#	"""
#
#	def __init__(self):

		#fig=plt.figure()
		file=ROOT.TFile("histos.root","read")
		Gfile=ROOT.TFile("histos_good.root", "read")
		
		histo=file.Get('self.Muon_pt')


		histo.Print()	
		histo.SetDirectory(gROOT)
		histo.Sumw2()
		histo.Plot()
		#histo.Draw()	

		#plt.Show()
    		

if __name__=="__main__":
	main()
