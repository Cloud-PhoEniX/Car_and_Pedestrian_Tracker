import cv2

video = cv2.VideoCapture('C:\\Users\\arnab\\Videos\\Captures\\Tesla.mp4')
classifier_file = 'C:\\Users\\arnab\\Downloads\\cars_detector.xml'

car_tracker = cv2.CascadeClassifier(classifier_file)

pedestrian_tracker_file =('C:\\Users\\arnab\\Downloads\\haarcascade_fullbody.xml')
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

while True:
    (read_successful, frame) = video.read()

    if read_successful:
        grayScaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    car = car_tracker.detectMultiScale(grayScaled_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(grayScaled_frame)

    for (x, y, w, h) in car:  # constructing a rectangular shape to locate the car
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    for (x, y, w, h) in pedestrian:  # constructing a rectangular shape to locate the car
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('Arnab Car Detector', frame)  # Displaying the image
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
print("code complete")