import os 
i = 10
while i < 515:
	os.system("python iperf_clients_700.py "+str(i))
	i = i + 100
