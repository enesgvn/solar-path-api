from flask import Flask, request, redirect
from daily_sun_path import dsp
from api_connection import api
from json import dumps
import consts

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return {'success': False, 'message': 'Sayfa bulunamadi.', 'code': 404}, 404


@app.route('/')
def index():
    #api dokümantasyonuna yönlendir.
    return redirect("https://documenter.getpostman.com/view/12721915/TWDdiYeE", code=302)


@app.route('/api/v1/solar-path', methods=['GET'])
def sun_path():
    data = {
        'apikey': request.args.get('apikey') if request.args.get('apikey') else None,
        'longitude': request.args.get('longitude') if request.args.get('longitude') else None,
        'latitude': request.args.get('latitude') if request.args.get('latitude') else None,
        'city_name': request.args.get('city') if request.args.get('city') else "none",
        'timezone': request.args.get('timezone') if request.args.get('timezone') else None,
        'time': request.args.get('time') if request.args.get('time') else None,
        'date': request.args.get('date') if request.args.get('date') else None
    }
    response = dsp.solar_path(data)

    log_data = {'apikey': dumps(data['apikey']), 'data': dumps(data), 'result': dumps(response)}
    _ = api.http_request(consts.HOST + "/api/request-logs", log_data, 'post')

    return response
