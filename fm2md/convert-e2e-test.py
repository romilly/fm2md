from unittest import TestCase
import unittest
from hamcrest import assert_that, contains_string
from fm2md.convert import Converter, read_file, LeanpubWriter


class ConverterTest(TestCase):
    def test_convert_creates_markdown_from_branch_titles(self):
        converter = Converter(read_file('data/OpenTechnologyWorkshop-1.0.1.mm'), LeanpubWriter())
        md = converter.convert_map()
        assert_that(md, contains_string('\n\n#Cambridge Engineering Labs\n\n'))
        assert_that(md, contains_string('I spent a delightful and stimulating day'))
        assert_that(md, contains_string('##Morning talks'))
        assert_that(md, contains_string('###Alex Bradbury'))
        assert_that(md, contains_string('series of 15-minute presentations'))

if __name__ == '__main__':
    unittest.main()
