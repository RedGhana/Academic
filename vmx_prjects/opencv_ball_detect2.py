import cv2
import numpy as np

# camera open
camera = cv2.VideoCapture(0)

# 繰り返し、画像を判定
while True:
    # カメラから画像を入力
    _, frame = camera.read()

    # グレースケール変換
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # med_val = np.median(gray)
    # sigma = 0.33  # 0.33
    # min_val = int(max(0, (1.0 - sigma) * med_val))
    # max_val = int(max(255, (1.0 + sigma) * med_val))

    edge = cv2.Canny(gray, threshold1 = 230, threshold2 = 350)
    # edge = cv2.bitwise_not(edge)

    # ハフ変換を用いた円検出
    # HoughCircles関数を使用して円を検出
    circles = cv2.HoughCircles(edge, 
                            cv2.HOUGH_GRADIENT, 
                            dp=1.8, 
                            minDist=50, 
                            param1=100, 
                            param2=25, 
                            minRadius=0, 
                            maxRadius=50)

    # 検出成功
    if circles is not None:
        # circles変数をfloatからintに変換
        circles = np.uint16(np.around(circles))

        for circle in circles[0, :]:
            # 円周を描画
            cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 255, 0), 3)

            # 中心点を描画
            cv2.circle(frame, (circle[0], circle[1]), 1, (0, 255, 255), 2)
            print("中心点: X: %.02f \tY:%.02f" %(circle[0], circle[1]))
        print("\n\n")
    else:
        print("未検出\n\n")

    cv2.imshow('video', frame)
    # 'q'キーが押されたらループから抜ける
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()