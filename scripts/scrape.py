import json
import sys
import time
import requests
import settings
import logging
from sqlalchemy.orm import sessionmaker
from models import Concert, create_concert_table, db_connect
from utils import post_to_discord


# Initialize Database connections
engine = db_connect()

create_concert_table(engine)

Session = sessionmaker(bind=engine)
session = Session()


def find_all_concerts():
    """
    Use BandsinTown API to search for concert events
    """

    for art in settings.ARTISTS:
        URL = settings.BIT_URL + art + '/events/search'

        param = {'app_id': settings.ID, 'api_version': settings.API,
                 'location': settings.LOCATION, 'radius': settings.RADIUS,
                 'format': 'json'}

        resp = requests.get(URL, params=param )

        if resp.status_code != 200:
            raise ApiError('{} response code'.format(resp.status_code))

        # Load JSON data from response
        json_data = json.loads(resp.text)

        old_result_found = 0
        new_results_found = 0
        post_image = 1
        for event in json_data:
            # Query the database to compare current listing to any
            # that already exists
            listing = session.query(Concert).filter_by(c_id=event['id']).first()

            if listing:
                old_result_found += 1

            # If no listing is found
            if listing is None:
                listing = Concert(
                    c_id =event['id'],
                    title=event['title'],
                    datetime=event['formatted_datetime']
                )

                session.add(listing)
                session.commit()
                new_results_found += 1

                if post_image == 1:
                    # Post picture of band/artist to discord channel
                    image = {'embed':
                             {'image':
                              {'url': json_data[0]['artists'][0]['thumb_url']}
                             }
                            }
                    post_to_discord(image)

                # Discord API requires messages to be JSON formatted
                # using 'content' field
                message = {'content': event['title'] + '\n' +
                                      event['formatted_datetime']}
                buffers = {'content': '-' * 60}

                try:
                    post_to_discord(message)
                    time.sleep(1)
                    post_to_discord(buffers)
                    time.sleep(3)
                except Exception as exc:
                    logging.warning('An error occured while posting to discord',
                          sys.exc_info())
                # Change post_image to False to avoid repeated image posts
                post_image -= 1

        if json_data == []:
            logging.info('Found No Results For {}'.format(art))

        if json_data:
            logging.info('Found {} posted result and '
                         '{} new results for {}'.format(old_result_found,
                                                        new_results_found, art))
    logging.info("Scrape was completed")

class ApiError(Exception):
    pass
