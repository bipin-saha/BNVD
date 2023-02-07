import cv2
import time


cap = cv2.VideoCapture("C:/Users/ASUS/Downloads/Video/c5.mp4")
fps = int(cap.get(cv2.CAP_PROP_FPS))
save_interval = 1

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame_count += 1
        time_now = time.time()
        if frame_count % round(fps * save_interval) == 0:
            img_path = "C:/Users/ASUS/OneDrive/Desktop/Vehicle DS/SemiSuper/" + str(time_now) + ".jpg"
            cv2.imwrite(img_path, frame)
            print("Saved :" + img_path)
            # optional 
            frame_count = 0

    # Break the loop
    else:
        break

cap.release()
cv2.destroyAllWindows()