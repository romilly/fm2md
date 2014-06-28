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

class AbstractReformatter():
    def append_text(self, text):
        raise Exception('My subclass should implement this')

    def add_image(self, image_url):
        raise Exception('My subclass should implement this')

    def get_md(self):
        raise Exception('My subclass should implement this')

    def get_script(self):
        raise Exception('My subclass should implement this')


class LeanpubReformatter(AbstractReformatter):
    def __init__(self):
        self.result = StringIO()
        self.script = StringIO()

    def append_text(self, text):
        self.result.write(text)

    def add_image(self, image_location):
        if image_location.startswith('http:'):
            raise Exception('nonce error')
        self.script.write('cp %s ./manuscript/images/\n' % image_location)

    def get_md(self):
        return self.result.getvalue()

    def get_script(self):
        return self.script.getvalue()


class Converter():
    def __init__(self, xml, writer=LeanpubReformatter()):
        self.map_xml = xml
        self.writer = writer
        self.html_converter = HTML2Text(out=writer.append_text)

    def convert_node(self, node, depth=1):
        if node.get('TEXT'):
            self.writer.append_text('\n\n%s%s\n\n' % (depth*'#', node.get('TEXT')))
        self.convert_html_in(node)
        if node.get('LINK'):
            self.writer.add_image(node.get('LINK'))
        if len(node):
            for child in node:
                self.convert_node(child, depth + 1)

    def get_trimmed_markdown(self):
        return remove_redundant_newlines(self.writer.get_md())

    def convert_map(self):
        fm = etree.XML(self.map_xml)
        root = fm.find('node')
        for node in root:
            self.convert_node(node)
        return (self.get_trimmed_markdown(), self.writer.get_script())

    def convert_html_in(self, node):
        html = node.find('richcontent')
        # first deal with notes
        if html is not None and len(html):
            html_text = etree.tostring(html)
            self.html_converter.handle(html_text)