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

    global stage

    # Get coordinates_
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
   
    elbow_angle = angle_cal(shoulder, elbow, wrist)

        
    if elbow_angle >=20:
        elbow_color = (20,255,57)
    else:
        elbow_color = (255,0,0)

    if elbow_angle > 160:
        stage = "down"
    if elbow_angle < 30 and stage == "down":
        stage = "up"
        
    return [[elbow,elbow_angle,elbow_color,stage]]

def right(landmarks):

    global stage
    # Get coordinates_
    shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
    # hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

    # shoulder_angle = angle_cal(hip, shoulder, elbow)
    elbow_angle = angle_cal(shoulder, elbow, wrist)
        
    if elbow_angle >=20:
        elbow_color = (20,255,57)
    else:
        elbow_color = (255,0,0)

    if elbow_angle > 160:
        stage = "down"
    if elbow_angle < 30 and stage == "down":
        stage = "up"
        
    return [[elbow,elbow_angle,elbow_color,stage]]
#     return shoulder_angle, elbow_angle

def visualize(strr,arr,image):
    for i in arr:
        cv2.putText(image, str(i[1]), 
                           tuple(np.multiply(i[0], [700,550]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, i[2], 1, cv2.LINE_AA
                                )
        cv2.putText(image, "Current",(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,0), 1, cv2.LINE_AA)
        cv2.putText(image, "Next",(600,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,0), 1, cv2.LINE_AA)
        
        # current
        if strr == "left":
            cv2.putText(image, f'Left:{i[3]}',(10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
        elif strr == "right":
            cv2.putText(image, f'Right:{i[3]}',(10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
        
        #next
        if i[3]=="up":
            nextt = "down"
        elif i[3]=="down":
            nextt = "up"
        if strr == "left":
            cv2.putText(image, f'Left:{nextt}',(600,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)
        elif strr == "right":
            cv2.putText(image, f'Right:{nextt}',(600,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)

    
def bicep_curl(image,pose):       

    results = pose.process(image)
        
    # Recolor back to BGR
    image.flags.writeable = True
    
    blank_image = np.ones((550,700,3), np.uint8)
    # Extract landmarks
    try:
        landmarks = results.pose_landmarks.landmark
        visualize("left",left(landmarks),blank_image)
        visualize("right",right(landmarks),blank_image)
                
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

