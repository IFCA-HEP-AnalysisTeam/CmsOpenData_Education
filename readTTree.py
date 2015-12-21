import ROOT
from ROOT import gROOT , TCanvas, TH1F
import numpy as n
from scipy.stats import norm
#from scipy import optimize
#import matplotlib.mlab as mlab
#import matplotlib.pylab as P
import array

from Muon import Muon
from Cuts_Config import Cuts


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
                self.Muon_distance = ROOT.std.vector('float')()
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

		# Self.vector is a list of all variable vectors set above. It is used in this code for simplify the syntaxis
		self.vector = [self.Muon_pt, self.Muon_px, self.Muon_py, self.Muon_pz, self.Muon_eta, self.Muon_energy, self.Muon_distance, self.dB, self.edB, self.Muon_isolation_sumPt, self.Muon_isolation_emEt, self.Muon_isolation_hadEt, self.Muon_numberOfValidHits, self.Muon_normChi2, self.Muon_charge, self.Muon_isGlobalMuon, self.Muon_isTrackerMuon] 
				
		# List of all muons as a list of Muon object (class Muon)
		self.all_muons = []


		# Define and init the histograms for each branch using TH1F from ROOT
		self.histograms={}
		self.selec_histograms={}

		# Vector for efficiency: Count the amount of muons along the cuts
		self.bin=[0.]*10

		# Dictionary: Set of variables to simplify the code later: SetBranchAddress, declare and fill histos, etc.
		self.variable = {
	                0: "pt",
			1: "px", 
			2: "py",
			3: "pz",
        	        4: "eta",
			5: "energy",
			6: "distance",
                        7: "dB",
			8: "edB",
                	9: "isolation_sumPt",
                	10: "isolation_emEt",
			11:"isolation_hadEt",
			12:"numberOfValidHits",
                	13: "normChi2",
                	14: "charge", 
			15: "isGlobalMuon", 
			16: "isTrackerMuon"
			}
		

                # Initialize the histograms for all and selected muons through the function "self.declareHisto"
		# ** Initialize the histograms for global variables and the mass and efficiency will be initialize later
	
		for i in range(0, len(self.variable)):
			self.declareHisto(i, self.variable[i], "h", 50, -300, 300)
			self.declareHisto(i, self.variable[i], "g", 50, -300, 300)
		self.declareHisto(len(self.variable), "Mass", "g",  50, -300, 300)
		self.declareHisto(len(self.variable)+1, "efficiency", "g",  50, -300, 300)



	#####################################################################
	###                        PROCESS                                ###
	#####################################################################

	def process(self):

		'''
		Initialization of the reading process. This function address the data stored in the tree to the different branches previously defined.
		'''
                
                #Address the data stored in the branches to the variables 
		
		for i in range(0, len(self.vector)): 
			self.tree.SetBranchAddress("Muon_"+self.variable[i], self.vector[i])

		# numEntries: Number of entries(events) of the tree
		numEntries= self.tree.GetEntries()
		# Cuts to select muon: Call to Cuts_Config
		self.cuts= Cuts()

		# Loop over all events 
		# -------------------------------------------------------------------------------
                # For each entry,the following loop populates the vector of variables, creates every muon and add it to all_muons list 
		# event = current entry of the tree
		for event in range(0, numEntries):
		        
                        # Local variable: Init a list of selected muons in this event.  	
			self.event_selected_muons = []
			
			self.tree.GetEntry(event)

			# Loop over the muons in this event 
			# ------------------------------------------------------------------------
			# position = current position in the event
			for position in range(0,self.vector[0].size()):
		     		# List of muon variables to create the Muon Object
				self.variables = []
				
				# Add the value of each variable to variables list
				for var in range(0, len(self.variable)):						
					self.variables.append(self.vector[var][position])
				#print self.vector[0][position]
				# Create the Muon: is identified by the event, a position in the event and the values of its variables
				muon=Muon(event, position, self.variables)

				# Add each muon to all_muon list
				self.all_muons.append(muon)
				
				# Fill all muons histograms
				for var in range(0, len(self.variable)):
                                        self.fillHisto(var, "h", self.vector[var][position])

				# Select the muon
				# -----------------------------------------------------------------
				if self.selector(muon, self.bin, self.cuts):
					# If the muon is between the defined cuts, add it to the selected muon list in the event 
					print "Selected muon belongs to ", event, " event"
					self.event_selected_muons.append(muon)

			# CHECK MASS - Only the events with more than 1 muons selected
			# -----------------------------------------------------------
			if len(self.event_selected_muons) > 1:
				print "evento con mas de 1 muon"
				
				# Loop over the event selected muons
				for i in range (0,len(self.event_selected_muons)):
                        	# this is made to ensure j=i+1 is not out of range 
                        		for j in range (i+1, len(self.event_selected_muons)):
						
                                		if (self.event_selected_muons[i].getCharge()*self.event_selected_muons[j].getCharge())<0:
                                        		#get its Lorentz vector through a ROOT function 
                                        		tlv1=ROOT.TLorentzVector()

                                        		tlv1.SetPxPyPzE(self.event_selected_muons[i].getPx(), self.event_selected_muons[i].getPy(), self.event_selected_muons[i].getPz(), self.event_selected_muons[i].getEnergy())
                                        		tlv2=ROOT.TLorentzVector()
                                        		tlv2.SetPxPyPzE(self.event_selected_muons[j].getPx(), self.event_selected_muons[j].getPy(), self.event_selected_muons[j].getPz(), self.event_selected_muons[j].getEnergy())


                                        		#self.pt_1.append(self.event_selected_muons[i].getPt())
                                        		#self.pt_2.append(self.event_selected_muons[j].getPt())
                                        		mass=(tlv1+tlv2).M()
		#					print "the selected muon mass is: ", mass
                                        		if self.cuts.mass_min<mass:
								print "The mass is between the cuts: ", mass
								# Fill the selected muons
								for var in range(0, len(self.variable)):
									self.fillHisto( var, "g", self.vector[var][position]) 	
								self.fillHisto(len(self.variable), "g", mass)	


		####### Only For Debugging ########
		#for i in range(0,10):
		#	print self.all_muons[i].printMuon()
		
		
		# Create a rootfile for the histogramas
		self.fhistos = ROOT.TFile("histos.root", "RECREATE")
		
		# Write histograms in fhistos file
		for i in range(0, len(self.histograms)):
			self.histograms[i].Write()
	
		#Close file
		self.fhistos.Close()

		# Create a rootfile for the selected histograms
		self.shistos = ROOT.TFile("selec_histos.root", "RECREATE")
		# Write histograms in shistos file
                for i in range(0, len(self.selec_histograms)):
                        self.selec_histograms[i].Write()
		# Write efficiency histogram in selec_histos file
		self.bin[0]= len(self.all_muons)
                for i in range(0,len(self.bin)):
                        a=self.bin[i]
                        self.selec_histograms[len(self.variable)+1].Fill(a)
                        print "bin", i, a

                #Close file
                self.shistos.Close()


	def declareHisto(self, i, name, type, bins, min, max, xlabel='value'):
		'''
		Function to declare de histograms
		
		i = identify the histogram for each variable
		name = variable name
		bins = number of bins in histogram
		min = minimum X value of the histogram
		max = maximum X value of the histogram
		xlabel (optional) = name of X axis
		'''
		if type=="h":
			self.histograms[i]= ROOT.TH1F("h_"+name, name, bins, min, max)
		else: 
			self.selec_histograms[i]= ROOT.TH1F("g_"+name, name, bins, min, max)
		# Does not work
		#self.histograms[i].setXAxisTitle(xlabel+' of '+name)
		#self.histograms[i].SetYaxisTitle('events')
	
	def fillHisto(self, i, type, value, weight=1):
		'''
		Function to fill the histograms
		
		i = identify the histogram for each variable
		value = define the value for filling the histogram 
		'''
		if type=="h":
			self.histograms[i].Fill(value, weight)
		else:
			self.selec_histograms[i].Fill(value, weight)
	
	def addBin(self, bin, i):
                bin[i]=bin[i]+1
                return bin[i]



        def selector(self,muon,bin, cuts):
                i=0
                if not muon.getIsGlobalMuon():
                        return False
                i=i+1
		bin[i]=self.addBin(bin, i)

                if not  muon.getIsTrackerMuon():
                        return False

                i=i+1
		bin[i]=self.addBin(bin, i)

                if muon.getPt()<cuts.pt_min:
                        return False
                i=i+1
		bin[i]=self.addBin(bin, i)

                if muon.getEta() > cuts.eta_max:
                        return False
                i=i+1
		bin[i]=self.addBin(bin, i)

                if muon.getdB()> cuts.dB_max:
                        return False

                i=i+1
		bin[i]=self.addBin(bin, i)

                if ((muon.getIsolation_sumPt()+muon.getIsolation_emEt()+muon.getIsolation_hadEt())/muon.getPt())>cuts.isolation:
                        return False
                i=i+1
		bin[i]=self.addBin(bin, i)

                if muon.getDistance()> cuts.distance:
                        return False

                i=i+1
		bin[i]=self.addBin(bin, i)

                if muon.getNormChi2()>cuts.normChi2:
                        return False

                i=i+1
		bin[i]=self.addBin(bin, i)

                if muon.getNumberOfValidHits()<cuts.numValidHits:
			return False

                #Last bin for the efficiency.Just the number of good muons. 
                i=i+1
		bin[i]=self.addBin(bin, i)

                #print bin
                return True

