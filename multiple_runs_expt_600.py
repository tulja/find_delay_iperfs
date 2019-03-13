import os 
i = 50 
while i < 305:
	os.system("python iperf_clients_600.py "+str(i))
	i = i + 10
