import string

def read_input(path : str):
	f = open(path)
	lines = f.readlines()
	ret = []
	for i in range(0,len(lines),2):
		ret.append((lines[i].strip(), lines[i+1].strip()))
	return ret

def get_map(T : str):
	map = {}
	i = 0
	for char in T:
		if char not in map.keys():
			map[char] = i
			i = i + 1
	return map 


 
def naive(  T : str, pattern : str):
	n = len(T)
	m = len(pattern)
	for i in range(n-m+1):
		if pattern == T[i:i+m]:
			return i + 1
	return -1


def Rabin_Karp(T : str, pattern : str, d, q):
	n = len(T)
	m = len(pattern)
	h = pow(d,m-1)%q
	p = 0
	t = 0
	result = []
	for i in range(m):
		p = (d*p+ord(pattern[i]))%q
		t = (d*t+ord(T[i]))%q
	for s in range(n-m+1): 
		if p == t:
			if pattern == T[s:s+m]:
				return s + 1
		
		if s < n-m:
			t = ( t - h * ord(T[s]) ) % q
			t = (t*d + ord(T[s+m])) % q
			t = (t + q) % q
	return -1


def compute_prefix_function(pattern : str):
	m = len(pattern)
	shift_array = []
	shift_array.append(0)
	k = 0
	for q in range(1, m):
		while k > 0 and pattern[k] != pattern[q]:
			k = shift_array[k]
		if pattern[k] == pattern[q]:
			k = k + 1
		shift_array.append(k)
	return shift_array

def KMP(T : str, pattern : str):
	n = len(T)
	m = len(pattern)
	shift_array = compute_prefix_function(pattern)
	q = 0 
	for i in range(n):
		while q > 0 and pattern[q] != T[i]:
			q = shift_array[q]
		if pattern[q] == T[i]:
			q = q + 1
		if q == m:
			return i-m+1 + 1
			q = shift_array[q-1]
	return -1 

def pre_bc(pattern : str, m : int, map : dict):
	n = len(pattern)
	bc = [ m ] * len(map)

	for i in range(m-1):
		bc[map[pattern[i]]] = m - 1 - i

	return bc[0:len(map)]

def horspool(T : str, pattern : str, map : dict):
	n = len(T)
	m = len(pattern)
	bc = pre_bc(pattern, m, map)
	j = 0
	while j < n - m + 1:
		char = T[j + m - 1]
		if pattern[m-1] == char and pattern == T[j:j+m]:
			return j + 1
		j += bc[map[char]]
	return -1

import time 

if __name__ == "__main__":
	input = read_input("./input/input_strings.txt")
	naive_out = open("./output/naive/output.txt", "w")
	kmp_out = open("./output/KMP/output.txt", "w")
	Rabin_karp_out = open("./output/Rabin-karp/output.txt", "w")
	horspool_out = open("./output/horspool/output.txt", "w")
	for T, P in input:
		map = get_map(T)

		b = time.time()
		index = naive(T, P)
		e = time.time()
		naive_out.write("{} {} {} {}\n".format(len(T), len(P), index, e-b))

		b = time.time()
		index = Rabin_Karp(T, P, len(map), 243)
		e = time.time()
		Rabin_karp_out.write("{} {} {} {}\n".format(len(T), len(P), index, e-b))

		b = time.time()
		index = horspool(T, P, map)
		e = time.time()
		horspool_out.write("{} {} {} {}\n".format(len(T), len(P), index, e-b))

		b = time.time()
		index = KMP(T, P)
		e = time.time()
		kmp_out.write("{} {} {} {}\n".format(len(T), len(P), index, e-b))


