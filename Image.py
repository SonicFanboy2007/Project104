import cv2
img = cv2.imread("solar-system.jpg")


cv2.putText(img, "Sun", (90,90), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=1.5, color=(0,0,255))


cv2.putText(img, "Mercury", (120,260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "Venus", (195,260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "Earth", (290,260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "Mars", (385,260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "Jupiter", (580,375), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "Saturn", (770,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "Uranus", (975, 290), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "Neptune", (1118,285), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, 
            fontScale=0.5, color=(255,255,255))

cv2.imshow ("display", img)
cv2.waitKey(0) 