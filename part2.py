# Part 2 of the Python Review lab.

def isPrime(n):
 	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def encode(z, y):
	while not isPrime(z):
		z+=1
	while not isPrime(y):
		y+=1
	if 1 < y < 250 and 500 < z < 1000 :
		return True
	
	else:
		print("Invalid input: Outside range.")
		return None

		



def decode(coded_message):
	for y in range(2,250):
		if not isPrime(y):
			continue
		if coded_message % y == 0:
			z = coded_message / y
			if (isPrime(int(z)) and 500  < x <1000):
				return (z, y)
