import xml.dom.minidom

file = "7 -2.osm"
doc = xml.dom.minidom.parse(file)
nodes = doc.getElementsByTagName('node')

count = 0
count_time = 0
data = []
it=0

for node in nodes:
    tags = node.getElementsByTagName('tag')
    flag1 = 0
    flag2 = 0
    for tag in tags:
        if(tag.getAttribute('v')=="bank"):
            flag1 = 1
        if(flag1==1 and tag.getAttribute("k")=="name"):
            count +=1
            nm = tag.getAttribute("v")
            data.append(nm)
        if(flag1==1 and tag.getAttribute('k')=="opening_hours"):
            str1 = tag.getAttribute('v')
            print(str1)
            it+=1
            # s1 = str1.replace("Mo-Fr ", "").replace(":", " ").replace("-", " ").split(" ", 2)
            # print(s1)
            day1, day2, hours, minutes, s = map(str, str1.replace(":", " ").replace("-", " ").split(" ", 4))
            if((hours+minutes) <= "0900"):
                flag2 = 1
    if(flag2==1):
        count_time +=1
print(it)
print(data)
print(sorted(data), "\n")
print("Кол-во банков: ", count, "\n")
print("Кол-во банков для жаворонков: ", count_time)