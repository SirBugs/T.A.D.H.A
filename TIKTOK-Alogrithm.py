import re

LEAGUE = ['A = 44',
'B = 47',
'C = 46',
'D = 41',
'E = 40',
'F = 43',
'J = 42',
'H = 4d',
'I = 4c',
'J = 4f',
'K = 4e',
'L = 49',
'M = 48',
'N = 4b',
'O = 4a',
'P = 55',
'Q = 54',
'R = 57',
'S = 56',
'T = 51',
'U = 50',
'V = 53',
'W = 52',
'X = 5d',
'Y = 5c',
'Z = 5f',
'a = 64',
'b = 67',
'c = 66',
'd = 61',
'e = 60',
'f = 63',
'g = 62',
'h = 6d',
'i = 6c',
'j = 6f',
'k = 6e',
'l = 69',
'm = 68',
'n = 6b',
'o = 6a',
'p = 75',
'q = 74',
'r = 77',
's = 76',
't = 71',
'u = 70',
'v = 73',
'w = 72',
'x = 7d',
'y = 7c',
'z = 7f',
'0 = 35',
'1 = 34',
'2 = 37',
'3 = 36',
'4 = 31',
'5 = 30',
'6 = 33',
'7 = 32',
'8 = 3d',
'9 = 3c',
'- = 28',
'/ = 2a',
'| = 79',
'\\ = 59',
': = 3f',
'; = 3e',
'( = 2d',
') = 2c',
'[ = 5e',
'] = 58',
'{ = 7e',
'} = 78',
'< = 39',
'> = 3b',
'! = 24',
'# = 26',
'$ = 21',
'% = 20',
'^ = 5b',
'& = 23',
'* = 2f',
'= = 38',
'+ = 2e',
'_ = 5a',
'. = 2b',
'@ = 45']

def ENCRYPT(TEXT):
	HASH = ''
	for ONE in TEXT:
		#print ONE
		for A in LEAGUE:
			if '{} = '.format(ONE) in A:
				#print A.split(' = ')[1]
				HASH = HASH+A.split(' = ')[1]
			else:
				pass
	print '[{}] Hashed To -> {}'.format(TEXT, HASH)


def DECRYPT(HASH):
	HASH_PARTS_LIST = re.findall(r'.{1,2}',HASH,re.DOTALL)
	#print HASH_PARTS_LIST

	TEXT = ''
	for DOUBLE in HASH_PARTS_LIST:
		#print DOUBLE
		for A in LEAGUE:
			if ' = {}'.format(DOUBLE) in A:
				#print A.split(' = ')[1]
				TEXT = TEXT+A.split(' = ')[0]
			else:
				pass
	print '[{}] UnHashed To -> {}'.format(HASH, TEXT)

# // ENCRYPT('sir.bugs0x@gmail.com') => 766c772b67706276357d456268646c692b666a68
# // DECRYPT('766c772b67706276357d456268646c692b666a68') => sir.bugs0x@gmail.com