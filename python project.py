# caliculating the shoter angle between the hour and minute hand in an analog clock
def findAngle(hh, mm):
 
    # handle 24-hour notation
    hh = hh % 12
 
    # the position of the hour's hand
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)
 
    # the position of the minute's hand
    m = (mm * 360) // (60)
 
    # calculate the angle difference
    angle = abs(h - m)
 
    # consider the shorter angle and return it
    if angle > 180:
        angle = 360 - angle
 
    return angle
 
 
# Clock Angle Problem
if __name__ == '__main__':
 
    hh = 12
    mm = 00
 
    print(findAngle(hh, mm))