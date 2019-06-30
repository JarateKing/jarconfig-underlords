import time

while True:
	try:
		f = open("../../console.log", "r")
		print(f.read())
		f.close()
	except:
		print("error reading file, retrying")
		pass
	time.sleep(1)