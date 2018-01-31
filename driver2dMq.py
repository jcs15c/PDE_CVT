from __future__ import print_function
import numpy as np
import cvt_processing as cvt
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import time

num_gens = [250]
densities = [cvt.gauss, cvt.sinusoid]
iterations = 1000001
    	
for density in densities:
	for n in num_gens:
		d = "mq" + str(n) + str(density)[10]

		t1 = time.time()

		gens = cvt.gensample(n, density)
		js = cvt.macqueen_js(n)

		tot_dist = 0
		mid_dist = 0
		tots = []
		mids = []

		for i in range(iterations):
			gens, js, dist = cvt.macqueen_step(gens, js, density, True)
			mid_dist += dist
			tot_dist += dist
		
			if i % 10000 == 0:
				tots.append(tot_dist)
				mids.append(mid_dist)
				mid_dist = 0
				
		t2 = time.time()

		np.savetxt(d + "_2d_gens.csv", gens, delimiter=",")
		np.savetxt(d + "_2d_tot_dist.csv", np.asarray(tots), delimiter=",")
		np.savetxt(d + "_2d_distance.csv", np.asarray(mids), delimiter=",")
		
		tot_time = (t2 - t1)/60
		
		vor = Voronoi(gens)
		voronoi_plot_2d(vor)
		plt.savefig(d + "_2d_voronoi.png")
		plt.cla()

		plt.title("Total distance per 10000 iterations")
		plt.xlabel("time in minutes: " + str(tot_time))
		plt.plot(tots)
		plt.savefig(d + "_2d_total_dist.png")
		plt.cla()

		plt.title("Distance per 10000 iterations")
		plt.xlabel("time in minutes: " + str(tot_time))
		plt.plot(mids)
		plt.savefig(d + "_2d_distance.png")
		plt.cla()
