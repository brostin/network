
my_file = open('route.txt', 'r')  # open file in read-only mode

for line in my_file.readlines():  # calling readlines() method
	print(line.rstrip())  # using rstrip() method to delete trailing spaces -- right strip

my_file.close  # to prevent memory leaks and locking files