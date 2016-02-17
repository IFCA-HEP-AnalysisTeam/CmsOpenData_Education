import os
import logging

from CmsOpenData.AnalysisDesigner.Analyzer import Analyzer

class AnalyzerSel(Analyzer):
    """Selection Analyzer class. 

    The custom analyzers should inherit from this class
    """
    def beginJob(self, parameters=None):
	'''Executed before the first object comes in'''

        print '*** Begin job'
	#self.mainLogger.info( 'beginJob ')
	# Create a file, in the custom Analyzers, where the histograms will be saved 
	self.rootfile = ROOT.TFile("datafiles/goodHistos.root", "RECREATE")	
    def define_Histograms(self):
        Analyzer.define_Histograms()
        #Add the histogram for the efficiency
        self.h_efficiency=ROOT.TH1F('h_efficiency','efficiency',10,0,11)

    def process(self, event):
	'''Executed on every event'''


    def endJob(self):

	print "*** writing file",self.rootfile

        self.rootfile.Write();

        self.rootfile.Close();

        print "*** done"

