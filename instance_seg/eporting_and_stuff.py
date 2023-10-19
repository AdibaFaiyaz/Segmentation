from ultralytics import YOLO

import cv2

model = YOLO('best.pt')

cap = cv2.VideoCapture("test.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    results = model(frame, conf=0.6)
    annotated_frame = results[0].plot(boxes = False, conf = False, labels = False)
    cv2.imshow('custom', annotated_frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()
