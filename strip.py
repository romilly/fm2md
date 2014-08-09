#! /usr/bin/python
import codecs
import sys

def tidy(text):
    return text.replace(u"\u00A0", " ").replace("$%", "<strong>").replace('%$','</strong>')


if __name__ == '__main__':
    filename = sys.argv[1]
    with codecs.open(filename, encoding='utf8') as infile:
        text = tidy(infile.read())
    with codecs.open(filename, 'w', encoding='utf8') as outfile:
        outfile.write(text)
