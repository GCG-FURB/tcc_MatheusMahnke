import cv2
import numpy as np

current_img = cv2.imread("./teste.png")
p_img = cv2.imread("./teste.png", cv2.IMREAD_GRAYSCALE)
processed_img = cv2.threshold(p_img, 200, 255, cv2.THRESH_BINARY)[1]

def initialize():
    global current_img
    global processed_img
