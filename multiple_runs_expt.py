import os 
i = 400
while i <= 1000:
	os.system("python iperf_clients.py "+str(i))
	i = i + 100
