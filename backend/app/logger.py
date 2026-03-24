import logging
import json
from datetime import datetime


class JsonFormatter(logging.Formatter):

    def format(self, record):
        log_record = {
            "time": datetime.now().isoformat(),
            "level": record.levelname,
            "service": "smart_store",
            "message": record.getMessage(),
        }

        return json.dumps(log_record)


logger = logging.getLogger("smart_store_logger")
logger.setLevel(logging.INFO)

#Console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

#File Handler for logging
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

#Logging format
formatter = JsonFormatter()
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

