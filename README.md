# Concert Finder
Be automatically notified on your mobile when you're favorite artists/bands are performing in your area

Uses the Bandsintown API to gather your specific band's concert data and a Discord bot to post data
into a Discord channel of your choosing.                              
Information on how to acquire your own Discord bot token can be found [HERE](https://discordapp.com/developers/docs/intro)

Once you have your token it must be entered in settings.py with 'Bot' in front of it.    
Example: 'Bot NgA5MTQ3YnY2ORc0NDE1MTBz.F9Nkww.j3k4YAGtb1-bD7Om9zXYr6wsmVj'

Your Bandsintown API APP ID can be any string of your [choosing](http://www.bandsintown.com/api/authentication)

Find the Discord channel ID by right clicking your chosen text channel in the Discord App and selecting 'Copy ID'

Location string format must be full name of city followed by state abbreviation.    
Ex: 'New York, NY' , 'Austin, TX' , 'Seattle, WA' , 'Orlando, FL'

Be sure to download the Discord App on your smart phone for instant notifications

## Directions
 - Download this repository
 - Change the following settings in settings.py
    - ARTISTS
    - LOCATION
    - ID
    - TOKEN
    - CHANNEL
 - Add a database url to db_connect() in models.py
 - Run loop.py
