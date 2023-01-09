vowels = ['a', 'e', 'o', 'i', 'u']
youon = ['ya', 'yo', 'yu']
consonants = ['', 'k', 's', 't', 'n', 'h', 'm', 'r', 'g', 'z', 'b', 'p']
c = consonants + ['']
v = vowels + youon + ['ō', 'yō']
e = ['n', '']

sylDict = ['wa']
for x in c:
    for y in v:
        for z in e:
            if x=='s':
                if y=='i':
                    sylDict.append("shi"+z)
                    sylDict.append("sshi"+z)
                    continue
                elif y[0]=='y':
                    sylDict.append("sh"+y[-1]+z)
                    sylDict.append("ssh"+y[-1]+z)
                    continue
            elif x=='t':
                if y=='i':
                    sylDict.append("chi"+z)
                    continue
                elif y=='u':
                    sylDict.append("tsu"+z)
                    continue
                elif y[0]=='y':
                    sylDict.append("ch"+y[-1]+z)
                    continue
            elif x=='h':
                if y=='u':
                    sylDict.append("fu"+z)
                    continue
            elif x=='z':
                if y=='i':
                    sylDict.append("ji"+z)
                    continue
                elif y[0]=='y':
                    sylDict.append("j"+y[-1]+z)
                    continue
            elif x=='d':
                if y=='i'or y[0]=='y':
                    continue

            if x=='k' or x=='g' or x=='s' or x=='z' or x=='t' or x=='d'\
            or x=='h' or x=='b' or x=='p':
                sylDict.append(x+x+y+z)
            
            sylDict.append(x+y+z)
DICLEN = len(sylDict)
