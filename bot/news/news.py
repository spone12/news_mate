# News class

from requests.exceptions import HTTPError
from bot.news.NYTimes import NYTimes
from bot.createBot import logger
from bot.keyboards.inline import *
from bot.enums.newsSources import NewsSources

class News():
    """
        News class
    """

    def __init__(self):
        self.keyboard = InlineKeyboard()
        self.setNewsSource()
    
    def getNewsSources(self) -> InlineKeyboardMarkup:
        """
            Get a keyboard to select a news source
        """
        
        newsSources: dict[str, str] = NewsSources.NEWS_SOURCES.value
        return self.keyboard.createInlineKeyBoard(1, newsSources)
    
    def setNewsSource(self, source = 'source_NYT') -> bool:
        """
            Set news source
        """
        
        if source not in NewsSources.NEWS_SOURCES.value:
            logger.log(self.__class__.__name__, f"Source '{source}' is not exist!")
            raise Exception(f"Source '{source}' is not exist!")
            return False
        
        if source == 'source_NYT':
            self.source = NYTimes()
        return True
    
    def getSectionButtons(self) -> InlineKeyboardMarkup:
        """
            Get topic buttons
        """
        
        buttons = self.source.sectionButtons()
        return self.keyboard.createInlineKeyBoard(3, buttons)

    def getNews(self, section: str) -> str:
        """
            Get news from API
        """
    
        requestData = self.source.get(section)
        return self.source.getNews(requestData, section)
        