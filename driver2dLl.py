from __future__ import print_function
import numpy as np
import cvt_processing as cvt
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import time

num_gens = [250]
densities = [cvt.uniform, cvt.gauss, cvt.sinusoid]
iterations = 100
    	
for density in densities:
	for n in num_gens:
		d = "ll" + str(n) + str(density)[10]

		t1 = time.time()

		gens = cvt.gensample(n, density)
		sample = cvt.gensample(10000, density)

		energies = []

		for i in range(iterations):
			gens, energy = cvt.lloyd_step(gens, sample, density, True)
		
			energies.append(energy)
				
		t2 = time.time()

		np.savetxt(d + "_2d_gens.csv", gens, delimiter=",")
		np.savetxt(d + "_2d_energy.csv", np.asarray(energies), delimiter=",")
		
		tot_time = (t2 - t1)/60
		
		vor = Voronoi(gens)
		voronoi_plot_2d(vor)
		plt.savefig(d + "_2d_voronoi.png")
		plt.cla()

		plt.title("Energy per iteration")
		plt.xlabel("time in minutes: " + str(tot_time))
		plt.plot(energies)
		plt.savefig(d + "_2d_energy.png")
		plt.cla()
