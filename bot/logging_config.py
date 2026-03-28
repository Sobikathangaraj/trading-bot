import logging

def setup_logger():
    logger = logging.getLogger("trading_bot")
    
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("trading_bot.log")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger