import os
import logging 
import ROOT
from Analyzer_All import AnalyzerAll 

# Get tree from  mytree.root file
file = ROOT.gROOT.GetListOfFiles().FindObject("mytree.root")
if not file or not file.IsOpen():
    file = ROOT.TFile("/home/aidaph/CmsOpenData/Analyzer_Package/datafiles/mytree.root", "read")
else:
    print "The Tree file does not exist in the folder"

tree = file.Get("muons") 
analysis = AnalyzerAll()
'''tree.SetBranchAddress("Muon_pt", AnalyzerAll.Muon_pt)
tree.SetBranchAddress("Muon_px", AnalyzerAll.Muon_px)
tree.SetBranchAddress("Muon_py", AnalyzerAll.Muon_py)
tree.SetBranchAddress("Muon_pz", AnalyzerAll.Muon_pz)
tree.SetBranchAddress("Muon_eta", AnalyzerAll.Muon_eta)
tree.SetBranchAddress("Muon_energy", AnalyzerAll.Muon_energy)
tree.SetBranchAddress("Muon_distance", AnalyzerAll.Muon_distance)
tree.SetBranchAddress("Muon_dB", AnalyzerAll.Muon_dB)
tree.SetBranchAddress("Muon_edB", AnalyzerAll.Muon_edB)
tree.SetBranchAddress("Muon_isolation_sumPt",AnalyzerAll.Muon_isolation_sumPt )
tree.SetBranchAddress("Muon_isolation_emEt", AnalyzerAll.Muon_isolation_emEt )
tree.SetBranchAddress("Muon_isolation_hadEt", AnalyzerAll.Muon_isolation_hadEt)
tree.SetBranchAddress("Muon_isGlobalMuon", AnalyzerAll.Muon_isGlobalMuon)
tree.SetBranchAddress("Muon_isTrackerMuon", AnalyzerAll.Muon_isTrackerMuon)
tree.SetBranchAddress("Muon_numberOfValidHits", AnalyzerAll.Muon_numberOfValidHits)
tree.SetBranchAddress("Muon_normChi2", AnalyzerAll.Muon_normChi2)
tree.SetBranchAddress("Muon_charge", AnalyzerAll.Muon_charge)
'''
#Loop over events
#--------------------------------------------------------------------
# Get the number of entries(events) of the TTree (file.root)
numEntries= tree.GetEntries()

analysis.beginJob("histos.root")
print "Start the Analysis"
# For each event or entry,the following loop populates the tree branches, creates every muon and add it to all_muons list
for event in range(0, numEntries):
	mass= analysis.h_mass
	print "Proccess every event"
	analysis.process(tree, event)
analysis.endJob()
