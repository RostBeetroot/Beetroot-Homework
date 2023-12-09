import unittest


from nose.tools import *
from Homework_11 import func_for_task2


class TestPhonebookFunction(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_first_name_enter(self):
        func = func_for_task2.first_name_enter
        self.assertTrue(func)

    def test_create_phonebook(self):
        func = func_for_task2.create_phonebook()
        self.assertIsNone(func)

    def test_creat_data_entries(self):
        numb = '12346852585856456454654'
        func = func_for_task2.creat_data_entries(numb)
        self.assertIsNotNone(func)

    def test_search_on_phone(self):
        numb = '12345678'
        func = func_for_task2.search_on_phone(numb)
        self.assertEqual(func, 'You have entered less than 12 digits')

    def test_search_less_on_phone(self):
        numb = '1234567891234564889'
        func = func_for_task2.search_on_phone(numb)
        self.assertEqual(func, 'You have entered more than 12 digits')

    def test_search_more_on_phone(self):
        numb3 = '440123456798'
        func = func_for_task2.search_on_phone(numb3)
        self.assertEqual(func, [])

    def test_del_on_phone(self):
        numb = '123456789123'
        func = func_for_task2.del_on_phone(numb)
        self.assertIsNone(func)


if __name__ == '__main__':
    unittest.main()
