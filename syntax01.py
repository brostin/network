
"""
This is a multi-line comment.
It will appear as a description for your script:
help(syntax01).
"""


import re


list_of_interfaces = ['ge-0/0/0', 'xe-0/0/0']  #This is a single-line comment for our list

for interface in list_of_interfaces:
	if re.match('ge-*', interface):
		print("{0} is a 1G interface!".format(interface))
	elif re.match('xe-*', interface):
		print("{0} is a 10G interface".format(interface))
	else:
		print("Couldn't recognize the speed of interface: {0}'".format(interface))
## else:
##  	print("Iteration completed!")

print("Finished testing interfaces")
