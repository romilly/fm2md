#! /usr/bin/python
import codecs
import sys

def remove_nbs(text):
    return text.replace(u"\u00A0", " ")

if __name__ == '__main__':
    filename = sys.argv[1]
    with codecs.open(filename, encoding='utf8') as infile:
        text = remove_nbs(infile.read())
    with codecs.open(filename, 'w', encoding='utf8') as outfile:
        outfile.write(text)
