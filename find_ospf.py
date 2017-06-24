import re


def find_ospf_neighbors(ospf_output=None):
	if ospf_output is None:
		raise ValueError('No output passed to function!')
	ospf_neighbor_addresses = []
	ospf_neighbor_regex = re.compile('\s*((\d{1,3}\.){3}\d{1,3}) .*')
	for line in ospf_output:
		ospf_neighbor = ospf_neighbor_regex.search(line)
		if ospf_neighbor:
			ospf_neighbor_addresses.append(ospf_neighbor.group(1))
	return ospf_neighbor_addresses


def print_ospf_neighbors(list=None):
	if list is None:
		raise ValueError('Nothing passed to function!')
	i = 0
	print("\nParsing neighbors for a new device:")
	for ip in list:
		i += 1
		print('Neighbor #{0} - {1}'.format(i, ip))

if __name__ == "__main__":
	ospf_output_1 = open('show_ospf_1.txt', 'r')
	ospf_output_2 = open('show_ospf_2.txt', 'r')

	list1 = find_ospf_neighbors(ospf_output_1)
	list2 = find_ospf_neighbors(ospf_output_2)

	ospf_output_1.close()
	ospf_output_2.close()

	print_ospf_neighbors(list1)
	print_ospf_neighbors(list2)