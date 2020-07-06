from flask import Flask, render_template, Response, request
from obj_form import ObjForm
from pi_camera import Camera
import serial

app = Flask(__name__)
app.config['SECRET_KEY'] = 'scrtkey'
# pipe = serial.Serial('/dev/rfcomm0', 9600)

obj_to_find = None


def gen_img(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def gen2(camera):
    frame = camera.get_frame()
    yield frame


@app.route('/', methods=['GET', 'POST'])
def index():
    global obj_to_find
    form = ObjForm()
    if form.is_submitted():
        obj_to_find = request.form
        return render_template('autonomous.html', obj_to_find=obj_to_find)
    return render_template('index.html', form=form)


@app.route('/submit', methods=['GET'])
def submit():
    return render_template('autonomous.html', obj_to_find=obj_to_find)


@app.route('/manual')
def manual():
    return render_template('manual.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_img(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/image.jpg')
def image():
    return Response(gen2(Camera()),
                    mimetype='image/jpeg')


@app.route('/start/')
def start():
    print('start')
    # pipe.write('S')
    return '0'


@app.route('/found/')
def found():
    print('found object')
    # pipe.write('X')
    return '0'


@app.route('/left/')
def left():
    # pipe.write('L\n')
    return '0'


@app.route('/right/')
def right():
    # pipe.write('R\n')
    return '0'


@app.route('/forward/')
def forward():
    # pipe.write('F\n')
    return '0'


@app.route('/backward/')
def backward():
    # pipe.write('B\n')
    return '0'


if __name__ == '__main__':
    app.run(threaded=True)
