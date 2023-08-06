from jhdata.rest_apis.RequestParameters import RequestParameters


class Request:
    def __init__(self, name: str, **kwargs):
        self.request_parameters = RequestParameters(**kwargs)
        self.name = name
        self.response = None
        self.data = None

    def __setattr__(self, key, value):
        if hasattr(self.request_parameters, key):
            setattr(self.request_parameters, key, value)
        else:
            self.__dict__[key] = value
