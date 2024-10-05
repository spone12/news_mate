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

    def getAPI(self, section:str, api = "NYT") -> str:

        if api == "NYT":
            requestData = NYTimes().get(section)
            return NYTimes().getNews(requestData, section)

    def getSectionButtons(self) -> InlineKeyboardMarkup:
        """
            Get topic buttons
        """

        buttons = NYTimes().sectionButtons()
        return self.keyboard.createInlineKeyBoard(3, buttons)
    
    def getNewsSources(self) -> InlineKeyboardMarkup:
        """
            Get a keyboard to select a news source
        """
        
        newsSources: dict[str, str] = NewsSources.NEWS_SOURCES.value
        return self.keyboard.createInlineKeyBoard(1, newsSources)
        
    def getNews(self, section: str):
        """
            Get news from API
        """
        
        return self.getAPI(section)
    