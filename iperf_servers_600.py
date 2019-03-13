# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import os
import argparse

def start_iperf_server(num): 
	""" 
	function to print square of given num 
	"""
	print("Starting the server on port 60"+str(num)) 
	os.system("iperf3 -s -p 60"+str(num))


if __name__ == "__main__": 
	parser = argparse.ArgumentParser()
	parser.add_argument("n_threads", help="for input of number of threads for iperf flows",type=int)
	args = parser.parse_args()
	print "Read number of threads as "+str(args.n_threads)
	n_threads = args.n_threads
	# creating thread 
	all_threads = [0]*(n_threads+1)

	for x in xrange(1,n_threads):
		all_threads[x] = threading.Thread(target=start_iperf_server, args=(x,)) 

	for x in xrange(1,n_threads):
		all_threads[x].start()

	for x in xrange(1,n_threads):
		all_threads[x].join()

	# both threads completely executed 
	print("Done!") 

