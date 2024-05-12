import sqlite3
import xml.dom.minidom

con = sqlite3.connect('Space.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Satellite
(id INTEGER PRIMARY KEY,
name VARCHAR(30),
age VARCHAR(50)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Planet
(id INTEGER PRIMARY KEY,
name VARCHAR(30),
age VARCHAR(50),
satelliteID INTEGER,
FOREIGN KEY (satelliteId) REFERENCES Satellite (id)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Galaxy
(id INTEGER PRIMARY KEY,
name VARCHAR(30),
age VARCHAR(50),
planetId INTEGER,
FOREIGN KEY (planetId) REFERENCES Planet (id)
)''')

var_list1 = [
    (1, "C0158974", "100000", 1),
    (2, "C0158974", "100000", 2)
]

sql1 = '''\
    INSERT INTO Galaxy(id, name, age, planetId)
    VALUES(?,?,?,?)
'''

cur.executemany(sql1, var_list1)

var_list2 = [
    (1, "Mercury", "10000", 1),
    (2, "Mars", "50000", 2)
]

sql2 = '''\
    INSERT INTO Planet(id, name, age, satelliteId)
    VALUES(?,?,?,?)
'''

cur.executemany(sql2, var_list2)

var_list3 = [
    (1, "Stone", "5000"),
    (2, "Rock", "400")
]

sql3 = '''\
    INSERT INTO Satellite(id, name, age)
    VALUES(?,?,?)
'''

cur.executemany(sql3, var_list3)

cur.execute('''
    SELECT * FROM Galaxy''')
for i in cur.fetchall():
    print(i)

cur.execute('''
    SELECT COUNT(*) FROM Planet''')
print("Total Planets: ", cur.fetchone()[0])

cur.execute('''
    SELECT AVG(age) FROM Satellite''')
print("AVG age of satellite: ", cur.fetchone()[0])

con.close()

# из таблицы в xml

conn = sqlite3.connect('Space.db')
cursor = conn.cursor()

cursor.execute('''SELECT * FROM Galaxy''')

rows = cursor.fetchall()

doc = xml.dom.minidom.Document()
root = doc.createElement('GalaxyData')
doc.appendChild(root)

for row in rows:
    record = doc.createElement('record')
    root.appendChild(record)
    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('Space_data.xml', 'w') as f:
    f.write(doc.toprettyxml())

conn.close()

# из xml в таблицу

conn1 = sqlite3.connect("Space.db")
cursor = conn1.cursor()
xml_file = 'Space_data.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('record')

for user in users:
    name = user.getElementsByTagName('name')[0].childNodes[0].data
    age = user.getElementsByTagName('age')[0].childNodes[0].data
    planetId = user.getElementsByTagName('planetId')[0].childNodes[0].data

    cursor.execute("INSERT INTO Galaxy (name, age, planetId) VALUES (?, ?, ?)",
                   (name, age, planetId))

conn1.commit()
conn1.close()
