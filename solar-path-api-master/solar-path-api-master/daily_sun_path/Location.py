from .datetime_tools import string_to_date, string_to_time

class Location:
    def __init__(self, city_name, timezone, time, date, latitude, longitude):
        self.city_name = city_name
        self.time_zone = timezone
        self.time = string_to_time(time)
        self.date = string_to_date(date)
        self.local_latitude = latitude
        self.local_longitude = longitude
        self.standard_longitude = self.time_zone * 15.0
