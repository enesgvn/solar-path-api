from .Location import Location
from .AST import AST
from .Solar import Solar
from api_connection import api
import consts


def solar_path(data):
    try:
        check_apikey(data['apikey'])
        result = api.http_request(consts.HOST + "/api/apikey-exist",
                                  {"apikey": data['apikey']}, 'post')
        if not result['success']:
            return result

        check_longitude(data['longitude'])
        check_latitude(data['latitude'])
        check_timezone(data['timezone'])
        time = check_time(data['time'])
        date = check_date(data['date'])
        location = Location(data['city_name'], float(data['timezone']), time, date, longitude=float(data['longitude']),
                            latitude=float(data['latitude']))
        ast = AST(location)
        solar = Solar(ast, location.local_latitude)
        result = {
            'success': True,
            'message': location.city_name + ' icin hesaplama basarili',
            'altitude': solar.altitude,
            'azimuth': solar.azimuth
        }

        return result

    except ValueError as err:
        return {'success': False, 'message': err.args[0]}
    except TypeError as err:
        return {'success': False, 'message': err.args[0]}
    except Exception as err:
        return {'success': False,
                'message': err.args[0],
                'link': "https://www.google.com"}


def check_longitude(longitude):
    if not longitude:
        raise ValueError("Longitude(boylam) degeri girilmeli.")
    elif float(longitude) < -180 or float(longitude) > 180:
        raise ValueError("Longitude(boylam) degeri [-180,180] araliginda olmali.")


def check_latitude(latitude):
    if not latitude:
        raise ValueError("Latitude(enlem) degeri girilmeli.")
    elif float(latitude) < -90 or float(latitude) > 90:
        raise ValueError("Latitude(enlem) degeri [-90,90] araliginda olmali.")


def check_timezone(timezone):
    if not timezone:
        raise ValueError("Timezone degeri girilmeli.")
    elif float(timezone) < -12 or float(timezone) > 14:
        raise ValueError("Timezone degeri [-12,14] araliginda olmali.")


def check_time(time):
    if not time:
        import datetime
        now = datetime.datetime.now().time()
        return ":".join([str(now.hour), str(now.minute)])
    return time


def check_date(date):
    if not date:
        import datetime
        now = datetime.datetime.now().date()
        return "/".join([str(now.day), str(now.month), str(now.year)])
    return date


def check_apikey(apikey):
    if not apikey:
        raise ValueError("Api key gerekli")
