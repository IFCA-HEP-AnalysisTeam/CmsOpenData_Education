import ROOT as ROOT
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from Muon import Muon
from readTTree import readTTree


def main ():

		# Max and min variables

		pt_min = 12
		eta_max = 2.4
		distance = 0.2
		dB_max = 0.02 # cm. dB=impact parameter
		#normChi2_max = 10
		isolation = 0.15
		#dimensionless. (sumPt+emEnergy+hadEnergy)/muon.pt = maxima energia antes de considerarlo como un jet de particulas.
		mass_min = 60
		chi2 = 10
		numValidHits = 10

		# Good muons list
		good_muons = []
	
		read=readTTree()
		muons=read.process()

		bin=[]

		# Histograms for good muons variables
		h_pt = ROOT.TH1F('g_pt', 'good_pt', 50, -2, 300)
		for iMuon in range(0, len(muons)):
			#muons[iMuon].printMuon()
			# Good muons list
        		if selector(muons[iMuon], pt_min):
				#muons[iMuon].printMuon()
				good_muons.append(muons[iMuon])			
				h_pt.Fill(muons[iMuon].getPt())
		# Print elements of good_muons
		#for jMuon in range (0, len(good_muons)):
		#	good_muons[jMuon].printMuon()

		fhistosGood= ROOT.TFile("histos_good.root", "RECREATE")

		h_pt.Write()
	
		fhistosGood.Close()
	
def selector(muon,pt_min):
	
		i=0
		# Minimum transverse momentum (pt) and maximum eta angle
		if muon.getPt() > pt_min :
		
			return False

		return True

def addBin(i):
		bin[i]=0
	
	

if __name__ == "__main__":
    main()
