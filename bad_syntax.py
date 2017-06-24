interface = 'ge-0/0/0'

if re.match('ge-*', interface):
	print("{0} is a 1G interface!".format(interface))