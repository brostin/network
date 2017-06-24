rx_bytes_orig = 8501
rx_bytes_new = rx_bytes_orig + 1500

print("Original RX bytes count: {0}".format(rx_bytes_orig))
print("New RX bytes count: {0}".format(rx_bytes_new))

print("Here is the memory location of the original variable: {0}".format(id(rx_bytes_orig)))
print("Here is the memory location of the new variable: {0}".format(id(rx_bytes_new)))