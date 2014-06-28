from unittest import TestCase
import unittest
from hamcrest import assert_that, contains_string
from fm2md.convert import Converter, read_file


class ConverterTest(TestCase):
    def test_convert_creates_markdown_from_branch_titles(self):
        converter = Converter(read_file('data/OTW-Afternoondemos.mm'))
        (md, script) = converter.convert_map()
        assert_that(md, contains_string('\n\n#Richard Bowman\n\n'))
        assert_that(md, contains_string('\n\n##3d Printed Platform for Microscopy\n\n'))
        assert_that(md, contains_string('\n\nPratap is a year 10 student at the Perse School, Cambridge. \n\n')) ## space!
        assert_that(script, contains_string('cp ../../../Dropbox/rareblog/images/opentechworkshop/josie.jpg ./manuscript/images/\n'))

if __name__ == '__main__':
    unittest.main()
