vowels = ['a', 'e', 'o', 'i', 'u']
consonants = ['m', 'n', 'ng', 'p', 't', 'k', 'wh', 'r', 'w', 'h']
c = consonants + ['']
v = ['ā', 'ē', 'ī', 'ō', 'ū']
for i in vowels:
    for j in vowels:
        if i!=j:
            v.append(i+j)
e = ['']
