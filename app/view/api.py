import json
from random import randint

from app import app
from flask import request, make_response
from Database import db
from Database.models import ApiHistory
from Config import Configuration as cfg
from Logger import log
import datetime
from random import randint


@app.route('/api/set', methods=['POST', 'GET'])
def api_insert():
    data = request.get_json()
    if data:
        if data.keys() == cfg.VALID_KEYS:
            log('api_insert', f"Save {data=}...")
            item = ApiHistory(db.get_connection())
            item.new(data['device'], data['key'], data['val'])
            return {'Status': 'OK', 'Data': data}

    log('api_insert', f"Error {data=}")
    return {'Status': 'ERROR', 'Data': data}, 422


@app.route('/api/get/array', methods=['GET'])
def get_array():
    # array = [['date', 'voltage']]
    array = []
    date = datetime.datetime.now()
    for _ in range(randint(10, 30)):
        array.append([str(date.time().strftime("%m.%d.%y at %H:%M:%S")), randint(200, 240)])
        date += datetime.timedelta(seconds=15)
    response = make_response()
    response.headers['Content-type'] = 'application/json'
    response.data = json.dumps(array)
    # response.data = {'array': array}

    print(array)
    return response


@app.route('/api/get', methods=['GET'])
def api_load():
    # data = request.get_json()
    # if data:
    #     if ""
    header = request.headers

    keys = {
        'array': get_array
    }
    if 'key' in request.json.keys():
        key = request.json['key']
        if 'par' in request.json.keys():
            params = request.json['par']

    response = make_response()
    response.status_code = 400
    response.data = " params 'key' or 'par' not found "
    return response


@app.route("/api/set/cookie")
def set_cookie():
    if not request.cookies.get('User-id'):
        res = make_response("Set cookie success")
        res.set_cookie('User-id', str(randint(0, 100)), max_age=60*60)
        return res
    
    return make_response(f"Current User-id: {request.cookies.get('User-id')}")

