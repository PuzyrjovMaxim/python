s = 'Day, mice. "Year" is a mistake#'
Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
raz = [',', '.', ';', ' ', '#', '\"']
a = s.split()
b = ''
for i in a:
    dl = len(i)
    z = list(i)
    for j in range(len(z)):
        if (not(z[j] in raz)):
            if(z[j] in Lower):
                if((Lower.index(z[j]) + dl) == 26):
                    z[j] = Lower[25]
                    b += z[j]
                else:
                    i1 = (Lower.index(z[j]) + 1 + dl) % 26 -1
                    z[j] = Lower[i1]
                    b += z[j]
            if (z[j] in Upper):
                if ((Upper.index(z[j]) + dl) == 26):
                    z[j] = Upper[25]
                    b += z[j]
                else:
                    i1 = (Upper.index(z[j]) + 1 + dl) % 26 - 1
                    z[j] = Upper[i1]
                    b += z[j]
        else:
            b += z[j]
    b += ' '

print(b)
