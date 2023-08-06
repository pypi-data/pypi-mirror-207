from unittest import TestCase
from pdfparser import PDFTextExtractor

class TestPDFTextExtractor(TestCase):
   
   extractor = PDFTextExtractor()
   
   def test_extract_text_from_valid_pdf(self):   
      text = self.extractor.extract_texts(["test_data/sample.pdf"])
      self.assertEqual(len(text), 1)
      
   def test_warning_on_empty_pdf(self):
      ...
      
   def test_error_on_corrupted_pdf(self):
      ...