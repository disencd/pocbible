import bible
import constants
import exceptions

class pocbible():
    def __init__(self):
        pass

    def _validate_book_name(self, name) -> bool:
        """

        :param name:
        :return:
        """
        return True if name in constants.BOOKLIST or \
                       name in constants.ABBR_BOOKLIST \
            else False

    def get_number_of_books(self) -> int:
        """
        Get the number of books in Bible
        :return:
        """
        return constants.BOOKLIST.__len__()

    def get_booknames(self) -> list:
        """
        Get the name of books in Bible
        :return:
        """
        return constants.BOOKLIST.__repr__()

    def get_chapter_of_books(self, name:str) -> int:
        """
        Get the chapter of each books
        :param name:
        :return:
        """
        try:
            self._validate_book_name(name)

            _index = constants.BOOKLIST.index(name)

            return constants.CHAPTERSLIST[_index][1]
        except:
            raise exceptions.ErrorHandler(name)
