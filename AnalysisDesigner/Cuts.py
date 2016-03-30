class Cuts(object):
        def __init__(self, isGlobal = 1, pt_min = 5, eta_max = 2.4, normChi2 = 10, numValidHitsSTATk = 10, numValidHits = 10, numOfMatches = 1, dz_max = 0.2, dB_max = 0.02, relIsolation = 0.15, mass_min = 0):

                self.isGlobal = isGlobal
                self.pt_min = pt_min
                self.eta_max = eta_max
                self.normChi2 = normChi2
                self.numValidHitsSTATk =  numValidHitsSTATk 
                self.numValidHits = numValidHits
                self.numOfMatches = numOfMatches
                self.dz_max = dz_max
                self.dB_max = dB_max # cm. dB=impact parameter
                self.relIsolation = relIsolation
                #dimensionless. (sumPt+emEnergy+hadEnergy)/muon.pt = maxima energia antes de considerarlo como un jet de particulas.
                self.mass_min = mass_min
