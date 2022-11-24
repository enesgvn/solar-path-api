import math

def sind(degree):
    # aldığı parametreyi derece olarak kabul eden sinus metodu
    return math.sin(math.radians(degree))


def cosd(degree):
    # aldığı parametreyi derece olarak kabul eden cosinus metodu
    return math.cos(math.radians(degree))


def asind(degree):
    # aldığı parametreyi derece olarak kabul eden arcsinus metodu
    return math.degrees(math.asin(degree))


def range_mapping(x, in_min, in_max, out_min, out_max):
    # Bir sayıyı bir aralıktan başka bir aralığa yeniden eşler.
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
