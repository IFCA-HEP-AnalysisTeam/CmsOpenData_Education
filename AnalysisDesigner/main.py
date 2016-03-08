import os
import logging 
import ROOT
from Analyzer_All import AnalyzerAll 
from Analyzer_Selection import AnalyzerSel

#######################################################
###                   Analysis                      ###
#######################################################

analysis = AnalyzerAll()
#--------------------------------------------------------------------
# Get the number of entries(events) of the TTree (file.root)
analysis.beginJob("histos.root")
print "Start the Analysis"
# For each event or entry,the following loop populates the tree branches, creates every muon and add it to all_muons list
for event in range(0, analysis.numEntries):
	analysis.process(event)
analysis.endJob()



#######################################################
###                Analysis SELECTION               ###
#######################################################
analysisSel = AnalyzerSel()

# Loop over events
#--------------------------------------------------------------------
# Get the number of entries(events) of the TTree (file.root) and apply the selection criteria
#numEntries= analysis.tree.GetEntries()
analysisSel.beginJob("goodhistos.root")
print "Start the Analysis"
# For each event or entry,the following loop populates the tree branches, creates every muon and add it to all_muons list
for event in range(0, analysisSel.numEntries):
        analysisSel.process(event)
analysisSel.endJob()
