# Step 1: Import ONLY OpenCV (no dlib, no mediapipe needed!)
import cv2

# Step 2: Load OpenCV's built-in Haar Cascade face detection model
# cv2.data.haarcascades automatically finds the path on your computer
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 3: Connect to your webcam
cap = cv2.VideoCapture(0)

while True:
    # Step 4: Read the frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Step 5: Flip the frame so it acts like a mirror
    frame = cv2.flip(frame, 1)

    # Step 6: Convert to grayscale (Haar Cascades require grayscale to work)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 7: Detect faces
    # scaleFactor and minNeighbors help filter out false positives
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Step 8: Loop through all detected faces
    i = 0
    for (x, y, w, h) in faces:
        i += 1
        
        # Calculate bottom-right coordinates
        x1, y1 = x + w, y + h

        # Draw the green rectangle
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        # Put the text above the box
        cv2.putText(frame, 'Face #' + str(i), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Step 9: Display the video window
    cv2.imshow('OpenCV Built-in Face Tracking', frame)

    # Step 10: Press 'q' to quit safely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 11: Release everything
cap.release()
cv2.destroyAllWindows()