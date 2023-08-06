import os
import unittest
from yaml_sych.cache import YamlCache

class TestYamlCache(unittest.TestCase):
    def setUp(self):
        self.cache_file = 'test_cache.yaml'
        self.cache = YamlCache(self.cache_file, mode='w', number_lists=True)

    def tearDown(self):
        if os.path.exists(self.cache_file):
            os.remove(self.cache_file)

    def test_set_and_get_item(self):
        self.cache['hello'] = 'world'
        self.assertEqual(self.cache['hello'], 'world')

    def test_contains_key(self):
        self.cache['key'] = 'value'
        self.assertTrue('key' in self.cache)
        self.assertFalse('non_existent_key' in self.cache)

    def test_list_conversion(self):
        example_list = [1, 2, 3]
        self.cache['list'] = example_list
        retrieved_value = self.cache['list']
        self.assertIsInstance(retrieved_value, dict)
        self.assertEqual(retrieved_value, {0: 1, 1: 2, 2: 3})

    def test_read_only_mode(self):
        self.cache['key'] = 'value'
        read_only_cache = YamlCache(self.cache_file, mode='r')
        self.assertEqual(read_only_cache['key'], 'value')
        with self.assertRaises(ValueError):
            read_only_cache['key'] = 'new_value'

    def test_write_mode(self):
        self.cache['key'] = 'value'
        write_cache = YamlCache(self.cache_file, mode='w')
        self.assertFalse('key' in write_cache)

if __name__ == '__main__':
    unittest.main()