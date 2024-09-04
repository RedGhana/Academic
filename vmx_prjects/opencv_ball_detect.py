import cv2
import numpy as np
from datetime import datetime
from time import sleep

# camera open
camera = cv2.VideoCapture(0)

# 繰り返し、画像を判定
try:
    while True:
        # カメラから画像を入力
        _, frame = camera.read()

        # マスク画像取得
        def getMask(l, u):
            # HSVに変換
            hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            
            lower = np.array(l)
            upper = np.array(u)

            # 色相が正の値のとき、赤以外のマスク
            if lower[0] >= 0:
                mask = cv2.inRange(hsv, lower, upper)
            
            # 色相が負の値のとき、赤用のマスク
            else:
                h = hsv[:, :, 0]
                s = hsv[:, :, 1]
                v = hsv[:, :, 2]
                mask = np.zeros(h.shape, dtype=np.uint8)
                mask[((h < lower[0]*-1) | h > upper[0]) & (s > lower[1]) & (s < upper[1]) & (v > lower[2]) & (v < upper[2])] = 255

            return cv2.bitwise_and(frame, frame, mask = mask)
        
        # 輪郭取得
        def getContours(img, t, r):
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            ret, thresh = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
            # 一番大きい輪郭を抽出
            contours.sort(key=cv2.contourArea, reverse=True)

            # 一つ以上検出
            if len(contours) > 0:
                for cnt in contours:
                    # 最小外接円を描く
                    (x, y), radius = cv2.minEnclosingCircle(cnt)
                    center = (int(x), int(y))
                    radius = int(radius)

                    if radius > r:
                        radius_frame = cv2.circle(frame, center, radius, (0, 255, 0) , 0)
                        return radius_frame, x, y
                return frame, None, None
            else:
                return frame, None, None
            
        # マスクの最小HSVと最大HSVを指定 ただし赤の場合は最小Hを負の値にする
        # 青マスク H110~150 S45~255 V100~255
        res_blue = getMask([110, 45, 100], [150, 255, 255])

        # 赤マスク H0~10または170~180 S50~255 V200~255
        res_red = getMask([-10, 50, 200], [170, 255, 255])

        # 輪郭取得
        contours_frame_blue, blue_x, blue_y = getContours(res_blue, 80, 10)  #(画像, 明度閾値, 最小半径)
        contours_frame_red, red_x, red_y = getContours(res_red, 50, 10)  #(画像, 明度閾値, 最小半径)

        # 再生
        if blue_x != None and blue_y != None:
            print("青球検出!!\nX: %.2f\tY:%.2f\n" %(blue_x, blue_y))
            cv2.imshow('video', contours_frame_blue)
        elif red_x != None and red_y != None:
            print("赤球検出!!\nX: %.2f\tY:%.2f\n" %(red_x, red_y))
            cv2.imshow('video', contours_frame_red)
        else:
            print("未検出\n")
            cv2.imshow('video', frame)
        # 'q'キーが押されたらループから抜ける
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("-- Exit --")
    camera.release()
    cv2.destroyAllWindows()
    exit()

camera.release()
cv2.destroyAllWindows()