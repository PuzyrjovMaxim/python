fin = open('input.txt', encoding='utf-8')
fout = open('output.txt', 'w', encoding='utf-8')

n = int(fin.readline())
stations = [0 for i in range(1, n)]
max = 0

line = fin.readline()
while line:
    name, surname, s1, s2 = line.split()
    stat1, stat2 = int(s1), int(s2)
    if(stat2>stat1):
        for i in range(stat1 - 1, stat2 - 1):
            stations[i] += 1
            if(stations[i] > max) :
                max = stations[i]
    elif(stat1>stat2):
        for i in range(stat2 - 1, stat1 - 1):
            stations[i] += 1
            if(stations[i] > max) :
                max = stations[i]
    line = fin.readline()
for i in range(len(stations)):
    if(stations[i]==max):
        fout.write(str(i+1) + '-' + str(i+2) + '\n')
