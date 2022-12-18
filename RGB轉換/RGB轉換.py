import matplotlib.pyplot as plt
import cv2

img_BGR = cv2.imread('zebra.jpg')
plt.subplot(2,2,1)
plt.imshow(img_BGR)
#plt.axis('off')
plt.title('BGR')
cv2.imwrite('plot1.jpg',img_BGR)

img_RGB = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2RGB)
plt.subplot(2,2,2)
plt.imshow(img_RGB)
#plt.axis('off')
plt.title('RGB')
cv2.imwrite('plot2.jpg',img_RGB)

img_GRAY = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2GRAY)
print(img_BGR.shape)
print(img_GRAY.shape)
print(type(img_GRAY))
print(img_GRAY.astype)

print(img_GRAY.dtype.name, img_BGR.dtype.name)

from skimage import io,data
img=data.chelsea()
print(img.dtype.name)

plt.subplot(2,2,3); plt.imshow(img_GRAY);
#lt.axis('off');
plt.title('GRAY')

cv2.imwrite('plot3.jpg',img_GRAY)

img_HSV = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2HSV)
plt.subplot(2,2,4); plt.imshow(img_HSV);
#plt.axis('off');
plt.title('HSV')

cv2.imwrite('plot4.jpg',img_HSV)
plt.show()
