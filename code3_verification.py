
import os
import threading
import time

lock = threading.RLock()

path = '/path/to/the/directory/'

files = []

for r,d,f in os.walk(path):
	print(f)
	for file in f:
		if '.txt' in file:
			files.append(os.path.join(r,file))

class mythread(threading.Thread):
	f = 'o'
	def __init__(self, i,dic):
		threading.Thread.__init__(self)
		self.f = i
	def run(self):    
		file = open(self.f)
		for x in file:
		    l = x.split()
		    lock.acquire()
		    for w in l:
		        if w in dic:
		            dic[w] += 1
		        else:
		            dic[w] = 1
		    lock.release()


# USING MULTIPLE THREADS
thread_list = []
dic = {}
for f in files:
    t = mythread(f,dic)
    t.start()
    thread_list.append(t)

time.sleep(1)

for t in thread_list :
    t.join()

print(dic)

# USING NORMAL METHOD 
dic2 = {}
for f in files:
	file = open(f)
	for x in file:
	    l = x.split()
	    for w in l:
	        if w in dic2:
	            dic2[w] += 1
	        else:
	            dic2[w] = 1

print(dic2)

# COMPARING THE RESULTS 
print(dic==dic2)