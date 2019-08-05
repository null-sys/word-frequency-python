
import os

path = '/path/to/the/directory/'

files = []

for r,d,f in os.walk(path):
	print(f)
	for file in f:
		if '.txt' in file:
			files.append(os.path.join(r,file))

dic = {}
for f in files:
	file = open(f)
	for x in file:
	    l = x.split()
	    for w in l:
	        if w in dic:
	            dic[w] += 1
	        else:
	            dic[w] = 1

print(dic)
