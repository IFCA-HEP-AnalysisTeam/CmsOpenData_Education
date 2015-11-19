import ROOT as ROOT
from ROOT import *
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from Muon import Muon
from readTTree import readTTree

import time

class Selection(object):
 
 
	def __init__(self,pt_min,eta_max,distance,dB_max,isolation,mass_min,normChi2_max,numValidHits ):
	#Otros posibles constructores eligiendo el numero de cortes y en cuales variables."Serian Muchos"


		#self.pt_min = pt_min
		#self.eta_max = eta_max
		#self.distance = distance
		#self.dB_max = dB_max
		#self.normChi2_max = normChi2_max
		#self.isolation = isolation
		###dimensionless. (sumPt+emEnergy+hadEnergy)/muon.pt = maxima energia antes de considerarlo como un jet de particulas. 
		#self.mass_min = mass_min
		#self.numValidHits = numValidHits 

		# Good muons, mass, pt list
		self.good_muons = []
		self.mass=[]
		self.pt_1=[]
		self.pt_2=[]	

		#####self read y self muons???????########Tambien puedo llamar a esta clase y su metodo desde el script principal(donde este el main, no???
		#read_time=time.time()
		read=readTTree()
		self.muons=read.process()
		#print("Read time: % seconds" % (time.time() - read_time))
		self.bin=[0.]*10
		self.bin[0]=len(self.muons)

		# Histograms for good muons variables
		self.G_pt = ROOT.TH1F('g_pt', 'Transverse Momentum good Muons', 50, -2, 300)
		self.G_eta=ROOT.TH1F( 'g_eta', 'Angle Transverse good Muons', 50, -50 , 50 )

		
		self.G_mass = ROOT.TH1F('g_mass', 'Muon mass', 50, -2, 300)
		self.g_efficiency = ROOT.TH1F('g_efficiency', 'Efficiency', 10, 0, 10000)

		#selector_time=time.time()
		for iMuon in range(0, len (self.muons)):
			#muons[iMuon].printMuon()

			# The selector function evaluates if the inner muon is GlobalMuon and TrackerMuon returning a boolean type before starting the selection for the different variables cuts. 
        		if self.selector(self.muons[iMuon],self.bin, pt_min, eta_max, distance, dB_max, isolation, normChi2_max, numValidHits):
				#append this muon to the good muons list.
				#muons[iMuon].printMuon()
				self.good_muons.append(self.muons[iMuon])
				self.G_pt.Fill(self.muons[iMuon].getPt())
                                self.G_eta.Fill(self.muons[iMuon].getEta())
		

		######??????????meter los histogramas en el bucle de good muos y comentar.	
		for i in range (0,len(self.good_muons)):
			print "Entra en for i"
			# this for is made to ensure j=i+1 is not out of range
			for j in range (i+1, len(self.good_muons)):
				if not self.good_muons[j].getEvent() == self.good_muons[i].getEvent():
					break
				print "i y j son del mismo evento"
				if (self.good_muons[i].getCharge()*self.good_muons[i+1].getCharge())<0:
					#get its Lorentz vector through a ROOT function 
					print "hola2"
					tlv1=ROOT.TLorentzVector()

					tlv1.SetPxPyPzE(self.good_muons[i].getPx(), self.good_muons[i].getPy(), self.good_muons[i].getPz(), self.good_muons[i].getEnergy())
					tlv2=ROOT.TLorentzVector()
					tlv2.SetPxPyPzE(self.good_muons[i+1].getPx(), self.good_muons[i+1].getPy(), self.good_muons[i+1].getPz(), self.good_muons[i+1].getEnergy())
										
 					self.pt_1.append(self.good_muons[i].getPt())
					self.pt_2.append(self.good_muons[i+1].getPt())
					mass=(tlv1+tlv2).M()
					if self.mass_min<mass<120:
						self.mass.append(mass)
						print mass
						self.G_mass.Fill(mass)

		
		self.Ghistos = ROOT.TFile("histos_good.root", "RECREATE")

		for i in range(0,len(self.bin)):
			a=self.bin[i]
			self.g_efficiency.Fill(a)
			print "bin", i, self.bin[i]
                
		self.g_efficiency.Write()
		self.G_pt.Write()
               	self.G_eta.Write()
                self.G_mass.Write()
		self.Ghistos.Close()
		
		# Print elements of good_muons
		#for jMuon in range (0, len(good_muons)):
		#	good_muons[jMuon].printMuon()
		#print("Selector time: % seconds" % (time.time() - selector_time))
		
	def addBin(self, bin, i):
		bin[i]=bin[i]+1
		return bin[i]
		
	def selector(self,muon,bin, pt_min,eta_max,distance,dB_max,isolation,normChi2_max,numValidHits):	
		i=0
		if not muon.getIsGlobalMuon():
			return False
		i=i+1
		bin[i]=self.addBin(bin,i)

                if muon.getIsTrackerMuon():
			return False
                
		i=i+1
		bin[i]=self.addBin(bin, i)

		
		if muon.getPt()<pt_min:
			return False
		i=i+1
                bin[i]=self.addBin(bin, i)
	
		if muon.getEta() > eta_max:		
			return False
		i=i+1
		bin[i]=self.addBin(bin, i)
 		
 		
		if muon.getdB()> dB_max:
			return False
		
		i=i+1
                bin[i]=self.addBin(bin, i)


		if ((muon.getIsolation_sumPt()+muon.getIsolation_emEt()+muon.getIsolation_hadEt())/muon.getPt())>isolation:
			return False	
		i=i+1
                bin[i]=self.addBin(bin, i)
 
		if abs(muon.getvertex_z()-muon.getVertex_Z())> distance:
			return False

		i=i+1
		bin[i]=self.addBin(bin, i)

		if muon.getNormChi2()>normChi2_max:
			return False

		i=i+1
                bin[i]=self.addBin(bin, i)
		 
		if muon.getNumberOfValidHits()<numValidHits:
			return False

		#Last bin for the efficiency.Just the number of good muons. 
		i=i+1
                bin[i]=self.addBin(bin, i)
	


		#print bin
                return True

