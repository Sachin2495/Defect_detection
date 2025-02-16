import unittest
from src.preprocessing.image_preprocessing import ImagePreprocessor

class TestImagePreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = ImagePreprocessor()

    def test_preprocess_image(self):
        # Assuming we have a sample image for testing
        sample_image = "path/to/sample/image.jpg"
        processed_image = self.preprocessor.preprocess_image(sample_image)
        
        # Add assertions to verify the processed image
        self.assertIsNotNone(processed_image)
        # Further assertions can be added based on expected output

if __name__ == '__main__':
    unittest.main()