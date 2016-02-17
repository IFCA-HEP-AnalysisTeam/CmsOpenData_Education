import os
import logging

from CmsOpenData.AnalysisDesigner.Analyzer import Analyzer

class AnalyzerSel(Analyzer):
    """Selection Analyzer class. 

    The custom analyzers should inherit from this class
    """
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

    def process(self, event):
	'''Executed on every event'''


    def endJob(self):

	print "*** writing file",self.rootfilename

        self.rootfilename.Write();

        self.rootfile.Close();

        print "*** done"

