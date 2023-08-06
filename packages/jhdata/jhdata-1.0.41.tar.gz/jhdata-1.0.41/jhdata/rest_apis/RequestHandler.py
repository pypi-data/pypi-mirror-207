from concurrent.futures import ThreadPoolExecutor, wait

from jhdata.rest_apis.Request import Request
from jhdata.rest_apis.RequestParameters import RequestParameters


class RequestHandler:
    def __init__(self, parallel_workers=10):
        self.requests = []
        self.request_defaults = RequestParameters()
        self.parallel_workers = parallel_workers

    def add(self, request: Request):
        self.requests.append(request)
        return self

    def execute(self):
        return self.transform(lambda request: request.execute())

    def transform(self, function, timeout=None):
        futures = []

        with ThreadPoolExecutor(max_workers=1) as executor:
            for request in self.requests:
                futures.append(executor.submit(function, request))

        wait(futures, timeout)
        return self
