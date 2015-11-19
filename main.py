import ROOT as ROOT
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from Muon import Muon
from readTTree import readTTree
from Selector import Selection
from Histos import Histos
import time



def main ():

	#start_time = time.time()

	pt_min = 5
	eta_max = 2.4
	distance = 0.2
	dB_max = 0.02 # cm. dB=impact parameter
	#normChi2_max = 10
	isolation = 0.15
	#dimensionless. (sumPt+emEnergy+hadEnergy)/muon.pt = maxima energia antes de considerarlo como un jet de particulas.
	mass_min = 20
	normChi2_max = 10
	numValidHits = 10

	# Call class Selector for doing the muon selection
	# The cut config of each variable has been passed as argument.
	selector= Selection(pt_min, eta_max, distance, dB_max, isolation, mass_min, normChi2_max, numValidHits)
	# Call histos class to draw the histogram(s)
	# Pass the variable or variables which we want to draw as parameter 
	histo=Histos()
	# Dictionary with the variables for drawing in histos
	variable = {
		'pt': 'pt',
		'eta': 'eta',
		'distance': 'distance',
		'dB': 'dB',
		'isolation':'isolation',
		'mass':'mass',
		'normChi2': 'normChi2',
		'numValidHits': 'numValidHits',
		'efficiency': 'efficiency'}
	
	# Choose which variables want to draw in histos and pass them as parameters
	#histo.drawHisto(variable['eta'], variable['pt'])
	#histo.drawSelHisto(variable['eta'], variable['mass'])

	histo.GaussianFit(variable['pt'])
	#print("---Total time: %s seconds ---" % (time.time() - start_time))	
	
if __name__ == "__main__":
    main()

