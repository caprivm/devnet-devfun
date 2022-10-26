import unittest

from improved_json_search import *

class json_search_test(unittest.TestCase):
    """Test module to test search function in 'recursive_json_search.py'"""

    def test_search_found(self):
        """Key should be found, return list should not be empty"""
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        """Key should not be found, showul return an empty list"""
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        """Should return a list"""
        self.assertIsInstance(json_search(key1,data),list)

if __name__ == '__main__':
    unittest.main()