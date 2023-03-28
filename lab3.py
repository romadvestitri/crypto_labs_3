import random
import gmpy2

def read_binary_file(path):
	file_content = ""
	with open(path, "rb") as f:
		file_content = f.read()

	content_code_list = [char for char in file_content]
	return content_code_list

def write_to_binary_file(file_path, content):
	with open(file_path, "wb") as f:
		arr = bytes(content)
		f.write(bytes(content))

def gcd_extended(num1, num2):
	if num1 == 0:
		return (num2, 0, 1)
	else:
		div, x, y = gcd_extended(num2 % num1, num1)
	return (div, y - (num2 // num1) * x, x)

def fast_pow(x, y):
	if y == 0:
		return 1
	if y == -1:
		return 1. / x
	p = fast_pow(x, y // 2)
	p *= p
	if y % 2:
		p *= x
	return p

def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
        return r

def MillerRabin(n, s = 50):  
    for j in xrange(1, s + 1):
            a = random.randint(1, n - 1)
            b = toBinary(n - 1)
            d = 1
            for i in xrange(len(b) - 1, -1, -1):
                x = d
                d = (d * d) % n
                if d == 1 and x != 1 and x != n - 1:
                    return True # Составное
                if b[i] == 1:
                    d = (d * a) % n
                    if d != 1:
                        return True # Составное
                    return False # Простое

def check_keys(p,q,b):
	if p < 0 or q < 0 or b < 0:
		raise ValueError("Negative keys")

	if (not gmpy2.is_prime(p)) or (not gmpy2.is_prime(q)):
		raise ValueError("Not prime p or q")

	
	if p % 4 != 3 or q % 4 != 3:
		raise ValueError("Modulo of p or q not equal 3")

	if p * q <= b:
		raise ValueError("b is greater than p * q")

	if p * q < 256:
		raise ValueError("Small values of p and q")

	return True

def Encrypt(path, p, q, b):
	check_keys(p,q,b)

	contents = read_binary_file(path)
	
	lastslash = path.rfind("/")
	partpath = path[0:lastslash] + "/"
	point = path.rfind(".")
	extension = path[point+1:len(path)]
	filename = path[lastslash+1:point]
	filename = "encrypted_"+filename
	new_path = partpath + filename + "_"+extension + ".txt"
	
	
	 

	
	
	n = p * q
	
	plaintext = ''
	ciphedtext = ''
	#b = random.randint(1, n)
	for i in range(len(contents)):
		m = contents[i]
		plaintext += str(contents[i]) + ' '
		c = m*(m+b)%n
		ciphedtext += str(c) + ' '
	f = open(new_path, "w")
	f.write(ciphedtext)
	f.close()

	f = open("plaintext.txt", "w")
	f.write(plaintext)
	f.close()

	print('encrypted')
	return plaintext, ciphedtext



def Decrypt(path, p, q, b):
	check_keys(p,q,b)

	f = open(path, "r")
	ciphedtext = f.read()
	f.close()
	lastslash = path.rfind("/")
	partpath = path[0:lastslash] + "/"
	point = path.rfind(".")
	lastunderline = path.rfind("_")
	extension = path[lastunderline+1:point]
	filename = path[path.find("encrypted_")+10:lastunderline]
	filename = partpath + "decrypted_" + filename + "." + extension
	print(filename)

	print(extension)

	c_arr = []
	result = []
	n = p * q
	plaintext = ''
	f = open(path, "r")
	for line in f:
		c_arr = line.split()
		
		for i in range(len(c_arr)):
			D = (b*b + 4*int(c_arr[i]))%n
			#print(f'D{i} counted')

			mp = pow(D, (p+1)//4, p)
			mq = pow(D, (q+1)//4, q)
			
			#print(f'mp and mq {i} counted')
			a = gcd_extended(p,q)

			yp = a[1]
			yq = a[2]

			d_arr = [0,0,0,0]
			d_arr[0] = ((yp * p * mq + yq * q * mp) % n)
			d_arr[1] = (n - d_arr[0])
			d_arr[2] = ((yp * p * mq - yq * q * mp) % n)
			d_arr[3] = (n - d_arr[2]) 
			#print(f'd_arr {i} counted')
			m_arr = [0,0,0,0]

			for j in range(len(d_arr)):
				if (d_arr[j] - b) % 2 == 0:
					m_arr[j] = ((d_arr[j] - b)//2) % n
				else:
					m_arr[j] = ((d_arr[j] - b + n)//2) % n
				if m_arr[j] < 256:
					plaintext += str(m_arr[j]) + " "
					result.append(m_arr[j])
			#print(m_arr)
	f.close()		
	f = open("plaintext1.txt", "w")
	f.write(plaintext)
	f.close()
	write_to_binary_file(filename, result)
	return ciphedtext, plaintext
try:
	c_arr = Encrypt("/Users/roman/TI/lab3/test.jpg", 5003, 5227, 1234)
except ValueError as err:
	print(str(err))
Decrypt("/Users/roman/TI/lab3/encrypted_test_jpg.txt",5003, 5227, 1234)
