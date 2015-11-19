import ROOT
import matplotlib
matplotlib.use('QT4agg')
import matplotlib.pylab as P
import array

class Muon(object):

	# Vertex_Z se ha quitado,  numberOfValidHits y normChi2!!!!!!!
	def __init__(self, event, position, muon):
#	def __init__(self, event, position, pt):
		self.event = event
		self.position = position
		self.pt = muon [0]
		self.px= muon[1]
		self.py= muon[2]
		self.pz= muon[3]
		self.eta = muon[4]
		self.energy = muon[5]
		self.vertex_z = muon[6]
		self.dB= muon[7]
		self.edB= muon[8]
		self.isolation_sumPt= muon[9]
		self.isolation_emEt= muon[10]
		self.isolation_hadEt= muon[11]
		self.isGlobalMuon=muon[15]
		self.isTrackerMuon=muon[16]
		self.numberOfValidHits=muon[12]
		self.normChi2=muon[13]
		self.charge=muon[14]
		self.Vertex_Z=muon[17]

	def setMuon(pt, eta, energy):
                self.pt=pt
                self.eta=eta
                self.energy=energy

	def getEvent(self):
                return self.event

        def getPosition (self):
                return self.position


	def getPt(self):
                return self.pt
	

	def getPx(self):
		return self.px
	
	def getPy(self):
		return self.py
	
	def getPz(self):
		return self.pz

	def getEta(self):
		return self.eta

	def getEnergy(self):
		return self.energy

	def getvertex_z(self):
		return self.vertex_z

	def getdB(self):
		return self.dB

	def getedB(self):
		return self.edB

	def getIsolation_sumPt(self):
		return self.isolation_sumPt

	def getIsolation_emEt(self):
		return self.isolation_emEt	

	def getIsolation_hadEt(self):
		return self.isolation_hadEt

	def getIsGlobalMuon(self):
		return self.isGlobalMuon

	def getIsTrackerMuon(self):
		return self.isTrackerMuon

	def getNumberOfValidHits(self):
		return self.numberOfValidHits

	def getNormChi2(self):
		return self.normChi2

	def getCharge(self):
		return self.charge

	def getVertex_Z(self):
		return self.Vertex_Z

	def printMuon(self):
		print " Muon del evento: "+ repr(self.getEvent()) + " con posicion: " + repr(self.getPosition()) +  " tiene como variables: \n "+ "pt: "+ repr(self.getPt())+ ", eta: "+ repr(self.getEta())

