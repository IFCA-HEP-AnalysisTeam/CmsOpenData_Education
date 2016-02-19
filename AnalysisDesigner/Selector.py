import os
import logging
import ROOT

import Cuts as cuts

class Selector(object):
	''' Class that make the selection from a defined Cuts'''
	def __init__(self):
	    print '''***Selector create'''
	    
	def beginSelector(self):
	    print ('***Start the analysis: Create the histogram for the efficiency')
            self.ghistos = ROOT.TFile("datafiles/goodHistos.root", "write")
            #self.h_efficiency=ROOT.TH1F('h_efficiency','efficiency',10,0,11)


	def selector(self, particle, cuts):
		'''Main class for making the selection'''
		if not self.Muon_isGlobalMuon[particle]:
                        return False
                self.h_efficiency.Fill(2)

                if not self.Muon_isTrackerMuon[particle]:
                        return False
                self.h_efficiency.Fill(3)

                if self.Muon_pt [particle] < cuts.pt_min:
                        return False
                self.h_efficiency.Fill(4)

                if self.Muon_eta[particle] > cuts.eta_max:
                        return False
                self.h_efficiency.Fill(5)

                if self.Muon_dB[particle] > cuts.dB_max:
                        return False

                self.h_efficiency.Fill(6)

                if ((self.Muon_isolation_sumPt[particle]+self.Muon_isolation_emEt[particle]+self.Muon_isolation_hadEt[particle])/self.Muon_pt[particle]) > cuts.isolation:
                        return False
                self.h_efficiency.Fill(7)

                if self.Muon_distance[particle] > cuts.distance:
                        return False

                self.h_efficiency.Fill(8)

                if self.Muon_normChi2[particle] > cuts.normChi2:
                        return False

                self.h_efficiency.Fill(9)

                if self.Muon_numberOfValidHits[particle] < cuts.numValidHits:
                        return False

                self.h_efficiency.Fill(10)

                return True

	def endSelector(self):
		print '*** Selection finished'
		#self.h_efficiency.Write()
                #self.ghistos.Close()
                print "Histogram for the efficiency saved in datafiles/goodHistos.root file"

