from flask import Flask, render_template, Response, request
from pyparrot.Bebop import Bebop
import math

app = Flask(__name__)
bebop = Bebop(drone_type="Bebop2", ip_address="192.168.42.1")

def html(content):
   return '<html><head>Dados</head><body>' + content + '</body></html>'

@app.route('/ask')
def ask():
    bebop.ask_for_state_update()
    return Response()

@app.route('/')
def index():
    return html('<p>battery: '+str(bebop.sensors.battery)+'</p>'
                +'<p>lat: '+str(bebop.sensors.sensors_dict["GpsLocationChanged_latitude"])+'</p>'
                +'<p>long: '+str(bebop.sensors.sensors_dict["GpsLocationChanged_longitude"])+'</p>')

@app.route('/connect')
def connect():
    success = bebop.connect(2)
    if(success):
        print("connected")
    else:
        print("fail to connect")
    return Response(success)

@app.route('/disconnect')
def disconnect():
    bebop.disconnect()
    return Response()

@app.route('/takeoff')
def takeoff():
    print("taking off")
    bebop.set_max_altitude(1)
    bebop.safe_takeoff(10)
    return Response()


@app.route('/set-max-altitude')
def set_max_altitude():
    max_altitude = request.args.get('maxAltitude')
    print("max altitude: "+max_altitude)
    bebop.set_max_altitude(max_altitude)
    return Response()

@app.route('/land')
def land():
    print("landing")
    bebop.safe_land(10)
    return Response()

    
@app.route('/force-land')
def force_land():
    print("landing")
    bebop.land()
    return Response()

@app.route('/right')
def right():
    print("right")
    pitch = request.args.get('pitch', 20)
    duration = request.args.get('duration', 0.5)

    bebop.fly_direct(roll=0, pitch=pitch, yaw=0, vertical_movement=0, duration=duration)
    return Response()

@app.route('/left')
def left():
    print('left')
    pitch = request.args.get('pitch', -20)
    duration = request.args.get('duration', 0.5)

    bebop.fly_direct(roll=0, pitch=pitch, yaw=0, vertical_movement=0, duration=duration)
    return Response()

@app.route('/forward')
def forward():
    print('forward')
    roll = request.args.get('roll', 20)
    duration = request.args.get('duration', 0.5)

    bebop.fly_direct(roll=roll, pitch=0, yaw=0, vertical_movement=0, duration=duration)
    return Response()

@app.route('/backward')
def backward():
    print("backward")
    roll = request.args.get('roll', -20)
    duration = request.args.get('duration', 0.5)

    bebop.fly_direct(roll=roll, pitch=0, yaw=0, vertical_movement=0, duration=duration)
    return Response()

@app.route('/emergency')
def emergency():
    print("emergency")
    bebop.emergency_land()
    return Response()


def get_yaw_angle_from_coordinates(x, y, x_dest, y_dest):
  delta_x = x_dest - x
  delta_y = y_dest - y
  result = math.atan2(delta_y, delta_x)
  return result

@app.route('/turn-to-coordinates')
def turn_to_coordinates():
    print("turn to coordinates")
    src_lat = request.args.get('lat')
    src_lon = request.args.get('lon')
    current_lat = 0.0
    current_lon = 0.0
    angle = get_yaw_angle_from_coordinates(current_lat, current_lon, src_lat, src_lon)
    bebop.fly_direct(roll=0, pitch=0, yaw=angle, vertical_movement=0, duration=2)
    return Response()

@app.route('/forward-for-5-seconds')
def forward_for_5_seconds():
    print("forward for 5 seconds")
    bebop.safe_takeoff(2)
    bebop.fly_direct(roll=20, pitch=0, yaw=0, vertical_movement=0, duration=5)
    bebop.safe_land(10)
    return Response()

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")