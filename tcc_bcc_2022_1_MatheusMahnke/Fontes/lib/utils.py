import math

def get_yaw_direction(lat, lon, lat_dest, lon_dest, yaw):
    exp_yaw = get_yaw_angle_from_coordinates(lat, lon, lat_dest, lon_dest)
    positive_exp_yaw = radian_to_positive(exp_yaw)
    positive_yaw = radian_to_positive(yaw)
    diff = positive_exp_yaw - positive_yaw
    print("diff:"+str(diff))
    if(diff > 0 and diff < math.pi):
        return 1
    return 0

def radian_to_positive(degree):
    angle = math.fmod(degree, math.pi)
    if (angle < 0):
        angle = angle + (math.pi * 2)
    return angle

def get_yaw_angle_from_coordinates(latitude, longitude, latitude_dest, longitude_dest):
    delta_x = latitude_dest - latitude
    delta_y = longitude_dest - longitude
    result = math.atan2(delta_y, delta_x)
    return result


def is_on_destiny(lat, lon, lat_dest, lon_dest):
    round_value = 5
    lat_rounded = round(lat, round_value)
    lon_rounded = round(lon, round_value)
    dst_lat_rounded = round(lat_dest, round_value)
    dst_lon_rounded = round(lon_dest, round_value)
    print("rounded lat: " + str(lat_rounded))
    print("rounded lon: " + str(lon_rounded))
    print("rounded dst_lat: " + str(dst_lat_rounded))
    print("rounded dst_lon: " + str(dst_lon_rounded))
    if(lat_rounded == dst_lat_rounded and lon_rounded == lon_rounded):
        return True
    return False