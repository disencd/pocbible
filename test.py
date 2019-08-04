import unittest
import pocbible as poc

class PocBibleTest(unittest.TestCase):

    def setUp(self):
        self.poc_obj = poc.pocbible()

    def test_get_booknames(self):
        _names = self.poc_obj.get_booknames()
        print("Test get the book names - {}".format(_names))

    def test_get_number_of_books(self):
        _number = self.poc_obj.get_number_of_books()
        print("Test get the number of book - {}".format(_number))

    def test_get_chapter_of_authors(self):
        _number = self.poc_obj.get_chapter_of_books("John")
        print("Test get the number of chapters of Book John - {}".format(_number))

        _number = self.poc_obj.get_chapter_of_books("Numbers")
        print("Test get the number of chapters of Book Numbers - {}".format(_number))

    @unittest.expectedFailure
    def test_error_get_chapter_of_authors(self):
        _number = self.poc_obj.get_chapter_of_books("Joh")
        print("Test get the number of chapters of Book Joh - {}".format(_number))

if __name__ == '__main__':
    unittest.main()