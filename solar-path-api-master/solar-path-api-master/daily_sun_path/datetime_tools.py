from datetime import datetime


def string_to_time(str_time):
    """
        HH:MM formatındaki bir stringi datetime.time objesine çevirir.
        :param str_time HH:MM formatında bir string
        :return datetime.time
    """
    return datetime.strptime(str_time, '%H:%M').time()


def string_to_date(str_date):
    """
        DD/MM/YYYY formatındaki bir stringi datetime.date objesine çevirir.
        :param str_date DD/MM/YYYY formatında bir string değer.
        :return datetime.date
    """
    return datetime.strptime(str_date, '%d/%m/%Y').date()


def day_of_year(date_time):
    """
        tarihen yılın kaçıncı gününe denk geldiğini hesaplar.
        :param date_time datetime.datetime tipinde olmalı
        :return int
    """
    return int(date_time.strftime('%j'))


def time_to_seconds(time):
    """
        datetime.time tipindeki bir nesnenin saniye karşılığını verir.
        :param time datetime.time tipinde bir nesne
        :return int
    """
    return time.hour * 3600 + time.minute * 60
