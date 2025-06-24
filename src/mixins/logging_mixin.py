from pathlib import Path
import logging
from rich import print

from constants import LOGGING_FILE, LOGGER_INIT_MSG

class LoggingMixin:
    
    def initialize_logger(self, verbose: bool, file_path: Path) -> None:
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        self._verbose = verbose
        
        # File handler 
        
        handler = logging.FileHandler(
            filename = file_path / LOGGING_FILE,
            encoding= 'utf-8'
        )
        handler.setLevel(logging.DEBUG)
        
        # Add handler
        
        self._logger.addHandler(handler)
        self._logger.info(LOGGER_INIT_MSG)
     
    def log(self, message: str) -> str | None:         
        """Logs the given message to the log

        Args:
            message (str): Message to log

        Returns:
            str | None: Message that was logged if is verbose
        """
        
        # NOTE: Assumes initialize_logger() already called
        
        self._logger.info(message)
        
        if self._verbose:
            print(message)