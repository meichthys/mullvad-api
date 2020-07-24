"""Contains the MullvadAPI class"""

import requests


class MullvadAPI:
    """
    An object containing a dictionary representation of data returned by
    the Mullvad API
    """

    def __init__(self):
        self.data = dict()
        self.api_url = "https://am.i.mullvad.net/json"
        self.update()

    def update(self):
        try:
            response = requests.get(self.api_url)
            self.data = response.json()
        except:
            raise MullvadAPIError(
                "Could not fetch Mullvad API data. Check your network connection."
            )


class MullvadAPIError(Exception):
    """Failed to fetch Mullvad API data."""

    pass
