
import cv2


image = cv2.imread("Profile.jpg")
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.divide(grey_image,invertedblur,scale=258.0)


cv2.imwrite("Profile-sketch.png", sketch)

############













