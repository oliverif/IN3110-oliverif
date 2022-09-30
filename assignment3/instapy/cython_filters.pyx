import numpy as np
cimport numpy as np
import cython



def cython_color2gray(unsigned char [:,:,:] image):
    """Convert rgb pixel array to grayscale using cython implementation.

    Args:
        image (np.array) Input will be cast to cdef unsigned char memoryview
    Returns:
        np.array: gray_image
    """


    # Get the image dimensions
    cdef int nx = image.shape[1]
    cdef int ny = image.shape[0]

    # Create memoryview with unsigned char(uint8) as type. Memoryview is more efficient for retrieving items through
    # indexing.
    cdef unsigned char[:,:,:] gray_image = np.empty((ny,nx,3), dtype=np.uint8)

    # Pre define variables to avoid interaction with python api
    cdef double r = 0.21
    cdef double g = 0.72
    cdef double b = 0.07
    cdef int i,j
    cdef unsigned char gray_val

    # Iterate through image and assign gray value to memoryview
    for i in range(ny):
        for j in range(nx):
            gray_val = <unsigned char>(image[i, j,0] * r + image[i, j,1] *g + image[i, j,2] * b) #Cast result to uint8
            gray_image[i,j,0] = gray_image[i,j,1] = gray_image[i,j,2] = gray_val
    
    #convert memoryview to numpy array
    return np.asarray(gray_image)

def cython_color2sepia(unsigned char[:,:,:] image):
    """Convert rgb pixel array to sepia using cython implementation

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    cdef int nx = image.shape[1]
    cdef int ny = image.shape[0]

    cdef unsigned char[:,:,:] sepia_image = np.empty((ny,nx,3), dtype=np.uint8)

    cdef double[:,:] sepia_matrix = np.asarray(
        [
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131],
        ]
    )
    cdef int i,j,n,m
    cdef double tmp

    for i in range(ny):
        for j in range(nx):
            for n in range(3):
                sepia_image[i, j, n] = <unsigned char> min(image[i, j, 0] * sepia_matrix[n, 0] + image[i, j, 1] * sepia_matrix[n, 1] + image[i, j, 2] * sepia_matrix[n, 2],255)
    
    return np.asarray(sepia_image)

