# NYTimes


from requests.exceptions import HTTPError
from bot.news.NYTimes import *
from bot.create_bot import logger

class News():
    """
        News class
    """

    def __init__(self):
        pass

    def getAPI(self, api = "NYT"):

        if api == "NYT":
            return NYTimes().get('home.json')

    def sendMessage(self):
        """
            Send news messages in chat
        """
        
        response = []
        responseAPI = self.getAPI()
        
        for i in range(0, responseAPI['num_results'] - 1):
            response.append(responseAPI[i]['url'])
        
        return response
        