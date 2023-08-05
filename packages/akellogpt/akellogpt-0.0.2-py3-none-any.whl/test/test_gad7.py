import unittest, responses
from screening.mental_health import GAD7
from settings import API_URL

class TestGAD7(unittest.TestCase):

    @responses.activate
    def test_gad7_test(self):
        responses.add(responses.POST, API_URL,
                      json={'score': 3}, status=200)
        gad7 = GAD7(akello_api_token='<token>')
        gad7.score_screener()
        assert (len(gad7.questions) == 7)
        assert(gad7.score > 0)

if __name__ == '__main__':
    unittest.main()
