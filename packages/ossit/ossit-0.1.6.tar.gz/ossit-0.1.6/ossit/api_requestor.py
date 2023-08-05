import http.client
from abc import ABC

from app import ossit


class APIRequestor(ABC):
    domain_key = ossit.domain_key
    base_url = ossit.base_url
    version = ossit.version

    @classmethod
    def create_connection(cls):
        connection = http.client.HTTPSConnection(cls.base_url)
        connection.putheader("Authorization", f"Bearer {cls.domain_key}")
        return connection

    @classmethod
    def get_request(cls, path, query=""):
        connection = cls.create_connection()
        connection.request("GET", f"/api/{path}?{query}")
        return ossit.OssitResponse(connection.getresponse()).parse_response()

    @classmethod
    def post_request(cls, path, query, body):
        connection = cls.create_connection()
        connection.request("POST", f"/api/{path}?{query}", body)
        return ossit.OssitResponse(connection.getresponse()).parse_response()



