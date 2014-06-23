from unittest import TestCase
import unittest
from hamcrest import assert_that, contains_string
from fm2md.convert import Converter, read_file


class ConverterTest(TestCase):
    def test_convert_creates_markdown_from_branch_titles(self):
        converter = Converter(read_file('data/OpenTechnologyWorkshop-1.0.1.mm'))
        md = converter.convert_map()
        assert_that(md, contains_string('\n\n#Cambridge Engineering Labs\n\n'))

if __name__ == '__main__':
    unittest.main()
