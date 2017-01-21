#!/usr/bin/env python
from fm2md.convert import Converter
from sys import argv

path = argv[1]
converter = Converter(path)
converter.convert_map()