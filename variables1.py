#This are strings
ip_1 = '192.168.100.1'
ip_2 = '192.168.100.2'
ip_3 = '192.168.100.3'

#This is a list
list_of_ips = [ip_1, ip_2, ip_3]

#This is a dictionary
#where (key: value) -> (ip: serial number)
serial_numbers = {ip_1: '123ADGRJDJA', ip_2: '254LIDFJRK', ip_3: '768AWOASOEQD'}

for ip in list_of_ips:
	print("This host: {0} has this serial: {1}".format(ip, serial_numbers[ip]))

