# Import Header Files
import sys
import os
import os.path
import json
import urllib
import string
import gzip
import hashlib

# prefix1 = https://topo-data.caida.org/team-probing/list-7.allpref24/team-1/
# prefix2 = 
# prefix3 = 

# set counter for DailyList
counter = 1

# container for all unique ip's and traces
total_all_trace = set()
total_all_ip = set()

# counters for all unique ip's and traces
total_all_trace_count = 0
total_all_ip_count = 0
list_count = 1

# build list of daily files
DailyList = []
f = open("daily1.txt", "r")
for item in f:
	item = item.split()
	DailyList.append(item[2])
f.close()

# get length of list
list_length = len(DailyList)

# iterate throuth DailyList
for item in DailyList:

	# get value for address
	address = item

	# reset list_count
	#list_count = 1

	# fresh assignment of lists and sets
	all_src = []
	unique_src = set()
	all_dst = []
	unique_dst = set()
	all_ip = []
	unique_ip = set()
	all_trace = []
	unique_trace = set()

	# fresh counters
	t_src = 0
	u_src = 0
	t_dst = 0
	u_dst = 0
	t_ip = 0
	u_ip = 0
	t_trace = 0
	u_trace = 0

	# open files each time
	of1 = open("total_src.txt", "w")
	of2 = open("unique_src.txt", "w")
	of3 = open("total_dst.txt", "w")
	of4 = open("unique_dst.txt", "w")
	of5 = open("total_ip.txt", "w")
	of6 = open ("unique_ip.txt", "w")
	of7 = open("total_trace.txt", "w")
	of8 = open("unique_trace.txt", "w")	
	of9 = open("stats.txt", "a")

	# download page from internet and store in filesystem
	urllib.urlretrieve("https://topo-data.caida.org/team-probing/list-7.allpref24/team-1/daily/2016/cycle-20160103/" + address, "warts.gz")

	try:
		#os.system("zcat warts.gz | sc_warts2json > warts.json")
		inF = gzip.open("warts.gz", "rb")
		outF = open("warts", "wb")
		outF.write(inF.read())
		inF.close()
		outF.close()
	except:
		pass

	try:
		# read binary file and convert to text
		os.system("sc_warts2json warts > warts.json")
	except:
		pass

	# open file for read
	f = open("warts.json", "r")

	# print counter for visual affirmation
	print (counter)
	counter += 1

	# read through each line in file
	for line in f:
		try:
			# decode json
			myjson = json.loads(line)

			# find dictionary values and catch
			src = myjson['src']

			all_src.append(src)
			unique_src.add(src)
			all_ip.append(src)
			unique_ip.add(src)
			total_all_ip.add(src)

			dst = myjson['dst']

			all_dst.append(dst)
			unique_dst.add(dst)
			total_all_ip.add(dst)
			unique_ip.add(dst)
			total_all_ip.add(dst)

			hops = myjson['hops']

			trace = []

			# build strings for trace
			test = ''
			for item in hops:
				addr = item['addr']
				all_ip.append(addr)
				unique_ip.add(addr)
				total_all_ip.add(addr)
				if addr != test:
					trace.append(addr + ' ')
				test = addr

			# strip extra characters from list
			list1 = ''.join(trace)

			# get hash of trace
			#m = hashlib.md5() *************
			#m.update(list1)   *************

			# store all hashed traces
			all_trace.append(m.hexdigest())
			unique_trace.add(m.hexdigest())
			total_all_trace.add(m.hexdigest())


		except:
			"Failed to read ", counter

	# write to file and keep count
	for item in all_src:
		of1.write(item+' ')
		t_src += 1
	for item in unique_src:
		of2.write(item+' ')
		u_src += 1
	for item in all_dst:
		of3.write(item+' ')
		t_dst += 1
	for item in unique_dst:
		of4.write(item+' ')
		u_dst += 1
	for item in all_ip:
		of5.write(item+' ')
		t_ip += 1
	for item in unique_ip:
		of6.write(item+' ')
		u_ip += 1
	for item in all_trace:
		of7.write(item+'\n')
		t_trace += 1
	for item in unique_trace:
		of8.write(item+'\n')
		u_trace += 1

	# for each iteration, print stats to file (each vantage point)
	of9.write(address + '\n')
	of9.write("Total Source IPs: " + str(t_src) + '\n')
	of9.write("Unique Source IPs: " + str(u_src) + '\n')
	of9.write("Total Destination IPs: " + str(t_dst) + '\n')
	of9.write("Unique Destination IPs: " + str(u_dst) + '\n')
	of9.write("Total IPs: " + str(t_ip) + '\n')
	of9.write("Unique IPs: " + str(u_ip) + '\n')
	of9.write("Total Traces: " + str(t_trace) + '\n')
	of9.write("Unique Traces: " + str(u_trace) + '\n')
	of9.write("*************************************\n")

	# close files
	of1.close()
	of2.close()
	of3.close()
	of4.close()
	of5.close()
	of6.close()
	of7.close()
	of8.close()
	of9.close()

	# reset trace list
	del trace[:]
	#trace = ''
	del all_src[:]
	unique_src.clear()
	del all_dst[:]
	unique_dst.clear()
	del all_ip[:]
	unique_ip.clear()
	del all_trace[:]
	unique_trace.clear()


	# for every 10, start a new file to save memory
	flag = False
	if (counter % 10 == 0) or (counter == list_length):
		of10 = open("/home/jay/Ark/cycle-1/all_unique_ip_" + str(list_count) + ".txt", "w")
		of11 = open("/home/jay/Ark/cycle-1/all_unique_trace_" + str(list_count) + ".txt", "w")

		# write to file
		for item in total_all_ip:
			of10.write(item + '\n')
			total_all_ip_count += 1
		for item in total_all_trace:
			of11.write(item + '\n')
			total_all_trace_count += 1

		# close files
		of10.close()
		of11.close()

		# reset containers for all unique values
		total_all_trace.clear()
		total_all_ip.clear()

		# increment list counter
		list_count += 1


# find ip totals
count = 1

# reset containers
total_all_ip.clear()
total_all_ip_count = 0

# for each file, combine unique values in one list
while (count <= (list_count - 1)):
	f = open("/home/jay/Ark/cycle-1/all_unique_ip_" + str(count) + ".txt", "rb")
	for item in f:
		total_all_ip.add(item)
	count += 1
	f.close()

	# write all unique values to one file
	of = open("/home/jay/Ark/cycle-1/all_unique_ip.txt", "w")
	for item in total_all_ip:
		of.write(item + '\n')
		total_all_ip_count += 1
	of.close()
	total_all_ip.clear()

# find trace totals
count = 1

# reset containers
total_all_trace.clear()
total_all_trace_count = 0

# for each file, combine all unique values in one list
while (count <= (list_count - 1)):
	f = open("/home/jay/Ark/cycle-1/all_unique_trace_" + str(count) + ".txt", "rb")
	for item in f:
		total_all_trace.add(item)
	count += 1
	f.close()

	# write all unique values to one file
	of = open("/home/jay/Ark/cycle-1/all_unique_trace.txt", "w")
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