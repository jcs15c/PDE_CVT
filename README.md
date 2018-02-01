# CVT Function Library

This library contains functions to generate Centroidal Voronoi points in n-dimensional space. 

## Point Generation

Points are generated on the unit hypercube according to a given density function. The hypercube can be scaled and translated within the processing script.

```python
   gensample(n, density=uniform, dim=2)
```

```python
   import cvt_processing as cvt
   
   # 2D Example
   uniform_pts  = cvt.gensample(100)
   gauss_pts    = cvt.gensample(100, cvt.gauss)
   sinusoid_pts = cvt.gensample(100, density=cvt.sinusoid)

   # 5D Example
   uniform_pts_5d  = cvt.gensample(100, dim=5)
   gauss_pts_5d    = cvt.gensample(100, cvt.gauss, dim=5)
   sinusoid_pts_5d = cvt.gensample(100, cvt.sinusoid, 5)


```
![Spherical CVT Example](https://github.com/jcs15c/sphere_cvt/blob/master/output/examples/Spherical_CVT_Example.png "Spherical_CVT_Example")
