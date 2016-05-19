import sys
import os
import json

os.system('clear')
f = open("test.json", "r")
for line in f:
	trace = ''
	myjson = json.loads(line)
	
	hops = myjson['hops']
	print 'All Visited IP Addresses:'
	for item in hops:
		addr = item['addr']
		print addr

		trace += addr+' '

	print ' '
	print 'Complete Trace:'
	print trace
	print ' '
