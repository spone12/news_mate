# News class

from requests.exceptions import HTTPError
from bot.news.NYTimes import *
from bot.createBot import logger
from bot.keyboards.inline import *
from bot.enums.newsSources import NewsSources

class News():
    """
        News class
    """

    def __init__(self):
        self.keyboard = InlineKeyboard()
        self.newsSources = NewsSources.NEWS_SOURCES.value

    def getAPI(self, section:str, api = "NYT"):

        if api == "NYT":
            return NYTimes().get(section)

    def getSections(self):

        sections = NYTimes().getSections()
        BUTTONS: dict[str, str] = {}
        
        for i, section in enumerate(sections):
            BUTTONS['section_' + str(i)] = section
        
        return self.keyboard.createInlineKeyBoard(3, BUTTONS)
    
    def getSectionById(self, id:int):
        return NYTimes().getSectionById(id)
    
    def getNewsSources(self):
        """
            Get a keyboard to select a news source
        """
        
        newsSources: dict[str, str] = self.newsSources
        return self.keyboard.createInlineKeyBoard(1, newsSources)
        
    def getNews(self, section: str):
        """
            Get news from API
        """
        
        responseAPI = self.getAPI(section)
        NEWS = "<b>{0}</b>\n\n".format(section.capitalize())

        topNews = responseAPI['num_results'] - 1
        if topNews > int(getenv("MAX_NEWS")):
            topNews = int(getenv("MAX_NEWS"))

        for i in range(0, topNews):
            NEWS += "<a href='{0}'>{1}: {2}</a>\n\n".format(responseAPI[i]['url'], (i + 1), responseAPI[i]['title'])
        
        return NEWS
        