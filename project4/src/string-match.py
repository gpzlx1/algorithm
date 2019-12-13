import string
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
			print("Pattern occurs with shift {}".format(i))


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
        		print("Pattern occurs with shift {}".format(s))
        if s < n-m:
            t = (t-h*ord(T[s]))%q
            t = (t*d+ord(T[s+m]))%q 
            t = (t+q)%q 


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
			print("Pattern occurs with shift {}".format(i-m+1))
			q = shift_array[q-1]

def pre_bc(pattern : str, m : int, map : dict):
	n = len(pattern)
	bc = [ m ] * m
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
			print("Pattern occurs with shift {}".format(j))
		j += bc[map[char]]

if __name__ == "__main__":
	P = "GCAGAGAG"
	T = "TTTTGCAGAGAG"
	naive(T, P)
	Rabin_Karp(T, P, 20, 20)
	KMP(T, P)
	map = get_map(T)
	horspool(T, P, map)


