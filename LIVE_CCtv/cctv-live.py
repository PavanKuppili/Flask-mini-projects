from flask import Flask,render_template,Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)      

def cctv_live():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            success, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video')
def video():
    return Response(cctv_live(), mimetype='multipart/x-mixed-replace; boundary=frame')
    

if __name__ == '__main__':
    app.run(debug=True)