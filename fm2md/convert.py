from StringIO import StringIO
from unittest import TestCase
import unittest
from hamcrest import assert_that, contains_string
from html2text import HTML2Text
from lxml import etree

def read_file(name):
    with open(name) as inp:
        result = inp.read()
    return result

# TODO: handle non-ascii chars
# TODO: set sub-head level based on map level
# TODO: Handle hyperlinks
# TODO: Handle images

class ConverterTest(TestCase):
    def test_convert_creates_markdown_from_branch_titles(self):
        converter = Converter(read_file('data/OpenTechnologyWorkshop-1.0.1.mm'))
        md = converter.convert_map()
        assert_that(md, contains_string('\n\n#Cambridge Engineering Labs\n\n'))

def remove_redundant_newlines(text):
    return text.replace("\n\n[\n]*","\n\n")

class Converter():
    def __init__(self, text):
        self.map_text = text
        self.result = StringIO()
        self.html_converter = HTML2Text(out=self.append)

    def append(self, text):
        self.result.write(text)

    def convert_node(self, node):
        if node.get('TEXT'):
            self.result.write('\n\n#%s\n\n' % node.get('TEXT'))
        self.convert_html_in(node)
        if len(node):
            for child in node:
                self.convert_node(child)

    def convert_map(self):
        fm = etree.XML(self.map_text)
        root = fm.find('node')
        for node in root:
            self.convert_node(node)
        return remove_redundant_newlines(self.result.getvalue())

    def convert_html_in(self, node):
        html = node.find('richcontent')
        # first deal with notes
        if html is not None and len(html):
            html_text = etree.tostring(html)
            self.html_converter.handle(html_text)

if __name__ == '__main__':
    unittest.main()