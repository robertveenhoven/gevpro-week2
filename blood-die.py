#!/usr/bin/python3

import sys
import json
from collections import namedtuple

def main():
	matchlist=[]
	file = json.load(open('blood-die.json'))
	output = open('blood-die-result.json','w')
	
	matching = namedtuple('matching', ('language', 'classification', 'blood', 'die'))
	for language in file:
		result = matching(language[0],language[1],language[2],language[3])
		blood = result.blood.split()
		die = result.die.split()
		#[json.dump(language,output) for i in blood if i in die]
		[matchlist.append(language) for item in blood if item in die]
		

	[print (item) for item in matchlist]
	
	
if __name__ == "__main__":
	main()
