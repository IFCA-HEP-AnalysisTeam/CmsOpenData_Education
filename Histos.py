import ROOT as ROOT
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from Muon import Muon
from readTTree import readTTree
#from Selector import Selector

from ROOT import gROOT, TH1F, TGraph
import matplotlib as plt
import numpy

#def main():
#class Histos(object)
#	"""
#	Draw Histograms
#	"""
#
#	def __init__(self):


file=ROOT.TFile("histos.root","read")
Gfile=ROOT.TFile("histos_good.root", "read")

histo=file.Get('h_pt')

ROOT.TCanvas.__init__._creates = False
canvas = ROOT.TCanvas()

ROOT.SetOwnership(canvas, False)
	
canvas.cd()
canvas.Range(-68.75, -7.5, 856.25, 42.5)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetBorderSize(2)
canvas.SetTickx(1)
canvas.SetTicky(1)
canvas.SetLeftMargin(0.15)
canvas.SetRightMargin(0.05)
canvas.SetTopMargin(0.05)
canvas.SetBottomMargin(0.15)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas._showGuideLines = False


histo.Draw()
plot = {'canvas': canvas}

canvas.Update()
canvas.Draw()		

canvas.SaveAs("h_pt.png")

    		
ROOT.gApplication.Run()

#if __name__=="__main__":
#	main()
