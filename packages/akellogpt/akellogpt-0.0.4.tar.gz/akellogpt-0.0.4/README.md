# akello-gpt
[![PyPI version](https://badge.fury.io/py/akellogpt.svg)](https://badge.fury.io/py/akellogpt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


![Alt text](/banner.jpg "akello-gpt")

# Overview
akello-gpt is a service designed to help developers build engaging patient experience to collect screening information. We do this by implementing a deterministic model designed for healthcare applications. 

# Supported screeners
* **Patient Health Questionnaire-9 (PHQ-9)** 
* **General Anxiety Disorder-7 (GAD7)**
* **Kessler Psychological Distress Scale (K10)**
* **Mood Disorder Questionnaire (MDQ)**
* **The Suicide Behaviors Questionnaire-Revised (SBQ-R)**


# Installation and Setup

Install the python package using pip
```bash
pip install akellogpt
```

Setup
```python
from akellogpt.screening.mental_health import PHQ9
phq9 = PHQ9('<AKELLO_AI_API_TOKEN>')
```

Add responses for the screener
```python
for question in phq9.questions:
    question_number = question['order']    
    question.add_response(patient_responses[question_number])
```

Score the screener and view the score
```python
phq9.score_screener()
print(phq9.score) 
```

# Future work
We will be expanding akello-gpt to support Workflows

# Contributing to akello-gtp
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Added some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request
6. Tests are in akellogpt/test. To run the tests: python setup.py test
