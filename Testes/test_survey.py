import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""
    def test_store_single_response(self):
        """Testa se uma unica resposta é armazenada de forma correta""" 
        question = "What language did u first learn to speek"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Testa se tres respostas sao armazenadas corretamente"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','spanish','mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()