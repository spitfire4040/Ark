import sys
import os

trace = []
all_trace = []
unique_trace = set()

src = ''
dst = ''
hop = ''
ip = ''
addr = ''

count = 1

for x in range(1, 4):
	for filename in os.listdir("/home/jay/Desktop/Ark-3-day/team-" + str(x) + "-3-day"):
		print count
		count += 1
		f = open("/home/jay/Desktop/Ark/team-" + str(x) + "/" + filename, "r")
		out1 = open("/home/jay/Desktop/Ark-3-day/all-traces-3-day.txt", "w")
		out2 = open("/home/jay/Desktop/Ark-3-day/unique-traces-3-day.txt", "w")

		for line in f:
			line = line.split()
			if line[0] != 'traceroute':
				hop = line[0]
				ip = line[1]
				addr = ip + '-' + hop + ' '
				trace.append(addr)

			else:
				src = line[2]
				dst = line[4]
				if not trace:
					pass
				else:
					while '*' in trace[-1]:
						del(trace[-1])
					trace = ''.join(trace)
					all_trace.append(trace)
					unique_trace.add(trace)
				trace = []
				trace.append(src + ':' + dst + ' ')
		try:
			while '*' in trace[-1]:
				del(trace[-1])
			trace = ''.join(trace)
			all_trace.append(trace)
			unique_trace.add(trace)
		except:
			pass

		for item in all_trace:
			out1.write(item)
			out1.write('\n')

		for item in unique_trace:
			out2.write(item)
			out2.write('\n')

		f.close()
		out1.close()
		out2.close()