"""
Unit tests for PHQ9 Screener
"""

import unittest
import responses
from akello.screening.mental_health import PHQ9
from akello.settings import API_URL


class TestPHQ9(unittest.TestCase):
    """
    Unit tests for PHQ9 Screener
    """
    @responses.activate
    def test_phq9_object(self):
        """
        Simple test to load the PHQ9 object
        """
        responses.add(responses.POST, f'{API_URL}/akello-gpt', json={'score': 3}, status=200)
        phq9 = PHQ9(api_token='<token>', account_id='', user_id='')
        phq9.score_screener()
        assert len(phq9.questions) == 9
        assert phq9.score > 0


if __name__ == '__main__':
    unittest.main()
