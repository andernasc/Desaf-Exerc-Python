import hashlib

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(file2, 'rb').read())

if((hash1 != hash2)):
	print('Files are different ({} != {})'.format(file1, file2))
	print('The hash of the file1 is: {}'.format(hash1.hexdigest()))
	print('The hash of the file2 is: {}'.format(hash2.hexdigest()))
else:
	print('Files are the same ({} = {})'.format(file1, file2))
	print('The hash of the file1 is: {}'.format(hash1.hexdigest()))
	print('The hash oxf the file2 is: {}'.format(hash2.hexdigest()))
