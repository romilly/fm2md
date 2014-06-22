from StringIO import StringIO
from io import BytesIO
from unittest import TestCase
import unittest
from hamcrest import assert_that, contains_string
from lxml import etree

__author__ = 'romilly'


class ConverterTest(TestCase):
    def test_convert_creates_markdown_from_branch_titles(self):
        fm_map_text="""
<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
    <node CREATED="1403324538187" ID="ID_1174925319" LINK="blogging.mm" MODIFIED="1403325128141">
        <node CREATED="1403327396798" ID="ID_1814263954" MODIFIED="1403327399747" TEXT="with friend"/>
        <node CREATED="1403327400238" ID="ID_1765392023" MODIFIED="1403327409522" TEXT="objection overcome"/>
    </node>
</map>
"""
        fm_map = BytesIO(fm_map_text)
        converter = Converter(fm_map)
        md = converter.convert()
        assert_that(md, contains_string('#with friend'))
        assert_that(md, contains_string('#objection overcome'))

# TODO: add support for html links

class Converter():
    def __init__(self, map_file):
        self._map_file = map_file

    def convert_this(self, branch):
        if branch.get('TEXT'):
            self.result.write('#%s\n' % branch.get('TEXT'))

    def convert(self):
        self.result = StringIO()
        fm = etree.parse(self._map_file)
        root = fm.find('node')
        for branch in root.iter():
            self.convert_this(branch)
        return self.result.getvalue()


if __name__ == '__main__':
    unittest.main()