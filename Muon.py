import ROOT
import matplotlib
matplotlib.use('QT4agg')
import matplotlib.pylab as P
import array

class Muon(object):

	def __init__(self, event, position, pt, eta, energy, vertex):

		self.event = event
		self.position = position
		self.pt = pt
		self.eta = eta
		self.energy = energy
		self.vertex = vertex


	def setPt(pt):
		self.pt=pt

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

	def getEta(self):
		return self.eta

	def getEnergy(self):
		return self.energy

	def printMuon(self):
		print " Muon del evento: "+ repr(self.getEvent()) + " con posicion: " + repr(self.getPosition()) +  " tiene como variables: \n "+ "pt: "+ repr(self.getPt())+ ", eta: "+ repr(self.getEta())

