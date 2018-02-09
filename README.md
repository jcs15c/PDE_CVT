# CVT Function Library

This library contains functions to generate Centroidal Voronoi points in n-dimensional space. 

## Point Generation

Monte Carlo Points are generated randomly on the unit hypercube according to a given density function. 

```python
   gensample(n, density=uniform, dim=2)
```

```python
   ## srs_sample_test.py ##
   import cvt_processing as cvt
   
   # 2D Example
   uniform_pts  = cvt.gensample(100)
   gauss_pts    = cvt.gensample(100, cvt.gauss)
   sinusoid_pts = cvt.gensample(100, density=cvt.sinusoid)

   # 5D Example
   uniform_pts_5d  = cvt.gensample(3, dim=5)
   gauss_pts_5d    = cvt.gensample(3, density=cvt.gauss, dim=5)
   sinusoid_pts_5d = cvt.gensample(3, cvt.sinusoid, 5)

   ...
```
![Monte Carlo Sample Points](https://github.com/jcs15c/PDE_CVT/blob/master/example_images/srs_sample_fig.png "Monte_Carlo_Sample")
```
   #Text output
   5D Uniform  
   [[-0.97116734 -0.89501887  0.87471317 -0.9724642  -0.0399111 ]
    [ 0.62883577 -0.16562635 -0.60997768  0.47627556  0.23456399]
    [-0.84076283 -0.63156464 -0.11728075  0.57704989  0.14870551]]
   5D Gaussian
   [[ 0.64050097  0.21388999  0.02376145 -0.35474419 -0.07424126]
    [-0.06280193 -0.32578181  0.13600938 -0.16542369 -0.06875906]
    [-0.35886008 -0.18699282  0.1814123   0.22894681 -0.07602129]]
   5D Sinusoidal
   [[ 0.60487684  0.62588684 -0.5362688  -0.56225787 -0.48133396]
    [ 0.53603422  0.36057289 -0.31797064 -0.42140368 -0.34892563]
    [-0.71101366  0.49457508 -0.42284865 -0.42804622 -0.38915426]]
```

While randomly generated points are necessary, they can occasionally "clump," lelading to an uneven distribution. To alleviate this, three other methods of point generation are included, two with random elements and one entirely deterministic. Each method adds a degree of uniformity to the selection of points.

Kmeans++ is a method of Monte Carlo sampling in which each point is randomly selected proportional to the distance between it and the closest point already selected. That is to say, points further away from already selected points are more likely to be selected. The exponent chosen for this distance, with the default being 2, determines by what probability points are chosen.

Halton points are a deterministic method of sampling that uses coprime numbers to select a pseudo-random sequence of numbers, which are then paired in n dimensions. While some values give points with a clear linear relation, small coprimes give points of low-discrepancy.

Lainized Hypercube points are selected such that each point occupies a particular "row and column" in 2D, with scalability to higher dimensions. This ensures a random selection of points, but ensures that the points are not clustered around a particular location.