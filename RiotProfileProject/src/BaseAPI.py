import requests

class BaseAPI:
    def __init__(self, base_url: str, headers: dict = None):
        """
        initializes BaseAPI with given URL and optional headers

        :param base_url: Base URL for API
        :param headers: Optional headers to be used in the API requests
        """
        self.base_url = base_url
        self.headers = headers or {}

        # create session obj to maintain same connection
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def close(self):
        """
        closes the current session when done with API client
        """
        self.session.close()