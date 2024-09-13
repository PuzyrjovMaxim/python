import random

alph_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_upp = [chr(i) for i in range(ord('A'), ord('Z')+1)]


a1 = ''.join(alph_lower)
a2 = ''
for i in range(int(len(a1)/2)):
    r = random.randint(0, len(a1)-1)
    a2 += a1[r]
    a1 = a1.replace(a1[r], "", 1)
key_lower = list(a2)
alph_lower1 = list(a1)
print(alph_lower1)
print(key_lower)

a3 = ''.join(alph_upp)
a4 = ''
for i in range(int(len(a3)/2)):
    r = random.randint(0, len(a3)-1)
    a4 += a3[r]
    a3 = a3.replace(a3[r], "", 1)
key_upp = list(a4)
alph_upp1 = list(a3)
print(alph_upp1)
print(key_upp)

s = input()
m = list(s)
for j in range(len(m)):
    if m[j] in alph_lower1:
        i = alph_lower1.index(m[j])
        m[j] = key_lower[i]
    elif m[j] in key_lower:
        i = key_lower.index(m[j])
        m[j] = alph_lower1[i]
    elif m[j] in alph_upp1:
        i = alph_upp1.index(m[j])
        m[j] = key_upp[i]
    elif m[j] in key_upp:
        i = key_upp.index(m[j])
        m[j] = alph_upp1[i]
print(''.join(m))

for j in range(len(m)):
    if m[j] in alph_lower1:
        i = alph_lower1.index(m[j])
        m[j] = key_lower[i]
    elif m[j] in key_lower:
        i = key_lower.index(m[j])
        m[j] = alph_lower1[i]
    elif m[j] in alph_upp1:
        i = alph_upp1.index(m[j])
        m[j] = key_upp[i]
    elif m[j] in key_upp:
        i = key_upp.index(m[j])
        m[j] = alph_upp1[i]
print(''.join(m))
