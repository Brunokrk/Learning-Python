import unittest
from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
    """Testes para 'name_function.py' """
    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""
        formatted_name = get_formated_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_fisrt_last_midle_name(self):
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""
        formatted_name = get_formated_name('Wolfgang','mozart','aMadeuS')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')


unittest.main()