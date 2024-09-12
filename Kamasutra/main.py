import random

alph_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_upp = [chr(i) for i in range(ord('A'), ord('Z')+1)]
print(alph_lower)


a1 = ''.join(alph_lower)
a2 = ''
for i in range(len(a1)):
    r = random.randint(0, len(a1)-1)
    a2 += a1[r]
    a1 = a1.replace(a1[r], "", 1)
key_lower = list(a2)
print(key_lower)

print(alph_upp)

a3 = ''.join(alph_upp)
a4 = ''
for i in range(len(a3)):
    r = random.randint(0, len(a3)-1)
    a4 += a3[r]
    a3 = a3.replace(a3[r], "", 1)
key_upp = list(a4)
print(key_upp)

s = input()
m = list(s)
for j in range(len(m)):
    if m[j] in alph_lower:
        i = alph_lower.index(m[j])
        m[j] = key_lower[i]
    elif m[j] in alph_upp:
        i = alph_upp.index(m[j])
        m[j] = key_upp[i]
res = ''.join(m)
print(res)