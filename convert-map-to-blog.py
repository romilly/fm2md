#! /usr/bin/python
from fm2md.convert import Converter, read_file
from sys import argv
import os

path = argv[1]
directory = os.path.split(path)
converter = Converter(read_file(path), directory)
print converter.convert_map()