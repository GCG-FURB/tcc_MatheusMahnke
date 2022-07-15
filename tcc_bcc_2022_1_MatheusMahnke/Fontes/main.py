from pyparrot.Bebop import Bebop
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import depth_estimation
from vision import *
import globals
from utils import *
import math

bebop = Bebop(drone_type="Bebop2", ip_address="192.168.42.1")

class Server:
    yaw = 0.0
    exp_yaw = 0.0

    lat = 0.0
    lon = 0.0

    #Adicionar coordenadas destino
    lat_dest = -26.747040
    lon_dest = -49.177756

    rounded_yaw = 0
    rounded_yaw_angle = 0

    def rond_and_set_angles(self):
        self.rounded_yaw_angle = round(self.exp_yaw, 1)
        self.rounded_yaw = round(self.yaw, 1)

    def turn_to_coordinates(self):
        expected_yaw_to_print = utils.get_yaw_angle_from_coordinates(self.lat, self.lon, self.lat_dest, self.lon_dest)
        self.exp_yaw = expected_yaw_to_print
        self.rond_and_set_angles()
        while(self.rounded_yaw != self.rounded_yaw_angle):
            direction = utils.get_yaw_direction(self.lat, self.lon, self.lat_dest, self.lon_dest, self.yaw)
            expected_yaw_to_print = utils.get_yaw_angle_from_coordinates(self.lat, self.lon, self.lat_dest, self.lon_dest) # remover
            print("Lat: " + str(self.lat))
            print("Lat: " + str(self.lat_dest) + " esperado")
            print("Lon: " + str(self.lon))
            print("Lon: " + str(self.lon_dest) + " esperado")
            print("yaw: " + str(self.yaw))
            print("yaw: " + str(expected_yaw_to_print) + " esperado")
            print("rounded_yaw: " + str(self.rounded_yaw))
            print("rounded_yaw: " + str(self.rounded_yaw_angle) + " esperado")
            if (direction == 1):
                print("virando pra direita")
                bebop.fly_direct(roll=0, pitch=0, yaw=20, vertical_movement=0, duration=0.5)
            else:
                print("virando pra esquerda")
                bebop.fly_direct(roll=0, pitch=0, yaw=-20, vertical_movement=0, duration=0.5)

            self.rond_and_set_angles()

    def sensors_update(self, args):
        if "GpsLocationChanged_latitude" in bebop.sensors.sensors_dict:
            lat = bebop.sensors.sensors_dict["GpsLocationChanged_latitude"]
            self.lat = lat
        if "GpsLocationChanged_longitude" in bebop.sensors.sensors_dict:
            lon = bebop.sensors.sensors_dict["GpsLocationChanged_longitude"]
            self.lon = lon
        if "AttitudeChanged_yaw" in bebop.sensors.sensors_dict:
            yaw = bebop.sensors.sensors_dict["AttitudeChanged_yaw"]
            self.yaw = yaw


    def run_vision():
        vision = Vision()
        vision.run()
        
    def process_image():
        de = depth_estimation.DepthEstimation()
        de.run()
        
        
    def avoid_to_right():
        print("starting right direction avoid")
        print("getting image")
        run_vision()
        print("processing image")
        process_image()

        img = globals.current_img
        threshold = globals.processed_img

        h, w, channels = img.shape

        high_one_thrid = h // 3

        center_center = threshold[high_one_thrid:high_one_thrid * 2, :]

        non_zero_center = cv2.countNonZero(center_center)
        if(non_zero_center > 1000):
            print("move right")
            bebop.fly_direct(roll=20, pitch=0, yaw=0, vertical_movement=0, duration=5)
            self.avoid_to_right()

    def avoid_to_left():
        print("starting left direction avoid")
        print("getting image")
        run_vision()
        print("processing image")
        process_image()

        img = globals.current_img
        threshold = globals.processed_img

        h, w, channels = img.shape

        high_one_thrid = h // 3

        center_center = threshold[high_one_thrid:high_one_thrid * 2, :]

        non_zero_center = cv2.countNonZero(center_center)
        if(non_zero_center > 1000):
            print("move left")
            bebop.fly_direct(roll=-20, pitch=0, yaw=0, vertical_movement=0, duration=5)
            self.avoid_to_left()

    def run_collision_avoider():
        img = globals.current_img
        threshold = globals.processed_img

        h, w, channels = img.shape

        one_third = w // 3
        left_part = threshold[:, :one_third]
        right_part = threshold[:, one_third * 2:]

        high_one_thrid = h // 3

        center_center = threshold[high_one_thrid:high_one_thrid * 2, :]

        non_zero_center = cv2.countNonZero(center_center)
        print("non_zero_center: " + str(non_zero_center))
        if (non_zero_center > 1000):
            left_count = cv2.countNonZero(left_part)
            print("left_count: " + str(left_count))
            right_count = cv2.countNonZero(right_part)
            print("right_count: " + str(right_count))
            if (left_count < 1000 and left_count <= right_count):
                self.avoid_to_left()
            else:
                self.avoid_to_right()

    def start(self):
        success = bebop.connect(10)
        if (success):
            bebop.set_indoor(is_outdoor=False)
            bebop.set_user_sensor_callback(self.sensors_update, None)
            bebop.ask_for_state_update()
            bebop.safe_takeoff(10)
            bebop.smart_sleep(5)
            while((round(lat, 4) != round(lat_dest, 4))
            and (round(lon, 4) != round(lon_dest, 4))):
                self.turn_to_coordinates()
                print("getting image")
                run_vision()
                print("processing image")
                process_image()
                print("getting avoid direction")
                run_collision_avoider()
                cv2.imwrite('./results/detect-obstacle-raw_img.jpg', globals.current_img)
                cv2.imwrite('./results/detect-obstacle-processed_img.jpg', globals.processed_img)
                bebop.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=10)
                counter = counter + 1
            bebop.safe_land(10)
            bebop.disconnect()


server = Server()
server.start()

