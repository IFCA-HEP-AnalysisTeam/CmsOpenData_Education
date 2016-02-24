import os
import logging 
import ROOT
from Analyzer_All import AnalyzerAll 
from Analyzer_Selection import AnalyzerSel

# Get tree from  mytree.root file
file = ROOT.gROOT.GetListOfFiles().FindObject("mytree.root")
if not file or not file.IsOpen():
    file = ROOT.TFile("/home/aidaph/CmsOpenData/Analyzer_Package/datafiles/mytree.root", "read")
else:
    print "The Tree file does not exist in the folder"

tree = file.Get("muons") 
analysis = AnalyzerAll()
tree.SetBranchAddress("Muon_pt", analysis.Muon_pt)
tree.SetBranchAddress("Muon_px", analysis.Muon_px)
tree.SetBranchAddress("Muon_py", analysis.Muon_py)
tree.SetBranchAddress("Muon_pz", analysis.Muon_pz)
tree.SetBranchAddress("Muon_eta", analysis.Muon_eta)
tree.SetBranchAddress("Muon_energy", analysis.Muon_energy)
tree.SetBranchAddress("Muon_distance", analysis.Muon_distance)
tree.SetBranchAddress("Muon_dB", analysis.Muon_dB)
tree.SetBranchAddress("Muon_edB", analysis.Muon_edB)
tree.SetBranchAddress("Muon_isolation_sumPt",analysis.Muon_isolation_sumPt )
tree.SetBranchAddress("Muon_isolation_emEt", analysis.Muon_isolation_emEt )
tree.SetBranchAddress("Muon_isolation_hadEt", analysis.Muon_isolation_hadEt)
tree.SetBranchAddress("Muon_isGlobalMuon", analysis.Muon_isGlobalMuon)
tree.SetBranchAddress("Muon_isTrackerMuon", analysis.Muon_isTrackerMuon)
tree.SetBranchAddress("Muon_numberOfValidHits", analysis.Muon_numberOfValidHits)
tree.SetBranchAddress("Muon_normChi2", analysis.Muon_normChi2)
tree.SetBranchAddress("Muon_charge", analysis.Muon_charge)

#Loop over events
#--------------------------------------------------------------------
# Get the number of entries(events) of the TTree (file.root)
numEntries= tree.GetEntries()

analysis.beginJob("histos.root")
print "Start the Analysis"
# For each event or entry,the following loop populates the tree branches, creates every muon and add it to all_muons list
for event in range(0, numEntries):
	analysis.process(tree, event)
analysis.endJob()
