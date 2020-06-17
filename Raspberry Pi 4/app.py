from flask import Flask, render_template
# import serial


app = Flask(__name__)
# pipe = serial.Serial('/dev/rfcomm0', 9600)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/left/')
def left():
    print('left')
    # pipe.write('L\n')
    return '0'


@app.route('/right/')
def right():
    print('right')
    # pipe.write('R\n')
    return '0'


@app.route('/forward/')
def forward():
    print('forward')
    # pipe.write('F\n')
    return '0'


@app.route('/backward/')
def backward():
    print('backward')
    # pipe.write('B\n')
    return '0'


if __name__ == '__main__':
    app.run()
