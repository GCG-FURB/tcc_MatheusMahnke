import globals

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
img_counter = 0


class Vision():
    def run(self):
            camera.capture(rawCapture, format="bgr", use_video_port=True)
            img = cv2.flip(rawCapture.array, 0)
            img = cv2.flip(img, 1)
            globals.current_img = img
            rawCapture.truncate(0)
