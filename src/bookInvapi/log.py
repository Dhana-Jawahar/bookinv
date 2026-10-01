import logging
import logging.handlers
import sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Create HTTP handler
http_handler = logging.handlers.HTTPHandler('','/path',method='GET',secure=True, credentials=('username','password'), context=None) 
http_handler.setLevel(logging.INFO)
logger= logging.getLogger(__name__)
logger.addHandler(console_handler)
logger.addHandler(http_handler)

def log_function(func):
    def logwrapper():
        logger.info(f" Start: {func.__name__}")
        try:
            result = func()
            logger.info(f"Completed: {func.__name__}")
            return result

        except Exception:
            logger.exception(f"Error: {func.__name__}")
            raise
    return logwrapper