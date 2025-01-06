from dotenv import load_dotenv

import requests
import os

class APITest:

    def __init__(self):
        load_dotenv()

        self.gameName = os.environ.get('gameName')
        self.tagLine = os.environ.get('tagLine')

        #TODO: Find api key automatically
        self.apiKey = os.environ.get('apiKey')

    def get_puuid(self) -> str:
        link = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{}/{}?api_key={}".format(
            self.gameName, self.tagLine, self.apiKey)

        response = requests.get(link)

        return response.json()['puuid']

    # Top 3 Mastery Champs
    def get_top_champs(self) -> dict:
        link = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{}/top?api_key={}".format(
            self.get_puuid(), self.apiKey)
        
        response = requests.get(link)

        return response.json()