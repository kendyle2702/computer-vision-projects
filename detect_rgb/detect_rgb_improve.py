import cv2
import numpy as np

# get video
vid = cv2.VideoCapture(0)

#loop
while True:
    ret, frame = vid.read()
    
    h, w, _ = frame.shape
    
    x1, y1 = w // 3, h // 3
    x2, y2 = w * 2 // 3, h * 2 // 3
    
    roi = frame[y1:y2,x1:x2] 
    
    hsv_image = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    hue_image = hsv_image[:,:,0]
    
    hue_mean = np.mean(hue_image)
    
    h_mean = np.mean(hsv_image[:, :, 0])
    s_mean = np.mean(hsv_image[:, :, 1])
    v_mean = np.mean(hsv_image[:, :, 2])

    if v_mean < 50:
        print("black")
    elif s_mean < 30 and v_mean > 200:
        print("white")
    elif s_mean < 30:
        print("gray")
    elif (0 <= h_mean <= 10) or (h_mean >= 160):
        print("red")
    elif 11 <= h_mean <= 25:
        print("orange")
    elif 26 <= h_mean <= 34:
        print("yellow")
    elif 35 <= h_mean <= 85:
        print("green")
    elif 86 <= h_mean <= 100:
        print("cyan")
    elif 101 <= h_mean <= 130:
        print("blue")
    elif 131 <= h_mean <= 145:
        print("purple")
    elif 146 <= h_mean <= 159:
        print("pink")
    else:
        print("unknown color")

    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()