# test_modelsynapse.py
"""
Tests for ModelSynapse module.
"""

import unittest
from modelsynapse import ModelSynapse

class TestModelSynapse(unittest.TestCase):
    """Test cases for ModelSynapse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelSynapse()
        self.assertIsInstance(instance, ModelSynapse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelSynapse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
