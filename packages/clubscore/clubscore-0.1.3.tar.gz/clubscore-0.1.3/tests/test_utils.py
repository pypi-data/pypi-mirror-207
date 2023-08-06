import unittest
from PIL import Image
import os
from clubscore.utils import coloraPNG, diagonal_resize, matchWord, getTeams


class TestUtils(unittest.TestCase):


    def test_matchWord(self):
        s = "Juventus"
        arr = ["Milan", "Inter", "Roma", "Juve"]
        matched_word = matchWord(s, arr)
        self.assertEqual(matched_word, "juve")

    def test_match_not_found(self):
        # Test when a match is not found in the array
        s = "Napoli"
        arr = ["Juventus", "Inter", "Milan", "Roma"]
        with self.assertRaises(Exception):
            matchWord(s, arr)

    def test_match_closest_found(self):
        # Test when a match is not found, but a close match is found
        s = "Napli"
        arr = ["Juventus", "Inter", "Milan", "napoli"]
        self.assertEqual(matchWord(s, arr), "napoli")


class TestImages(unittest.TestCase):
    def test_images_identical(self):
        # Load the two PNG images
        print(os.path)
        img1 = Image.open("base.png")
        img2 = Image.open("base1.png")

        # Assert that the two images have the same size and mode
        self.assertEqual(img1.size, img2.size)
        self.assertEqual(img1.mode, img2.mode)

        # Assert that the pixels in the two images are identical
        self.assertEqual(img1, img2)


if __name__ == '__main__':
    unittest.main()
