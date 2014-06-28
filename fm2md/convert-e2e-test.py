import os
import shutil
from unittest import TestCase
import unittest
from hamcrest import assert_that, contains_string
from fm2md.convert import Converter, read_file, LeanpubReformatter

# As an end-to-end test, this needs to muck about with the file system.:(
def prepare_test_directory(test_dir):
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(os.path.join(test_dir, 'manuscript','images'))


class ConverterTest(TestCase):
    def test_convert_creates_markdown_from_branch_titles(self):
        test_dir = './data/test/'
        prepare_test_directory(test_dir)
        formatter = LeanpubReformatter(test_dir)
        converter = Converter(read_file('data/OTW-Afternoondemos.mm'), formatter)
        converter.convert_map()
        md = formatter.get_md()
        assert_that(md, contains_string('\n\n#Richard Bowman\n\n'))
        assert_that(md, contains_string('\n\n##3d Printed Platform for Microscopy\n\n'))
        assert_that(md, contains_string('\n\nPratap is a year 10 student at the Perse School, Cambridge. \n\n')) ## space!
        script = formatter.get_script()
        assert_that(script, contains_string('cp ../../../Dropbox/rareblog/images/opentechworkshop/josie.jpg ./data/test/manuscript/images/\n'))

if __name__ == '__main__':
    unittest.main()
