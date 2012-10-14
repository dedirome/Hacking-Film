import urlparse
import httplib


class HttpException:
    """
    A standard web-specific exception that stores error code and message.

    """

    def __init__(self, http_code, message):
        self.http_code = int(http_code)
        self.message = message

    @property
    def http_code(self):
        return self.http_code

    @property
    def message(self):
        return self.message


class Adapter:
    """
    An adapter class that processes GET calls to APIs.

    """

    def __init__(self, base_url):
        self.base_url = base_url

    @property
    def base_url(self):
        return self.base_url

    @property
    def connection(self):
        return httplib.HTTPConnection(self.base_url)

    def get_path(self, path):
        conn = self.connection
        conn.request("GET", path)
        response = conn.getresponse()
        headers = dict(response.getheaders())

        if (response.status == 200):
            data = response.read()
        elif (response.status in (301, 302)):
            # Recursively follow redirects until there isn't a location header
            if (headers.has_key('location')):
                new_conn, url = self.resolve_http_redirect(conn, headers['location'])

                if (self.base_url in url):
                    url = url[len("http://" + self.base_url):]

                conn = httplib.HTTPConnection(new_conn)
                conn.request("GET", url)
                response = conn.getresponse()

                if (response.status == 200):
                    data = response.read()
        else:
            print response.status, response.reason
            raise HttpException(response.status, response.reason)

        return data


    def resolve_http_redirect(self, conn, url, depth = 0):
        if (depth > 10):
            raise Exception("Redirected " + depth + " times, giving up.")

        parsed_object = urlparse.urlparse(url, allow_fragments = True)
        conn = httplib.HTTPConnection(parsed_object.netloc)
        path = parsed_object.path

        if (parsed_object.query):
            path += '?' + parsed_object.query

        conn.request("HEAD", path)
        response = conn.getresponse()
        headers = dict(response.getheaders())

        if (headers.has_key('location') and headers['location'] != url):
            return self.resolve_http_redirect(conn, headers['location'], depth + 1)
        else:
            return parsed_object.netloc, path
