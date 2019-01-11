#! python3
# Opens a directory in the host computer or 
# networked location based on a pre-defined keyword

import subprocess, sys, pyperclip, shelve

keyword_log = 'savedata/saved_locations.txt'
shelfFile = shelve.open(keyword_log)


def store(args):
	"""
	Stores a keyword and file path
	"""
	kw = args[2]
	loc = ' '.join(args[3:])
	shelfFile[kw] = loc


def recall(args):
	# Opens a file explorer window to the location of the 
	# mapped keyword
	subprocess.Popen(r'explorer /select, ' + shelfFile[args[2]])


def list_stored(args):
	# Lists all keywords and paths saved
	print("\n\nStored keywords and locations")
	print("-"*60 + "\n")
	keys = list(shelfFile.keys())
	keys.sort()
	for kw in keys:
		print("{0:^15}| {1}".format(kw, shelfFile[kw]))
	print("\n" + "-"*60)
	print("\n\n")


commands = {
	'store': store,
	'recall': recall,
	'list': list_stored,
}


if len(sys.argv) > 1:
	if sys.argv[1] == 'store' or sys.argv[1] == 's':
		store(sys.argv)
	elif sys.argv[1] == 'recall' or sys.argv[1] == 'r':
		recall(sys.argv)
	elif sys.argv[1] in commands:
		cmd = commands.get(sys.argv[1])
		cmd(sys.argv)
else:
	subprocess.Popen(r'explorer /select, ' + pyperclip.paste())

shelfFile.close()



