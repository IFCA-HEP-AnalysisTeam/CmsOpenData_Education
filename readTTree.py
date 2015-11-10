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
		self.Vertex_Z = ROOT.std.vector('float')()

				
		# List of all muons as a list of Muon object (class Muon)
		self.all_muons = []

		# Define and init the histograms for each branch using TH1F from ROOT
		self.h_pt=ROOT.TH1F( 'h_pt', 'Muons Transverse Momentun', 50, -2, 20000 )
		self.h_px=ROOT.TH1F( 'h_px', 'Muons x- Momentun', 50, -300, 300 )
		self.h_py=ROOT.TH1F( 'h_py', 'Muons y- Momentun', 50, -300, 300 )
		self.h_pz=ROOT.TH1F( 'h_pz', 'Muons z- Momentun', 50, -300, 300 )
		self.h_eta=ROOT.TH1F( 'h_eta', 'Angle Transvese', 50, -50 , 50 )
		self.h_energy=ROOT.TH1F('h_energy','Muons Energy', 50, -300,300)
		self.h_charge=ROOT.TH1F('h_charge','Muons Charge', 50,-2,2)
		self.h_normChi2=ROOT.TH1F('h_normChi2', 'Muons Chi2', 50, -200,200)
		self.h_numberOfValidHits=ROOT.TH1F('h_numberOfValidHits', 'Number of Valid Hits', 50, -200,200)
		self.h_dB=ROOT.TH1F('h_dB','Impact Parameter',50,-1,200)
		#self.h_edB=ROOT.TH1F('h_edB','Impact Parameter Error',50,-1,200) Pintar como barras de error en el histograma?
		self.h_isolation_sumPt=ROOT.TH1F('h_isolation_sumPt','IsolationX',50, -300,300)
		self.h_isolation_emEt=ROOT.TH1F('h_isolation_emEt','IsolationX',50, -300,300)

	def process(self):

		'''
		Initialization of the reading process. This function address the data stored in the 		    tree to the different branches previously defined above. For each variable, the 
		first parameter in the sentence is the name you want for the branch and the second one 
		is the name of the real variable where the data is adressed,as we said before. This
	        variable or branch name create a physical memory direction in your computer where   		    store the information that it contains.
		'''

		self.tree.SetBranchAddress("Muon_pt", self.Muon_pt)
		self.tree.SetBranchAddress("Muon_px", self.Muon_px)
		self.tree.SetBranchAddress("Muon_py", self.Muon_py)
		self.tree.SetBranchAddress("Muon_pz", self.Muon_pz)
		self.tree.SetBranchAddress("Muon_eta", self.Muon_eta)
                self.tree.SetBranchAddress("Muon_energy", self.Muon_energy)
                self.tree.SetBranchAddress("Muon_vertex_z", self.Muon_vertex_z)
		self.tree.SetBranchAddress("Muon_dB", self.dB)
		self.tree.SetBranchAddress("Muon_edB", self.edB)
		self.tree.SetBranchAddress("Muon_isolation_sumPt",self.Muon_isolation_sumPt )
		self.tree.SetBranchAddress("Muon_isolation_emEt",self.Muon_isolation_emEt )
		self.tree.SetBranchAddress("Muon_isolation_hadEt",self.Muon_isolation_hadEt)
		self.tree.SetBranchAddress("Muon_isGlobalMuon", self.Muon_isGlobalMuon)
		self.tree.SetBranchAddress("Muon_isTrackerMuon", self.Muon_isTrackerMuon)
		self.tree.SetBranchAddress("Muon_numberOfValidHits",self.Muon_numberOfValidHits)
		self.tree.SetBranchAddress("Muon_normChi2",self.Muon_normChi2)
		self.tree.SetBranchAddress("Muon_charge",self.Muon_charge)
		self.tree.SetBranchAddress("Primary_Vertex_Z",self.Vertex_Z)		

		# numEntries: Number of entries(events) of the tree
		numEntries= self.tree.GetEntries()
	
		# For each event or entry,the following loop populates the tree branches, creates every muon and add it to all_muons list	
		for event in range(0, numEntries):

			# Address the data of each physical variable registed in this event or entry number to its branch associated listed above.   
			self.tree.GetEntry(event)

			# Loop all muons in each entry = vector size
			for position in range(0,self.Muon_pt.size()):
		     	   	#muon=Muon(event, position, self.Muon_pt[position], self.Muon_eta[position], self.Muon_energy[position], self.Muon_vertex_z[position])
				#He quitado el self.Muon_Vertex_Z[position]

				muon=Muon(event, position, self.Muon_pt[position], self.Muon_px[position],self.Muon_py[position],self.Muon_pz[position],self.Muon_eta[position], self.Muon_energy[position], self.Muon_vertex_z[position], self.dB[position], self.edB[position],self.Muon_isolation_sumPt[position],self.Muon_isolation_emEt[position],self.Muon_isolation_hadEt[position],self.Muon_isGlobalMuon[position],self.Muon_isTrackerMuon[position], self.Muon_numberOfValidHits[position],self.Muon_normChi2[position],self.Muon_charge[position], self.Vertex_Z[position])

				# Add each muon to all_muon list
				self.all_muons.append(muon)

				# print muon components
				#muon.printMuon()

				# Fill the histogram for each variable
				self.h_pt.Fill(self.Muon_pt[position])
				self.h_px.Fill(self.Muon_px[position])
				self.h_py.Fill(self.Muon_py[position])
				self.h_pz.Fill(self.Muon_pz[position])
				self.h_eta.Fill(self.Muon_eta[position])
				self.h_energy.Fill(self.Muon_energy[position])
				self.h_charge.Fill(self.Muon_charge[position])
				self.h_normChi2.Fill(self.Muon_normChi2[position])
				self.h_numberOfValidHits.Fill(self.Muon_numberOfValidHits[position])
				self.h_dB.Fill(self.dB[position])
				self.h_isolation_sumPt.Fill(self.Muon_isolation_sumPt[position])
				self.h_isolation_emEt.Fill(self.Muon_isolation_emEt[position])		

		# Create a rootfile for the histogramas
		self.fhistos = ROOT.TFile("histos.root", "RECREATE")
		# Write histograms in fhistos file
		self.h_pt.Write()
		self.h_px.Write()
		self.h_py.Write()
		self.h_pz.Write()
		self.h_eta.Write()
		self.h_energy.Write()
		self.h_normChi2.Write()
		self.h_numberOfValidHits.Write()
		self.h_dB.Write()
		self.h_isolation_sumPt.Write()
		self.h_isolation_emEt.Write()
		self.h_eta.Write()

		#Close the file
		self.fhistos.Close()

		#return muon list
		return self.all_muons
