import ROOT as ROOT
import sys
import getopt
import numpy
from Histos import Histos
import time

from ROOT import *
from ROOT import TProof, TFileCollection, TChain


def main ():

	start_time = time.time()
	
	chain = TChain("muons")
	#chain = TDSet("TTree", "muons")
	chain.Add("../mytree.root")
#	print chain.GetEntries()
	
	##############  INIT PROOF ########################
	proof = TProof.Open("")
	
	# ONLY for make the debugging in the slaves
	pl=TProof.Mgr("").GetSessionLogs()
	pl.Display()

	# SET PROOF 
	chain.SetProof(True)
	
	time.sleep(1)  # needed for GUI to settle

	chain.Process('TPySelector', 'Analyzer_PROOF' )
#	chain.Process("MySelector.C+")	

	# DRAW HISTOS
	# ----------------------------------------------------------------
	histo=Histos()

        # Here you have a dictionary with the main variables used in the analysis
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

        # Exercise 1:
        # Choose which variables you want to draw in a  histogram and pass them as parameters
        histo.drawHisto(variable['eta'], variable['pt'])
		
	# Exercise 2:
        # Now select the good muons. Try to find the right cut to approach the real Z event

        ## Change the default cuts in "Cuts.py" script

        # Check up drawing the new histos. Try to draw the same variable before and after the cut

        #histo.drawSelHisto(variable['eta'], variable['mass'])
        #histo.drawTwoHistos(variable['eta'])

        # Make the fits in the mass histogram
        histo.GaussianFit(variable['mass'])

######################Falta#################################################

# En la funcion/es de pintar, poder establecer los limites xmin, xmax, y el inumero de bines y la escala lineal o logaritmica desde el ejecutable principal.
# Fit Breit Wigner

#############################################################################

	print("---Total time: %s seconds ---" % (time.time() - start_time))

	
if __name__ == "__main__":
    main()
