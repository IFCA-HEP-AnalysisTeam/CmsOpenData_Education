import os
import logging

class Analyzer(object):
    """Base Analyzer class. 

    The custom analyzers should inherit from this class
    """
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        """Create an analyzer.
        Parameters (also stored as attributes for later use):
        cfg_ana: configuration parameters for this analyzer (e.g. a pt cut)
        cfg_comp: configuration parameters for the data or MC component (e.g. DYJets)
        looperName: name of the Looper which runs this analyzer.
        Attributes:
        dirName : analyzer directory, where you can write anything you want
        """
	self.file = ROOT.gROOT.GetListOfFiles().FindObject("mytree.root")
        if not self.file or not file.IsOpen():
            self.file = ROOT.TFile("datafiles/mytree.root", "read")
        self.tree = self.file.Get("muons")

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
       	self.dirName = self.looperName
        self.dirName = '/'.join( [self.name] )
        os.mkdir( self.dirName )


        # this is the main logger corresponding to the looper.
        # each analyzer could also declare its own logger
        # self.mainLogger = logging.getLogger( looperName )
        # print self.mainLogger.handlers
        #self.beginLoopCalled = False

    def beginJob(self, parameters=None):
	'''Executed before the first object comes in'''

        print '*** Begin job'
	#self.mainLogger.info( 'beginJob ')
	# Create a file, in the custom Analyzers, where the histograms will be saved 
	self.rootfile = ROOT.TFile("datafiles/histos.root", "RECREATE")	


    def process(self, event):
	'''Executed on every event'''


    def endJob(self):

	print "*** writing file",self.rootfilename

        self.rootfilename.Write();

        self.rootfile.Close();

        print "*** done"

