import cvt_processing as cvt
import matplotlib.pyplot as plt
import numpy as np

# Generate other arrays
lloyd_sample = cvt.srs_pts(1000)
macqueen_js  = cvt.macqueen_js(25)

# Set up initial points for each algorithm
init_pts = cvt.srs_pts(25)
ll_one_it = np.array(init_pts, copy=True)
mq_one_it = np.array(init_pts, copy=True)

# Do one iteration of each algorithm
ll_one_it = cvt.lloyd_step(ll_one_it, lloyd_sample)
mq_one_it, macqueen_js = cvt.macqueen_step(mq_one_it, macqueen_js)

# Do 999 more iterations of Macqueens algorithm
mq_1000_it = np.array(mq_one_it, copy=True)
for i in range(999):
g    mq_1000_it, macqueen_js = cvt.macqueen_step(mq_1000_it, macqueen_js)

    
init_pts_t = np.transpose(init_pts)
mq_one_it_t = np.transpose(mq_one_it)
ll_one_it_t = np.transpose(ll_one_it)
mq_1000_it_t = np.transpose(mq_1000_it)

f, arrs = plt.subplots(2, 2)
for arrx in arrs:
    for arrxy in arrx:
        arrxy.set(adjustable='box-forced', aspect='equal')
        arrxy.axis([0,1,0,1])
        arrxy.set_xticklabels([])
        arrxy.set_yticklabels([])

arrs[0][0].set_title("Init Points")
arrs[0][0].plot(init_pts_t[0], init_pts_t[1], 'k.')

arrs[1][0].set_title("MacQueen One Iteration")
arrs[1][0].plot(mq_one_it_t[0], mq_one_it_t[1], 'k.')

arrs[0][1].set_title("Lloyds One Iteration")
arrs[0][1].plot(ll_one_it_t[0], ll_one_it_t[1], 'k.')

arrs[1][1].set_title("Lloyds 1000 Iterations")
arrs[1][1].plot(mq_1000_it_t[0], mq_1000_it_t[1], 'k.')

f.savefig("../example_images/cvt_fig.png", bbox_inches='tight')
