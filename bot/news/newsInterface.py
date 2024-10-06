# Main Interface NEWS API

from abc import ABC, ABCMeta, abstractmethod


class NewsAPInterface(ABC):

    @abstractmethod
    def get(self, url: str, params = "", headers = "") -> str: raise NotImplementedError

    @abstractmethod
    def getSections(self) -> list: raise NotImplementedError

    @abstractmethod
    def sectionButtons(self) -> dict: raise NotImplementedError

    @abstractmethod
    def getNews(self, data: str, section: str) -> str: raise NotImplementedError
    