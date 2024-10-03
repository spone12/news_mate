# News class

from requests.exceptions import HTTPError
from bot.news.NYTimes import *
from bot.create_bot import logger
from bot.keyboards.inline import *

class News():
    """
        News class
    """

    def __init__(self):
        self.keyboard = InlineKeyboard()

    def getAPI(self, api = "NYT"):

        if api == "NYT":
            return NYTimes().get('home.json')

    def getSections(self):

        sections = NYTimes().getSections()
        BUTTONS: dict[str, str] = {}
        
        for i, section in enumerate(sections):
            BUTTONS['section_' + str(i)] = section
        
        return self.keyboard.createInlineKeyBoard(3, BUTTONS)
    
    def getSectionById(self, id:int):
        return NYTimes().getSectionById(id)
        

    def sendMessage(self):
        """
            Send news messages in chat
        """
        
        responseAPI = self.getAPI()
        #print(responseAPI)
        BUTTONS: dict[str, str] = {}

        topNews = responseAPI['num_results'] - 1
        if topNews > 5:
            topNews = 5

        for i in range(0, topNews):
            BUTTONS['news_' + str(i + 1)] = responseAPI[i]['title']
        
        return self.keyboard.createInlineKeyBoard(2, BUTTONS)
        