# import files
import sys
import os
import os.path

# cycle through all 3 teams
for x in range(1, 4):
	print '***********'

	# cycle through each day
	for y in range(1, 4):
		print '###########'

		# re-initialize variables each time (clear)
		trace = []
		all_trace = []
		unique_trace = set()

		src = ''
		dst = ''
		hop = ''
		ip = ''
		addr = ''	

		# check for directories and create if necessary
		if not os.path.exists("/home/jay/Desktop/Ark3/output"):
			os.makedirs("/home/jay/Desktop/Ark3/output")

		if not os.path.exists("/home/jay/Desktop/Ark3/output/team-" + str(x)):
			os.makedirs("/home/jay/Desktop/Ark3/output/team-" + str(x))

		if not os.path.exists("/home/jay/Desktop/Ark3/output/team-" + str(x) + "/day-" + str(y)):
			os.makedirs("/home/jay/Desktop/Ark3/output/team-" + str(x) + "/day-" + str(y))	

		# cycle through each file for team/day
		for filename in os.listdir("/home/jay/Desktop/Ark3/team-" + str(x) + "/day-" + str(y)):

			# print filename for visual affirmation
			print filename

			# open file for read
			f = open("/home/jay/Desktop/Ark3/team-" + str(x) + "/day-" + str(y) + "/" + filename, "r")

			# open files for write
			out1 = open("/home/jay/Desktop/Ark3/output/team-" + str(x) + "/day-" + str(y) + "/all-traces.txt", "w")
			out2 = open("/home/jay/Desktop/Ark3/output/team-" + str(x) + "/day-" + str(y) + "/unique-traces.txt", "w")

			try:
				# iterate through each line
				for line in f:

					# split line into pieces
					line = line.split()

					# build trace string (line not traceroute)
					if line[0] != 'traceroute':
						hop = line[0]
						ip = line[1]
						addr = ip + '-' + hop + ' '
						trace.append(addr)

					# reset and append running list each time line == traceroute
					if line[0] == 'traceroute':

						# get values for src, dst
						src = line[2]
						dst = line[4]

						# check for empty list and append if good
						if not trace:
							pass
						else:

							# eliminate trailing '*'s
							while '*' in trace[-1]:
								del(trace[-1])

							# convert list to string
							trace = ''.join(trace)

							# append string to running lists
							all_trace.append(trace)
							unique_trace.add(trace)

						# reset trace
						trace = []

						# append src, dst to new trace
						trace.append(src + ':' + dst + ' ')

			except:
				pass

			# once more at end to catch last trace
			try:
				# eliminate trailing '*'s
				while '*' in trace[-1]:
					del(trace[-1])

				# convert list to string
				trace = ''.join(trace)

				# append string to running lists
				all_trace.append(trace)
				unique_trace.add(trace)
			except:
				pass

		# write all_trace to file
		for item in all_trace:
			out1.write(item)
			out1.write('\n')

		# write unique_trace to file
		for item in unique_trace:
			out2.write(item)
			out2.write('\n')

		# close files
		f.close()
		out1.close()
		out2.close()