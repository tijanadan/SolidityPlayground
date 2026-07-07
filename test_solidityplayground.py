# test_solidityplayground.py
"""
Tests for SolidityPlayground module.
"""

import unittest
from solidityplayground import SolidityPlayground

class TestSolidityPlayground(unittest.TestCase):
    """Test cases for SolidityPlayground class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityPlayground()
        self.assertIsInstance(instance, SolidityPlayground)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityPlayground()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
