import ROOT
import numpy as n
from scipy.stats import norm
#from scipy import optimize
#import matplotlib.mlab as mlab
import matplotlib
matplotlib.use('QT4agg')
import matplotlib.pylab as P
import array

class readTTree(object):
	"""
	Read TTree
	"""
        def __init__(self):

                """
                TwoMuonAnalyzer initializer
                """
                self.f = ROOT.TFile("mytree.root", "read")
                self.tree = self.f.Get("muons")

		self.Muon_pt = ROOT.std.vector('float')()
		self.Muon_eta = ROOT.std.vector('float')()
                self.Muon_energy = ROOT.std.vector('float')()
                self.Muon_vertex_z = ROOT.std.vector('float')()

		self.npart = ROOT.std.vector('int')()

		self.all_pt = [] 
		self.all_eta = []
                self.all_energy = []
                self.all_vertex_z = []		


	def process(self):

		self.tree.SetBranchAddress("Muon_pt", self.Muon_pt)
		self.tree.SetBranchAddress("Muon_eta", self.Muon_eta)
                self.tree.SetBranchAddress("Muon_energy", self.Muon_energy)
                self.tree.SetBranchAddress("Muon_vertex_z", self.Muon_vertex_z)
		
		self.tree.SetBranchAddress("npart", self.npart)
                
		numEntries= self.tree.GetEntries()

		for i in range(0, numEntries):

			'''
			Populate the tree
			'''
			self.tree.GetEntry(i)

			for iMuon in range(0, self.npart[0] ):
				self.all_pt.append(self.tree.Muon_pt[iMuon])
				self.all_eta.append(self.tree.Muon_eta[iMuon])
                                self.all_energy.append(self.tree.Muon_energy[iMuon])
                                self.all_vertex_z.append(self.tree.Muon_vertex_z[iMuon])



	def plotter(self):
                """
                Plots the histograms
                """
                fig1 = P.figure()

                ax_1 = fig1.add_subplot(211)
                ax_1.hist(self.all_pt, bins = 60, alpha=0.5, label="All Muons pt", log = True)
                ax_1.set_xlabel("Transverse Momentum")
                ax_1.set_ylabel("frequency")
                ax_1.legend(loc='upper right')

                P.show()
