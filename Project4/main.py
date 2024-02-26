# #1
# l = ['1', '1', '2', '3', '3', '3', '4']
# x = set(l)
# print(l)
# print(len(x))
# print(x)

# #2
# l = [i for i in range(5)]
# x = [j for j in range(10, 1, -1 )]
# print(x)
# a = set(l)
# b = set(x)
# c = a & b
# print(sorted(c))

#3
# a = list(map(int, input().split()))
# c = set()
# for i in range(len(a)):
#     if(a[i] in c):
#         print("YES")
#     else:
#         print("NO")
#     c.add(a[i])

#4
# a = [i for i in 'rgbwp']
# b = [j for j in 'gbpdm']
# c = set(a) & set(b)
# print(len(c))
# print(c)
# print(set(a).difference(set(b)))
# print(set(b).difference(set(a)))

#5
# s1 = [i for i in '1345']
# s2 = [i for i in '234']
# s3 = [i for i in '839']
# s4 = [i for i in '12389']
# c = set(s1) & set(s2) & set(s3) & set(s4)
# print(c)
# b = set(s1) | set(s2) | set(s3) | set(s4)
# print(b)

#6
n = int(input())
k1 = []