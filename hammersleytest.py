from __future__ import print_function
import cvt_processing as cvt
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d

def plot_voronois(pts1, pts2, iteration):
    vor1 = Voronoi(pts1)
    vor2 = Voronoi(pts2)

    ax1 = plt.subplot(121, aspect='equal', adjustable='box-forced', )
    voronoi_plot_2d(vor1, ax1, show_vertices=False)

    ax2 = plt.subplot(122, aspect='equal', adjustable='box-forced', sharex=ax1, sharey=ax1)
    voronoi_plot_2d(vor2, ax2, show_vertices=False)
    
    plt.savefig("Hammersley_Test/Hammersley_Test_" + iteration + ".png")
    ax1.cla()
    ax2.cla()
    return

n = 100
for i in range(5):
    hpts = cvt.hammersley_pts(n)
    hpts = np.transpose(hpts)
    hjs = cvt.macqueen_js(n)

    pts = cvt.gensample(n, cvt.gauss)
    js = cvt.macqueen_js(n)

    dist1sum = 0
    dist2sum = 0

    dists1 = []
    dists2 = []
    
    for j in range(25000):
        hpts, hjs, dist1 = cvt.macqueen_step(hpts, hjs, cvt.gauss, True)
        pts, js, dist2 = cvt.macqueen_step(pts, js, cvt.gauss, True)

        dist1sum += dist1
        dist2sum += dist2
        
        if ( j % 1000 ) == 0 or j == 25000:
            plot_voronois(hpts, pts, str(i) + '_' + str(j) )

            if j:
                dists1.append(dist1sum)
                dists2.append(dist2sum)
                
                dist1sum = 0
                dist2sum = 0


    plt.clf()
    plt.plot(dists1, 'r')
    plt.plot(dists2, 'b')
    plt.title('Red: Hammersley ; Blue: Monte Carlo')
    plt.savefig('Hammersley_Test/Hammersley_Test_Distance_' + str(i) + '.png')
    
