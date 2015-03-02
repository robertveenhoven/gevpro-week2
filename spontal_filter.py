#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET


def main(argv):

	tree = ET.parse(argv[1])
	root = tree.getroot()
	
	for point in root.findall('POINT'):
		start=float(point.find('F0_START').text)
		end=float(point.find('F0_END').text)
		bottom=int(point.find('BOTTOM_HZ').text)
		top=int(point.find('TOP_HZ').text)
		
		if not (bottom < end < top) or not (bottom < start < top):
			root.remove(point)
	tree.write(argv[2])

if __name__ == "__main__":
	main(sys.argv)

