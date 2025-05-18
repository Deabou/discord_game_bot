import requests
import os
import steam_web_api


class SteamAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
