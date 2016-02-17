import os
import logging

from CmsOpenData.AnalysisDesigner.Analyzer import Analyzer

class AnalyzerAll(Analyzer):
    """Analyzer class for all muons. 

    """
    def beginJob(self, parameters=None):
	'''Executed before the first object comes in'''

        print '*** Begin job'
	#self.mainLogger.info( 'beginJob ')
	# Create a file, in the custom Analyzers, where the histograms will be saved 
	self.rootfile = ROOT.TFile("datafiles/histos.root", "RECREATE")	
	Analyzer.define_Histograms()


    def process(self, event):
	'''Executed on every event'''
	



    def endJob(self):

	print "*** writing file",self.rootfilename

        self.rootfilename.Write();
        self.rootfile.Close();

        print "*** done"

