

import unittest
import tempfile
from unittest.mock import patch
from cpdfkit import CPDFKit, generate_pdf
from cpdfkit.exceptions import (
    InvalidDelayException   
)

import time

class TestDelay(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for storing test output files
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_kit =  CPDFKit()
        self.test_url = "https://codingcow.de"


    def tearDown(self):
        # Clean up the temporary directory
        self.test_dir.cleanup()

    def test_negative_delay_input(self):
        """Test the handling of negative delay inputs in PDF generation.

        This test verifies that an `InvalidDelayException` is raised when 
        the `js_delay` parameter is provided with a negative value, ensuring 
        that the function correctly enforces input validation.
        """       
        with self.assertRaises(InvalidDelayException):
            generate_pdf(
                url_or_path= self.test_url,
                format="A4",
                margin_top=10,
                margin_bottom=10,
                margin_left=10,
                margin_right=10,
                js_delay=-2, # Invalid value
                landscape=False
            )

    def test_invalid_type_delay_input_string(self):
        """Test the handling of string type delay inputs in PDF generation.

        This test verifies that an `InvalidDelayException` is raised when 
        the `js_delay` parameter is provided with a string value, ensuring 
        that the function correctly enforces input validation for types.
        """      
        with self.assertRaises(InvalidDelayException):
            generate_pdf(
                url_or_path= self.test_url,
                format="A4",
                margin_top=10,
                margin_bottom=10,
                margin_left=10,
                margin_right=10,
                js_delay="2", # Invalid value
                landscape=False
            )

    def test_invalid_type_delay_input_float(self):
        """Test the handling of float type delay inputs in PDF generation.

        This test verifies that an `InvalidDelayException` is raised when 
        the `js_delay` parameter is provided with a float value, ensuring 
        that the function correctly enforces input validation for types.
        """                
        with self.assertRaises(InvalidDelayException):
            generate_pdf(
                url_or_path= self.test_url,
                format="A4",
                margin_top=10,
                margin_bottom=10,
                margin_left=10,
                margin_right=10,
                js_delay=0.2, # Invalid value
                landscape=False
            )

    def test_valid_delay_input(self):
        # Test that no error is raised and a valid value does not change in value during the process
        test_kit = CPDFKit()
        delay = test_kit._sanitize_delay(200)
        self.assertIsNotNone(delay, "Delay should be returned")
        self.assertIsInstance(delay, int, "Output should be of type int") 
        self.assertEqual(delay, 200)        

