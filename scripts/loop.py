import time
import sys
import settings
import logging
from scrape import find_all_concerts


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    while True:
        logging.info("Starting Scrape Cycle {}".format(time.ctime()))
        try:
            find_all_concerts()
        except KeyboardInterrupt:
            logging.warning("Program Exiting....")
        except Exception as exc:
            logging.warning('An Error Occured While Scraping:', sys.exc_info())
        else:
            logging.info('Successful Scrape {}'.format(time.ctime()))
            logging.info('\n\n')
        # Every 24 hours
        time.sleep(60 * 1440)
