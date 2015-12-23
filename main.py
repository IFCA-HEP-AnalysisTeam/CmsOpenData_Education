import ROOT as ROOT
import sys
import getopt
from DataFormats.FWLite import Events, Handle
from Histos import Histos
from Analyzer import Analyzer
import time



def main ():

	start_time = time.time()
       
        # To start this exercise you must call different classes which make the analysis

        analysis=Analyzer()
        analysis.process()
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
	histo.drawHisto(variable['eta'])

        # Exercise 2:
	# Now select the good muons. Try to find the right cut to approach the real Z event

        ## Change the default cuts in "Cuts.py" script

        # Check up drawing the new histos. Try to draw the same variable before and after the cut

	#histo.drawSelHisto(variable['mass'])
	#histo.drawTwoHistos(variable['eta'])

        # Make the fits in the mass histogram
	#histo.GaussianFit(variable['mass'])
         
######################Falta#################################################

# En la funcion/es de pintar, poder establecer los limites xmin, xmax, y el inumero de bines y la escala lineal o logaritmica desde el ejecutable principal.
# Fit Breit Wigner

#############################################################################

	print("---Total time: %s seconds ---" % (time.time() - start_time))
        
	
if __name__ == "__main__":
    main()
