#! /usr/bin/python
from fm2md.convert import Converter
from sys import argv

path = argv[1]
converter = Converter(path)
print converter.convert_map()