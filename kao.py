# -*- coding: utf-8 -*-
import cv2
import time

img = cv2.imread('uchitane_far.png')
window = "Push ESC key to stop this program"

def detect_face(img):
    cascade = cv2.CascadeClassifier(img)
    facerect = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

    #顔の数だけ処理
    if len(facerect) > 0:
        for rect in facerect:
            #矩形描画
            cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),(255,255,255),3)

    cv2.imshow(window, img)
    print(facerect)

if(__name__ == '__main__'):

    # デフォルトカメラは0
    capture = cv2.VideoCapture(1)

    # キャプチャ処理
    while(True):
        key = cv2.waitKey(5)
        if(key == 27):
            print("exit.")
            break

        # 画像キャプチャ
        ret, img = capture.read()

        # 取り込み開始になっていなかったら上の処理に戻る
        if(ret == False):
            print("Capture Failed. ")
            break

        #顔検出
        detect_face(img)
        time.sleep(0.050)

    capture.release()
    cv2.destroyAllWindows()

# cv2.imshow("In the middle of processing", img)
# 終了処理
cv2.waitKey(0)
# 編集した画像を保存する
cv2.imwrite('edit.png', img)