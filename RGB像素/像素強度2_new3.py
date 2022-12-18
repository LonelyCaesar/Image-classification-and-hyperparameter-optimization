import  cv2
import  numpy as np
img=cv2.imread('zebra.jpg')
B,G,R=cv2.split(img)
zeros=np.zeros(img.shape[:2],dtype='uint8')
full1=np.full(img.shape[:2],50,dtype='uint8')
print(full1)
B2=cv2.merge([B,zeros,zeros])
G2=cv2.merge([zeros,G,zeros])
R2=cv2.merge([zeros,zeros,R])
cv2.imwrite('zebra_B.png',B2)
cv2.imwrite('zebra_G.png',G2)
cv2.imwrite('zebra_R.png',R2)
