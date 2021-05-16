import cv2
import mediapipe as mp
import numpy as np
from angle_calculation import angle_cal

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

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
        shoulder_color = (0,0,255)
        
    if elbow_angle >=60:
        elbow_color = (20,255,57)
    else:
        elbow_color = (0,0,255)
        
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
        shoulder_color = (0,0,255)
        
    if elbow_angle >=60:
        elbow_color = (20,255,57)
    else:
        elbow_color = (0,0,255)
        
    return [[shoulder,shoulder_angle,shoulder_color],[elbow,elbow_angle,elbow_color]]
#     return shoulder_angle, elbow_angle

def visualize(arr,frame):
    for i in arr:
        cv2.putText(frame[0], str(i[1]), 
                           tuple(np.multiply(i[0], [int(frame[1]*1.8),int(frame[2]*1.6)]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, i[2], 2, cv2.LINE_AA
                                )
    
def dumbell_press(cap):
    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            frame_height, frame_width, _ = frame.shape
            frame = cv2.resize(frame,(int(frame_width*1.8),int(frame_height*1.6)))
            
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                
                visualize(left(landmarks),[image,frame_width,frame_height])
                visualize(right(landmarks),[image,frame_width,frame_height])
                
            except:
                pass
            
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(41,255,249), thickness=3, circle_radius=5), 
                                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=4, circle_radius=2) 
                                    )               
            
            return image

