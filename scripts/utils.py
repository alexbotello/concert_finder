import requests
import settings


def post_to_discord(json_param):
    """ Post a message to discord channel

    JSON Params
    ------------
    content : str
        The message contents (up to 2000 characters)

    embed : embed object
        Example - {  'embed': {
                         'image': {
                             'url': "http://theimageurlhere"
                          }
                      }
                  }
    """
    resp = requests.post(settings.BASE_URL + '/channels/' +
                         settings.CHANNEL + '/messages', json=json_param,
                         headers={'Authorization': settings.TOKEN})

    if resp.status_code != 200:
        raise ValueError('POST /content/ {}'.format(resp.status_code))
    print("Message posted. ID: {}".format(resp.json()['id']))
