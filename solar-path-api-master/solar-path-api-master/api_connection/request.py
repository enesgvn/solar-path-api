try:
    from connect import Connect
except:
    from .connect import Connect


class Request:
    def __init__(self, con):
        self.connect = con
        self.result = ""

    def post(self, data):
        self.result = self.connect.request.post(self.connect.URL, data=data)

    def get(self, params):
        self.result = self.connect.request.get(self.connect.URL, params=params)

    def text(self):
        return self.result.text

    def json(self):
        return self.result.json()
