my_ip = '192.168.2.2'
list_of_ips = ['192.168.100.1', '172.16.2.1', '10.0.0.1', '169.124.1.1']
check = False

for ip in list_of_ips:
	if ip is my_ip:
		print('Awesome! List contains my IP address: {0}'.format(ip))
		check = True
	else:
		pass
else:
	if check is not True:
		print('Depressing! We did not find my IP address {0}! :( '.format(my_ip))