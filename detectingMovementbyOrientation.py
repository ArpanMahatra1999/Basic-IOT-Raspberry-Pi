from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    # getting orientation by gyroscope
    orientation = sense.get_orientation()

    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']

    print("Pitch = {0}, roll = {1} & yaw = {2}.".format(pitch, roll, yaw))
