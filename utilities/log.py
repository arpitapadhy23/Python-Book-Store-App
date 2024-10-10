import logging
import os

def setup_logger(log_file):

    log_dir = './logs'
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(filename=f'{log_dir}/{log_file}',
                        format='%(asctime)s %(message)s',
                        filemode='a')

    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)
    return logger