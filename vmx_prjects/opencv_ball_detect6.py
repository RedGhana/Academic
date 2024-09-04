#-*- coding:utf-8 -*-
import cv2
import numpy as np

def empty(x):
    pass
cv2.namedWindow('Parameters')
cv2.resizeWindow('Parameters', width=1000, height=400)
cv2.createTrackbar('k_size_set', 'Parameters', 1, 10, empty) #3
cv2.createTrackbar('canny_1st', 'Parameters', 90, 500, empty) #80
cv2.createTrackbar('canny_2nd', 'Parameters', 60, 500, empty) #120
cv2.createTrackbar('minDist_set', 'Parameters', 100, 200, empty)
cv2.createTrackbar('param1_set', 'Parameters', 100, 300, empty) #100
cv2.createTrackbar('param2_set', 'Parameters', 30, 300, empty) #30
cv2.createTrackbar('minRadius_set', 'Parameters',510, 1000, empty) #250
cv2.createTrackbar('maxRadius_set', 'Parameters', 0, 1000, empty ) #500

# ハフ変換
def detect_circle(img):
    # ハフ変換を用いた円検出
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #2. Gaussian blur
    kernel = cv2.getTrackbarPos("k_size_set", "Parameters")
    kernel = (kernel * 2) + 1
    img_blur = cv2.GaussianBlur(img_gray, (kernel, kernel), None)
    
    #2.5.Canny Edge Detection
    thres1_val = cv2.getTrackbarPos('canny_1st', 'Parameters')
    thres2_val = cv2.getTrackbarPos('canny_2nd', 'Parameters')
    img_edge = cv2.Canny(img_blur, threshold1=thres1_val, threshold2=thres2_val)
    
    # HoughCircles関数を使用して円を検出
    circles = cv2.HoughCircles(img_edge, cv2.HOUGH_GRADIENT,
                               dp=1,
                               minDist=cv2.getTrackbarPos('minDist_set', 'Parameters'),
                               param1=cv2.getTrackbarPos('param1_set', 'Parameters'),
                               param2=cv2.getTrackbarPos('param2_set', 'Parameters'),
                               minRadius=cv2.getTrackbarPos('minRadius_set', 'Parameters'),
                               maxRadius=cv2.getTrackbarPos('maxRadius_set', 'Parameters'),
                               )
    circle = None
    if circles is not None:
        # 検出成功

        # circles変数をfloatからintに変換
        circles = np.uint16(np.around(circles))

        circle = circles[0, (np.argmax(circles, axis=1)[0,2]) ]
    return circle, img_edge

# camera open
camera = cv2.VideoCapture(0)
_, frame = camera.read()
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
height, width = frame.shape[:2]
print(f'Height: {height}, Width: {width}')

while True:
    # 入力画像の読み込み
    _, frame = camera.read()

    # 結果を出力
    circle, img = detect_circle(frame)
    if circle is not None:
        # 円周を描画
        cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 255, 0), 3)

        # 中心点を描画
        cv2.circle(frame, (circle[0], circle[1]), 1, (0, 255, 255), 2)
        print("中心点: X: %.02f \tY:%.02f" %(circle[0], circle[1]))
    else:
        print("未検出\n\n")

    cv2.imshow('video', frame)
    cv2.imshow('video2', img)

    # 'q'キーが押されたらループから抜ける
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()