import cvt_processing as cvt
import matplotlib.pyplot as plt
import numpy as np

uniform_pts  = cvt.srs_pts(100)
gauss_pts    = cvt.srs_pts(100, 2, cvt.gauss)
sinusoid_pts = cvt.srs_pts(100, dim=2, density=cvt.sinusoid)

uniform_pts_5d  = cvt.srs_pts(3, dim=5)
gauss_pts_5d    = cvt.srs_pts(3, dim=5, density=cvt.gauss)
sinusoid_pts_5d = cvt.srs_pts(3, 5, cvt.sinusoid)

uniform_pts_t  = np.transpose(uniform_pts)
gauss_pts_t    = np.transpose(gauss_pts)
sinusoid_pts_t = np.transpose(sinusoid_pts)


f, arrs = plt.subplots(1, 3)
for arr in arrs:
    arr.set(adjustable='box-forced', aspect='equal')
    arr.axis([-1,1,-1,1])
    arr.set_xticklabels([])
    arr.set_yticklabels([])

arrs[0].set_title("Uniform")
arrs[0].plot(uniform_pts_t[0], uniform_pts_t[1], 'k.')

arrs[1].set_title("Gauss")
arrs[1].plot(gauss_pts_t[0], gauss_pts_t[1], 'k.')

arrs[2].set_title("Sinusoidal")
arrs[2].plot(sinusoid_pts_t[0], sinusoid_pts_t[1], 'k.')

f.tight_layout()
f.savefig("../example_images/srs_sample_fig.png", bbox_inches='tight')

print "5D Uniform"
print uniform_pts_5d
print "5D Gaussian"
print gauss_pts_5d
print "5D Sinusoidal"
print sinusoid_pts_5d
