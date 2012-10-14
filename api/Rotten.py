import re
from adapter import Adapter


# Rotten Tomatoes API adapter
class Rotten:
    """
    Contains API calls for communicating with the Rotten Tomatoes API.

    """

    # Initializes with Rotten Tomatoes base URL.
    def __init__(self, base_url=u'http://api.rottentomatoes.com/api/public/v1.0/', api_key=u''):
        self.base_url = base_url
        self.api_key = api_key
        self.adapter = Adapter(base_url)

    # Gets/sets the base URL for connecting to the Rotten Tomatoes API.
    @property
    def base_url(self):
        return self.base_url


    # API Methods

    # Gets box office information for movies
    def box_office(self, limit=u'16', country=u'us'):
        path = self.base_url + u'lists/movies/box_office.json?apikey=%s&limit=%s&country=%s' % (self.api_key, limit, country)

        result = self.adapter.get_path(path)

        return result


    # Gets the latest movies in theaters
    def in_theaters(self, page_limit=u'16', page=u'1', country=u'us'):
        path = self.base_url + u'lists/movies/in_theaters.json?apikey=%s&page_limit=%s&page=%s&country=%s' % (self.api_key, page_limit, page, country)
        print path

        result = self.adapter.get_path(path)

        return result


    # Get movie opening information
    def opening(self, limit=u'16', country=u'us'):
        path = self.base_url + u'lists/movies/in_theaters.json?apikey=%s&limit=%s&country=%s' % (self.api_key, limit, country)

        result = self.adapter.get_path(path)

        return result


    # Gets upcoming movies
    def upcoming(self, page_limit=u'16', page=u'1', country=u'us'):
        path = self.base_url + u'lists/movies/in_theaters.json?apikey=%s&page_limit=%s&page=%s&country=%s' % (self.api_key, page_limit, page, country)

        result = self.adapter.get_path(path)

        return result
