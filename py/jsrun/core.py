import requests
import base64
import hashlib


class JSRUN:
    def __init__(self,app_id: int,  app_secret: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.__headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    def launch(self, lang:str, code: str):
        data = {
        "appId": self.app_id,
        "sign": hashlib.md5((code + self.app_secret).encode(encoding='UTF-8')).hexdigest(),
        "lang": lang,
        "code": base64.b64encode(code.encode("utf-8")),
    }

        try:
            response = requests.post(
                url='http://jsrun.net/api/run', data=data, headers=self.__headers
            )
        except:
            return None

        res = response.json()

        return res
