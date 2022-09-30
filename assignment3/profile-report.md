# Profiling report

## Questions

A few questions below to help understand the kind of information we can get from profiling outputs.
 We are not asking for lots of detail, just 1-2 sentences each.

### Question 1

> Which profiler produced the most useful output, and why?

line_profiler, as it provided timings of each line of code. cProfile gave timings of a lot of other functions I likely
don't have control over, and not any details into my developed function. At least not as interpretable as line_profiler

### Question 2

> Pick one profiler output (e.g. `cprofile numpy_color2sepia`).
  Based on this profile, where should we focus effort on improving performance?

> **Hint:** two things to consider when picking an optimization:

> - how much time is spent in the step? (reducing a step that takes 1% of the time all the way to 0 can only improve performance by 1%)
> - are there other ways to do it? (simple steps may already be optimal. Complex steps often have many implementations with different performance)

selected profile: line_profiler cython_color2sepia

The focus should clearly be on optimizing the for loops. It's clear most of the time is spent in the inner loop.
So finding some optimizations here is probably valuable. Loop unrolling or optimizing cache usage somehow.


## Profile output

Paste the outputs of `python3 -m instapy.profiling` below:

<details>
<summary>cProfile output</summary>

```
Profiling python color2gray with cprofile:
         2766260 function calls in 2.986 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    1.648    0.549    2.986    0.995 python_filters.py:8(python_color2gray)
   921600    1.071    0.000    1.071    0.000 python_filters.py:20(<listcomp>)
        1    0.000    0.000    0.963    0.963 cProfile.py:106(runcall)
   921600    0.219    0.000    0.219    0.000 {built-in method builtins.sum}
   923043    0.047    0.000    0.047    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 multiarray.py:80(empty_like)
        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}


Profiling numpy color2gray with cprofile:
         20 function calls in 0.007 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.006    0.002    0.007    0.002 numpy_filters.py:7(numpy_color2gray)
        1    0.000    0.000    0.002    0.002 cProfile.py:106(runcall)
        3    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 multiarray.py:80(empty_like)
        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}


Profiling numba color2gray with cprofile:
         11 function calls in 0.004 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.004    0.001    0.004    0.001 numba_filters.py:6(numba_color2gray)
        1    0.000    0.000    0.001    0.001 cProfile.py:106(runcall)
        3    0.000    0.000    0.000    0.000 serialize.py:29(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}


Profiling cython color2gray with cprofile:
         50 function calls in 0.003 seconds

   Ordered by: cumulative time
   List reduced from 12 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.003    0.001    0.003    0.001 cython_filters.pyx:7(cython_color2gray)
        1    0.000    0.000    0.001    0.001 cProfile.py:106(runcall)
        3    0.000    0.000    0.000    0.000 stringsource:1001(memoryview_fromslice)
        9    0.000    0.000    0.000    0.000 stringsource:346(__cinit__)
        6    0.000    0.000    0.000    0.000 stringsource:659(memoryview_cwrapper)
        9    0.000    0.000    0.000    0.000 stringsource:299(align_pointer)
        3    0.000    0.000    0.000    0.000 stringsource:520(__getbuffer__)
        6    0.000    0.000    0.000    0.000 stringsource:665(memoryview_check)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 stringsource:374(__dealloc__)


Profiling python color2sepia with cprofile:
         8295863 function calls in 6.919 seconds

   Ordered by: cumulative time
   List reduced from 12 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    2.903    0.968    6.919    2.306 python_filters.py:27(python_color2sepia)
  2764800    2.932    0.000    2.932    0.000 python_filters.py:50(<listcomp>)
        1    0.000    0.000    2.367    2.367 cProfile.py:106(runcall)
  2764800    0.670    0.000    0.670    0.000 {built-in method builtins.sum}
  2764800    0.413    0.000    0.413    0.000 {built-in method builtins.min}
     1443    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.asarray}
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numpy color2sepia with cprofile:
         527 function calls (512 primitive calls) in 0.052 seconds

   Ordered by: cumulative time
   List reduced from 74 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.005    0.002    0.052    0.017 numpy_filters.py:26(numpy_color2sepia)
     24/9    0.014    0.001    0.047    0.005 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.032    0.011 <__array_function__ internals>:177(clip)
        3    0.000    0.000    0.032    0.011 fromnumeric.py:2085(clip)
        3    0.000    0.000    0.032    0.011 fromnumeric.py:51(_wrapfunc)
        3    0.000    0.000    0.032    0.011 {method 'clip' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.032    0.011 _methods.py:126(_clip)
        3    0.032    0.011    0.032    0.011 _methods.py:107(_clip_dep_invoke_with_casting)
        1    0.000    0.000    0.017    0.017 cProfile.py:106(runcall)
        3    0.000    0.000    0.015    0.005 <__array_function__ internals>:177(einsum)


Profiling numba color2sepia with cprofile:
         11 function calls in 0.008 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.008    0.003    0.008    0.003 numba_filters.py:33(numba_color2sepia)
        1    0.000    0.000    0.003    0.003 cProfile.py:106(runcall)
        3    0.000    0.000    0.000    0.000 serialize.py:29(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}


Profiling cython color2sepia with cprofile:
         65 function calls in 0.019 seconds

   Ordered by: cumulative time
   List reduced from 12 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.019    0.006    0.019    0.006 cython_filters.pyx:41(cython_color2sepia)
        1    0.000    0.000    0.006    0.006 cProfile.py:106(runcall)
        3    0.000    0.000    0.000    0.000 stringsource:1001(memoryview_fromslice)
       12    0.000    0.000    0.000    0.000 stringsource:346(__cinit__)
        9    0.000    0.000    0.000    0.000 stringsource:659(memoryview_cwrapper)
       12    0.000    0.000    0.000    0.000 stringsource:299(align_pointer)
        3    0.000    0.000    0.000    0.000 stringsource:520(__getbuffer__)
        9    0.000    0.000    0.000    0.000 stringsource:665(memoryview_check)
        6    0.000    0.000    0.000    0.000 stringsource:374(__dealloc__)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```

</details>

<details>
<summary>line_profiler output</summary>

```
Profiling python color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 5.83746 s
File: /home/oliverif/courses/IN3110-oliverif/assignment3/instapy/python_filters.py
Function: python_color2gray at line 8

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     8                                           def python_color2gray(image: np.array) -> np.array:
     9                                               """Convert rgb pixel array to grayscale
    10
    11                                               Args:
    12                                                   image (np.array)
    13                                               Returns:
    14                                                   np.array: gray_image
    15                                               """
    16         3         60.0     20.0      0.0      gray_image = np.empty_like(image)
    17                                               # iterate through the pixels, and apply the grayscale transform
    18      1443        416.0      0.3      0.0      for i in range(len(image)):
    19    923040     261595.0      0.3      4.5          for j in range(len(image[i])):
    20    921600    2523599.0      2.7     43.2              gray_val = sum([p * w for p, w in zip(image[i, j], PIXEL_WEIGHTS)])
    21   3686400    1476638.0      0.4     25.3              for c in range(len(gray_image[i, j])):
    22   2764800    1575150.0      0.6     27.0                  gray_image[i, j][c] = gray_val
    23
    24         3          0.0      0.0      0.0      return gray_image

Profiling numpy color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 0.005119 s
File: /home/oliverif/courses/IN3110-oliverif/assignment3/instapy/numpy_filters.py
Function: numpy_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def numpy_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15
    16         3         19.0      6.3      0.4      gray_image = np.empty_like(image)
    17
    18                                               # Multiply color weights with image allows vectorized multiplication.
    19                                               # Summing along axis 2 and assingning directly to the axis 2 of gray image.
    20         3       1271.0    423.7     24.8      gray_image[:, :, 0] = gray_image[:, :, 1] = gray_image[:, :, 2] = (
    21         3       3683.0   1227.7     71.9          image[:, :, 0] * 0.21 + image[:, :, 1] * 0.72 + image[:, :, 2] * 0.07
    22                                               )
    23         3        146.0     48.7      2.9      return gray_image.astype(np.uint8)

Profiling numba color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 0 s
File: /home/oliverif/courses/IN3110-oliverif/assignment3/instapy/numba_filters.py
Function: numba_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @jit(nopython=True, cache=True)
     7                                           def numba_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15
    16                                               gray_image = np.empty_like(image)
    17
    18                                               # These predefenitions will allow numba to convert more of the code to c code.
    19                                               nx = image.shape[1]
    20                                               ny = image.shape[0]
    21                                               r = 0.2100
    22                                               g = 0.7200
    23                                               b = 0.0700
    24
    25                                               # Iterate through image and assign gray value to numpy array
    26                                               for i in range(ny):
    27                                                   for j in range(nx):
    28                                                       gray_val = image[i, j, 0] * r + image[i, j, 1] * g + image[i, j, 2] * b  # Cast result to uint8
    29                                                       gray_image[i, j, 0] = gray_image[i, j, 1] = gray_image[i, j, 2] = gray_val  # Faster than gray_image[i,j,:]
    30                                               return gray_image.astype(np.uint8)

Profiling cython color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 0.325854 s
File: instapy/cython_filters.pyx
Function: cython_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def cython_color2gray(unsigned char [:,:,:] image):
     8                                               """Convert rgb pixel array to grayscale using cython implementation.
     9
    10                                               Args:
    11                                                   image (np.array) Input will be cast to cdef unsigned char memoryview
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15
    16
    17                                               # Get the image dimensions
    18         3          1.0      0.3      0.0      cdef int nx = image.shape[1]
    19         3          0.0      0.0      0.0      cdef int ny = image.shape[0]
    20
    21                                               # Create memoryview with unsigned char(uint8) as type. Memoryview is more efficient for retrieving items through
    22                                               # indexing.
    23         3         24.0      8.0      0.0      cdef unsigned char[:,:,:] gray_image = np.empty((ny,nx,3), dtype=np.uint8)
    24
    25                                               # Pre define variables to avoid interaction with python api
    26         3          0.0      0.0      0.0      cdef double r = 0.21
    27         3          2.0      0.7      0.0      cdef double g = 0.72
    28         3          0.0      0.0      0.0      cdef double b = 0.07
    29                                               cdef int i,j
    30                                               cdef unsigned char gray_val
    31
    32                                               # Iterate through image and assign gray value to memoryview
    33         3          0.0      0.0      0.0      for i in range(ny):
    34      1440        324.0      0.2      0.1          for j in range(nx):
    35    921600     162670.0      0.2     49.9              gray_val = <unsigned char>(image[i, j,0] * r + image[i, j,1] *g + image[i, j,2] * b) #Cast result to uint8
    36    921600     162724.0      0.2     49.9              gray_image[i,j,0] = gray_image[i,j,1] = gray_image[i,j,2] = gray_val
    37
    38                                               #convert memoryview to numpy array
    39         3        109.0     36.3      0.0      return np.asarray(gray_image)

Profiling python color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 12.7751 s
File: /home/oliverif/courses/IN3110-oliverif/assignment3/instapy/python_filters.py
Function: python_color2sepia at line 27

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    27                                           def python_color2sepia(image: np.array) -> np.array:
    28                                               """Convert rgb pixel array to sepia
    29
    30                                               Args:
    31                                                   image (np.array)
    32                                               Returns:
    33                                                   np.array: sepia_image
    34                                               """
    35         3         53.0     17.7      0.0      sepia_image = np.empty_like(image, dtype=np.uint8)
    36                                               # Iterate through the pixels
    37                                               # applying the sepia matrix
    38         6         33.0      5.5      0.0      sepia_matrix = np.asarray(
    39         3          3.0      1.0      0.0          [
    40         3          4.0      1.3      0.0              [0.393, 0.769, 0.189],
    41         3          3.0      1.0      0.0              [0.349, 0.686, 0.168],
    42         3          2.0      0.7      0.0              [0.272, 0.534, 0.131],
    43                                                   ],
    44         3          1.0      0.3      0.0          dtype="double",
    45                                               )
    46
    47      1443        953.0      0.7      0.0      for i in range(len(image)):
    48    923040     550866.0      0.6      4.3          for j in range(len(image[i])):
    49   3686400    2440581.0      0.7     19.1              for n in range(3):
    50   2764800    9782574.0      3.5     76.6                  sepia_image[i, j, n] = min(255, sum([p * s for p, s in zip(sepia_matrix[n], image[i, j])]))
    51
    52                                               # Return image
    53                                               # don't forget to make sure it's the right type!
    54         3          2.0      0.7      0.0      return sepia_image

Profiling numpy color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 0.073729 s
File: /home/oliverif/courses/IN3110-oliverif/assignment3/instapy/numpy_filters.py
Function: numpy_color2sepia at line 26

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    26                                           def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    27                                               """Convert rgb pixel array to sepia
    28
    29                                               Args:
    30                                                   image (np.array)
    31                                                   k (float): amount of sepia filter to apply (optional)
    32
    33                                               The amount of sepia is given as a fraction, k=0 yields no sepia while
    34                                               k=1 yields full sepia.
    35
    36                                               (note: implementing 'k' is a bonus task,
    37                                               you may ignore it for Task 9)
    38
    39                                               Returns:
    40                                                   np.array: sepia_image
    41                                               """
    42
    43         3          7.0      2.3      0.0      if not 0 <= k <= 1:
    44                                                   # validate k (optional)
    45                                                   raise ValueError(f"k must be between [0-1], got {k=}")
    46
    47         3         60.0     20.0      0.1      sepia_image = np.empty_like(image, dtype=np.uint8)
    48
    49                                               # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    50         6         39.0      6.5      0.1      sepia_matrix = np.add(
    51         9         71.0      7.9      0.1          np.asarray(
    52         3          5.0      1.7      0.0              [
    53         3          7.0      2.3      0.0                  [1, 0, 0],
    54         3          6.0      2.0      0.0                  [0, 1, 0],
    55         3          5.0      1.7      0.0                  [0, 0, 1],
    56                                                       ]
    57                                                   )
    58         3          5.0      1.7      0.0          * (1 - k),
    59         9         39.0      4.3      0.1          np.asarray(
    60         3          3.0      1.0      0.0              [
    61         3          4.0      1.3      0.0                  [0.393, 0.769, 0.189],
    62         3          5.0      1.7      0.0                  [0.349, 0.686, 0.168],
    63         3          5.0      1.7      0.0                  [0.272, 0.534, 0.131],
    64                                                       ],
    65                                                   )
    66         3          3.0      1.0      0.0          * k,
    67                                               )
    68
    69                                               # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    70                                               # use Einstein sum to apply pixel transform matrix
    71                                               # Apply the matrix filter and clip the values to 255. Note that out=sepia_image ensures the type of sepia_image is
    72                                               # presevered.
    73         6      46817.0   7802.8     63.5      sepia_image = np.clip(
    74         3      26617.0   8872.3     36.1          np.einsum("ijk,lk->ijl", image, sepia_matrix, optimize=True),
    75         3          7.0      2.3      0.0          a_min=0,
    76         3          4.0      1.3      0.0          a_max=255,
    77         3          5.0      1.7      0.0          out=sepia_image,
    78         3          5.0      1.7      0.0          casting="unsafe",
    79                                               )
    80         3         10.0      3.3      0.0      return sepia_image

Profiling numba color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 0 s
File: /home/oliverif/courses/IN3110-oliverif/assignment3/instapy/numba_filters.py
Function: numba_color2sepia at line 33

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    33                                           @jit(nopython=True, cache=True)
    34                                           def numba_color2sepia(image: np.array) -> np.array:
    35                                               """Convert rgb pixel array to sepia
    36
    37                                               Args:
    38                                                   image (np.array)
    39                                               Returns:
    40                                                   np.array: sepia_image
    41                                               """
    42                                               sepia_image = np.empty_like(image, dtype="uint8")
    43                                               # Iterate through the pixels
    44                                               # applying the sepia matrix
    45
    46                                               sepia_matrix = np.asarray(
    47                                                   [
    48                                                       [0.393, 0.769, 0.189],
    49                                                       [0.349, 0.686, 0.168],
    50                                                       [0.272, 0.534, 0.131],
    51                                                   ]
    52                                               )
    53                                               nx = image.shape[1]
    54                                               ny = image.shape[0]
    55
    56                                               for i in range(ny):
    57                                                   for j in range(nx):
    58                                                       for n in range(3):
    59                                                           tmp = 0
    60                                                           for m in range(3):
    61                                                               tmp += sepia_matrix[n, m] * image[i, j, m]
    62
    63                                                           sepia_image[i, j, n] = min(tmp, 255)
    64                                                           # sepia_image[i, j, n] = min(255, sum([p * s for p, s in zip(sepia_matrix[n], image[i, j])]))
    65
    66                                               # Return image
    67                                               # don't forget to make sure it's the right type!
    68                                               return sepia_image

Profiling cython color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 0.719715 s
File: instapy/cython_filters.pyx
Function: cython_color2sepia at line 41

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    41                                           def cython_color2sepia(unsigned char[:,:,:] image):
    42                                               """Convert rgb pixel array to sepia using cython implementation
    43
    44                                               Args:
    45                                                   image (np.array)
    46                                               Returns:
    47                                                   np.array: gray_image
    48                                               """
    49
    50         3          2.0      0.7      0.0      cdef int nx = image.shape[1]
    51         3          2.0      0.7      0.0      cdef int ny = image.shape[0]
    52
    53         3         33.0     11.0      0.0      cdef unsigned char[:,:,:] sepia_image = np.empty((ny,nx,3), dtype=np.uint8)
    54
    55         6          9.0      1.5      0.0      cdef double[:,:] sepia_matrix = np.asarray(
    56         3         22.0      7.3      0.0          [
    57         3          1.0      0.3      0.0              [0.393, 0.769, 0.189],
    58         3          1.0      0.3      0.0              [0.349, 0.686, 0.168],
    59         3          2.0      0.7      0.0              [0.272, 0.534, 0.131],
    60                                                   ]
    61                                               )
    62                                               cdef int i,j,n,m
    63                                               cdef double tmp
    64
    65         3          1.0      0.3      0.0      for i in range(ny):
    66      1440        302.0      0.2      0.0          for j in range(nx):
    67    921600     182392.0      0.2     25.3              for n in range(3):
    68   2764800     536821.0      0.2     74.6                  sepia_image[i, j, n] = <unsigned char> min(image[i, j, 0] * sepia_matrix[n, 0] + image[i, j, 1] * sepia_matrix[n, 1] + image[i, j, 2] * sepia_matrix[n, 2],255)
    69
    70         3        127.0     42.3      0.0      return np.asarray(sepia_image)
```

</details>
