import time
import sys
import settings
from scrape import find_all_concerts


if __name__ == "__main__":
    while True:
        print("Starting Scrape Cycle {}".format(time.ctime()))
        try:
            find_all_concerts()
        except KeyboardInterrupt:
            print("Program Exiting....")
        except Exception as exc:
            print('An Error Occured While Scraping:', sys.exc_info())
        else:
            print('Successful Scrape {}'.format(time.ctime()))
            print('\n\n')
        # Every 24 hours
        time.sleep(60 * 1440)
