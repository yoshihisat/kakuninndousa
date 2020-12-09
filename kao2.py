#coding: utf-8
import cv2

cascade_file = "haarcascade_frontalface_alt.xml"
image_file = "uchitane_far.png"

img = cv2.imread(image_file)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))

if len(face_list) == 0:
  print("Fail recognise")
  quit()

for (x, y, w, h) in face_list:
  print("顔の座標 =", x, y, w, h)
  color = (0, 0, 225)
  pen_w = 8
  cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)

cv2.imwrite("after.png", img)