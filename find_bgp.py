import re

def find_bgp_neighbors (this_bgp_config=None):
	if this_bgp_config == None:
		raise ValueError, 'No config passed to function!'
	bgp_neighbor_addresses = []
	bgp_neighbor_regex = re.compile('\s*neighbor ((\d{1,3}\.){3}\d{1,3});')
	for line in this_bgp_config:
		bgp_neighbor = bgp_neighbor_regex.search(line)
		
		if bgp_neighbor:
			bgp_neighbor_addresses.append(bgp_neighbor.group(1))
	return bgp_neighbor_addresses
	
bgp_config_1 = open('config-bgp-1.txt', 'r')
bgp_config_2 = open('config-bgp-2.txt', 'r')

list1 = find_bgp_neighbors(bgp_config_1)
list2 = find_bgp_neighbors(bgp_config_2)

bgp_config_1.close()
bgp_config_2.close()
