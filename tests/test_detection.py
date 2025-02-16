import unittest
from src.detection.defect_detection import DefectDetector
from src.utils.helpers import load_image

class TestDefectDetector(unittest.TestCase):

    def setUp(self):
        self.detector = DefectDetector()
        self.test_image_path = 'data/raw/test_image.jpg'  # Example path for a test image
        self.image = load_image(self.test_image_path)

    def test_detect_defects(self):
        defects = self.detector.detect_defects(self.image)
        self.assertIsInstance(defects, list)  # Check that the result is a list
        # Additional assertions can be added based on expected defect locations

if __name__ == '__main__':
    unittest.main()