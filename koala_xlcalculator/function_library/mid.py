
# Excel reference: https://support.office.com/en-us/article/MID-MIDB-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028


from .excel_lib import KoalaBaseFunction
from ..exceptions import ExcelError
from ..koala_types import XLCell

class Mid(KoalaBaseFunction):
    """"""

    @staticmethod
    def mid(text, start_num, num_chars):
        """"""

        if isinstance(text, XLCell):
            text = str(text.value)
        else:
            text = str(text)

        if len(text) > Mid.CELL_CHARACTER_LIMIT:
            raise ExcelError("#VALUE!", 'text is too long. Is %s needs to be %s or less.' % (len(text), Mid.CELL_CHARACTER_LIMIT))

        if type(start_num) != int:
            raise ExcelError("#VALUE!", '%s is not an integer' % str(start_num))

        if type(num_chars) != int:
            raise ExcelError("#VALUE!", '%s is not an integer' % str(num_chars))

        if start_num < 1:
            raise ExcelError("#VALUE!", '%s is < 1' % str(start_num))

        if num_chars < 0:
            raise ExcelError("#VALUE!", '%s is < 0' % str(num_chars))

        return text[start_num - 1 : start_num - 1 + num_chars]
