vowels = ['a', 'e', 'o', 'i', 'u']
consonants = ['p', 't', 'k', 'ph', 'kh', 'th', 'b', 'd', 'g', 'm', 'n',\
'f', 'v', 's', 'z', 'h', 'sh', 'r', 'l']
endings = ['m', 'n', 'r', 'l']
diphthongs = ['ai', 'yu', 'eu', 'yo', 'wi']
clusters = ['pl', 'pr', 'ps', 'ts', 'ch', 'kl', 'kr', 'ks', 'bl', 'br', 'bz', 'dv', 'dz',\
'gl', 'gr', 'gz', 'sp', 'st', 'sk', 'sm', 'sn', 'sl', 'shr', 'shl']
c = consonants + clusters + ['']
v = vowels + diphthongs
e = endings + ['']