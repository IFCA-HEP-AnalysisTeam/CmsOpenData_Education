import ROOT
from ROOT import gROOT , TCanvas, TH1F
import numpy as n
from scipy.stats import norm
#from scipy import optimize
#import matplotlib.mlab as mlab
#import matplotlib.pylab as P
import array

from Muon import Muon

class readTTree(object):
	"""
	Read TTree
	"""
        def __init__(self):

		# Get the tree from the file 
                self.f = ROOT.TFile("mytree.root", "read")
                self.tree = self.f.Get("muons")

		# Define and init the variables for each branch as ROOT vectors
		self.Muon_pt = ROOT.std.vector('float')()
		self.Muon_eta = ROOT.std.vector('float')()
                self.Muon_energy = ROOT.std.vector('float')()
                self.Muon_vertex_z = ROOT.std.vector('float')()
		
		# List of all muons as a list of Muon object (class Muon)
		self.all_muons = []
		self.good_muons = [] 

		self.h_pt=ROOT.TH1F( 'h_pt', 'Muons Transverse Momentun', 50, -2, 300 )

	def process(self):

		# Tell the tree to populate these given variables when reading an entry. 
		# First parameter is the branch name and second is the address of the variable where the branch data is placed. 
		self.tree.SetBranchAddress("Muon_pt", self.Muon_pt)
		self.tree.SetBranchAddress("Muon_eta", self.Muon_eta)
                self.tree.SetBranchAddress("Muon_energy", self.Muon_energy)
                self.tree.SetBranchAddress("Muon_vertex_z", self.Muon_vertex_z)
		
		# numEntries: Number of entries(events) of the tree
		numEntries= self.tree.GetEntries()
		#print numEntries
		# For each event, populate the tree branches, create every muon and add it to all_muons list
		for event in range(0, numEntries):

			# Populate the tree
			self.tree.GetEntry(event)

			# Loop all muons in each entry = vector size
			for position in range(0,self.Muon_pt.size()):
		     	   	muon=Muon(event, position, self.Muon_pt[position], self.Muon_eta[position], self.Muon_energy[position], self.Muon_vertex_z[position])
				# Add each muon to all_muon list
				self.all_muons.append(muon)
				# print muon components
				#muon.printMuon()
				# Fill the histogram for each variable
				self.h_pt.Fill(self.Muon_pt[position])
		# Create a rootfile for the histogramas
		self.fhistos = ROOT.TFile("histos.root", "RECREATE")
		# Write histograms in file
		self.h_pt.Write()
		self.fhistos.Close()
		#return muon list
		return self.all_muons
					
	def plotter(self):
                """
                Plots the histograms
                """
#                fig1 = P.figure()

#                ax_1 = fig1.add_subplot(211)
#                ax_1.hist(self.all_pt, bins = 60, alpha=0.5, label="All Muons pt", log = True)
#                ax_1.set_xlabel("Transverse Momentum")
#                ax_1.set_ylabel("frequency")
#                ax_1.legend(loc='upper right')
#                P.show()

		#c1 = ROOT.TCanvas( 'c1', 'Muons', 1)
		h_pt= TH1F( 'self.Muon_pt', 'Muons Transverse Momentun', 50, -2, 300 )
		for i in range (0, self.Muon_pt.size()):

			h_pt.Fill(self.Muon_pt[i])
		
		h_pt.Draw()
		#c1.Update()
