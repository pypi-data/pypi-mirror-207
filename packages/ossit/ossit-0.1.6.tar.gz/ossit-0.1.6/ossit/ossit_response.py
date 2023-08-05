import json


class OssitResponse:
    def __init__(self, response):
        self.response = response

    def parse_response(self):
        return json.loads(self.response.read().decode("utf-8"))
