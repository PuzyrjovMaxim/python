# s = 'Hello World'
# print(s[0:5])     #   1)a
# print(s[0:len(s) - 2])    #1)b
# print(s[::2])    #1)c
# print(s[::-2])    #1)d

#2
# print(s.count(' ') + 1)

#3
# print(s.replace('','*')[1: len(s.replace('','*')) - 1])

#4
s = ' Hello,  WOrld, nine ,   nicht .  '
s = s.replace(',', ', ')
s = s.replace('.', '. ')
#s = s.replace
s = s.strip()
print(s)
x = ''
# for i in range(0, len(s) - 1):
#     if(s[i] == s[i+1] == ' '):
#         x += ''
#     else:
#         x+= s[i]
a = s.split()
s = ' '.join(a)
print(s)