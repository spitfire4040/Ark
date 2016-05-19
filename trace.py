import os
import sys

trace = set()
tracecount = 0

f1 = open("ark_trace.txt", "r")
f2 = open("ark_trace1.txt", "r")
f3 = open("ark_trace2.txt", "r")

for line in f1:
	trace.add(line)
	tracecount += 1

for line in f2:
	trace.add(line)
	tracecount += 1

for line in f3:
	trace.add(line)
	tracecount += 1

print "total traces: ", tracecount
print "total unique traces: ", len(trace)