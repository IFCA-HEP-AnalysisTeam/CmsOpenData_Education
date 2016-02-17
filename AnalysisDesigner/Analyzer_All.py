import os
import logging

from CmsOpenData.AnalysisDesigner.Analyzer import Analyzer

class AnalyzerAll(Analyzer):
    """Analyzer class for all muons. 

    """
    def beginJob(self, parameters=None):
	'''Executed before the first object comes in'''

        print '*** Begin job'
	#self.mainLogger.info( 'beginJob ')
	# Create a file, in the custom Analyzers, where the histograms will be saved 
	self.rootfile = ROOT.TFile("datafiles/histos.root", "RECREATE")	
<<<<<<< HEAD
	Analyzer.define_Histograms()
=======

	# Define the histograms for all muons
	self.h_pt=ROOT.TH1F( 'h_pt', 'Muons Transverse Momentun', 50, -2, 200 )
        self.h_px=ROOT.TH1F( 'h_px', 'Muons x- Momentun', 50, -300, 300 )
        self.h_py=ROOT.TH1F( 'h_py', 'Muons y- Momentun', 50, -300, 300 )
        self.h_pz=ROOT.TH1F( 'h_pz', 'Muons z- Momentun', 50, -300, 300 )
        self.h_eta=ROOT.TH1F( 'h_eta', 'Angle Transvese', 50, -8 , 8 )
        self.h_energy=ROOT.TH1F('h_energy','Muons Energy', 50, -300,300)
        self.h_distance=ROOT.TH1F('h_distance','Distance from Primary vertex Z ', 50, -300,300)
        self.h_charge=ROOT.TH1F('h_charge','Muons Charge', 50,-2,2)
        self.h_normChi2=ROOT.TH1F('h_normChi2', 'Muons Chi2', 50, -200,200)
        self.h_numberOfValidHits=ROOT.TH1F('h_numberOfValidHits', 'Number of Valid Hits', 50, 0,200)
        self.h_dB=ROOT.TH1F('h_dB','Impact Parameter',50,-1,200)
        #self.h_edB=ROOT.TH1F('h_edB','Impact Parameter Error',50,-1,200) >> Pintar como barras de error en el histograma?
        self.h_isolation_sumPt=ROOT.TH1F('h_isolation_sumPt','IsolationX',50, -300,300)
        self.h_isolation_emEt=ROOT.TH1F('h_isolation_emEt','IsolationX',50, -300,300)
        self.h_isolation_hadEt=ROOT.TH1F('h_isolation_hadEt','IsolationX',50, -300,300)
        self.h_efficiency=ROOT.TH1F('h_efficiency','efficiency',10,0,11)
        self.h_mass=ROOT.TH1F('h_mass', 'Inv_mass',500, 0,200)
>>>>>>> bf61997f2457635c63eb63e3051585cbac561fc4


    def process(self, event):
	'''Executed on every event'''
<<<<<<< HEAD
	

=======
>>>>>>> bf61997f2457635c63eb63e3051585cbac561fc4


    def endJob(self):

	print "*** writing file",self.rootfilename

        self.rootfilename.Write();
<<<<<<< HEAD
=======

>>>>>>> bf61997f2457635c63eb63e3051585cbac561fc4
        self.rootfile.Close();

        print "*** done"

