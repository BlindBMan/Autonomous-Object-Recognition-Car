import cv2
import requests
from io import BytesIO
from PIL import Image
import time
import matplotlib.pyplot as plt
import numpy as np
from darkflow.net.build import TFNet


options = {"model": "cfg/yolo.cfg",
           "load": "darkflow/bin/yolo.weights",
           "threshold": 0.1,
           "gpu": 1.0}

tfnet = TFNet(options)


def send_signal():
    requests.get('http://192.168.1.5:5000/found', timeout=5)


found = 0

while found == 0:
    r = requests.get('http://192.168.1.5:5000/image.jpg', timeout=5)
    img_bytes = Image.open(BytesIO(r.content))
    img = cv2.cvtColor(np.array(img_bytes), cv2.COLOR_RGB2BGR)

    result = tfnet.return_predict(img)
    if len(result) > 0:
        sorted_result = sorted(result, key=lambda i: i['confidence'], reverse=True)
        print(sorted_result[0]['label'])

        for pred in sorted_result:
            if pred['label'] == 'book':
                send_signal()
                found = 1
                break

    # plt.imshow(curr_img)
    # plt.show()

    time.sleep(2)
