from flask import Flask, render_template, Response
import cv2
from exercises.dumbell_press import dumbell_press
#Initialize the Flask app
app = Flask(__name__)

def gen_frames():  
    cap = cv2.VideoCapture(0)
    while True:
        # success, frame = cap.read()  # read the camera frame
        # if not success:
        #     break
        # else:

        frame = dumbell_press(cap)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)