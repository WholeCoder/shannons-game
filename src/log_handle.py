import logging

def get_logger(name: str, level: int = logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel

    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger