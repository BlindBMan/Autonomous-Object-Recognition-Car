import cv2
import requests
from io import BytesIO
from PIL import Image
import time
import matplotlib.pyplot as plt
import numpy as np
from darkflow.net.build import TFNet


options = {"model": "cfg/yolov2-custom.cfg",
           "load": "darkflow/bin/yolov2-custom.weights",
           "threshold": 0.2,
           "gpu": 1.0}
tresh = 0.7

tfnet = TFNet(options)


def send_signal():
    requests.get('http://192.168.1.5:5000/found', timeout=5)


while True:
    r = requests.get('http://192.168.1.2:5000/image.jpg', timeout=5)
    curr_img = Image.open(BytesIO(r.content))
    curr_img_cv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

    result = tfnet.return_predict(curr_img_cv2)
    if len(result) > 0:
        sorted_result = sorted(result, key=lambda i: i['confidence'], reverse=True)
        if sorted_result[0]['confidence'] > tresh:
            print(sorted_result[0]['label'])

        if sorted_result[0]['label'] == 'book':
            send_signal()
            break

    # plt.imshow(curr_img)
    # plt.show()

    time.sleep(2)
