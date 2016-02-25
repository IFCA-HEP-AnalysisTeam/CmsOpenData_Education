import os
import logging
import ROOT

from Analyzer import Analyzer
from Selector import Selector

class AnalyzerSel(Analyzer):
    """Selection Analyzer class. 
    The custom analyzers should inherit from this class
    """
<<<<<<< HEAD
    def DefineHistograms(self):
        Analyzer.DefineHistograms(self)
        #Add histograms for the mass and efficiency
=======
    def beginJob(self, parameters=None):
	'''Executed before the first object comes in'''

        print '*** Begin job'
	#self.mainLogger.info( 'beginJob ')
	# Create a file, in the custom Analyzers, where the histograms will be saved 
	self.rootfile = ROOT.TFile("datafiles/goodHistos.root", "RECREATE")	
<<<<<<< HEAD
    def define_Histograms(self):
        Analyzer.define_Histograms()
        #Add the histogram for the efficiency
>>>>>>> master
        self.h_efficiency=ROOT.TH1F('h_efficiency','efficiency',10,0,11)
=======
	# Define the histograms for selected muons
	self.g_pt=ROOT.TH1F( 'g_pt', 'Muons Transverse Momentun', 50, -2, 200 )
        self.g_px=ROOT.TH1F( 'g_px', 'Muons x- Momentun', 50, -300, 300 )
        self.g_py=ROOT.TH1F( 'g_py', 'Muons y- Momentun', 50, -300, 300 )
        self.g_pz=ROOT.TH1F( 'g_pz', 'Muons z- Momentun', 50, -300, 300 )
        self.g_eta=ROOT.TH1F( 'g_eta', 'Angle Transvese', 50, -8 , 8 )
        self.g_energy=ROOT.TH1F('g_energy','Muons Energy', 50, -300,300)
        self.g_distance=ROOT.TH1F('g_distance','Distance from Primary vertex Z ', 50, -300,300)
        self.g_charge=ROOT.TH1F('g_charge','Muons Charge', 50,-2,2)
        self.g_normChi2=ROOT.TH1F('g_normChi2', 'Muons Chi2', 50, -200,200)
        self.g_numberOfValidHits=ROOT.TH1F('g_numberOfValidHits', 'Number of Valid Hits', 50, -200,200)
        self.g_dB=ROOT.TH1F('g_dB','Impact Parameter',50,-1,200)
        #self.g_edB=ROOT.TH1F('h_edB','Impact Parameter Error',50,-1,200) >> Pintar como barras de error en el histograma?
        self.g_isolation_sumPt=ROOT.TH1F('g_isolation_sumPt','IsolationX',50, -300,300)
        self.g_isolation_emEt=ROOT.TH1F('g_isolation_emEt','IsolationX',50, -300,300)
        self.g_isolation_hadEt=ROOT.TH1F('g_isolation_hadEt','IsolationX',50, -300,300)
        self.g_mass=ROOT.TH1F('g_mass', 'Inv_mass',60, 0,200)	 
>>>>>>> bf61997f2457635c63eb63e3051585cbac561fc4

    def process(self, tree, event):
	'''Executed on every event'''
	tree.GetEntry(event)
	selec = Selector()
	for particle in range(0,self.Muon_pt.size()):
                        # Fill the histogram for each variable
                                self.h_efficiency.Fill(1)
                                # Get the mass. ONLY if the events has more than 1 muon
                                if (self.Muon_pt.size()) > 1:
                                    for j in range (particle+1,self.Muon_pt.size()):
                                        if (self.Muon_charge[particle]*self.Muon_charge[j])<0:
                                                        # get the Lorentz vector for the both muons through a ROOT function 
                                                        tlv1=ROOT.TLorentzVector()
                                                        tlv1.SetPxPyPzE(self.Muon_px[particle], self.Muon_py[particle], self.Muon_pz[particle],self.Muon_energy[particle])

                                                        tlv2=ROOT.TLorentzVector()
                                                        tlv2.SetPxPyPzE(self.Muon_px[j], self.Muon_py[j], self.Muon_pz[j],self.Muon_energy[j])

                                                        # Get the mass = (TLV Muon1 + TLV Muon2).M()
                                                        mass=(tlv1+tlv2).M()
                                                        #print mass

                                                        # If the both muons are selected between the cuts fill the histogram 
		                                        if selec.selector(self,particle) and selec.selector(self, j):
								self.h_mass.Fill(mass)

				# Apply the selection over all particles in the event calling the selector function and fill the histograms for each variable
                                if selec.selector(self, particle):
					self.FillHistograms( particle)



    def endJob(self):

	self.h_efficiency.Write()
	Analyzer.endJob(self)


