import unittest, responses
from screening.mental_health import PHQ9
from settings import API_URL




class TestPHQ9(unittest.TestCase):

    @responses.activate
    def test_phq9_test(self):
        responses.add(responses.POST, API_URL,
                      json={'score': 3}, status=200)
        phq9 = PHQ9(akello_api_token='<token>')
        phq9.score_screener()
        assert (len(phq9.questions) == 9)
        assert(phq9.score > 0)

if __name__ == '__main__':
    unittest.main()
