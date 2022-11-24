from .math_tools import *
from .datetime_tools import day_of_year
"""
       Solar Altitude ve Solar Azimuth değerlerini hesaplayan sınıf
       Solar Altitude -> sin(α) = sin(L)sin(δ)+cos(L)cos(δ)cos(h)
               α -> Solar Altitude
               L -> Local Latitude
               δ -> Declination
               h -> Hour Angle
       Solar Azimuth -> sin(z) = cos(δ)sin(h)/cos(α)
               z -> Solar Azimuth
               δ -> Declination
               h -> Hour Angle
               α -> Solar Altitude
"""

class Solar:
    def __init__(self, ast, latitude):
        """
            :param ast AST objesi olmalı
            :param latitude sayı olmalı
        """
        self.ast = ast
        self.latitude = latitude
        self.hour_angle = self.__calculate_hour_angle()
        self.declination = self.__calculate_declination()
        self.altitude = float(format(self.__calculate_altitude(), '.2f'))
        self.azimuth = float(format(self.__calculate_azimuth(), '.2f'))

    def __calculate_hour_angle(self):
        # h = (AST - 12) * 15
        return (self.ast.ast - 12) * 15

    def __calculate_declination(self):
         # δ = 23.45 * sin(360/365 * (284 + N))
         # N -> Yılın günü
         # Yılın herhangi bir günü için derece cinsinden sapmayı hesaplar.
        return 23.45 * sind(360 / 365 * (284 + day_of_year(self.ast.location.date)))

    def __calculate_altitude(self):
        # Güneş ışınları ile yatay düzlem arasındaki açıdır.
        # Neden arcsinus ? Hesaplanan değerin formülde a'ya değil de sin(a)'ya eşit olduğu söylendiğinden
        # bu sin(a)'nın kaç derece olduğunu bulabilmek için arcsin kullanıldı.
        a = sind(self.latitude) * sind(self.declination) + cosd(self.latitude) * cosd(
            self.declination) * cosd(self.hour_angle)
        return asind(a)

    def __calculate_azimuth(self):
        # Kuzey Yarımküre için güneyden veya Güney Yarımküre için kuzeyden itibaren yatay düzlemde ölçülen güneş
        # ışınlarının açısıdır.
        z = cosd(self.declination) * sind(self.hour_angle) / cosd(self.altitude)
        return asind(z)
