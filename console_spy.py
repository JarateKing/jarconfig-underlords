import time

oldlog = ""

while True:
	try:
		f = open("../../console.log", "r")
		newlog = f.read()
		if oldlog != newlog:
			print(newlog.replace(oldlog, ""), end="", flush=True)
			oldlog = newlog
		f.close()
	except:
		print("error reading file, retrying")
		pass
	time.sleep(1)