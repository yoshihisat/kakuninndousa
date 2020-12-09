import cv2
import os

assert os.path.isfile(face_cascade_path), 'haarcascade_frontalface_default.xml がない'
assert os.path.isfile(eye_cascade_path), 'eye_cascade_path.xml がない'

# Haar-like特徴分類器の読み込み

face_cascade_path = '/usr/local/opt/opencv/share/'\
                    'OpenCV/haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = '/usr/local/opt/opencv/share/'\
                   'OpenCV/haarcascades/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)



# イメージファイルの読み込み
img = cv2.imread('uchitane_far.png')

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 顔を検知
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=6)