import os
from pathlib import Path


LOGGING_FILE = "organizer.log"
LOGGER_INIT_MSG = "\nOrganizer Started\n"
JSON_ENV = "FD_JSON_DIR" 
JSON_DIR = Path().home() / Path(os.getenv(JSON_ENV, "")).expanduser()