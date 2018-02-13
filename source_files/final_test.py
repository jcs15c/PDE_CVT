import cvt_processing as cvt
import matplotlib.pyplot as plt
import numpy as np

n = 50

srs_pts = cvt.srs_pts(n)
kpp_pts = cvt.kpp_pts(n)
hal_pts = cvt.halton_pts(n)
ham_pts = cvt.hammersley_pts(n)
lhs_pts = cvt.latin_pts(n)
cvt_pts = cvt.cvt_pts(n)
lvt_pts = cvt.cvt_lhs_pts(n)

points = [srs_pts, kpp_pts, hal_pts, ham_pts,
          lhs_pts, cvt_pts, lvt_pts]

methods = ["SRS", "Kmeans++", "Halton",
           "Hammersley", "LHS", "CVT", "Latinized CVT"]

f, arrs = plt.subplots(7, 2, figsize=(4,15) )
for i in range(len(arrs)):
    for arr in arrs[i]:
        arr.set(adjustable='box-forced', aspect='equal')
        arr.axis([-1,1,-1,1])
        arr.set_xticklabels([])
        arr.set_yticklabels([])

    arrs[i][0].set_ylabel(methods[i])

    pts = np.array(points[i], copy=True)

    pts_t = np.transpose(pts)
    arrs[i][0].plot(pts_t[0], pts_t[1], 'k.')

    proj_pts = cvt.inverse_transform(pts)
    proj_t = np.transpose(proj_pts)
    arrs[i][1].plot(proj_t[0], proj_t[1], 'k.')


arrs[0][0].set_title("Uniform")
arrs[0][1].set_title("Gaussian")
f.subplots_adjust(wspace=0, hspace=0.10)
f.savefig("../example_images/final_fig.png", bbox_inches='tight')

