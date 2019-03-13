# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import os
import argparse
import subprocess
from subprocess import check_output

output = ""
def start_iperf_client(num): 
	""" 
	function to print square of given num 
	"""
	print("Starting the iperf client session on port 70"+str(num)) 
	server_ip = "10.0.0.2"
	os.system("iperf3 -c "+server_ip+" -t 20 -p 70"+str(num)+"")


def start_netperf():
	global output
	cmd = "netperf -P 0 -l 18 -t TCP_RR -H \"10.0.0.2\" -- -r 1,1 -o P50_LATENCY,P90_LATENCY,P99_LATENCY"
	#process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
	print "Netperf Done!"


if __name__ == "__main__": 

	global output
#	f= open("guru99.txt","w+")
	parser = argparse.ArgumentParser()
	parser.add_argument("n_threads", help="for input of number of threads for iperf flows",type=int)
	args = parser.parse_args()
	print "Read number of threads as "+str(args.n_threads)
	n_threads = args.n_threads
	
	# creating thread 
	all_threads = [0]*(n_threads+1)

	netperf_thread = threading.Thread(target=start_netperf) 
	netperf_thread.start()

	print "Started Netperf "

	for x in xrange(1,n_threads):
		all_threads[x] = threading.Thread(target=start_iperf_client, args=(x,)) 

	for x in xrange(1,n_threads):
		all_threads[x].start()
		
	for x in xrange(1,n_threads):
		all_threads[x].join()

	netperf_thread.join()
	# both threads completely executed 
	print("Done!") 
	print("Latency observed as "+str(output))
	with open('latencies_600.dat', 'a') as the_file:
			the_file.write(str(n_threads)+","+str(output))
