from StringIO import StringIO
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