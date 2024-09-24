# NYTimes

import requests
from requests.exceptions import HTTPError
from bot.news.newsInterface import *
import json
from os import getenv

from bot.create_bot import logger

class NYTimes(NewsAPInterface):

    _urlAPI = "https://api.nytimes.com/svc/topstories/v2/{0}?api-key={1}"

    def __init__(self):
        self.logger = logger
        self.token = getenv("NYT_TOKEN")
        self.checkToken()

    def checkToken(self):

        if not self.token:
            self.logger.log(self.__class__.__name__, f"Token is not filled in .env file")
            raise Exception('Token is not filled in .env file!')

    def get(self, url: str, params = "", headers = "") -> str:

        formatedUrl = self._urlAPI.format(url, self.token)
        data = ""
        headers = {
            'Accept': 'application/json'
        }

        try:
            request = requests.get(formatedUrl, params = params, headers=headers)
            request.raise_for_status()
        except HTTPError as http_err:
            self.logger.log(self.__class__.__name__, f"HTTP error occurred: {http_err}")
        except Exception as err:
            self.logger.log(self.__class__.__name__, f"Other error occurred: {err}")
        else:
            data = json.loads(request.text)
            print(data)
            
        return data
