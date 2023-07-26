import inspect
import requests

class Endpoint:
    api_uri = "https://api.beehiiv.com/v2"

    def __init__(self, api_key):
        '''init'''
        self.api_key = api_key

    def _craft_url(self, endpoint, params):
        '''make api url'''
        return "{}{}".format(
            self.api_uri,
            endpoint.format(*params),
        )

    def _create_call_headers(self):
        '''create headers'''
        return {
            "Authorization": "Bearer {}".format(self.api_key),
        }

    def _make_call(self, endpoint, params, data=None, method="GET"):
        '''make call api'''
        return requests.request(
            method,
            headers=self._create_call_headers(),
            url=self._craft_url(endpoint, params),
            data=data,
        )

