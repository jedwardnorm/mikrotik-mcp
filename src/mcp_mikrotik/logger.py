import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(module)s - %(funcName)s')
app_logger = logging.getLogger(__name__)
