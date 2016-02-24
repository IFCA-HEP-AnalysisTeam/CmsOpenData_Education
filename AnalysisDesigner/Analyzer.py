import os
import logging
import ROOT

class Analyzer(object):
    """Base Analyzer class. 

    The custom analyzers should inherit from this class
    """
    def __init__(self):
        """Create an analyzer.
        Parameters (also stored as attributes for later use):
        cfg_ana: configuration parameters for this analyzer (e.g. a pt cut)
        cfg_comp: configuration parameters for the data or MC component (e.g. DYJets)
        looperName: name of the Looper which runs this analyzer.
        Attributes:
        dirName : analyzer directory, where you can write anything you want
        """
	#self.file = ROOT.gROOT.GetListOfFiles().FindObject("mytree.root")
        #if not self.file or not file.IsOpen():
        #    self.file = ROOT.TFile("datafiles/mytree.root", "read")
        #self.tree = self.file.Get("muons")

	#  Define and init the variables for each branch as ROOT vectors
	self.Muon_pt = ROOT.std.vector('float')()
        self.Muon_px= ROOT.std.vector('float')()
        self.Muon_py= ROOT.std.vector('float')()
        self.Muon_pz= ROOT.std.vector('float')()
        self.Muon_eta = ROOT.std.vector('float')()
        self.Muon_energy = ROOT.std.vector('float')()
        self.Muon_distance = ROOT.std.vector('float')()
        self.Muon_dB = ROOT.std.vector('float')()
        self.Muon_edB = ROOT.std.vector('float')()
        self.Muon_isolation_sumPt = ROOT.std.vector('float')()
        self.Muon_isolation_emEt = ROOT.std.vector('float')()
        self.Muon_isolation_hadEt = ROOT.std.vector('float')()
        self.Muon_isGlobalMuon = ROOT.std.vector('int')()
        self.Muon_isTrackerMuon = ROOT.std.vector('int')()
        self.Muon_numberOfValidHits = ROOT.std.vector('int')()
        self.Muon_normChi2 = ROOT.std.vector('float')()
        self.Muon_charge = ROOT.std.vector('int')()
	# Create a directory for this Analyzer
        #self.dirName = '/'.join( [type(self).__name__] )
        #os.mkdir( self.dirName )


        # this is the main logger corresponding to the looper.
        # each analyzer could also declare its own logger
        # self.mainLogger = logging.getLogger( looperName )
        # print self.mainLogger.handlers
        #self.beginLoopCalled = False

    def beginJob(self, name):
	'''Executed before the first object comes in'''

        print '*** Begin job'
	self.DefineHistograms()
	self.rootfile= ROOT.TFile("datafiles/"+name, "RECREATE") 

    def process(self, tree,event):
	'''Executed on every event'''
	pass

    def endJob(self):

	print "*** writing file", self.rootfile
        self.WriteHistograms()
	self.rootfile.Close()
	print "*** done"


    ### DEFINE AND FILL HISTOGRAMS ### 

    def DefineHistograms(self):
	'''Function that define the histograms for all and selected analyzers'''
	# Define and init the histograms for each branch as a TH1F object from ROOT

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
	self.h_mass=ROOT.TH1F('h_mass', 'MassInv', 50, -300, 300)


    def FillHistograms(self, particle):
	'''Function that fill the histograms for each variable and particle in the event'''
	self.h_pt.Fill(self.Muon_pt[particle])
        self.h_px.Fill(self.Muon_px[particle])
        self.h_py.Fill(self.Muon_py[particle])
        self.h_pz.Fill(self.Muon_pz[particle])
        self.h_eta.Fill(self.Muon_eta[particle])
        self.h_energy.Fill(self.Muon_energy[particle])
        self.h_distance.Fill(self.Muon_distance[particle])
        self.h_charge.Fill(self.Muon_charge[particle])
        self.h_normChi2.Fill(self.Muon_normChi2[particle])
        self.h_numberOfValidHits.Fill(self.Muon_numberOfValidHits[particle])
       	self.h_dB.Fill(self.Muon_dB[particle])
        self.h_isolation_sumPt.Fill(self.Muon_isolation_sumPt[particle])
       	self.h_isolation_emEt.Fill(self.Muon_isolation_emEt[particle])
        self.h_isolation_hadEt.Fill(self.Muon_isolation_hadEt[particle])

    def WriteHistograms(self):
        '''Function to write Histograms: Neither mass nor efficiency
	Add here the histograms to print'''
	self.h_pt.Write()
        self.h_px.Write()
        self.h_py.Write()
        self.h_pz.Write()
        self.h_eta.Write()
        self.h_energy.Write()
        self.h_distance.Write()
        self.h_charge.Write()
        self.h_normChi2.Write()
        self.h_numberOfValidHits.Write()
        self.h_dB.Write()
        self.h_isolation_sumPt.Write()
        self.h_isolation_emEt.Write()
        self.h_isolation_hadEt.Write()
	self.h_mass.Write()
