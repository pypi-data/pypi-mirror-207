"""
API Helper for Akello AI services
"""

import requests


class API():
    """
    API helper for Akello AI services
    """

    def __init__(self, token, api_url, headers=None):
        self.url = api_url
        self.headers = headers
        self.token = token

    def post(self, data):
        """
        POST method
        """
        resp = requests.post(self.url, json=data, headers=self.headers, timeout=10)
        assert resp.status_code == 200
        return resp

    def score_screening_question(self, screening_question):
        """
        Calls akello-gpt to score a question
        """
        resp = self.post(screening_question)
        return resp.json()['score']
