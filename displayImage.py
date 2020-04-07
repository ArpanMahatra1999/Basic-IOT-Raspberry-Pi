from sense_hat import SenseHat

sense = SenseHat()
v = (148, 0, 211)
i = (75, 0, 130)
b = (0, 0, 255)
g = (0, 255, 0)
y = (255, 255, 0)
o = (255, 127, 0)
r = (255, 0, 0)
e = (0, 0, 0)

image = [e, e, v, v, v, v, e, e,
         i, i, i, i, b, b, b, b,
         g, g, g, g, g, g, g, g,
         g, g, g, g, g, g, g, g,
         y, y, y, y, o, o, o, o,
         y, y, y, y, o, o, o, o,
         r, r, r, r, r, r, r, r,
         i, b, i, b, i, b, i, b]

sense.set_pixels(image)
