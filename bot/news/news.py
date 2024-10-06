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
        self.source = 'NYT' 

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
    
    def setNewsSource(self, source: str) -> bool:
        """
            Set news source
        """
        
        if source not in NewsSources.NEWS_SOURCES.value:
            logger.log(self.__class__.__name__, f"Source '{source}' is not exist!")
            raise Exception(f"Source '{source}' is not exist!")
            return False
                
        self.source = source.split('_')[1]
        return True

    def getNews(self, section: str) -> str:
        """
            Get news from API
        """
        
        if self.source == "NYT":
            requestData = NYTimes().get(section)
            return NYTimes().getNews(requestData, section)
        