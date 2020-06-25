from flask import Flask, render_template, Response
from pi_camera import Camera
import serial

app = Flask(__name__)
pipe = serial.Serial('/dev/rfcomm0', 9600)


def gen_img(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_img(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/left/')
def left():
    pipe.write('L\n')
    return '0'


@app.route('/right/')
def right():
    pipe.write('R\n')
    return '0'


@app.route('/forward/')
def forward():
    pipe.write('F\n')
    return '0'


@app.route('/backward/')
def backward():
    pipe.write('B\n')
    return '0'


if __name__ == '__main__':
    app.run(threaded=True)
