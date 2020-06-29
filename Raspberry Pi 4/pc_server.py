import cv2
import requests
from io import BytesIO
from PIL import Image
import time
import matplotlib.pyplot as plt


while True:
    r = requests.get('http://192.168.1.9:5000/image.jpg')
    curr_img = Image.open(BytesIO(r.content))
    plt.imshow(curr_img)
    plt.show()

    time.sleep(1)
