from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    if t > 36:
        bg = [0, 100, 0]
        tc = [255, 255, 255]
    else:
        bg = [0, 0, 100]
        tc = [200, 200, 0]

    msg = "Temperature = {0} Pressure = {1} Humidity = {2} .".format(t, p, h)
    sense.show_message(msg, scroll_speed=0.1, text_colour=tc, back_colour=bg)
