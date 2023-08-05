"""
Common classes for screening
"""
import pathlib
import yaml
from yaml import CLoader as Loader
from akellogpt.common.api import API
from akellogpt.settings import API_URL

CURRENT_PATH = str(pathlib.Path(__file__).parent.resolve())


class Screener:
    """
    Screener
    """

    YAML_FILE = None

    def __init__(self, akello_api_token, akello_api_url=API_URL):
        self.score = 0
        self.questions = []
        self.api = API(akello_api_token, akello_api_url)
        self.akello_api_token = akello_api_token

        with open(f'{CURRENT_PATH}/yaml/{self.YAML_FILE}', 'r', encoding="utf-8") as file:
            screener = yaml.load(file, Loader=Loader)
            self.load_question_and_options(screener['questions'])

    def add_question(self, key, question):
        """
        Add a question to the screener
        """

        question = ScreeningQuestion(key, question)
        self.questions.append(question)
        return question

    def load_question_and_options(self, questions):
        """
        Load question and options from a questions object
        """

        for question in questions:
            screening_question = ScreeningQuestion(question['order'],
                                                   question['question'],
                                                   api=self.api)
            for option in question['options']:
                screening_question.add_option(option['name'], option['value'])
            self.questions.append(screening_question)

    def score_screener(self):
        """
        Score the screener
        """

        self.score = sum(question.score_question() for question in self.questions)


    def to_json(self):
        """
        Convert to a JSON object
        """

        return {
            'score': self.score,
            'questions': [question.to_json() for question in self.questions]
        }

class ScreeningQuestion:
    """
    Screening Question
    """

    def __init__(self, key, question, api=None):
        self.api = api
        self.score = 0
        self.key = key
        self.question = question
        self.options = []
        self.responses = []

    def add_option(self, name, value):
        """
        Add an option to the screening question
        """

        option = ScreeningOption(name, value)
        self.options.append(option)

    def add_response(self, response):
        """
        Add a response to the screening question
        """

        self.responses.append(response)

    def score_question(self):
        """
        Score the screening question (API call)
        """
        self.score = self.api.score_screening_question(self.to_json())
        return self.score

    def to_json(self):
        """
        Return the object as a JSON
        """

        return {
            'score': self.score,
            'key': self.key,
            'question': self.question,
            'options': [option.to_json() for option in self.options],
            'responses': self.responses
        }

class ScreeningOption(dict):
    """
    Screening Option
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_json(self):
        """
        Return the object as a JSON
        """
        return {
            'name': self.name,
            'value': self.value
        }
