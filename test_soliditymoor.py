# test_soliditymoor.py
"""
Tests for SolidityMoor module.
"""

import unittest
from soliditymoor import SolidityMoor

class TestSolidityMoor(unittest.TestCase):
    """Test cases for SolidityMoor class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityMoor()
        self.assertIsInstance(instance, SolidityMoor)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityMoor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
