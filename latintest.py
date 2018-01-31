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
    
    plt.savefig("Latin_Test/Latin_Test_" + iteration + ".png")
    ax1.cla()
    ax2.cla()
    return

n = 100
for i in range(5):
    pts1 = cvt.gensample(n)
    js1  = cvt.macqueen_js(n)

    pts2 = np.copy(pts1)
    js2  = np.copy(pts2)

    dist1sum = 0
    dist2sum = 0
 
    dists1 = []
    dists2 = []
    
    for j in range(25000):
        pts1, js1, dist1 = cvt.macqueen_step(pts1, js1, cvt.uniform, True)
        pts1 = cvt.latin_shift(pts1)

        pts2, js2, dist2 = cvt.macqueen_step(pts2, js2, cvt.uniform, True)

        dist1sum += dist1
        dist2sum += dist2
        
        if ( j % 1000 ) == 0 or j == 25000:
            plot_voronois(pts1, pts2, str(i) + '_' + str(j) )

            if j:
                dists1.append(dist1sum)
                dists2.append(dist2sum)
                
                dist1sum = 0
                dist2sum = 0


    plt.clf()
    plt.semilogy(dists1, 'r')
    plt.semilogy(dists2, 'b')
    plt.title('Red: latinized ; Blue: Monte Carlo')
    plt.savefig('Latin_Test/Latin_Test_Distance_' + str(i) + '.png')
    
