# Import Header Files
import sys
import os
import os.path
import urllib
import string
import gzip

# build list of daily files
teamlist = []
f = open("team-2-list", "r")

for item in f:
	teamlist.append(item)

f.close()


# iterate throuth teamlist
for item in teamlist:
	item = item.split()

	# get value for address from teamlist
	address = item[2]

	# get value for day from teamlist
	date = item[3]
	date = date.split('-')
	day = date[0]

	try:
		# download page from internet and store in filesystem
		urllib.urlretrieve("https://topo-data.caida.org/team-probing/list-7.allpref24/team-2/daily/2016/cycle-201604" + day + "/" + address, "warts.gz")

		inF = gzip.open("warts.gz", "rb")
		outF = open("warts", "wb")
		outF.write(inF.read())
		inF.close()
		outF.close()


		# read binary file and convert to text
		os.system("sc_warts2text warts > warts.txt")


		#change file type
		new_address = string.replace(address, '.gz', '.txt')


		if (os.path.isfile("warts.txt")):
			os.rename("warts.txt", "/home/jthom/Ark/team-2/" + new_address)


		if (os.path.isfile("warts.gz")):
			os.remove("warts.gz")

		if (os.path.isfile("warts")):
			os.remove("warts")

	except:
		pass