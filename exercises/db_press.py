import cv2
import mediapipe as mp
import numpy as np
from exercises.angle_calculation import angle_cal
from mediapipe.python.solutions.pose import PoseLandmark

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

POSE_CONNECTIONS = frozenset([
    (PoseLandmark.RIGHT_SHOULDER, PoseLandmark.LEFT_SHOULDER),
    (PoseLandmark.RIGHT_SHOULDER, PoseLandmark.RIGHT_ELBOW),
    (PoseLandmark.RIGHT_ELBOW, PoseLandmark.RIGHT_WRIST),
    (PoseLandmark.LEFT_SHOULDER, PoseLandmark.LEFT_ELBOW),
    (PoseLandmark.LEFT_ELBOW, PoseLandmark.LEFT_WRIST),
    (PoseLandmark.LEFT_ELBOW, PoseLandmark.LEFT_WRIST),
    (PoseLandmark.RIGHT_ELBOW, PoseLandmark.RIGHT_WRIST),
    (PoseLandmark.LEFT_WRIST, PoseLandmark.LEFT_PINKY),
    (PoseLandmark.LEFT_WRIST, PoseLandmark.LEFT_INDEX),
    (PoseLandmark.LEFT_WRIST, PoseLandmark.LEFT_THUMB),
    (PoseLandmark.RIGHT_WRIST, PoseLandmark.RIGHT_PINKY),
    (PoseLandmark.RIGHT_WRIST, PoseLandmark.RIGHT_INDEX),
    (PoseLandmark.RIGHT_WRIST, PoseLandmark.RIGHT_THUMB),
    (PoseLandmark.LEFT_PINKY, PoseLandmark.LEFT_INDEX),
    (PoseLandmark.RIGHT_PINKY, PoseLandmark.RIGHT_INDEX),
    (PoseLandmark.RIGHT_SHOULDER, PoseLandmark.RIGHT_HIP),
    (PoseLandmark.LEFT_SHOULDER, PoseLandmark.LEFT_HIP),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.LEFT_HIP),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.LEFT_HIP),
    (PoseLandmark.LEFT_HIP, PoseLandmark.LEFT_KNEE),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.LEFT_HIP),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.RIGHT_KNEE),
    (PoseLandmark.LEFT_KNEE, PoseLandmark.LEFT_ANKLE),
    (PoseLandmark.RIGHT_KNEE, PoseLandmark.RIGHT_ANKLE),
    (PoseLandmark.LEFT_ANKLE, PoseLandmark.LEFT_HEEL),
    (PoseLandmark.LEFT_ANKLE, PoseLandmark.LEFT_FOOT_INDEX),
    (PoseLandmark.RIGHT_ANKLE, PoseLandmark.RIGHT_HEEL),
    (PoseLandmark.RIGHT_ANKLE, PoseLandmark.RIGHT_FOOT_INDEX),
    (PoseLandmark.LEFT_HEEL, PoseLandmark.LEFT_FOOT_INDEX),
    (PoseLandmark.RIGHT_HEEL, PoseLandmark.RIGHT_FOOT_INDEX)
])

def left(landmarks):
    
    # Get coordinates_
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

    shoulder_angle = angle_cal(hip, shoulder, elbow)
    elbow_angle = angle_cal(shoulder, elbow, wrist)
    
    if shoulder_angle >=70:
        shoulder_color = (20,255,57)
    else:
        shoulder_color = (255,0,0)
        
    if elbow_angle >=60:
        elbow_color = (20,255,57)
    else:
        elbow_color = (255,0,0)
        
    return [[shoulder,shoulder_angle,shoulder_color],[elbow,elbow_angle,elbow_color]]
#     return shoulder_angle, elbow_angle

def right(landmarks):
    
    # Get coordinates_
    shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
    hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

    shoulder_angle = angle_cal(hip, shoulder, elbow)
    elbow_angle = angle_cal(shoulder, elbow, wrist)
    
    if shoulder_angle >=70:
        shoulder_color = (20,255,57)
    else:
        shoulder_color = (255,0,0)
        
    if elbow_angle >=60:
        elbow_color = (20,255,57)
    else:
        elbow_color = (255,0,0)
        
    return [[shoulder,shoulder_angle,shoulder_color],[elbow,elbow_angle,elbow_color]]

def visualize(arr,image):
    for i in arr:
        cv2.putText(image, str(i[1]), 
                           tuple(np.multiply(i[0], [700,550]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, i[2], 2, cv2.LINE_AA
                                )
    
def dumbbell_press(image,pose):
    ## Setup mediapipe instance        

    results = pose.process(image)
        
    # Recolor back to BGR
    image.flags.writeable = True
    
    blank_image = np.ones((550,700,3), np.uint8)
    # Extract landmarks
    try:
        landmarks = results.pose_landmarks.landmark
                
        visualize(left(landmarks),blank_image)
        visualize(right(landmarks),blank_image)
                
    except:
        pass
            
            # Render detections
    mp_drawing.draw_landmarks(blank_image, results.pose_landmarks, POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(41,255,249), thickness=1, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=3, circle_radius=3) 
                                    )
    mp_drawing.draw_landmarks(image, results.pose_landmarks, POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(41,255,249), thickness=1, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=3, circle_radius=3) 
                                    )            
            
    return image, blank_image


