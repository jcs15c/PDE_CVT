import cvt_processing as cvt
import matplotlib.pyplot as plt
import numpy as np

uniform_pts  = cvt.gensample(100)
gauss_pts    = cvt.gensample(100, cvt.gauss)
sinusoid_pts = cvt.gensample(100, density=cvt.sinusoid)

uniform_pts_5d  = cvt.gensample(3, dim=5)
gauss_pts_5d    = cvt.gensample(3, density=cvt.gauss, dim=5)
sinusoid_pts_5d = cvt.gensample(3, cvt.sinusoid, 5)

uniform_pts_t  = np.transpose(uniform_pts)
gauss_pts_t    = np.transpose(gauss_pts)
sinusoid_pts_t = np.transpose(sinusoid_pts)

ax1 = plt.subplot(131, aspect='equal')
ax1.axis([-1,1,-1,1])
ax1.set_title("Uniform")
ax1.plot(uniform_pts_t[0], uniform_pts_t[1], 'k.')

ax2 = plt.subplot(132, aspect='equal')
ax2.axis([-1,1,-1,1])
ax2.set_title("Gauss")
ax2.plot(gauss_pts_t[0], gauss_pts_t[1], 'k.')

ax3 = plt.subplot(133, aspect='equal')
ax3.axis([-1,1,-1,1])
ax3.set_title("Sinusoidal")
ax3.plot(sinusoid_pts_t[0], sinusoid_pts_t[1], 'k.')

plt.show()

print "5D Uniform"
print uniform_pts_5d
print "5D Gaussian"
print gauss_pts_5d
print "5D Sinusoidal"
print sinusoid_pts_5d
