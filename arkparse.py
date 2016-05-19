import sys
import os

trace = []
all_trace = []
unique_trace = set()

src = ''
dst = ''

f = open("/home/jay/Desktop/daily.l7.t1.c004642.20160401.aal-dk.warts.txt", "r")

for line in f:
	line = line.split()
	if line[0] == 'traceroute':
		src = line[2]
		dst = line[4]
		trace = []
		hop = 1

	else:
		trace.append(line[1] )

