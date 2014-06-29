from StringIO import StringIO
import os
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


class FileWriter():
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.result = StringIO()
        self.script = StringIO()

    def write(self, text):
        self.result.write(text)

    def append_to_script(self, text):
        self.script.write(text)

    def close(self):
        with open(os.path.join(self.target_dir, 'manuscript','Chapter1.txt'),'w') as ofile:
            ofile.write(self.result.getvalue())
        with open(os.path.join(self.target_dir, 'copy-images.sh'),'w') as ofile:
            ofile.write(self.script.getvalue())

class LeanpubReformatter():
    def __init__(self, target_dir, writer = None):
        self.target_dir = target_dir
        if writer is None:
            self.writer = FileWriter(target_dir)
        else:
            self.writer = writer


    def append_text(self, text):
        self.writer.write(text)

    def add_image(self, image_location):
        if image_location.startswith('http:'):
            raise Exception('nonce error')
        self.writer.append_to_script('cp %s %s\n' % (
            image_location, os.path.join(self.target_dir, 'manuscript', 'images/')))

    def close(self):
        self.writer.close()


class Converter():
    def __init__(self, xml, formatter=LeanpubReformatter('.')):
        self.map_xml = xml
        self.formatter = formatter
        self.html_converter = HTML2Text(out=formatter.append_text)

    def convert_node(self, node, depth=1):
        if node.get('TEXT'):
            self.formatter.append_text('\n\n%s%s\n\n' % (depth*'#', node.get('TEXT')))
        self.convert_html_in(node)
        if node.get('LINK'):
            self.formatter.add_image(node.get('LINK'))
        if len(node):
            for child in node:
                self.convert_node(child, depth + 1)

    def get_trimmed_markdown(self):
        return remove_redundant_newlines(self.formatter.get_md())

    def convert_map(self):
        fm = etree.XML(self.map_xml)
        root = fm.find('node')
        for node in root:
            self.convert_node(node)
        self.formatter.close()

    def convert_html_in(self, node):
        html = node.find('richcontent')
        # first deal with notes
        if html is not None and len(html):
            html_text = etree.tostring(html)
            self.html_converter.handle(html_text)