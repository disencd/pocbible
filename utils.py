import bible
import constants

def getverses(book_index, chapter_index):
    """

    :param book_index:
    :param chapter_index:
    :return:
    """

    for val in constants.INDICES:
        if book_index is val[0] or ((book_index - 1) is val[0]):
            if val[1] is chapter_index:
                print(val[2])

