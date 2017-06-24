def test_scope():
	private_string = 'private'
	print('The variable {0} may be referenced anywhere'.format(global_string))
	return


global_string = 'global'
test_scope()
print('The variable {0} may not'.format(private_string))