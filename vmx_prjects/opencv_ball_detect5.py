#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 赤色の検出
def detect_red_color(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 赤色のHSVの値域1
    hsv_min = np.array([0,130,120])
    hsv_max = np.array([30,255,255])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色のHSVの値域2
    hsv_min = np.array([150,130,120])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色領域のマスク（255：赤色、0：赤色以外）
    mask = mask1 + mask2

    # マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img

# 緑色の検出
def detect_green_color(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 緑色のHSVの値域1
    hsv_min = np.array([30, 64, 0])
    hsv_max = np.array([90,255,255])

    # 緑色領域のマスク（255：赤色、0：赤色以外）
    mask = cv2.inRange(hsv, hsv_min, hsv_max)

    # マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img

# 青色の検出
def detect_blue_color(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 青色のHSVの値域1
    hsv_min = np.array([90, 64, 0])
    hsv_max = np.array([150,255,255])

    # 青色領域のマスク（255：赤色、0：赤色以外）
    mask = cv2.inRange(hsv, hsv_min, hsv_max)

    # マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img

# 円形フィッティング
def detect_circle(img):
    result = []
    
    # 輪郭を抽出
    contours, hierarchy =  cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(contours):
        # ノイズを除外
        if len(cnt) < 20:
            continue
        print(cnt)
        # 円形フィッティング
        # 輪郭に外接する円を取得する。
        center, radius = cv2.minEnclosingCircle(cnt)

        result.append([int(center[0]), int(center[1]) , int(radius)])
    return result
    
# camera open
camera = cv2.VideoCapture(0)
_, frame = camera.read()
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
height, width = frame.shape[:2]
print(f'Height: {height}, Width: {width}')

while True:
    # 入力画像の読み込み
    _, frame = camera.read()

    # 色検出（赤、緑、青）
    red_mask, red_masked_img = detect_red_color(frame)
    # green_mask, green_masked_img = detect_green_color(frame)
    # blue_mask, blue_masked_img = detect_blue_color(frame)

    # 結果を出力
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    circles = detect_circle(red_mask)
    if len(circles) != 0:
        circle_x, circle_y, circle_radius = circles[ np.argmax(circles, axis=0)[2] ]
        # 描画する。
        cv2.circle(frame, (circle_x, circle_y) , circle_radius, (0, 255, 0), 3)
        print("X: %d\t Y:%d\t R:%d\n" %(circle_x, circle_y, circle_radius))
    else:
        print("未検出\n")
    cv2.imshow('video', gray)
    cv2.imshow('video2', frame)

    # 'q'キーが押されたらループから抜ける
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()