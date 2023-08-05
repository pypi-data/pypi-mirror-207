"""
Collection of supported Mental Health screeners
"""

from akellogpt.screening import Screener


class PHQ9(Screener):
    """
    PHQ9 Screener
    """

    YAML_FILE = 'phq9.yaml'
    name = 'PHQ9'

class GAD7(Screener):
    """
    GAD7 Screener
    """

    YAML_FILE = 'gad7.yaml'
    name = 'GAD7'


class SBQR(Screener):
    """
    SBQR Screener
    """
    YAML_FILE = 'sbq-r.yaml'
    name = 'SBQR'
