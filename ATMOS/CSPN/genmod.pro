pro genmod
	restore,'T550g420He09Q130b08.xdr'

	openw,2,'cspn.model'
	printf,2,'# Model  cmass   T[K]     ne [cm^-3]    vturb [cm/s]'
	printf,2,"'CMASS'"
	printf,2,"'NONMAGNETIC'"
	printf,2,"'NORMAL'"
	printf,2,n_elements(d.t)

	for i = 0, n_elements(d.t)-1 do begin
		printf,2, d.m[i], d.T[i], d.xne[i], 1.d5, 0.d0
	endfor

	close,2

	stop
end