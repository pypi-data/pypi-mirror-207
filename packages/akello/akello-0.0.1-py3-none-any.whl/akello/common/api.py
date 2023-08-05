"""
API Helper for Akello AI services
"""

import requests


class API():
    """
    API helper for Akello AI services
    """

    def __init__(self, api_token, api_url, account_id, user_id, measurement_type, headers={}):
        headers['Authorization'] = 'Token %s' % api_token
        self.url = api_url
        self.headers = headers
        self.token = api_token
        self.account_id = account_id
        self.user_id = user_id
        self.measurement_type = measurement_type

    def post(self, endpoint, params=None, data=None):
        """
        POST method
        """
        resp = requests.post(f'{self.url}/{endpoint}', json=data, params=params, headers=self.headers, timeout=10)
        assert resp.status_code == 200
        return resp

    def put(self, endpoint, params=None, data=None):
        resp = requests.put(f'{self.url}/{endpoint}', json=data, params=params, headers=self.headers, timeout=10)
        assert resp.status_code == 200
        return resp

    def score_screening_question(self, screening_question):
        """
        Calls akello-gpt to score a question
        """
        resp = self.post(endpoint='akello-gpt', data=screening_question)
        return resp.json()

    def save_screening_question_score(self, screening_question):
        type = f'{self.measurement_type}_{screening_question.key}'
        params = {
            'account_id': self.account_id,
            'measurement_type': type,
            'user_id': self.user_id,
            'data': screening_question.to_json()}
        resp = self.put(endpoint='measurement', params=params)
        assert resp.status_code == 200
        return resp
