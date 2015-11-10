import ROOT
import matplotlib
matplotlib.use('QT4agg')
import matplotlib.pylab as P
import array

class Muon(object):

	# Vertex_Z se ha quitado,  numberOfValidHits y normChi2!!!!!!!
	def __init__(self, event, position, pt,px,py,pz, eta, energy,vertex_z, dB,edB,isolation_sumPt,isolation_emEt,isolation_hadEt,isGlobalMuon,isTrackerMuon,numberOfValidHits, normChi2, charge, Vertex_Z):
#	def __init__(self, event, position, pt):
		self.event = event
		self.position = position
		self.pt = pt
		self.px=px
		self.py=py
		self.pz=pz
		self.eta = eta
		self.energy = energy
		self.vertex_z = vertex_z
		self.dB=dB
		self.edB=edB
		self.isolation_sumPt=isolation_sumPt
		self.isolation_emEt=isolation_emEt
		self.isolation_hadEt=isolation_hadEt
		self.isGlobalMuon=isGlobalMuon
		self.isTrackerMuon=isTrackerMuon
		self.numberOfValidHits=numberOfValidHits
		self.normChi2=normChi2
		self.charge=charge
		self.Vertex_Z=Vertex_Z

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

