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
	

freq, stokes = readSpec('test.spec')
f, ax = pl.subplots()

ind = np.argsort(freq)
freq = freq[ind]
stokes = stokes[ind,:]

ax.plot(2.99792458e18/freq, stokes[:,0],'r')
		
			
pl.tight_layout()