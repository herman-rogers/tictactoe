import unittest, sys, os

sys.path.append("..")

from lib.datahandler.loadingdata import*

class testIfImagesLoadCorrectly(unittest.TestCase):

    def testImageExists(self):
        image = load_data.loadPng("computer.png")
        self.assertTrue(image)

    def testImageException(self):
        self.failUnlessRaises(SystemExit, load_data.loadPng, "penguine.png")

if __name__ == "__main__":
    unittest.main()
