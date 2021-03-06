from __future__ import print_function
import numpy as np
from scipy.special import erfinv

scorner = -1			#Moves the unit square
sside = 2				#Scales the unit square
	
def uniform(pt):
	return 1

def gauss(pt):
	exponent = 0

	for i in range(len(pt)):
		exponent += pt[i]**2

	return np.exp(-10*exponent)

def sinusoid(pt):
	exponent = 0
	sin_part = 0.05

	for i in range(len(pt)):
		exponent += pt[i]**2
		sin_part *= np.sin(np.pi * pt[i])**2

	return (np.exp(-20*exponent) + sin_part)/2

def inverse_transform(pts):
        pts = (pts - scorner)/sside

        pts = np.transpose(pts)
        npts = np.zeros_like(pts)

        for i in range(pts.shape[0]):
                npts[i] = 0.5 + 0.167*np.sqrt(2) * \
                          erfinv(2*pts[i] - 1)

        return np.transpose(npts)*sside + scorner
        
#Generates n sample points in dim dimensions
def srs_pts(n, dim=2, density=uniform):
	gens = np.zeros([n, dim])
	
	for i in range(n):
		while True:
			y = np.random.rand(dim) * sside + scorner
			test = np.random.rand()
			if density(y) >= test:
				gens[i] = y
				break			

	return gens

#Generates parallel array of js for MacQueens algorithm
def macqueen_js(n):
	return np.ones(n, dtype=np.int)

#Generates n sample points in dim dimensions
#Samples according to distance from each other generator
#	with alpha as the weight
def kpp_pts(n, density=uniform, dim=2, alpha=2):
	gens = np.zeros([n, dim])

	gens[0] = np.random.rand(dim)	#Generate first point
	
	for i in range(1,len(gens)):		#Loop over each generator
		while True:						#Loop until generator is selected
			test_pt = srs_pts(1, gens.shape[1], density)[0]	#Potential generator
			test_dist = np.random.rand()*np.sqrt(dim)			#Rejection threshhold

			short_dist = np.inf			#Find shortest distance from testpt
			for j in range(0,i):
				d = np.linalg.norm( gens[j] - test_pt )
				if d < short_dist:
					short_dist = d

			if short_dist**2 <  test_dist:
				gens[i] = test_pt
				break

	return gens

def macqueen_step(gens, js, density=uniform, distance_return=False):
	k = len(gens)

	y = srs_pts(1, gens.shape[1], density)[0]

	short_dist = np.inf
	ind = -1

	for i in range(k):
		d = np.linalg.norm(gens[i] - y)
		if d < short_dist :
			ind = i
			short_dist = d

	old_gen = gens[ind] * 1 
	gens[ind] = (js[ind]*gens[ind] + y)/(js[ind] + 1)
	js[ind] = js[ind] + 1

	if distance_return:
		return gens, js, np.linalg.norm(gens[ind] - old_gen)

	return gens, js

def lloyd_step(gens, sample, density=uniform, energy_return=False):
	k = gens.shape[0]

	bins = np.zeros([k,gens.shape[1]])        #stores centroid information
	bin_count = np.zeros(k)

	energy = 0

	for pt in sample:        #loop over sample points...
		short_dist = np.inf
		ind = 0
		for i in range(len(gens)):    #...to find closest generator
			d = np.linalg.norm(gens[i] - pt)
			if d < short_dist:
				short_dist = d
				ind = i
			
		energy += d**2

		bins[ind] += pt
		bin_count[ind] += 1

	for j in range(k):
		if bin_count[j] == 0:
			bins[j] = srs_pts(1, gens.shape[1], density)[0]
			bin_count[j] = 1
		gens[j] = bins[j] / bin_count[j]

	if energy_return:
		return gens, energy

	return gens
			
def calc_energy(gens, n, density=uniform):
	energy = 0
	sample = srs_pts(n, 2, density)
	for pt in sample:        #loop over sample points...
		short_dist = np.inf
		ind = 0
		for i in range(len(gens)):    #...to find closest generator
			d = np.linalg.norm(gens[i] - pt)
			if d < short_dist:
				short_dist = d
				ind = i

		energy += d**2 		#add distance^2 to energy
	return energy

def halton_pts(n, dims=2):
        pts = np.zeros([dims, n])
        
        for dim in range(dims):
                pts[dim] = halton_sequence(primes(dim), n)

        return np.transpose(pts)*sside + scorner

def hammersley_pts(n, dims=2):
        pts = np.zeros([dims, n])

        pts[0] = np.linspace(0, 1, num=(n+1))[:-1]

        for dim in range(dims)[1:]:
                pts[dim] = halton_sequence(primes(dim), n)

        return np.transpose(pts)*sside + scorner
        
def halton_sequence(b, n):
        seq = np.zeros(n)
        for i in range(n+1)[1:]:
                j = i - 1
                f = 1.0
	        r = 0.0
	        while i > 0:
		        f = f/b
		        r = r + f * (i % b)
		        i = np.floor(i / b)
                seq[j] = r        
        return seq

        
def latin_pts(n, dim=2):
	pts = np.zeros([dim,n])	
	inds = np.arange(n)
	dims = np.arange(dim)	

        for j in dims:
                Upts = np.random.rand(n)
                Pj = np.random.permutation(n)
                pts[j] = ( Pj + 1 - 0.5 ) / n
                
        return np.transpose(pts)*sside + scorner

def latin_shift(pts):
        pts = (pts - scorner)/sside
        n, d = pts.shape	
	inds = np.arange(n)
	dims = np.arange(d)	
        
        for j in dims:
                pts = pts[pts[:,j].argsort()]
                Upts = np.random.rand(n)
                pts = np.transpose(pts)
                pts[j] = (inds  + 1 - Upts) / n
                pts = np.transpose(pts)

        return pts*sside + scorner

def cvt_pts(n, dim=2):
        pts = srs_pts(n, dim)
        js = macqueen_js(n)
        
        for i in range(100000):
                pts, js = macqueen_step(pts, js)

        return pts

def cvt_lhs_pts(n, dim=2):
        pts = latin_pts(n, dim)
        js = macqueen_js(n)

        for i in range(100000):
                pts, js = macqueen_step(pts, js)
                if (i+1) % 10000 == 0:
                        pts = latin_shift(pts)

        return latin_shift(pts)

#returns the ith prime, starting at 2 = i_0
def primes(i):
        prime_list = [ 2,  3,  5,  7,  11, 13,\
                       17, 19, 23, 29, 31, 37,\
                       41, 43, 47, 53, 61, 67,\
                       71, 73, 79, 83, 89, 97 ]
        return prime_list[i]
