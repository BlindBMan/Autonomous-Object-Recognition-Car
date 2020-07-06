import cv2
import requests
from io import BytesIO
from PIL import Image
import time
import numpy as np
from darkflow.net.build import TFNet


options = {"model": "cfg/yolov2-custom.cfg",
           "load": "darkflow/bin/yolov2-custom.weights",
           "threshold": 0.2,
           "gpu": 1.0}
tresh = 0.7

tfnet = TFNet(options)


def send_signal():
    requests.get('http://192.168.1.2:5000/found', timeout=5)


def main():
    obj_list = open('labels.txt', 'r').read().split('\n')
    subm = requests.get('http://192.168.1.2:5000/submit', timeout=5)
    while subm.status_code != 200:
        time.sleep(1)
        subm = requests.get('http://192.168.1.2:5000/submit', timeout=5)
    txt = subm.text
    target = [i for i in obj_list if txt.find(i) > 0][0]
    print(target)
    obj_detect(target)


def obj_detect(target):
    found = 0
    while found == 0:
        r = requests.get('http://192.168.1.2:5000/image2.jpg', timeout=5)
        if r.status_code == 200:
            curr_img = Image.open(BytesIO(r.content))
            curr_img_cv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

            result = tfnet.return_predict(curr_img_cv2)
            if len(result) > 0:
                sorted_result = sorted(result, key=lambda i: i['confidence'], reverse=True)
                if sorted_result[0]['confidence'] > tresh:
                    print(sorted_result[0]['label'])

                if sorted_result[0]['label'] == target:
                    send_signal()
                    found = 1

        time.sleep(2)


if __name__ == '__main__':
    main()
