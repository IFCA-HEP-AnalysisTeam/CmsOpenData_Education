import ROOT
from ROOT import gROOT , TCanvas, TH1F
#import numpy as n
#from scipy.stats import norm
#from scipy import optimize
#import matplotlib.mlab as mlab
#import matplotlib.pylab as P
import array
from Cuts import Cuts

class Analyzer(object):
        """
        Analyzer
        """
	def __init__(self):
		'''
		Analyzer Constructor. Only read the tree from the root file.
		'''
                # Get tree from  mytree.root file
                self.file = ROOT.gROOT.GetListOfFiles().FindObject("mytree.root")
                if not self.file or not file.IsOpen():
                        self.file = ROOT.TFile("datafiles/mytree.root", "read")
		else:
			print "The Tree file does not exist in the folder"                

		self.tree = self.file.Get("muons")

                #Call Init function to initialize the tree and set branches             
                self.init()


        def init(self):
		'''
		Function to declare the variables for each branch and the histograms for all
		and selected muons
		'''
                # Define and init the variables for each branch as ROOT vectors
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

                # Instance of Cuts Class to select the muons  
                self.cuts = Cuts()


                # Define and init the histograms for each branch as a TH1F object from ROOT
                #Mejora en la version 2: crear una lista o diccionario de histogramas y definir dos funciones para declarar los histogramas y rellenarlos. 

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
                self.h_mass=ROOT.TH1F('h_mass', 'Inv_mass',500, 0,200)



	#####################################################################
        ###                        PROCESS                                ###
        #####################################################################

        def process(self):
                '''
                Initialization of the reading process. This function reads the NTuples.root, 
                select the good muons and fill the histograms.
                '''
                #Mejora en la version 2:  funcion para automatizar SetBranchAddress. 

                self.tree.SetBranchAddress("Muon_pt", self.Muon_pt)
                self.tree.SetBranchAddress("Muon_px", self.Muon_px)
                self.tree.SetBranchAddress("Muon_py", self.Muon_py)
                self.tree.SetBranchAddress("Muon_pz", self.Muon_pz)
                self.tree.SetBranchAddress("Muon_eta", self.Muon_eta)
                self.tree.SetBranchAddress("Muon_energy", self.Muon_energy)
                self.tree.SetBranchAddress("Muon_distance", self.Muon_distance)
                self.tree.SetBranchAddress("Muon_dB", self.Muon_dB)
                self.tree.SetBranchAddress("Muon_edB", self.Muon_edB)
                self.tree.SetBranchAddress("Muon_isolation_sumPt",self.Muon_isolation_sumPt )
                self.tree.SetBranchAddress("Muon_isolation_emEt",self.Muon_isolation_emEt )
                self.tree.SetBranchAddress("Muon_isolation_hadEt",self.Muon_isolation_hadEt)
                self.tree.SetBranchAddress("Muon_isGlobalMuon", self.Muon_isGlobalMuon)
                self.tree.SetBranchAddress("Muon_isTrackerMuon", self.Muon_isTrackerMuon)
                self.tree.SetBranchAddress("Muon_numberOfValidHits",self.Muon_numberOfValidHits)
                self.tree.SetBranchAddress("Muon_normChi2",self.Muon_normChi2)
                self.tree.SetBranchAddress("Muon_charge",self.Muon_charge)


                #Loop over events
                #--------------------------------------------------------------------
                # Get the number of entries(events) of the TTree (file.root)
                numEntries= self.tree.GetEntries()

                # For each event or entry,the following loop populates the tree branches, creates every muon and add it to all_muons list
                for event in range(0, numEntries):

                        # Address the data of each physical variable registed in this event or entry number to its branch associated listed above.    
                        self.tree.GetEntry(event)

                # Loop over the muons in this event
                        for muon in range(0,self.Muon_pt.size()):
                        # Fill the histogram for each variable
                        # Mejora version 2
                                self.h_pt.Fill(self.Muon_pt[muon])
                                self.h_px.Fill(self.Muon_px[muon])
                                self.h_py.Fill(self.Muon_py[muon])
                                self.h_pz.Fill(self.Muon_pz[muon])
                                self.h_eta.Fill(self.Muon_eta[muon])
                                self.h_energy.Fill(self.Muon_energy[muon])
                                self.h_distance.Fill(self.Muon_distance[muon])
                                self.h_charge.Fill(self.Muon_charge[muon])
                                self.h_normChi2.Fill(self.Muon_normChi2[muon])
                                self.h_numberOfValidHits.Fill(self.Muon_numberOfValidHits[muon])
                                self.h_dB.Fill(self.Muon_dB[muon])
                                self.h_isolation_sumPt.Fill(self.Muon_isolation_sumPt[muon])
                                self.h_isolation_emEt.Fill(self.Muon_isolation_emEt[muon])    
                                self.h_isolation_hadEt.Fill(self.Muon_isolation_hadEt[muon])
				 
				# Get the mass. ONLY if the events has more than 1 muon
                                if (self.Muon_pt.size()) > 1:
                                    for j in range (muon+1,self.Muon_pt.size()):
                                        if (self.Muon_charge[muon]*self.Muon_charge[j])<0:
                                                        # get the Lorentz vector for the both muons through a ROOT function 
                                                        tlv1=ROOT.TLorentzVector()
                                                        tlv1.SetPxPyPzE(self.Muon_px[muon], self.Muon_py[muon], self.Muon_pz[muon],self.Muon_energy[muon])
                                                        
							tlv2=ROOT.TLorentzVector()
                                                        tlv2.SetPxPyPzE(self.Muon_px[j], self.Muon_py[j], self.Muon_pz[j],self.Muon_energy[j])
                                                        
							# Get the mass = (TLV Muon1 + TLV Muon2).M()
							mass=(tlv1+tlv2).M()
							#print mass
							# Fill the histogram for the mass
							self.h_mass.Fill(mass)
							

		# Save histograms for all muons in histos.root file
		self.fhistos = ROOT.TFile("datafiles/histos.root", "RECREATE")

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
        
		self.fhistos.Close()

		print "The histograms for all muons are saved in datafiles/histos.root"

