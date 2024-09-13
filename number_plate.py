# import cv2

# harcascade = "model/Car-number-plate-recognition-using-OpenCV-master\haarcascades"
# cap=cv2.VideoCapture(0)
# cap.set(3, 640) #widht
# cap.set(4, 480) #height
# min_area=500

# while True:
#   success, img = cap.read()

#   plate_cascade=cv2.CascadeClassifier(harcascade)
#   img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   plates = plate_cascade.detectMultiScale(img_gray)
#   for(x, y, w, h) in plates:
#     area=w*h
#     if area>min_area:
#       cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#       cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
#       cv2.imshow("Result", img)
#       if cv2.waitKey(2) & 0xff == ord('9'):
#         break

# import cv2

# harcascade = "model/Car-number-plate-recognition-using-OpenCV-master/haarcascades/haarcascade_russian_plate_number.xml"
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)  # width
# cap.set(4, 480)  # height
# min_area = 500

# # Load the Haar cascade classifier once
# plate_cascade = cv2.CascadeClassifier(harcascade)

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     plates = plate_cascade.detectMultiScale(img_gray)

#     for (x, y, w, h) in plates:
#         area = w * h
#         if area > min_area:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
#             img_roi = img[y:y+h, x:x+w]
#             cv2.imshow("ROI", img_roi)

#     cv2.imshow("Result", img)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Use 'q' to break the loop
#         break

# # Release the camera and destroy all windows
# cap.release()
# cv2.destroyAllWindows()


# import cv2

# # Path to the Haar cascade file
# harcascade = "model/Car-number-plate-recognition-using-OpenCV-master/haarcascades/haarcascade_russian_plate_number.xml"

# # Initialize video capture
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Error: Could not open video capture.")
#     exit()

# # Set width and height
# cap.set(3, 640)  # width
# cap.set(4, 480)  # height
# min_area = 500
# count=0

# # Load the Haar cascade classifier
# plate_cascade = cv2.CascadeClassifier(harcascade)
# if plate_cascade.empty():
#     print("Error: Could not load Haar cascade file.")
#     exit()

# while True:
#     success, img = cap.read()
#     if not success:
#         print("Error: Failed to read frame from camera.")
#         break

#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     plates = plate_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5)

#     for (x, y, w, h) in plates:
#         area = w * h
#         if area > min_area:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
#             img_roi = img[y:y+h, x:x+w]
#             cv2.imshow("ROI", img_roi)

#     cv2.imshow("Result", img)

#     if cv2.waitKey(1) & 0xFF == ord('s'):  # Use 'q' to break the loop
#         #break
#         cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
#     cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
#     cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
#     cv2.imshow("Results", img)
#     cv2.waitKey(500)
#     count += 1

# # Release the camera and destroy all windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
import os

# Path to the Haar cascade file
harcascade = "model/Car-number-plate-recognition-using-OpenCV-master/haarcascades/haarcascade_russian_plate_number.xml"

# Initialize video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

# Set width and height
cap.set(3, 640)  # width
cap.set(4, 480)  # height
min_area = 500
count = 0

# Create directory if it doesn't exist
if not os.path.exists("plates"):
    os.makedirs("plates")

# Load the Haar cascade classifier
plate_cascade = cv2.CascadeClassifier(harcascade)
if plate_cascade.empty():
    print("Error: Could not load Haar cascade file.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to read frame from camera.")
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
            img_roi = img[y:y + h, x:x + w]

            if cv2.waitKey(1) & 0xFF == ord('s'):
                # Save the region of interest as an image file
                cv2.imwrite(f"plates/scanned_img_{count}.jpg", img_roi)
                print(f"Saved: plates/scanned_img_{count}.jpg")
                cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
                cv2.imshow("Results", img)
                cv2.waitKey(500)
                count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Use 'q' to break the loop
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
