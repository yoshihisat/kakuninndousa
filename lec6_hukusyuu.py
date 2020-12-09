import cv2

img = cv2.imread('uchitane_far.png')
# rows には640が，colsには1280が代入される
# channelsにはbgrのカラーチャンネルの3が代入される
rows,cols,channels = img.shape

# 例として画像のx,y=640, 140の画素(ピクセル)を指定すると黄色[5, 188, 251]が得られる
# 色の並びは一般的なRGBではなくBGRの順番であることに注意
print(img[140, 640])



# 画素から青色を消したい場合は次のように処理する
for x in range(rows):
    for y in range(cols):
        b, g, r = img[x, y]
        if (b, g, r) == (255, 255, 255):
            continue
        img[x, y] = 0, g, r

# 長方形（水色の長方形）の描画
# 水色(255,255,0)
begin_point = (10, 20)
end_point = (40, 100)
cyan = (255,255,0)
img = cv2.rectangle(img, begin_point, end_point, cyan,thickness=3)

# 編集した画像を保存する
cv2.imwrite('edit.png', img)
