#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET


def main(argv):
	
	file = argv[1]
	outputfile = argv[2]
	
	tree = ET.parse(file)
	root = tree.getroot()
	
	for point in root.findall('POINT'):
		start=float(point.find('F0_START').text)
		end=float(point.find('F0_END').text)
		bottom=int(point.find('BOTTOM_HZ').text)
		top=int(point.find('TOP_HZ').text)
		
		if ((start < bottom) or (start > top) or (end < bottom) or (end > top)):
			root.remove(point)
		tree.write(outputfile)

if __name__ == " __main__":
	main(sys.argv)

