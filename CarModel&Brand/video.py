import cv2

video_path = "path_to_video.mp4"
output_dir = "frames_output_dir"

cap = cv2.VideoCapture(video_path)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(f"{output_dir}/frame_{frame_count}.jpg", frame)
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
