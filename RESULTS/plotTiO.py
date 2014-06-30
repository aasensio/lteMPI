import numpy as np
import matplotlib.pyplot as pl
import subprocess
import pdb
import struct

def readSpec(f):
	f = open(f)
	res = f.read()
	
	n = struct.unpack('i',res[0:4])
	
	freq = []
	stokes = []
	
	left = 4
	
	for i in range(n[0]):
		
		right = left + 4
		
		n = struct.unpack('i',res[left:right])
		
		left = right
		right = left + 8*n[0]
		t1 = np.asarray(struct.unpack('d'*n[0],res[left:right]))
		freq.append(t1)
		
		
		left = right
		right = left + 4*8*n[0]
		t2 = np.asarray(struct.unpack('d'*4*n[0],res[left:right])).reshape((n[0],4))
		stokes.append(t2)
		
		left = right
		
	freq = np.concatenate(freq)
	stokes = np.concatenate(stokes)
	return freq, stokes
	
files = ['hsra11.mod.atmos','emaltby11.mod.atmos','mmaltby11.mod.atmos','penumjti11.mod.atmos','cool11.mod.atmos']

fig, ax = pl.subplots(nrows=4,ncols=5, figsize=(12,12))

loop = 0
for f in files:
	freq, stokes = readSpec(f+'.spec')
	
	for i in range(4):
		ax[i,loop].plot(freq, stokes[:,i],'b')
		
	freq, stokes = readSpec(f+'.tio.spec')
	
	for i in range(4):
		ax[i,loop].plot(freq, stokes[:,i],'r')
		
	pdb.set_trace()