# test_lstmforecaster.py
"""
Tests for LSTMForecaster module.
"""

import unittest
from lstmforecaster import LSTMForecaster

class TestLSTMForecaster(unittest.TestCase):
    """Test cases for LSTMForecaster class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LSTMForecaster()
        self.assertIsInstance(instance, LSTMForecaster)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LSTMForecaster()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
