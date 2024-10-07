import logging
import os


class Logger():
    """
        Logger class
    """

    def __init__(self, logPath = 'log/'):
        self.logPath = logPath

    def log(self, logClass: str, message: str, level = 'error') -> None:
        """
            Dynamic log to files
        """

        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        logging.basicConfig(
            level    = logging.INFO,
            filename = f"{self.logPath}{logClass}_{level}.log",
            filemode = "a",
            format   = "%(asctime)s [%(levelname)s]: %(message)s"
        )
        getattr(logging, level)(message)
        print(message)
        return
    