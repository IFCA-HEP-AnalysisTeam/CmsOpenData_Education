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
		self.Muon_px= ROOT.std.vector('float')()
		self.Muon_py= ROOT.std.vector('float')()
		self.Muon_pz= ROOT.std.vector('float')()
		self.Muon_eta = ROOT.std.vector('float')()
                self.Muon_energy = ROOT.std.vector('float')()
                self.Muon_vertex_z = ROOT.std.vector('float')()
		self.dB = ROOT.std.vector('float')()
		self.edB = ROOT.std.vector('float')()
		self.Muon_isolation_sumPt = ROOT.std.vector('float')()
		self.Muon_isolation_emEt = ROOT.std.vector('float')()
		self.Muon_isolation_hadEt = ROOT.std.vector('float')()
		self.Muon_isGlobalMuon = ROOT.std.vector('int')()
		self.Muon_isTrackerMuon = ROOT.std.vector('int')()
		self.Muon_numberOfValidHits = ROOT.std.vector('int')()
		self.Muon_normChi2 = ROOT.std.vector('float')()
		self.Muon_charge = ROOT.std.vector('int')()
		self.Muon_Vertex_Z = ROOT.std.vector('float')()

		self.variable = {
                        0: "pt",
                        1: "px",
                        2: "py",
                        3: "pz",
                        4: "eta",
                        5: "energy",
                        6: "vertex_z",
                        7: "dB",
                        8: "edB",
                        9: "isolation_sumPt",
                        10: "isolation_emEt",
                        11:"isolation_hadEt",
                        12:"numberOfValidHits",
                        13: "normChi2",
                        14: "charge",
                        15: "isGlobalMuon",
                        16: "isTrackerMuon",
                        17: "Vertex_Z"}
		

		self.vector = [self.Muon_pt, self.Muon_px, self.Muon_py, self.Muon_pz, self.Muon_eta, self.Muon_energy, self.Muon_vertex_z, self.dB, self.edB, self.Muon_isolation_sumPt, self.Muon_isolation_emEt, self.Muon_isolation_hadEt, self.Muon_numberOfValidHits, self.Muon_normChi2, self.Muon_charge, self.Muon_isGlobalMuon, self.Muon_isTrackerMuon, self.Muon_Vertex_Z] 
				
		# List of all muons as a list of Muon object (class Muon)
		self.all_muons = []

		# Define and init the histograms for each branch using TH1F from ROOT
		self.histograms={}

		self.attributes = [[]]
		# Dictionary: Set of variables
		self.variable = {
	                0: "pt",
			1: "px", 
			2: "py",
			3: "pz",
        	        4: "eta",
			5: "energy",
			6: "vertex_z",
                        7: "dB",
			8: "edB",
                	9: "isolation_sumPt",
                	10: "isolation_emEt",
			11:"isolation_hadEt",
			12:"numberOfValidHits",
                	13: "normChi2",
                	14: "charge", 
			15: "isGlobalMuon", 
			16: "isTrackerMuon", 
			17: "Vertex_Z"}
			
		for i in range(0, len(self.variable)):
			#self.histograms[i]= ROOT.TH1F(self.variable[i], self.variable[i], 50, -300, 300)
			self.declareHisto(i, self.variable[i], 50, -300, 300)


	def process(self):

		'''
		Initialization of the reading process. This function address the data stored in the 		    tree to the different branches previously defined above. For each variable, the 
		first parameter in the sentence is the name you want for the branch and the second one 
		is the name of the real variable where the data is adressed,as we said before. This
	        variable or branch name create a physical memory direction in your computer where   		    store the information that it contains.
		'''
		# name of Vertez Z is Vertex_Z instead of Primary_Vertex_Z
		for i in range(0, len(self.vector)): 
			self.tree.SetBranchAddress("Muon_"+self.variable[i], self.vector[i])
		
		# numEntries: Number of entries(events) of the tree
		numEntries= self.tree.GetEntries()
	
		# For each event or entry,the following loop populates the tree branches, creates every muon and add it to all_muons list	
		for event in range(0, numEntries):

			# Address the data of each physical variable registed in this event or entry number to its branch associated listed above.   
			self.tree.GetEntry(event)

			# Loop all muons in each entry = vector size
			for position in range(0,self.vector[0].size()):
		     	   	#muon=Muon(event, position, self.Muon_pt[position], self.Muon_eta[position], self.Muon_energy[position], self.Muon_vertex_z[position])
				self.attributes=[]
				print len(self.variable)
				for var in range(0, len(self.variable)):
					
					self.attributes.append(self.vector[var][position])
				print self.attributes[0]
				muon=Muon(event, position, self.attributes)

			#	muon=Muon(event, position, self.Muon_pt[position], self.Muon_px[position],self.Muon_py[position],self.Muon_pz[position],self.Muon_eta[position], self.Muon_energy[position], self.Muon_vertex_z[position], self.dB[position], self.edB[position],self.Muon_isolation_sumPt[position],self.Muon_isolation_emEt[position],self.Muon_isolation_hadEt[position],self.Muon_isGlobalMuon[position],self.Muon_isTrackerMuon[position], self.Muon_numberOfValidHits[position],self.Muon_normChi2[position],self.Muon_charge[position], self.Vertex_Z[position])

				# Add each muon to all_muon list
				self.all_muons.append(muon)
				# print muon components
				#muon.printMuon()

				for i in range(0, len(self.variable)):
                		        self.fillHisto(i, self.vector[i][position])
		
		for i in range(0,10):
			print self.all_muons[i].printMuon()
			
		# Create a rootfile for the histogramas
		self.fhistos = ROOT.TFile("histos.root", "RECREATE")
		# Write histograms in fhistos file
		
		for i in range(0, len(self.histograms)):
			self.histograms[i].Write()
		
		#Close file
		self.fhistos.Close()

		#return muon list
		return self.all_muons

	def declareHisto(self, i, name, bins, min, max, xlabel='value'):
		self.histograms[i]= ROOT.TH1F("h_"+name, name, bins, min, max)
		# Does not work
		#self.histograms[i].setXAxisTitle(xlabel+' of '+name)
		#self.histograms[i].SetYaxisTitle('events')
	
	def fillHisto(self, i, value, weight=1):
		self.histograms[i].Fill(value, weight)


