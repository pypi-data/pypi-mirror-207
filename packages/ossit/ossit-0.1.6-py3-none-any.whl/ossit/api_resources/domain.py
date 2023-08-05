from ..api_requestor import APIRequestor


class Domain(APIRequestor):
    @classmethod
    def get_domain(cls):
        return cls.get_request('domains/')
