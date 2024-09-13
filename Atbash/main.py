alph_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_upp = [chr(i) for i in range(ord('A'), ord('Z')+1)]

# key_lower = [chr(i) for i in range(ord('z'), ord('a') - 1, -1)]
# key_upp = [chr(i) for i in range(ord('Z'), ord('A') - 1, -1)]

s = input()
m =list(s)
for j in range(len(m)):
    if m[j] in alph_lower:
        i = alph_lower.index(m[j])
        m[j] = alph_lower[len(alph_lower) - i - 1]
    elif m[j] in alph_upp:
        i = alph_upp.index(m[j])
        m[j] = alph_upp[len(alph_upp) - i - 1]
print(''.join(m))

for j in range(len(m)):
    if m[j] in alph_lower:
        i = alph_lower.index(m[j])
        m[j] = alph_lower[len(alph_lower) - i - 1]
    elif m[j] in alph_upp:
        i = alph_upp.index(m[j])
        m[j] = alph_upp[len(alph_upp) - i - 1]
print(''.join(m))