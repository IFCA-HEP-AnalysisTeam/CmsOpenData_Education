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

        self.file = ROOT.gROOT.GetListOfFiles().FindObject("mytree.root")
        if not self.file or not self.file.IsOpen():
            self.file = ROOT.TFile("datafiles/mytree.root", "read")
        self.tree = self.file.Get("muons")
        
        # Get the number of entries(events) of the TTree (file.root)
        self.numEntries=self.tree.GetEntries()
        self.Setup(self.tree)

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

    def process(self, event):
        '''Executed on every event'''
        pass


    def endJob(self):
        ''' 
        Executed after the analysis to write the histograms in the root file
        '''
        print "*** writing file", self.rootfile
        self.WriteHistograms()
        self.rootfile.Close()
        print "*** done"

    def Setup(self, tree):
        '''
        Setup, init the variables for the particle and set 
        branch addresses
   
        '''
        self.relIso = -999. 
        
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
        self.Muon_isStandAloneMuon = ROOT.std.vector('int')()
        self.Muon_isTrackerMuon = ROOT.std.vector('int')()
        self.Muon_numberOfValidHits = ROOT.std.vector('int')()
        self.Muon_numOfMatches= ROOT.std.vector('int')()
        self.Muon_NValidHitsSATk= ROOT.std.vector('int')()
        self.Muon_normChi2 = ROOT.std.vector('float')()
        self.Muon_charge = ROOT.std.vector('int')()
        
        tree.SetBranchAddress("Muon_pt", self.Muon_pt)
        tree.SetBranchAddress("Muon_px", self.Muon_px)
        tree.SetBranchAddress("Muon_py", self.Muon_py)
        tree.SetBranchAddress("Muon_pz", self.Muon_pz)
        tree.SetBranchAddress("Muon_eta", self.Muon_eta)
        tree.SetBranchAddress("Muon_energy", self.Muon_energy)
        tree.SetBranchAddress("Muon_distance", self.Muon_distance)
        tree.SetBranchAddress("Muon_dB", self.Muon_dB)
        tree.SetBranchAddress("Muon_edB", self.Muon_edB)
        tree.SetBranchAddress("Muon_isolation_sumPt", self.Muon_isolation_sumPt )
        tree.SetBranchAddress("Muon_isolation_emEt", self.Muon_isolation_emEt )
        tree.SetBranchAddress("Muon_isolation_hadEt", self.Muon_isolation_hadEt)
        tree.SetBranchAddress("Muon_isGlobalMuon", self.Muon_isGlobalMuon)
        tree.SetBranchAddress("Muon_isStandAloneMuon", self.Muon_isStandAloneMuon)
        tree.SetBranchAddress("Muon_isTrackerMuon", self.Muon_isTrackerMuon)
        tree.SetBranchAddress("Muon_numberOfValidHits", self.Muon_numberOfValidHits)
        tree.SetBranchAddress("Muon_numOfMatches", self.Muon_numOfMatches) 
        tree.SetBranchAddress("Muon_NValidHitsSATk", self.Muon_NValidHitsSATk)     
        tree.SetBranchAddress("Muon_normChi2", self.Muon_normChi2)
        tree.SetBranchAddress("Muon_charge", self.Muon_charge)
    
        # tree.SetBranchAddress("Muon_numOfMatches", self.Muon_numOfMatches)

   

    ### DEFINE AND FILL HISTOGRAMS ### 

    def DefineHistograms(self):
        '''Function that define the histograms for all and selected analyzers'''
        # Define and init the histograms for each branch as a TH1F object from ROOT

        self.h_MuonType=ROOT.TH1F('h_type', 'Number of Muons', 4, 1, 5)
        self.h_pt=ROOT.TH1F( 'h_pt', 'Muons Transverse Momentun', 50, 0, 200 )
        self.h_px=ROOT.TH1F( 'h_px', 'Muons x- Momentun', 50, -300, 300 )
        self.h_py=ROOT.TH1F( 'h_py', 'Muons y- Momentun', 50, -300, 300 )
        self.h_pz=ROOT.TH1F( 'h_pz', 'Muons z- Momentun', 50, -300, 300 )
        self.h_eta=ROOT.TH1F( 'h_eta', 'Angle Transvese', 50, -5 , 5 )
        self.h_energy=ROOT.TH1F('h_energy','Muons Energy', 50, -300,300)
        self.h_dz=ROOT.TH1F('h_dz','Distance from Primary vertex Z ', 50, -3,3)
        self.h_charge=ROOT.TH1F('h_charge','Muons Charge', 4,-2,2)
        self.h_normChi2=ROOT.TH1F('h_normChi2', 'Muons Chi2/ndof', 50, 0,100)
        self.h_numberOfValidHits=ROOT.TH1F('h_numberOfValidHits', 'Number of Valid Hits', 50, 0,50)
        self.h_numOfMatches=ROOT.TH1F('h_numOfMatches', 'Number of muon chambers matched',10, 0, 10)
        self.h_NValidHitsSATk=ROOT.TH1F('h_NValidHitsSATk', 'Number of hits in the muon chambers', 60, 0, 60)
        self.h_dB=ROOT.TH1F('h_dB','Impact Parameter',50,0,2)
        #self.h_edB=ROOT.TH1F('h_edB','Impact Parameter Error',50,-1,200) >> Pintar como barras de error en el histograma?
        self.h_isolation_sumPt=ROOT.TH1F('h_isolation_sumPt','Tracker Isolation',50, 0,300)
        self.h_isolation_emEt=ROOT.TH1F('h_isolation_emEt','ECAL Isolation',50, 0,300)
        self.h_isolation_hadEt=ROOT.TH1F('h_isolation_hadEt','HCAL Isolation',50, 0,300)
        self.h_isolation=ROOT.TH1F('h_isolation','Relative Isolation',50, 0,300)
        self.h_mass=ROOT.TH1F('h_mass', 'MassInv', 150, 0, 300)
     #   self.h_numOfMatches=ROOT.TH1F('h_numOfMatches', 'Number of matches in the Muon chambers', 8, 0, 8)

        
        
    def FillHistograms(self, particle):
       
        #self.relIso = self.Muon_isolation_hadEt[particle] + self.Muon_isolation_hadEt[particle] + self.Muon_isolation_sumPt[particle]/self.Muon_pt[particle]
        self.h_isolation.Fill((self.Muon_isolation_hadEt[particle] + self.Muon_isolation_hadEt[particle] + self.Muon_isolation_sumPt[particle])/self.Muon_pt[particle])
        '''Function that fill the histograms for each variable and particle in the event'''
        
        if self.Muon_isTrackerMuon[particle] == 1:
            self.h_MuonType.Fill(1)
            
        if self.Muon_isStandAloneMuon[particle] == 1:
            self.h_MuonType.Fill(2)

        if self.Muon_isGlobalMuon[particle] == 1: 
            self.h_MuonType.Fill(3)
        
        if self.Muon_isGlobalMuon[particle] == 1 and self.Muon_isTrackerMuon[particle] == 1: 
            self.h_MuonType.Fill(4)
        
        
        self.h_pt.Fill(self.Muon_pt[particle])
        self.h_px.Fill(self.Muon_px[particle])
        self.h_py.Fill(self.Muon_py[particle])
        self.h_pz.Fill(self.Muon_pz[particle])
        self.h_eta.Fill(self.Muon_eta[particle])
        self.h_energy.Fill(self.Muon_energy[particle])
        self.h_dz.Fill(self.Muon_distance[particle])
        self.h_charge.Fill(self.Muon_charge[particle])
        self.h_normChi2.Fill(self.Muon_normChi2[particle])
        self.h_numberOfValidHits.Fill(self.Muon_numberOfValidHits[particle])
        self.h_numOfMatches.Fill(self.Muon_numOfMatches[particle])
       	self.h_dB.Fill(self.Muon_dB[particle])
        self.h_isolation_sumPt.Fill(self.Muon_isolation_sumPt[particle])
       	self.h_isolation_emEt.Fill(self.Muon_isolation_emEt[particle])
        self.h_isolation_hadEt.Fill(self.Muon_isolation_hadEt[particle])
        self.h_NValidHitsSATk.Fill(self.Muon_NValidHitsSATk[particle])

                                   
    def WriteHistograms(self):
        '''Function to write Histograms: Neither mass nor efficiency
        Add here the histograms to print'''
        self.h_MuonType.Write()
        self.h_pt.Write()
        self.h_px.Write()
        self.h_py.Write()
        self.h_pz.Write()
        self.h_eta.Write()
        self.h_energy.Write()
        self.h_dz.Write()
        self.h_charge.Write()
        self.h_normChi2.Write()
        self.h_numberOfValidHits.Write()
        self.h_numOfMatches.Write()
        self.h_NValidHitsSATk.Write()
        self.h_dB.Write()
        self.h_isolation_sumPt.Write()
        self.h_isolation_emEt.Write()
        self.h_isolation_hadEt.Write()
        self.h_isolation.Write()
        #self_h_numOfMatches.Write()
        self.h_mass.Write()
