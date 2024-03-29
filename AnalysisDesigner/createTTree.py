# Name: TTreeCreatorMyStruct.py
#
# CMS Open Data
#
# Description: 
#
# Returns: 

import ROOT as ROOT
from DataFormats.FWLite import Events, Handle

class createTTree(object):

        def __init__(self, data_files):

                # To manage Pattuple information in Python (????)
                self.muonHandle = Handle('std::vector<pat::Muon>')
                self.vertexHandle = Handle('std::vector<reco::Vertex>')	
                #self.electronHandle = Handle('std::vector<pat::Electron>')
  
                # Open data files and get the events  
                self.events = Events(data_files)
  
                # Create a .root file using "RECREATE" option of TFile Class where the tree will be save.
                self.f = ROOT.TFile("datafiles/mytree.root","RECREATE")
                self.tree=ROOT.TTree("muons","muons tree")

                # Declare the name of your tree variables
                self.Muon_pt = ROOT.std.vector('float')()
                self.Muon_eta = ROOT.std.vector('float')()
                self.Muon_px = ROOT.std.vector('float')()
                self.Muon_py = ROOT.std.vector('float')()
                self.Muon_pz = ROOT.std.vector('float')()
                self.Muon_energy = ROOT.std.vector('float')()
                self.Muon_isGlobalMuon = ROOT.std.vector('int')() 
                self.Muon_isTrackerMuon = ROOT.std.vector('int')()
                self.Muon_isStandAloneMuon = ROOT.std.vector('int')()
                self.Muon_dB = ROOT.std.vector('float')()
                self.Muon_edB = ROOT.std.vector('float')()
                self.Muon_isolation_sumPt = ROOT.std.vector('float')()
                self.Muon_isolation_emEt = ROOT.std.vector('float')()
                self.Muon_isolation_hadEt = ROOT.std.vector('float')()
                self.Muon_numberOfValidHits = ROOT.std.vector('int')()
                self.Muon_normChi2 = ROOT.std.vector('float')()
                self.Muon_charge = ROOT.std.vector('int')()
                # distance in z axis between Primary vertex Z coordenate and muon's z vertex coordenate
                self.Muon_distance = ROOT.std.vector('float')()

                self.Vertex_Z = 0.	

                # Vectors for new branches

                self.Muon_isStandAloneMuon = ROOT.std.vector('int')()
                self.Muon_numOfMatches = ROOT.std.vector('int')() 
                #self.Muon_deltaPt = ROOT.std.vector('float')()
                self.Muon_NValidHitsSATK = ROOT.std.vector('int')()
                #self.Muon_NValidHitsInTk = ROOT.std.vector('int')()
                #self.Muon_NValidPixelHitsnTk = ROOT.std.vector('int')()

        def getMuons(self, event):
                """
                event: one element of self.events
                returns: the muons from each event in Pattuple file
                """

                event.getByLabel('patMuons', self.muonHandle)
                muons = self.muonHandle.product()
                return muons

        def getVertex(self, event):
                """
                event: one element of self.events               
                returns: the primary vertex of the event
                """

                event.getByLabel('offlinePrimaryVertices', self.vertexHandle)
                vertex = self.vertexHandle.product()[0] #it only takes the first element which corresponds to the primary vertex
                return vertex



        def process(self, maxEv = -1):
                """
                Create the tree branches and associated them to the particles variables created in the init function. 
                Process the events and fill the tree 
                maxEv: maximum number of processed events
                      maxEv=-1 runs over all the events
                
                """

                # Create the tree branches and associate them to the particle variables
 
                self.tree.Branch("Muon_pt", self.Muon_pt)
                self.tree.Branch("Muon_eta", self.Muon_eta)
                self.tree.Branch("Muon_px", self.Muon_px)
                self.tree.Branch("Muon_py", self.Muon_py)
                self.tree.Branch("Muon_pz", self.Muon_pz)
                self.tree.Branch("Muon_energy", self.Muon_energy)
                self.tree.Branch("Muon_isGlobalMuon", self.Muon_isGlobalMuon)
                self.tree.Branch("Muon_isTrackerMuon", self.Muon_isTrackerMuon)
                self.tree.Branch("Muon_isStandAloneMuon", self.Muon_isStandAloneMuon)	
                self.tree.Branch("Muon_dB", self.Muon_dB)
                self.tree.Branch("Muon_edB", self.Muon_edB)
                self.tree.Branch("Muon_isolation_sumPt", self.Muon_isolation_sumPt)
                self.tree.Branch("Muon_isolation_emEt", self.Muon_isolation_emEt)
                self.tree.Branch("Muon_isolation_hadEt", self.Muon_isolation_hadEt)
                self.tree.Branch("Muon_numberOfValidHits", self.Muon_numberOfValidHits)
                self.tree.Branch("Muon_normChi2", self.Muon_normChi2)
                self.tree.Branch("Muon_charge", self.Muon_charge)
                self.tree.Branch("Muon_distance",self.Muon_distance)

                self.tree.Branch("Muon_numOfMatches", self.Muon_numOfMatches)
                #self.tree.Branch("Muon_deltaPt", self.Muon_delaPt)
                self.tree.Branch("Muon_NValidHitsSATk", self.Muon_NValidHitsSATK)
                #self.tree.Branch("Muon_NValidHitsInTk", self.Muon_NValidHitsInTk)
                #self.tree.Branch("Muon_NValidPixelHitsnTk", self.Muon_NValidPixelHitsnTk)

                # Loop the events and populate the variables
                for N, event in enumerate(self.events):

                        if maxEv >= 0 and (N + 1) >= maxEv:
                            break

                        # Do this for each event:
                        muons = self.getMuons(event)
                        vertex = self.getVertex(event)
                        self.Vertex_Z = vertex.z()

                        #Do this for each particle in the event
                        for i, muon in enumerate(muons): 

                                self.Muon_pt.push_back(muon.pt())
                                self.Muon_eta.push_back(muon.eta())
                                self.Muon_px.push_back(muon.px())
                                self.Muon_py.push_back(muon.py())
                                self.Muon_pz.push_back(muon.pz())
                                self.Muon_energy.push_back(muon.energy())
                                self.Muon_isGlobalMuon.push_back(muon.isGlobalMuon())
                                self.Muon_isTrackerMuon.push_back(muon.isTrackerMuon())
                                self.Muon_isStandAloneMuon.push_back(muon.isStandAloneMuon())
                                self.Muon_dB.push_back(muon.dB(muon.PV3D))
                                self.Muon_edB.push_back(muon.edB(muon.PV3D))
                                self.Muon_isolation_sumPt.push_back(muon.isolationR03().sumPt)
                                self.Muon_isolation_emEt.push_back(muon.isolationR03().emEt)
                                self.Muon_isolation_hadEt.push_back(muon.isolationR03().hadEt)
                                self.Muon_charge.push_back(muon.charge())
                                
                                # DISTANCE
                                self.Muon_distance.push_back(abs(muon.vertex().z()-self.Vertex_Z))		
                               
                                self.Muon_numOfMatches.push_back(muon.numberOfMatches())
                
                
                                if not muon.globalTrack().isNull():

                                        self.Muon_numberOfValidHits.push_back(muon.numberOfValidHits())
                                        self.Muon_normChi2.push_back(muon.normChi2())

                                        # Next lines does not work -> The function numberOfValidTrackerHits does not exist for this DATA
                                        # if not muon.innerTrack().isNull():
                                        #       print muon.innerTrack()	
                                        #       #self.Muon_NValidHitsInTk.push_back(muon.innerTrack().hitPattern())
                                        #       self.Muon_NValidHitsInTk.push_back(muon.innerTrack().hitPattern().numberOfValidTrackerHits())
                                        #       self.Muon_NValidPixelHitsnTk.push_back(muon.innerTrack().hitPattern().numberOfValidPixelHits()) 

                                else:
                                        self.Muon_numberOfValidHits.push_back(-999)
                                        self.Muon_normChi2.push_back(-999)

                                if not muon.standAloneMuon().isNull():
                                        self.Muon_NValidHitsSATK.push_back(muon.standAloneMuon().hitPattern().numberOfValidMuonHits())

                        #Fill the tree
                        self.tree.Fill()

                        #Clear the variables
                        self.Muon_pt.clear()
                        self.Muon_eta.clear()
                        self.Muon_px.clear()
                        self.Muon_py.clear()
                        self.Muon_pz.clear()
                        self.Muon_energy.clear()
                        self.Muon_isStandAloneMuon.clear()
                        self.Muon_isGlobalMuon.clear()
                        self.Muon_isTrackerMuon.clear()
                        self.Muon_dB.clear()
                        self.Muon_edB.clear()
                        self.Muon_isolation_sumPt.clear()
                        self.Muon_isolation_emEt.clear()
                        self.Muon_isolation_hadEt.clear()
                        self.Muon_charge.clear()

                        self.Muon_numOfMatches.clear()

                        self.Muon_numberOfValidHits.clear()
                        self.Muon_normChi2.clear()

                        self.Muon_distance.clear()
                        self.Vertex_Z = 0.

                        self.Muon_NValidHitsSATK.clear()
                        #self.Muon_NValidHitsInTk.clear()
                        #self.Muon_NValidPixelHitsnTk.clear()

                # Write the tree in the .root file and close it
                print "Write"
                self.f.Write()
                self.f.Close()
