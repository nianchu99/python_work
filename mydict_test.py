import unittest
from mydict import Dict

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("Start")
    def tearDown(self):
        print("End")
    def test_init(self):
        d = Dict(a=1, b='bowenkei')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'bowenkei')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attribute_error(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()
