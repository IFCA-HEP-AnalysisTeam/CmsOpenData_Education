import os
import logging
import ROOT

from Cuts import Cuts

class Selector(object):
	''' Class that make the selection from a defined Cuts'''
	#def __init__(self):
	#    print '''***Selector created'''
	    

	def selector(self, analysis, particle):
		cuts = Cuts()

		'''Main class for making the selection'''
		if not analysis.Muon_isGlobalMuon[particle] or not analysis.Muon_isTrackerMuon[particle]:
                        return False
                analysis.h_efficiency.Fill(2)
                
                if analysis.Muon_pt [particle] < cuts.pt_min:
                        return False
                analysis.h_efficiency.Fill(3)

                if analysis.Muon_eta[particle] > cuts.eta_max:
                        return False
                analysis.h_efficiency.Fill(4)

                if analysis.Muon_normChi2[particle] > cuts.normChi2:
                        return False
                analysis.h_efficiency.Fill(5)
                
                if analysis.Muon_NValidHitsSATk[particle] < cuts.numValidHitsSTATk:
                        return False
                analysis.h_efficiency.Fill(6)
                
                if analysis.Muon_numberOfValidHits[particle] < cuts.numValidHits:
                        return False
                analysis.h_efficiency.Fill(7)
                                          
                if analysis.Muon_numOfMatches[particle] < cuts.numOfMatches:
                        return False
                analysis.h_efficiency.Fill(8)

                if analysis.Muon_distance[particle] > cuts.dz_max:
                        return False
                analysis.h_efficiency.Fill(9)
                
                if analysis.Muon_dB[particle] > cuts.dB_max:
                        return False
                analysis.h_efficiency.Fill(10)

                if ((analysis.Muon_isolation_sumPt[particle]+analysis.Muon_isolation_emEt[particle]+analysis.Muon_isolation_hadEt[particle])/analysis.Muon_pt[particle]) > cuts.relIsolation:
                        return False
                analysis.h_efficiency.Fill(11)
               
                return True



