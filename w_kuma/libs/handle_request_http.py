import requests
from w_kuma.secure_config import ZOOMEYE_HEADERS


class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        try:
            response = requests.get(url, headers=ZOOMEYE_HEADERS)
        except Exception as e:
            return {} if return_json else ""
        else:
            if response.status_code != 200:
                return {} if return_json else ""
            return response.json() if return_json else response.text
