import cv2
import numpy as np,sys
A = cv2.imread('C:/Users/zoresmile/Desktop/yl/image/1.png')
B = cv2.imread('C:/Users/zoresmile/Desktop/yl/image/2.png')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)
# Now add left and right halves of images in each level
#numpy.hstack(tup)
#Take a sequence of arrays and stack them horizontally
#to make a single array.
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape

    ls = np.hstack((la[:,:cols//2], lb[:,cols//2:]))
    # ls = np.hstack((la[:, :cols // 4], lb[:, cols // 4: cols//2], la[:, cols//2:3 * cols//4], lb[:, 3*cols//4: ]))
    LS.append(ls)
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))
# real = np.hstack((A[:,:cols//4],B[:,cols//4: cols//2], A[:, cols//2: 3*cols//4], B[:, 3*cols//4: ]))
cv2.imwrite('C:/Users/zoresmile/Desktop/yl/out/ls.png',ls_)
cv2.imwrite('C:/Users/zoresmile/Desktop/yl/out/real.png',real)