import cvt_processing as cvt
import matplotlib.pyplot as plt
import numpy as np

kpp_pts    = cvt.kppsample(100)
latin_pts  = cvt.latin_pts(100)
halton_pts = cvt.halton_pts(100)
hammer_pts = cvt.hammersley_pts(100)

kpp_pts_t    = np.transpose(kpp_pts)
latin_pts_t  = np.transpose(latin_pts)
halton_pts_t = np.transpose(halton_pts)
hammer_pts_t = np.transpose(hammer_pts)

f, arrs = plt.subplots(2, 2)
for arrx in arrs:
    for arrxy in arrx:
        arrxy.set(adjustable='box-forced', aspect='equal')
        arrxy.axis([0,1,0,1])
        arrxy.set_xticklabels([])
        arrxy.set_yticklabels([])

arrs[0][0].set_title("Kmeans++")
arrs[0][0].plot(kpp_pts_t[0], kpp_pts_t[1], 'k.')

arrs[1][0].set_title("Latinized")
arrs[1][0].plot(latin_pts_t[0], latin_pts_t[1], 'k.')

arrs[0][1].set_title("Halton")
arrs[0][1].plot(halton_pts_t[0], halton_pts_t[1], 'k.')

arrs[1][1].set_title("Hammersley")
arrs[1][1].plot(hammer_pts_t[0], hammer_pts_t[1], 'k.')

f.tight_layout()
f.savefig("../example_images/non_srs_fig.png", bbox_inches='tight')
