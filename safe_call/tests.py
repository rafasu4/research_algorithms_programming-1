import unittest
from safe_call import safe_call

def stam_func(x:int, y:float, z):
    return x+y+z

class TestStringMethods(unittest.TestCase):

    def test_no_error_raise(self):
        self.assertEqual(safe_call(stam_func, x=3, y=7.0, z=2), 12)
        self.assertEqual(safe_call(stam_func, x=1, y=7.4, z=4), 12.4)
        self.assertEqual(safe_call(stam_func, x=0, y=0.0, z=0), 0)

    def test_error_raise(self):
        with self.assertRaises(Exception):
            safe_call(stam_func, x=0, y=0, z=0)
        with self.assertRaises(Exception):
            safe_call(stam_func, x=0, y='0', z=0)
        with self.assertRaises(Exception):
            safe_call(stam_func, x='should fail here', y=0, z=0)
        with self.assertRaises(Exception):
            safe_call(stam_func, x=0)

if __name__ == '__main__':
    unittest.main()