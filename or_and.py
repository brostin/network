import re

list_of_ips = ['192.168.100.1', '172.16.2.1', '10.0.0.1', '169.124.1.1']

for ip in list_of_ips:
	if re.match('^10\.', ip) or re.match('^192\.168\.', ip):
		print(ip)
