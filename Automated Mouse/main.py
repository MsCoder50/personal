import cv2
import mediapipe as mp
import pyautogui
import threading

# Get screen resolution
screen_width, screen_height = pyautogui.size()

# Set the webcam resolution to match screen resolution
cap = cv2.VideoCapture(0)
cap.set(3, screen_width)
cap.set(4, screen_height)

hand_detector = mp.solutions.hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
drawing_utils = mp.solutions.drawing_utils

index_x, index_y = 0, 0

def process_frames():
    global index_x, index_y
    
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand_landmarks in hands:
                drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                index_finger_landmark = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_landmark = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]

                index_x = int(index_finger_landmark.x * frame_width)
                index_y = int(index_finger_landmark.y * frame_height)
                thumb_x = int(thumb_landmark.x * frame_width)
                thumb_y = int(thumb_landmark.y * frame_height)

                # Move the mouse cursor without sensitivity scaling
                pyautogui.moveTo(index_x, index_y)

        cv2.imshow('Virtual Mouse', frame)

        if cv2.waitKey(10) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

# Run frame processing in a separate thread
frame_thread = threading.Thread(target=process_frames)
frame_thread.start()

while True:
    # Use a sleep to reduce CPU usage
    pyautogui.sleep(0.01)

    # Perform click action with sensitivity scaling
    sensitivity_factor = 0.2
    thumb_y = pyautogui.position().y
    index_y_scaled = int(index_y * sensitivity_factor)
    if abs(index_y_scaled - thumb_y) < 20:
        pyautogui.click()
        pyautogui.sleep(1)
    elif abs(index_y_scaled - thumb_y) < 100:
        pyautogui.moveTo(index_x, index_y_scaled)

    if cv2.waitKey(10) & 0xFF == 27:  # Press 'Esc' to exit
        break
