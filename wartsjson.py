# Import Header Files
import sys
import os
import os.path
import json
import urllib
import string
import gzip
import hashlib

counter = 1

total_all_trace = set()
total_all_ip = set()

total_all_trace_count = 0
total_all_ip_count = 0

# build list of daily files
DailyList = []
f = open("daily1.txt", "r")
for item in f:
	item = item.split()
	DailyList.append(item[2])
f.close()

for item in DailyList:

	address = item

	all_src = []
	unique_src = set()
	all_dst = []
	unique_dst = set()
	all_ip = []
	unique_ip = set()
	all_trace = []
	unique_trace = set()

	t_src = 0
	u_src = 0
	t_dst = 0
	u_dst = 0
	t_ip = 0
	u_ip = 0
	t_trace = 0
	u_trace = 0

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


	os.system("zcat warts.gz | sc_warts2json > warts.json")
	f = open("warts.json", "r")

	print (counter)
	counter += 1

	loadcount = 1

	for line in f:
		try:
			myjson = json.loads(line)

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

			for item in hops:
				addr = item['addr']
				all_ip.append(addr)
				unique_ip.add(addr)
				total_all_ip.add(addr)
				trace.append(addr + ' ')

			list1 = ''.join(trace)
			all_trace.append(list1)
			unique_trace.add(list1)
			total_all_trace.add(list1)


		except:
			"Failed to read ", counter

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

	of1.close()
	of2.close()
	of3.close()
	of4.close()
	of5.close()
	of6.close()
	of7.close()
	of8.close()
	of9.close()

	trace = ''

of9 = open("stats.txt", "a")
of10 = open("all_unique_ip.txt", "w")
of11 = open("all_unique_trace.txt", "w")

for item in total_all_ip:
	of10.write(item + ' ')
	total_all_ip_count += 1
for item in total_all_trace:
	of11.write(item + '\n')
	total_all_trace_count += 1

of9.write("Total IP's: " + str(total_all_ip_count) + '\n')
of9.write("Total Traces: " + str(total_all_trace_count) + '\n')

of9.close()
of10.close()
of11.close()