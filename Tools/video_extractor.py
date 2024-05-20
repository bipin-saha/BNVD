import cv2
import time
import os
from concurrent.futures import ThreadPoolExecutor

def process_video(video):
    cap_path = os.path.join("VideoFiles", video)
    cap = cv2.VideoCapture(cap_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    save_interval = 1

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame_count += 1
            time_now = time.time()
            if frame_count % round(fps * save_interval) == 0:
                img_path = "ExtractedImageFiles/" + str(time_now) + ".jpg"
                cv2.imwrite(img_path, frame)
                print("Saved :" + img_path)
                frame_count = 0
        else:
            break

    cap.release()

if __name__ == "__main__":
    video_list = os.listdir("VideoFiles")
    
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        executor.map(process_video, video_list)
