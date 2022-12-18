import numpy as np
import cv2
img=cv2.imread('zebra.jpg')

#銳度
kernel1=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
img1=cv2.filter2D(img,-1,kernel1)
kernel2=np.array([
    [0.0625,0.0125,0.0625],
    [0.125,0.65,0.125],
    [0.0625,0.125,0.0625]],np.float32)
img2=cv2.filter2D(img,-1,kernel2)
cv2.imwrite('filter2D1.jpg',img1)
cv2.imshow('filter2D1',img1)
cv2.imwrite('filter2D2.jpg',img2)
cv2.imshow('filter2D2',img2)
cv2.waitKey()
cv2.destroyAllWindows()
print(kernel1)
print()
print(kernel2)

#黑色線條
kernel1=np.array([[-1,-2,-1],[0,0,0],[1,2,1]],np.float32)
kernel3=np.array([[-1,0,1],[-2,0,2],[-1,0,1]],np.float32)
img1=cv2.filter2D(img,-1,kernel1)
img3=cv2.filter2D(img,-1,kernel3)
kernel2=np.array([
    [0,1,0],
    [1,-4,1],
    [0,1,0]],np.float32)
img2=cv2.filter2D(img,-1,kernel2)
cv2.imwrite('filter2D3.jpg',img1)
cv2.imshow('filter2D3',img1)
cv2.imwrite('filter2D4.jpg',img2)
cv2.imshow('filter2D4',img2)
cv2.imwrite('filter2D5.jpg',img3)
cv2.imshow('filter2D5',img3)
cv2.waitKey()
cv2.destroyAllWindows()
print(kernel1)
print()
print(kernel2)

#厚度
a=cv2.Laplacian(img,cv2.CV_8U,ksize=1)
cv2.imshow('Laplacian_1',a)
cv2.imwrite('Laplacian_1.png',a)
a=cv2.Laplacian(img,cv2.CV_8U,ksize=5)
cv2.imshow('Laplacian_5',a)
cv2.imwrite('Laplacian_5.png',a)
a=cv2.Laplacian(img,cv2.CV_8U,ksize=9)
cv2.imshow('Laplacian_9',a)
cv2.imwrite('Laplacian_9.png',a)
cv2.waitKey()
cv2.destroyAllWindows()

