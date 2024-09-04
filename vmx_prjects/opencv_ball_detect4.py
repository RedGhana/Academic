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

# ハフ変換
def detect_circle(img):
    # ハフ変換を用いた円検出
    # ぼかし処理
    kernel = (7 * 2) + 1
    img = cv2.GaussianBlur(img, (kernel, kernel), None)
    # HoughCircles関数を使用して円を検出
    circles = cv2.HoughCircles(img, 
                            cv2.HOUGH_GRADIENT, 
                            dp=1.2, 
                            minDist=20, 
                            param1=120, 
                            param2=30, 
                            minRadius=0, 
                            maxRadius=100)
    return circles, img

# camera open
camera = cv2.VideoCapture(0)
_, frame = camera.read()
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
height, width = frame.shape[:2]
print(f'Height: {height}, Width: {width}')

while True:
    # 入力画像の読み込み
    _, frame = camera.read()
    frame = cv2.flip(frame, -1)

    # 色検出（赤、緑、青）
    red_mask, red_masked_img = detect_red_color(frame)
    # green_mask, green_masked_img = detect_green_color(frame)
    # blue_mask, blue_masked_img = detect_blue_color(frame)

    # 結果を出力
    circles, out_img = detect_circle(red_mask)
    # 検出成功
    if circles is not None:
        # circles変数をfloatからintに変換
        circles = np.uint16(np.around(circles))

        circle = circles[0, (np.argmax(circles, axis=1)[0,2]) ]
        # 円周を描画
        cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 255, 0), 3)

        # 中心点を描画
        cv2.circle(frame, (circle[0], circle[1]), 1, (0, 255, 255), 2)
        print("中心点: X: %.02f \tY:%.02f" %(circle[0], circle[1]))
    else:
        print("未検出\n\n")

    
    cv2.imshow('video', out_img)
    cv2.imshow('video2', frame)

    # 'q'キーが押されたらループから抜ける
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
