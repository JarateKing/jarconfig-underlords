import time

# keep track of the previous log
oldlog = ""

while True:
	try:
		# read the console log
		f = open("../../console.log", "r")
		newlog = f.read()
		if oldlog != newlog:
			# print any changes to it
			print(newlog.replace(oldlog, ""), end="", flush=True)
			oldlog = newlog
		f.close()
	except:
		# error message otherwise
		print("error reading file, retrying")
		pass
	time.sleep(1)