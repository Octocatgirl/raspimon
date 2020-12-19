from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

s.set_rotation(180)

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (255, 255, 255)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)



def fish00():
  img =[
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, k,
     b, b, b, b, b, b, b, k,
     b, b, b, b, b, b, b, k,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
       ]
  return img

def fish01():
  img = [
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, k,
     b, b, b, b, b, b, k, o,
     b, b, b, b, b, b, k, o,
     b, b, b, b, b, b, k, y,
     b, b, b, b, b, b, b, k,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
       ]
  return img

def fish02():
  img = [
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, k, k,
     b, b, b, b, b, k, o, o,
     b, b, b, b, b, k, o, c,
     b, b, b, b, b, k, y, y,
     b, b, b, b, b, b, k, k,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
         ]
  return img

def fish03():
  img = [
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, k, k, k,
     b, b, b, b, k, o, o, o,
     b, b, b, b, k, o, c, y,
     b, b, b, b, k, y, y, y,
     b, b, b, b, b, k, k, k,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
         ]
  return img
 
def fish04():
  img = [
     b, b, b, b, b, b, b, b,
     b, b, b, b, k, k, k, k,
     b, b, b, k, o, o, o, o,
     b, b, b, k, o, c, y, k,
     b, b, b, k, o, y, y, k,
     b, b, b, b, k, k, k, k,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
         ]
  return img
 
def fish05():
  img = [
     b, b, b, b, b, b, b, b,
     b, b, b, k, k, k, k, k,
     b, b, k, o, o, o, o, o,
     b, b, k, o, c, y, k, y,
     b, b, k, o, y, y, k, y,
     b, b, b, k, k, k, k, k,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
        ]
  return img

def fish06():
  img = [b, b, b, b, b, b, b, b,
         b, b, k, k, k, k, k, k,
         b, k, o, o, o, o, o, o,
         b, k, o, c, y, k, y, o,
         b, k, o, y, y, k, y, y,
         b, b, k, k, k, k, k, k,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish07():
  img = [b, b, b, b, b, b, b, b,
         b, k, k, k, k, k, k, b,
         k, o, o, o, o, o, o, k,
         k, o, c, y, k, y, o, o,
         k, o, y, y, k, y, y, k,
         b, k, k, k, k, k, k, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish08():
  img = [b, b, b, b, b, b, b, b,
         k, k, k, k, k, k, b, b,
         o, o, o, o, o, o, k, b,
         o, c, y, k, y, o, o, k,
         o, y, y, k, y, y, k, b,
         k, k, k, k, k, k, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img
 
def fish09():
  img = [
     b, b, b, b, b, b, b, b,
     k, k, k, k, k, b, b, k,
     o, o, o, o, o, k, b, k,
     c, y, k, y, o, o, k, r,
     y, y, k, y, y, k, b, k,
     k, k, k, k, k, b, b, k,
     b, b, b, b, b, b, b, b,
     b, b, b, b, b, b, b, b
        ]
  return img
 
def fish10():
  img = [b, b, b, b, b, b, b, k,
         k, k, k, k, b, b, k, r,
         o, o, o, o, k, b, k, r,
         y, k, y, o, o, k, r, k,
         y, k, y, y, k, b, k, r,
         k, k, k, k, b, b, k, r,
         b, b, b, b, b, b, b, k,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish11():
  img = [b, b, b, b, b, b, k, b,
         k, k, k, b, b, k, r, k,
         o, o, o, k, b, k, r, k,
         k, y, o, o, k, r, k, b,
         k, y, y, k, b, k, r, k,
         k, k, k, b, b, k, r, k,
         b, b, b, b, b, b, k, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish12():
  img = [b, b, b, b, b, k, b, b,
         k, k, b, b, k, r, k, b,
         o, o, k, b, k, r, k, b,
         y, o, o, k, r, k, b, b,
         y, y, k, b, k, r, k, b,
         k, k, b, b, k, r, k, b,
         b, b, b, b, b, k, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img
 
def fish13():
  img = [b, b, b, b, k, b, b, b,
         k, b, b, k, r, k, b, b,
         o, k, b, k, r, k, b, b,
         o, o, k, r, k, b, b, b,
         y, k, b, k, r, k, b, b,
         k, b, b, k, r, k, b, b,
         b, b, b, b, k, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish14():
  img = [b, b, b, k, b, b, b, b,
         b, b, k, r, k, b, b, b,
         k, b, k, r, k, b, b, b,
         o, k, r, k, b, b, b, b,
         k, b, k, r, k, b, b, b,
         b, b, k, r, k, b, b, b,
         b, b, b, k, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish15():
  img = [b, b, k, b, b, b, b, b,
         b, k, r, k, b, b, b, b,
         b, k, r, k, b, b, b, b,
         k, r, k, b, b, b, b, b,
         b, k, r, k, b, b, b, b,
         b, k, r, k, b, b, b, b,
         b, b, k, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img
 
def fish16():
  img = [
         b, k, b, b, b, b, b, b,
         k, r, k, b, b, b, b, b,
         k, r, k, b, b, b, b, b,
         r, k, b, b, b, b, b, b,
         k, r, k, b, b, b, b, b,
         k, r, k, b, b, b, b, b,
         b, k, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish17():
  img = [k, b, b, b, b, b, b, b,
         r, k, b, b, b, b, b, b,
         r, k, b, b, b, b, b, b,
         k, b, b, b, b, b, b, b,
         r, k, b, b, b, b, b, b,
         r, k, b, b, b, b, b, b,
         k, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish18():
  img = [b, b, b, b, b, b, b, b,
         k, b, b, b, b, b, b, b,
         k, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         k, b, b, b, b, b, b, b,
         k, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def fish19():
  img = [b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img
 
def fish20():
  img = [b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b,
         b, b, b, b, b, b, b, b
         ]
  return img

def runFish():
  images = [fish00, fish01, fish02, fish03, fish04, fish05, fish06, fish07, fish08, fish09, fish10, fish11, fish12, fish13, fish14, fish15, fish16, fish17, fish18, fish19, fish20 ]
  count = 0
  while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.3)
    count += 1

