# Main Interface NEWS API

from abc import ABC, ABCMeta, abstractmethod


class NewsAPInterface(ABC):

    @abstractmethod
    def get(self, url: str, params = "", headers = "") -> str: raise NotImplementedError
