
import cv2
import torch
import time
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array


# Load a MiDas model for depth estimation
#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)

# Move model to GPU if available
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

# Load transforms to resize and normalize the image
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform


# Open up the video capture from a webcam
#cap = cv2.VideoCapture(0)

#while cap.isOpened():

#    success, img = cap.read()

start = time.time()

img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply input transforms
input_batch = transform(img).to(device)

# Prediction and resize to original resolution
with torch.no_grad():
    prediction = midas(input_batch)

    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

depth_map = prediction.cpu().numpy()

depth_map = cv2.normalize(depth_map, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_64F)


end = time.time()
totalTime = end - start
print(totalTime)
fps = 1 / totalTime

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

depth_map = (depth_map*255).astype(np.uint8)

ret, threshold = cv2.threshold(depth_map, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("threshold", threshold)

#depth_map = threshold
#depth_map = cv2.applyColorMap(depth_map , cv2.COLORMAP_MAGMA)

cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)


cv2.imshow('Image', img)
#cv2.imshow('Depth Map', depth_map)
cv2.waitKey(0)
