from .datetime_tools import day_of_year
from .math_tools import asind, sind, cosd

class EquationTime:
    def __init__(self, date):
        self.date = date
        self.__day_of_year = day_of_year(date)
        self.__equation_time = self.__calculate_equation_of_time()

    def __calculate_equation_of_time(self):
        #ET = 9.87 sin(2B) - 7.53 cos(B) - 1.5 sin(B) [min]
        b = self.__calculate_b()
        return 9.87 * sind(2 * b) - 7.53 * cosd(b) - 1.5 * sind(b)

    def __calculate_b(self):
        # B = (N - 81) * 360/364 
        # N -> Belirtilen tarihin yılın kaçıncı günü olduğudur.
        return (self.__day_of_year - 81) * (360 / 364)

    @property
    def equation_time(self):
        #equation_time için getter metot
        return self.__equation_time
