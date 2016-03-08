# Import ROOT
import ROOT



#t file that contains the histograms for selected muons: goodHistos.root.
Gfile = ROOT.TFile("datafiles/goodhistos.root", "read")

### Get the root file that contains the histograms for all muons: histos.root.
Hfile = ROOT.TFile("datafiles/histos.root", "read")

### You must create a variable to store the histograms selected.
histo1 = Hfile.Get('h_pt')
histo2 = Gfile.Get('h_pt')

### Then create again a new the canvas where the histograms are going to be drawn
canvas = ROOT.TCanvas("myCanvas","All muons: Pt",800,600)

from ROOT import gStyle
### One more time, draw the histogram
histo1.SetTitle("pt good/all Comparation")

# To not print the top-right box of the first histogram
gStyle.SetOptStat(0)

# Draw the histograms in the same canvas
histo1.Draw()
histo2.Draw("same")

name = "pt"
canvas.SaveAs("../output_histograms/"+ name +".png")

### At last, draw the canvas
canvas.Draw()

### Change the line color 
histo1.SetLineColor(4)
histo2.SetLineColor(6)

### Change the bounds of the histograms for X Axis 
histo1.GetXaxis().SetRangeUser(40, 120);
histo2.GetXaxis().SetRangeUser(0, 200);

### Change the bins for the histograms by diving by a divisor of the initial number of bins. 
## Note: To restore the binning you must to draw the histo again.
histo1.Rebin(2)

### Create the legend. TLegend(x1, y1, x2, y2)
legend =ROOT.TLegend(0.1,0.2,0.30,0.3);
legend.SetHeader("Muon Transverse Momentum");
legend.AddEntry(histo1, "All pt","l");
legend.AddEntry(histo2, "Selected pt","l");

#legend->AddEntry("gr","Graph with error bars","lep");
legend.Draw();

### Twist linear scale for Y axe to the logaritmic one with the function SetLogy.
canvas.SetLogy()

name = "pt"
canvas.SaveAs("../output_histograms/"+ name +".png")

canvas.Draw()

### You must create a variable to store the histograms selected.
histo3=Hfile.Get('h_mass')
histo4=Gfile.Get('h_mass')

### Then create again a new the canvas where the histograms are going to be drawn
canvas = ROOT.TCanvas("myCanvas","All muons: mass",800,600)

from ROOT import gStyle
### One more time, draw the histogram
histo3.SetTitle("Mass good/all Comparation")

# To not print the top-right box of the first histogram
gStyle.SetOptStat(0)
# Draw the histograms in the same canvas
histo3.Draw()
histo4.Draw("same")

### Change the line color 
histo3.SetLineColor(4)
histo4.SetLineColor(6)

### Change the bounds of the histograms for X Axis 
histo3.GetXaxis().SetRangeUser(60, 120);
histo4.GetXaxis().SetRangeUser(60, 120);

### Change the bins for the histograms by diving by a divisor of the initial number of bins. 
## Note: To restore the binning you must to draw the histo again.
#histo1.Rebin(2)

### Create the legend. TLegend(x1, y1, x2, y2)
legend =ROOT.TLegend(0.1,0.2,0.30,0.3);
legend.SetHeader("Muon Invariant Mass");
legend.AddEntry(histo1, "All mass","l");
legend.AddEntry(histo2, "Selected mass","l");

#legend->AddEntry("gr","Graph with error bars","lep");
legend.Draw();

### Twist linear scale for Y axe to the logaritmic one with the function SetLogy.
canvas.SetLogy()


name = "mass"
canvas.SaveAs("../output_histograms/"+ name +".png")

### At last, draw the canvas
canvas.Draw()


### Draw the histogram again and check your changes 
canvas.Draw()
