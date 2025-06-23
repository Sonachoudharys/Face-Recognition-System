import cv2 as cv
import face_recognition

# Load known face
known_image = face_recognition.load_image_file(
    r"C:\Users\Anita\Desktop\Shripriti Educational & IT hub\Task-3_Face Recognition System\known_faces\sona.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Start webcam
cam = cv.VideoCapture(0)

if not cam.isOpened():
    print("Camera not working")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Can't receive frame")
        break

    # Resize for faster processing
    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv.cvtColor(small_frame, cv.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces([known_encoding], face_encoding)

        # Scale back up face locations
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # box margin
        margin = 20  # pixels
        top = max(0, top - margin)
        right = min(frame.shape[1], right + margin)
        bottom = min(frame.shape[0], bottom + margin)
        left = max(0, left - margin)

        if matches[0]:
            name = "Sona"
            color = (0, 255, 0)
        else:
            name = "Unknown"
            color = (0, 0, 255)

        # Draw rectangle and label
        cv.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv.FILLED)
        cv.putText(frame, name, (left + 6, bottom - 6), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display window
    cv.imshow('Face Recognition - Press Q to Exit', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
