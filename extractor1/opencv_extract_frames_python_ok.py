# Extract all frames from a video using Python (OpenCV)
import cv2


video_path = 'C:\\Users\\anton\\Desktop\\teste\\video.mkv'

cap = cv2.VideoCapture(video_path)

img_index = 0

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break
    cv2.imwrite('myphotos' + str(img_index) + '.png', frame)
    img_index += 1

cap.release()
cv2.destroyAllWindows()