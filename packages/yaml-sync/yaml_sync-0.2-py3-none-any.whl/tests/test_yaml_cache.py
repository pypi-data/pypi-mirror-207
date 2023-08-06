import os
import unittest
from yaml_sync import YamlCache

class TestYamlCache(unittest.TestCase):
    def setUp(self):
        self.cache_file = 'test_cache.yaml'
        self.cache = YamlCache(self.cache_file, mode='w', number_lists=True)

        self.ordered_cache_file = 'test_ordered_cache.yaml'
        self.ordered_cache = YamlCache(self.ordered_cache_file, mode='w',
                                       order=['second', 'first', 'third'])

    def tearDown(self):
        if os.path.exists(self.cache_file):
            os.remove(self.cache_file)

        if os.path.exists(self.ordered_cache_file):
            os.remove(self.ordered_cache_file)

    def test_set_and_get_item(self):
        self.cache['hello'] = 'world'
        self.assertEqual(self.cache['hello'], 'world')

    def test_ordered_writing(self):
        self.ordered_cache['first'] = 'hello'
        self.ordered_cache['second'] = 'world'
        self.ordered_cache['third'] = [1, 2, 3]
        self.ordered_cache['fourth'] = 'not in order'

        with open(self.ordered_cache_file, 'r') as f:
            lines = f.readlines()
            lines = [line.rstrip() for line in lines]

        self.assertEqual(lines[0], 'second: world')
        self.assertEqual(lines[1], 'first: hello')
        self.assertEqual(lines[2], 'third:')
        self.assertEqual(lines[3], '- 1')
        self.assertEqual(lines[4], '- 2')
        self.assertEqual(lines[5], '- 3')
        self.assertEqual(lines[6], 'fourth: not in order')

    def test_contains_key(self):
        self.cache['key'] = 'value'
        self.assertTrue('key' in self.cache)
        self.assertFalse('non_existent_key' in self.cache)

        self.cache['key2'] = None
        self.assertFalse('key2' in self.cache)

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