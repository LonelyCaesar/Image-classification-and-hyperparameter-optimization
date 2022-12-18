import  cv2
img=cv2.imread('zebra.jpg')
img1=cv2.blur(img,(5,10))
img2=cv2.GaussianBlur(img,(11,11),1)
img3= cv2.medianBlur(img,5)
img4 = cv2.bilateralFilter(img, 5, 10, 15)
#一般模糊
cv2.imwrite('zebra_blur.jpg',img1)
cv2.imshow('blur',img1)
#高斯模糊
cv2.imwrite('zebra_GaussianBlur.jpg',img2)
cv2.imshow('GaussianBlur',img2)
#中位模糊
cv2.imwrite('zebra_medianBlur.jpg',img3)
cv2.imshow('medianBlur',img3)
#雙向模糊
cv2.imwrite('zebra_bilateralFilter.jpg',img4)
cv2.imshow('bilateralFilter',img4)

cv2.waitKey()
cv2.destroyAllWindows()