# NYTimes

import requests
from requests.exceptions import HTTPError
from bot.news.newsInterface import *
import json
from os import getenv
import os
from collections import defaultdict
import io

from bot.create_bot import logger

class NYTimes(NewsAPInterface):
    """
        New York Times news
    """
    
    _urlAPI = "https://api.nytimes.com/svc/topstories/v2/{0}?api-key={1}"
    sections = [
        'arts',
        'automobiles',
        'books/review',
        'business',
        'fashion',
        'food',
        'health',
        'home',
        'insider',
        'magazine',
        'movies',
        'nyregion',
        'obituaries',
        'opinion',
        'politics',
        'realestate',
        'science',
        'sports',
        'sundayreview',
        'technology',
        'theater',
        't-magazine',
        'travel',
        'upshot',
        'us',
        'world'
    ]

    def __init__(self):
        self.logger = logger
        self.token = getenv("NYT_TOKEN")

    def checkToken(self):
        """
            Checking API token installation
        """
        
        if not self.token:
            self.logger.log(self.__class__.__name__, f"Token is not filled in .env file")
            raise Exception('Token is not filled in .env file!')
        return True

    def get(self, url: str, params = "", headers = "") -> str:

        if not self.checkToken():
            return False
        
        #return self.responseJsonParse("")

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
            
        return self.responseJsonParse(data)
    
    def responseJsonParse(self, jsonData):
        # __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
        # with io.open(os.path.join(__location__, 'ny.json'), encoding='utf-8') as file:
        #    jsonData = json.load(file)

        if not jsonData:
            return

        newsData = defaultdict(lambda: defaultdict(dict))

        # Main data
        for key in ['num_results', 'last_updated', 'section']:
            newsData[key] = jsonData[key]
        
        # News
        for k, res in enumerate(jsonData['results']):

            # Main news data
            for key in ['title', 'url', 'abstract', 'created_date']:
                newsData[k][key] = res[key]

            # Images
            for kI, image in enumerate(res['multimedia']):
                newsData[k]['images'][kI] = image
            
            if k == 5:
                break ########################### temporarily
        
        return newsData
