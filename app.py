import cv2
import mediapipe as mp
from database import info_print


mp_hand = mp.solutions.hands.Hands(max_num_hands=2)
draw_util = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)
finger_counter = 0
finger_tips = [8, 12 , 16, 20]
previuos_state, current_state = 0, 0

while True:
    finger_counter = 0

    success, frame = cap.read()
    if not success:
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hand.process(frameRGB)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            landmark = hand.landmark

            for tip in finger_tips:
                if landmark[tip].y < landmark[tip - 2].y:
                    finger_counter += 1

            if landmark[finger_tips[-1]].x < landmark[finger_tips[-1] - 2].x:
                finger_counter += 1

    current_state = finger_counter

    if finger_counter == 5 and current_state != previuos_state:
        info_print(5)
    if finger_counter == 2 and current_state != previuos_state:
        info_print(2)
    if finger_counter == 1 and current_state != previuos_state:
        info_print(1)

    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    previuos_state = current_state

cap.release()
cv2.destroyAllWindows()
