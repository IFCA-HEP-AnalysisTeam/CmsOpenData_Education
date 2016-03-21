_doc_ = " Testing TPROOF analysis in pyroot"

import ROOT
import sys
import os
import time

from ROOT import TPySelector

from Cuts_Config import Cuts
##############################################
###### Selector 
##############################################

class Selec(TPySelector):


	DEBUG = True

	def __init__(self):
		# Instance of Cuts Class to select the muons  
                self.cuts = Cuts()

	def Begin(self):
		''''
		MASTER: Begin
		'''
		print "MASTER: Begin"


	def Init(self, tree):
		'''
                SLAVE: Function to declare and set the variables for each branch
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

		self.Info('Init', '-'*30)
		
		# Set the variables for each branch
		self.fChain.SetBranchAddress("Muon_pt", self.Muon_pt);
                self.fChain.SetBranchAddress("Muon_eta", self.Muon_eta);
                self.fChain.SetBranchAddress("Muon_px", self.Muon_px);
                self.fChain.SetBranchAddress("Muon_py", self.Muon_py);
                self.fChain.SetBranchAddress("Muon_pz", self.Muon_pz);
                self.fChain.SetBranchAddress("Muon_energy", self.Muon_energy);
                self.fChain.SetBranchAddress("Muon_isGlobalMuon", self.Muon_isGlobalMuon);
                self.fChain.SetBranchAddress("Muon_isTrackerMuon", self.Muon_isTrackerMuon);
                self.fChain.SetBranchAddress("Muon_dB", self.Muon_dB);
                self.fChain.SetBranchAddress("Muon_edB", self.Muon_edB);
                self.fChain.SetBranchAddress("Muon_isolation_sumPt", self.Muon_isolation_sumPt);
                self.fChain.SetBranchAddress("Muon_isolation_emEt", self.Muon_isolation_emEt);
                self.fChain.SetBranchAddress("Muon_isolation_hadEt", self.Muon_isolation_hadEt);
                self.fChain.SetBranchAddress("Muon_numberOfValidHits", self.Muon_numberOfValidHits);
                self.fChain.SetBranchAddress("Muon_normChi2", self.Muon_normChi2);
                self.fChain.SetBranchAddress("Muon_charge", self.Muon_charge);
                self.fChain.SetBranchAddress("Muon_distance", self.Muon_distance);


	def SlaveBegin(self, tree):
    		'''
		SLAVE: Init and
		'''
		self.Info('SlaveBegin',self.__class__.__name__ )
		self.eventsProcessed = 0
		#Declare histos for all muons
		self.h_pt=ROOT.TH1F( 'h_pt', 'Muons Transverse Momentun', 50, -2, 200 )
                self.h_px=ROOT.TH1F( 'h_px', 'Muons x- Momentun', 50, -300, 300 )
                self.h_py=ROOT.TH1F( 'h_py', 'Muons y- Momentun', 50, -300, 300 )
                self.h_pz=ROOT.TH1F( 'h_pz', 'Muons z- Momentun', 50, -300, 300 )
                self.h_eta=ROOT.TH1F( 'h_eta', 'Angle Transvese', 50, -8 , 8 )
                self.h_energy=ROOT.TH1F('h_energy','Muons Energy', 50, -300,300)
                self.h_distance=ROOT.TH1F('h_distance','Distance from Primary vertex Z ', 50, -300,300)
                self.h_charge=ROOT.TH1F('h_charge','Muons Charge', 50,-2,2)
                self.h_normChi2=ROOT.TH1F('h_normChi2', 'Muons Chi2', 50, 20,200)
                self.h_numberOfValidHits=ROOT.TH1F('h_numberOfValidHits', 'Number of Valid Hits', 50, 0,200)
                self.h_dB=ROOT.TH1F('h_dB','Impact Parameter',50,-1,200)
                #self.h_edB=ROOT.TH1F('h_edB','Impact Parameter Error',50,-1,200) >> Pintar como barras de error en el histograma?
                self.h_isolation_sumPt=ROOT.TH1F('h_isolation_sumPt','IsolationX',50, -300,300)
                self.h_isolation_emEt=ROOT.TH1F('h_isolation_emEt','IsolationX',50, -300,300)
                self.h_isolation_hadEt=ROOT.TH1F('h_isolation_hadEt','IsolationX',50, -300,300)
                self.h_efficiency=ROOT.TH1F('h_efficiency','efficiency',10,0,11)
                self.h_mass=ROOT.TH1F('h_mass', 'Inv_mass',500, 0,200)

		#Declare Good histos
		self.g_pt=ROOT.TH1F( 'g_pt', 'Muons Transverse Momentun', 50, -2, 200 )
                self.g_px=ROOT.TH1F( 'g_px', 'Muons x- Momentun', 50, -300, 300 )
                self.g_py=ROOT.TH1F( 'g_py', 'Muons y- Momentun', 50, -300, 300 )
                self.g_pz=ROOT.TH1F( 'g_pz', 'Muons z- Momentun', 50, -300, 300 )
                self.g_eta=ROOT.TH1F( 'g_eta', 'Angle Transvese', 50, -50 , 50 )
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
		
		# Add histos to GetOutputList 
                self.GetOutputList().Add(self.h_pt)
                self.GetOutputList().Add(self.h_px)
                self.GetOutputList().Add(self.h_py)
                self.GetOutputList().Add(self.h_pz)
                self.GetOutputList().Add(self.h_eta)
                self.GetOutputList().Add(self.h_energy)
                self.GetOutputList().Add(self.h_distance)
                self.GetOutputList().Add(self.h_dB)
                self.GetOutputList().Add(self.h_isolation_sumPt)
                self.GetOutputList().Add(self.h_isolation_emEt)
                self.GetOutputList().Add(self.h_isolation_hadEt)
                self.GetOutputList().Add(self.h_numberOfValidHits)
                self.GetOutputList().Add(self.h_normChi2)
                self.GetOutputList().Add(self.h_charge)
		self.GetOutputList().Add(self.h_mass)
		self.GetOutputList().Add(self.h_efficiency)


                self.GetOutputList().Add(self.g_pt)
                self.GetOutputList().Add(self.g_px)
                self.GetOutputList().Add(self.g_py)
                self.GetOutputList().Add(self.g_pz)
                self.GetOutputList().Add(self.g_eta)
                self.GetOutputList().Add(self.g_energy)
                self.GetOutputList().Add(self.g_distance)
                self.GetOutputList().Add(self.g_dB)
                self.GetOutputList().Add(self.g_isolation_sumPt)
                self.GetOutputList().Add(self.g_isolation_emEt)
                self.GetOutputList().Add(self.g_isolation_hadEt)
                self.GetOutputList().Add(self.g_numberOfValidHits)
                self.GetOutputList().Add(self.g_normChi2)
                self.GetOutputList().Add(self.g_charge)
                self.GetOutputList().Add(self.g_mass)

	def Notify( self ):
		    self.Info('Notify', 'tree %s, file %s' % (self.fChain.GetName(), self.fChain.GetDirectory().GetName()))

	def Process(self, entry):
		'''
		SLAVE: Main function to read the entry(event), select the muon and fill histograms 
		'''
		# Address the data of each physical variable registed in this event or entry number to its branch associated listed above.  
		self.fChain.GetEntry(entry)
				
		# Selected events in the event
		self.event_selected_muons = []
		
		# print "processing entry: ", entry
		#if ( entry%1000==0):
		#	print ' Processing entry: ', entry

		 # Loop all muons in each event 
		for muon in range(0, self.Muon_pt.size()):
		#	print "position in entry:", entry, " is ", position, " with charge: ", self.Muon_charge[position]
			# Fill the histograms by calling fillHisto function(the variable for filling the histo, Muon_pt, for example; the value of that variable in the position within the event) .
			
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
                        self.h_efficiency.Fill(1)
	
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

                                                        # If the both muons are selected between the cuts fill the histogram 
                                                        if self.selector(muon) and self.selector(j):
                                                                self.g_mass.Fill(mass)

				# Apply the selection over all muons calling the selector function and fill the histograms for each variable
			if self.selector(muon):
                        	self.g_pt.Fill(self.Muon_pt[muon])
                                self.g_px.Fill(self.Muon_px[muon])
                                self.g_py.Fill(self.Muon_py[muon])
                                self.g_pz.Fill(self.Muon_pz[muon])
                                self.g_eta.Fill(self.Muon_eta[muon])
                                self.g_energy.Fill(self.Muon_energy[muon])
                                self.g_distance.Fill(self.Muon_distance[muon])
                                self.g_charge.Fill(self.Muon_charge[muon])
                                self.g_normChi2.Fill(self.Muon_normChi2[muon])
                                self.g_numberOfValidHits.Fill(self.Muon_numberOfValidHits[muon])
                                self.g_dB.Fill(self.Muon_dB[muon])
                                self.g_isolation_sumPt.Fill(self.Muon_isolation_sumPt[muon])
                                self.g_isolation_emEt.Fill(self.Muon_isolation_emEt[muon])
                                self.g_isolation_hadEt.Fill(self.Muon_isolation_hadEt[muon])			
	
		return True	

	def SlaveTerminate(self):
		print "Slave Terminate"

	
	def Terminate(self):
		print " Terminate "	
		self.file = ROOT.TFile("histos.root","RECREATE");
		
#		for var in range(0, len(self.variable)):
		self.GetOutputList().FindObject("h_pt").Write()
		self.GetOutputList().FindObject("h_px").Write()
		self.GetOutputList().FindObject("h_py").Write()
		self.GetOutputList().FindObject("h_pz").Write()
		self.GetOutputList().FindObject("h_eta").Write()
		self.GetOutputList().FindObject("h_energy").Write()
		self.GetOutputList().FindObject("h_distance").Write()
		self.GetOutputList().FindObject("h_dB").Write()
		self.GetOutputList().FindObject("h_isolation_sumPt").Write()
		self.GetOutputList().FindObject("h_isolation_emEt").Write()
		self.GetOutputList().FindObject("h_isolation_hadEt").Write()
		self.GetOutputList().FindObject("h_numberOfValidHits").Write()
		self.GetOutputList().FindObject("h_normChi2").Write()
		self.GetOutputList().FindObject("h_charge").Write()
		self.GetOutputList().FindObject("h_mass").Write()
		self.GetOutputList().FindObject("h_efficiency").Write()
		
		self.file.Close()


		self.fileG = ROOT.TFile("goodHistos.root","RECREATE");

	        #for var in range(0, len(self.variable)):
                self.GetOutputList().FindObject("g_pt").Write()
                self.GetOutputList().FindObject("g_px").Write()
                self.GetOutputList().FindObject("g_py").Write()
                self.GetOutputList().FindObject("g_pz").Write()
                self.GetOutputList().FindObject("g_eta").Write()
                self.GetOutputList().FindObject("g_energy").Write()
                self.GetOutputList().FindObject("g_distance").Write()
                self.GetOutputList().FindObject("g_dB").Write()
                self.GetOutputList().FindObject("g_isolation_sumPt").Write()
                self.GetOutputList().FindObject("g_isolation_emEt").Write()
                self.GetOutputList().FindObject("g_isolation_hadEt").Write()
                self.GetOutputList().FindObject("g_numberOfValidHits").Write()
                self.GetOutputList().FindObject("g_normChi2").Write()
                self.GetOutputList().FindObject("g_charge").Write()
		self.GetOutputList().FindObject("g_mass").Write()

		
                self.fileG.Close()
			

	#####################################################################
        ###                        SELECTION                              ###
        #####################################################################

        def selector(self,muon):
                '''
                Function to select the muons which are between a default cuts
                '''
                if not self.Muon_isGlobalMuon[muon]:
                        return False
                self.h_efficiency.Fill(2)

                if not self.Muon_isTrackerMuon[muon]:
                        return False
                self.h_efficiency.Fill(3)

                if self.Muon_pt [muon] < self.cuts.pt_min:
                        return False
                self.h_efficiency.Fill(4)

                if self.Muon_eta[muon] > self.cuts.eta_max:
                        return False
                self.h_efficiency.Fill(5)

                if self.Muon_dB[muon] > self.cuts.dB_max:
                        return False

                self.h_efficiency.Fill(6)
		if ((self.Muon_isolation_sumPt[muon]+self.Muon_isolation_emEt[muon]+self.Muon_isolation_hadEt[muon])/self.Muon_pt [muon]) > self.cuts.isolation:
                        return False
                self.h_efficiency.Fill(7)

                if self.Muon_distance[muon] > self.cuts.distance:
                        return False

                self.h_efficiency.Fill(8)

                if self.Muon_normChi2[muon] > self.cuts.normChi2:
                        return False

                self.h_efficiency.Fill(9)

                if self.Muon_numberOfValidHits[muon] < self.cuts.numValidHits:
                        return False

                self.h_efficiency.Fill(10)

                return True
