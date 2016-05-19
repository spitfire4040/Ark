import os
import sys

# find ip totals
count = 1
list_count = 8

# reset containers
total_all_ip = set()
total_all_ip_count = 0

# for each file, combine unique values in one list
while (count <= list_count):
	f = open("/home/jay/Ark/cycle-2/all_unique_ip_" + str(count) + ".txt", "rb")
	for item in f:
		total_all_ip.add(item)
	count += 1
	f.close()

	# write all unique values to one file
	of = open("/home/jay/Ark/cycle-2/all_unique_ip.txt", "w")
	for item in total_all_ip:
		of.write(item + '\n')
		total_all_ip_count += 1
	of.close()
	total_all_ip.clear()

# find trace totals
count = 1

# reset containers
total_all_trace = set()
total_all_trace_count = 0

# for each file, combine all unique values in one list
while (count <= list_count):
	f = open("/home/jay/Ark/cycle-2/all_unique_trace_" + str(count) + ".txt", "rb")
	for item in f:
		total_all_trace.add(item)
	count += 1
	f.close()

	# write all unique values to one file
	of = open("/home/jay/Ark/cycle-2/all_unique_trace.txt", "w")
	for item in total_all_trace:
		of.write(item + '\n')
		total_all_trace_count += 1
	of.close()
	total_all_trace.clear()

# append stats to the end of list for totals
f = open("stats.txt", "a")
f.write("Total IP's: " + str(total_all_ip_count) + '\n')
f.write("Total Traces: " + str(total_all_trace_count) + '\n')
f.close()