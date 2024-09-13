alph_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_upp = [chr(i) for i in range(ord('A'), ord('Z')+1)]
n = input()
s = input()
m = list(s)
for j in range(len(m)):
    if m[j] in alph_lower:
        i = (alph_lower.index(m[j]) + int(n)) % 26
        m[j] = alph_lower[i]
    elif m[j] in alph_upp:
        i = (alph_upp.index(m[j]) + int(n)) % 26
        m[j] = alph_upp[i]
print(''.join(m))
for j in range(len(m)):
    if m[j] in alph_lower:
        i = (alph_lower.index(m[j]) + 26 - int(n)) % 26
        m[j] = alph_lower[i]
    elif m[j] in alph_upp:
        i = (alph_upp.index(m[j]) + 26 - int(n)) % 26
        m[j] = alph_upp[i]
print(''.join(m))
