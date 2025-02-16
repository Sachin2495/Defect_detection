import os
import unittest
from src.utils.helpers import load_image, save_results

class TestHelpers(unittest.TestCase):

    def test_load_image(self):
        # Assuming a test image exists in the data/raw directory
        test_image_path = os.path.join('data', 'raw', 'test_image.jpg')
        image = load_image(test_image_path)
        self.assertIsNotNone(image)
        self.assertTrue(hasattr(image, 'shape'))  # Check if the image has shape attribute

    def test_save_results(self):
        # Test saving results to a file
        results = {'defects': [(100, 200), (150, 250)]}
        results_path = os.path.join('data', 'processed', 'results.json')
        save_results(results, results_path)

        # Check if the results file is created
        self.assertTrue(os.path.exists(results_path))

        # Clean up the created file after test
        if os.path.exists(results_path):
            os.remove(results_path)

if __name__ == '__main__':
    unittest.main()