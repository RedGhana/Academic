import cv2
import numpy as np

# camera open
camera = cv2.VideoCapture(0)

# 繰り返し、画像を判定
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
    def getContours(img, t):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        ret, thresh = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
        
        # med_val = np.median(gray)
        # sigma = 0.33  # 0.33
        # min_val = int(max(0, (1.0 - sigma) * med_val))
        # max_val = int(max(255, (1.0 + sigma) * med_val))

        edge = cv2.Canny(thresh, threshold1 = 230, threshold2 = 350)
        # edge = cv2.bitwise_not(edge)

        # ハフ変換を用いた円検出
        # HoughCircles関数を使用して円を検出
        circles = cv2.HoughCircles(edge, 
                                cv2.HOUGH_GRADIENT, 
                                dp=1.5, 
                                minDist=20, 
                                param1=100, 
                                param2=50, 
                                minRadius=20, 
                                maxRadius=50)
        return circles


    # # マスクの最小HSVと最大HSVを指定 ただし赤の場合は最小Hを負の値にする
    # # 青マスク H110~150 S45~255 V100~255
    # res_blue = getMask([110, 45, 100], [150, 255, 255])

    # 赤マスク H0~30または150~180 S64~255 V0~255
    # 赤マスク H0~10または170~180 S50~255 V200~255
    res_red = getMask([-30, 64, 0], [150, 255, 255])

    # 輪郭取得
    # contours_frame_blue, blue_x, blue_y = getContours(res_blue, 80, 10)  #(画像, 明度閾値, 最小半径)
    circles_red = getContours(res_red, 70)  #(画像, 明度閾値)

    # 再生

    # 検出成功
    if circles_red is not None:
        # circles変数をfloatからintに変換
        circles_red = np.uint16(np.around(circles_red))

        for circle in circles_red[0, :]:
            # 円周を描画
            cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 255, 0), 3)

            # 中心点を描画
            cv2.circle(frame, (circle[0], circle[1]), 1, (0, 255, 255), 2)
            print("中心点: X: %.02f \tY:%.02f" %(circle[0], circle[1]))
        print("\n\n")
        
    else:
        print("未検出\n\n")

    # # if blue_x != None and blue_y != None:
    # #     print("青球検出!!\nX: %.2f\tY:%.2f\n" %(blue_x, blue_y))
    # #     cv2.imshow('video', contours_frame_blue)
    # if red_x != None and red_y != None:
    #     print("赤球検出!!\nX: %.2f\tY:%.2f\n" %(red_x, red_y))
    #     cv2.imshow('video', contours_frame_red)
    # else:
    #     print("未検出\n")
    cv2.imshow('video', frame)

    # 'q'キーが押されたらループから抜ける
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()