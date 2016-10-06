#!/usr/bin/env python3
import subprocess
import sys
import string
import os

# YOUR CODE GOES here
numset = set('0123456789')


def func(x):
	x = x.lower()
	for (i,key) in enumerate(x):
		if key in string.ascii_lowercase or key in numset:
			return x[i:]

		
def dfs(path, prefix):
	files = [x for x in os.listdir(path) if x[0] != '.']
	files = sorted(files, key=func)
	num_dir, num_file = 0, 0
	for i,fname in enumerate (files):
		if i<len(files) - 1:
			curPrefix,	subdirPrefix = "├── ", "│   "
		else:
			curPrefix, subdirPrefix = "└── ", "    "
		print(prefix + curPrefix + fname)
		if os.path.isfile(os.path.join(curPath, fname)):		
			num_file =num_file+1
		else:
			num_dir=num_dir+1
			tdirN, tfileN = dfsTree(os.path.join(curPath, fname), prefix + subdirPrefix)
			dirN, fileN = dirN + tdirN, fileN + tfileN
	return dirN, fileN

def tree(path):
	print(path)
	num_dir,num_file = dfs(path, "")
	print()
	print(str(dirN) + (" directories, " if dirN != 1 else " directorie, ") + str(fileN) + (" files" if fileN != 1 else " files"))
	
if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
