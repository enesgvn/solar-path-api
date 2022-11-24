try:
    from request import Request
    from connect import Connect
except:
    from .request import Request
    from .connect import Connect


def http_request(url, params, method):
    switcher = {
        "GET": get,
        "POST": post,
        "DELETE": delete,
        "PUT": put,
        "PATCH": patch
    }
    res = switcher.get(method.upper(), invalid)
    return res(url, params)


def get(url, params):
    req = Request(Connect(url))
    req.get(params=params)
    return req.json()


def post(url, data):
    req = Request(Connect(url))
    req.post(data=data)
    return req.json()


def delete(url, params):
    pass


def put(url, params):
    pass


def patch(url, params):
    pass


def invalid(_, __):
    return {'success': False, 'message': 'invalid method name'}


# if __name__ == "__main__":
#     r = http_request("http://localhost/solarpathdatabaseapi/index.php/apikey-exist", {"apikey": "123d"},
#                      'POST')
#     print(r)
