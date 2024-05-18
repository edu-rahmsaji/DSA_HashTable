import unittest
from src.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_put(self):
        self.assertTrue(self.hash_table.put("hello", "world"))
    
    def test_get(self):
        self.hash_table.put("hello", "world")
        self.assertEqual(self.hash_table.get("hello"), "world")
    
    def test_remove(self):
        self.hash_table.put("hello", "world")
        self.assertTrue(self.hash_table.remove("hello"))
    
    def test_contains(self):
        self.hash_table.put("hello", "world")
        self.assertTrue(self.hash_table.contains("hello"))
        self.assertFalse(self.hash_table.contains("no"))

    def test_size(self):
        self.assertTrue(self.hash_table.size() == 0)
        self.hash_table.put("hello", "world")
        self.assertTrue(self.hash_table.size() == 1)

    def test_is_empty(self):
        self.assertTrue(self.hash_table.is_empty())
        self.hash_table.put("hello", "world")
        self.assertFalse(self.hash_table.is_empty())

    def test_keys(self):
        self.assertListEqual(self.hash_table.keys(), [])
        self.hash_table.put("hello", "world")
        self.assertListEqual(self.hash_table.keys(), ["hello"])

    def test_values(self):
        self.assertListEqual(self.hash_table.values(), [])
        self.hash_table.put("hello", "world")
        self.assertListEqual(self.hash_table.values(), ["world"])
