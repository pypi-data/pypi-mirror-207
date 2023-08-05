import requests
from settings import API_URL


class API(object):

    def __init__(self, token, headers):
        self.url = API_URL
        self.headers = headers

    def post(self, data):
        resp = requests.post(self.url, json=data, headers=self.headers)
        assert (resp.status_code == 200)
        return resp

    def score_screening_question(self, screening_question):
        resp = self.post(screening_question)
        return resp.json()['score']
