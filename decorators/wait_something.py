import time


def filter_dict(d, filter_keys):
    return {key: value for key, value in d.items() if key in filter_keys}


def retry_api(timeout, retry, check):
    def decorator(function):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < retry:
                value = function(*args, **kwargs)
                if isinstance(value, dict):
                    check_values = filter_dict(value, check.keys())
                else:
                    raise TypeError("API Response should be dict type")
                if check_values == check:
                    return value
                else:
                    print(f'Sleeping for {timeout} seconds')
                    time.sleep(timeout)
                    retries += 1
        return wrapper
    return decorator


class MockServer:
    """ Emulates an api given a set of fake responses

    Parameters:
    resp: tuple

    Returns:
    boolean
    """

    def __init__(self, resp):
        self.resp = resp
        self.s = self.generator()

    def generator(self):
        for r in self.resp:
            yield r

    def api(self):
        try:
            return next(self.s)
        except StopIteration as si:
            print(si, f'Exceeded limit of {len(self.resp)} retries')


class MockClient:
    """ Emulates a client calling an api

    Parameters:
    resp: tuple

    Returns:
    boolean
    """

    def __init__(self, broker):
        self.broker = broker

    @retry_api(timeout=1, retry=5, check={'status': 21})
    def get(self):
        return self.broker.api()


re = (
    {'status': 10, 'auth_number': '1234'},
    {'status': 21, 'auth_number': '1234'}
)

s = MockServer(resp=re)
c = MockClient(broker=s)

print(c.get())
