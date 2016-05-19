import sys
import os

traces = set()
ips = set()

ip_count = 0
trace_count = 0

for x in range(1, 4):
	f = open("/home/jay/Ark/cycle-" + str(x) + "/total_unique_ip.txt", "r")
	for line in f:
		ips.add(line)
	f.close()

	f = open("Unique-Traces", "w")
	for item in ips:
		f.write(item + "\n")
		ip_count += 1
	f.close()
	ips.clear()


for x in range(1, 4):
	f = open("/home/jay/Ark/cycle-" + str(x) + "/total_unique_trace.txt", "r")
	for line in f:
		traces.add(line)
	f.close()

	f = open("Unique-Traces", "w")
	for item in traces:
		f.write(item + "\n")
		trace_count += 1
	f.close()
	traces.clear()

print "Total IP's: ", ip_count
print "Total Traces: ", trace_count

f = open("Final-Tally.txt", "w")
f.write("Total IP's: " + str(ip_count) + '\n')
f.write("Total Traces: " + str(trace_count) + '\n')
f.close()