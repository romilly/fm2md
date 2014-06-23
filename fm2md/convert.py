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

class AbstractWriter():
    def append_text(self, text):
        raise Exception('My subclass should implement this')

    def add_image(self, image_url):
        raise Exception('My subclass should implement this')

    def get_value(self):
        raise Exception('My subclass should implement this')


class LeanpubWriter(AbstractWriter):
    def __init__(self):
        self.result = StringIO()

    def append_text(self, text):
        self.result.write(text)

    def add_image(self, image_url):
        pass

    def get_value(self):
        return self.result.getvalue()


class Converter():
    def __init__(self, xml, writer):
        self.map_xml = xml
        self.writer = writer
        self.html_converter = HTML2Text(out=writer.append_text)

    def convert_node(self, node, depth=1):
        if node.get('TEXT'):
            self.writer.append_text('\n\n%s%s\n\n' % (depth*'#', node.get('TEXT')))
        self.convert_html_in(node)
        if len(node):
            for child in node:
                self.convert_node(child, depth + 1)

    def convert_map(self):
        fm = etree.XML(self.map_xml)
        root = fm.find('node')
        for node in root:
            self.convert_node(node)
        return remove_redundant_newlines(self.writer.get_value())

    def convert_html_in(self, node):
        html = node.find('richcontent')
        # first deal with notes
        if html is not None and len(html):
            html_text = etree.tostring(html)
            self.html_converter.handle(html_text)