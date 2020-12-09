import cv2
import numpy as np
from MyModule.MyFileSelector import MyFileSelector

mfs = MyFileSelector()
mfs.show_ddialog()
png_filename = mfs.get_filename()

if png_filename == '未選択です' or png_filename == '選択をキャンセルしました':
    print('ファイルがただしく選択されていません')
    quit()


# 定数定義
FILE_PREFIX = png_filename[0:-4] # 後ろから4文字削除
ORG_FILE_NAME = png_filename

BLUE_FILE_NAME = FILE_PREFIX + "_b.png"
GREEN_FILE_NAME = FILE_PREFIX + "_g.png"
RED_FILE_NAME = FILE_PREFIX + "_r.png"

ORG_WINDOW_NAME = "org"
BLUE_WINDOW_NAME = "blue"
GREEN_WINDOW_NAME = "green"
RED_WINDOW_NAME = "red"

# 元のカラー画像を読み込む
org_img = cv2.imread(ORG_FILE_NAME, cv2.IMREAD_COLOR)

# ゼロ埋めの画像配列
if len(org_img.shape) == 3:
        height, width, channels = org_img.shape[:3]
else:
        height, width = org_img.shape[:2]
        channels = 1

# org_img.dtypeは`dtype(uint8)`のように画像のビット深度が入る
zeros = np.zeros((height, width), org_img.dtype)

# RGB分離
img_blue_c1, img_green_c1, img_red_c1 = cv2.split(org_img)

img_blue_c3 = cv2.merge((img_blue_c1, zeros, zeros))
img_green_c3 = cv2.merge((zeros, img_green_c1, zeros))
img_red_c3 = cv2.merge((zeros, zeros, img_red_c1))

# ウィンドウを作成
cv2.namedWindow(ORG_WINDOW_NAME)
cv2.namedWindow(BLUE_WINDOW_NAME)
cv2.namedWindow(GREEN_WINDOW_NAME)
cv2.namedWindow(RED_WINDOW_NAME)

# ウィンドウに表示
cv2.imshow(ORG_WINDOW_NAME, org_img)
cv2.imshow(BLUE_WINDOW_NAME, img_blue_c3)
cv2.imshow(GREEN_WINDOW_NAME, img_green_c3)
cv2.imshow(RED_WINDOW_NAME, img_red_c3)

# ファイルに保存
cv2.imwrite(BLUE_FILE_NAME, img_blue_c3)
cv2.imwrite(GREEN_FILE_NAME, img_green_c3)
cv2.imwrite(RED_FILE_NAME, img_red_c3)

# 終了処理
cv2.waitKey(0)
cv2.destroyAllWindows()