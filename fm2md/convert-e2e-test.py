import os
import shutil
from unittest import TestCase
import unittest
from hamcrest import assert_that, contains_string
from fm2md.convert import Converter

# As an end-to-end test, this needs to muck about with the file system.:(
def prepare_test_directory(test_dir):
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir)


def contents_of(*elements):
    path = os.path.join(*elements)
    with open(path) as file_to_read:
        return file_to_read.read()

# TODO: Add tests for image in right place, image title

class ConverterTest(TestCase):
    def test_convert_creates_markdown_from_branch_titles(self):
        test_dir = './data/test/'
        prepare_test_directory(test_dir)
        shutil.copy('data/OTW-Afternoondemos.mm', 'data/test/OTW-Afternoondemos.mm')
        converter = Converter('data/test/OTW-Afternoondemos.mm')
        converter.convert_map()
        md = contents_of(test_dir, 'manuscript','Chapter0.txt')
        assert_that(md, contains_string('{frontmatter}\n\n#Introduction\n\n'))
        md = contents_of(test_dir, 'manuscript','Chapter1.txt')
        assert_that(md, contains_string('{mainmatter}\n\n#Richard Bowman\n\n'))
        assert_that(md, contains_string('\n\n##3d Printed Platform for Microscopy\n\n'))
        md = contents_of(test_dir, 'manuscript','Chapter5.txt')
        assert_that(md, contains_string('\n\nPratap is a year 10 student at the Perse School, Cambridge. \n\n')) ## space!
        script = contents_of(test_dir, 'copy-images.sh')
        assert_that(script, contains_string('#! /usr/bin/bash\n'))
        assert_that(script, contains_string('cp ../../../Dropbox/rareblog/images/opentechworkshop/josie.jpg data/test/manuscript/images/\n'))

if __name__ == '__main__':
    unittest.main()
