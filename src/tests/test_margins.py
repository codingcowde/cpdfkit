import unittest
import tempfile
from unittest.mock import patch
from cpdfkit import CPDFKit, generate_pdf
from cpdfkit.exceptions import (
    InvalidMarginException   
)

class TestMargins(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for storing test output files
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_kit =  CPDFKit()
        self.test_url = "https://codingcow.de"
        

    def tearDown(self):
        # Clean up the temporary directory
        self.test_dir.cleanup()

    def test_invalid_margin_input(self):
        # Test that an error is raised if any of the margins has an invalid value
        with self.assertRaises(InvalidMarginException):
            _ = generate_pdf(
                url_or_path= self.test_url,
                format="A4",
                margin_top=10,
                margin_bottom=-10, # Invalid value
                margin_left=10,
                margin_right=10,
                js_delay=2,
                landscape=False
            )

    def test_invalid_type_margin_input(self):
        # Test that an error is raised if any of the margins has an invalid type
        with self.assertRaises(InvalidMarginException):
            self.test_kit._sanitize_margins("10")            
    
    def test_negative_margin_input(self):
        # Test that an error is raised if any of the margins has negative value
        with self.assertRaises(InvalidMarginException):
            self.test_kit._sanitize_margins(-10)
               
    def test_valid_margin_input(self):
        # Test that no error is raised and a valid value does not change in value during the process
        test_kit = CPDFKit()
        sanitized_margin = test_kit._sanitize_margins(20)
        self.assertIsNotNone(sanitized_margin, "Margin should be returned")
        self.assertIsInstance(sanitized_margin, int, "Output should be of type int or float") 
        self.assertEqual(sanitized_margin, 20)