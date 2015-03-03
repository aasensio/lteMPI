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
	
files = ['hsra11.mod.atmos','emaltby11.mod.atmos','mmaltby11.mod.atmos','cool11.mod.atmos']

fig, ax = pl.subplots(nrows=4,ncols=2, figsize=(8,10), sharex=True)

loop = 0
for f in files:
	freq, stokes = readSpec(f+'.spec')
	if (loop == 0):
		cont = stokes[0,0]
	
	for i in range(2):
		ax[loop,i].plot(2.99792458e18/freq-5250.2, stokes[:,3*i] / cont,'b')
		
	freq, stokes = readSpec(f+'.tio.spec')
	
	for i in range(2):
		ax[loop,i].plot(2.99792458e18/freq-5250.2, stokes[:,3*i] / cont,'r')
		
	ax[loop,0].set_title(f)
	
	ax[loop,0].set_ylabel(r'I/I$_{QS}$')
	ax[loop,1].set_ylabel(r'V/I$_{QS}$')
	ax[loop,0].set_xlabel(r'$\lambda-5250.2$ [$\AA$]')
	ax[loop,1].set_xlabel(r'$\lambda-5250.2$ [$\AA$]')
	
	loop += 1
	
		
pl.tight_layout()
pl.savefig('TiO.pdf')