# Image Processing

#### 1. Pixel Processing (Point Processing)

- simplest

$g(x, y) = T(f(x, y))$

- For **brightness** change, add the value to the pixel value
- For **contrast** change, multiply the value to the pixel value

#### 2. LSIS and Convolution

- Linear Shift Invariant System
- Linearity:

  - ![alt text](conv_output/image.png)

- Shift Invariance:

  - ![alt text](conv_output/image-1.png)

- Ideal Lens is LSIS
  - Linearity: Brightness variation
  - Shift invariance: Scene Movement

##### - Convolution:

- slide a function from left to right of another function
- their product is the convolution, **convolved**!!
- Impulse Response of Human Eye:
  - Point Spread Function (PSF)
    ![alt text](conv_output/image-2.png)

#### 3. Linear Image Filters

- Conolution with Discrete Images
- $h[i-m, j-n]$ is where the flipping happens
  - also called **kernel/mask/filter**

![alt text](conv_output/image-3.png)

$$
\large
g[i, j] = \sum_{m=1}^{M} \sum_{n=1}^{N} f[m,n]h[i-m, j-n]
$$

##### Examples:

i. ![alt text](conv_output/image-4.png)

ii. With Sobel Filter:
`kernel = np.array([[1, 0, -1],
                  [2, 0, -2],
                  [1, 0, -1]])`

![alt text](conv_output/image-7.png)

##### Simple and Vectorized Convolution Code (Sobel Filter)

- `np.sum()` used for faster computation

![alt text](conv_output/image-9.png)

iii. With Unsharp Mask:
`kernel = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])`
![alt text](conv_output/image-5.png)

iv. Laplacian Filter:
`kernel = np.array([[0, 1, 0],
                  [1, -4, 1],
                  [0, 1, 0]])`
![alt text](conv_output/image-6.png)

#### 4. Non-Linear Image Filters
