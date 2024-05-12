import cgi
import sqlite3

print("Content-type: text/html\n")

form = cgi.FieldStorage()
text1 = form.getfirst("GalaxyId", "не задано")
text2 = form.getfirst("Galaxy", "не задано")
text3 = form.getfirst("AgeGalaxy", "не задано")
text4 = form.getfirst("planetId", "не задано")

print(text1)
print(text2)
print(text3)
print(text4)

print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Обработка галактик</title>
    </head>
    <body>""")
# print("<h1>Обработка галактик</h1>")
# #print("<p>Книга: {}</p>".format(text1))
# #print("<p>Автор: {}</p>".format(text2))
# print("<p>Id Галактики: %s</p>" % text1)
# print("<p>Галактика: %s</p>" % text2)
# print("<p>Возраст галактики: %s</p>" % text3)
# print("<p>Id планеты: %s</p>" % text4)



con = sqlite3.connect("Space.db")
cursor = con.cursor()

try:
    cursor.execute("INSERT INTO Galaxy (id, name, age, planetId) VALUES (?, ?, ?, ?)", (text1, text2, text3, text4))
    con.commit()
    print("<h2>Данные успешно добавлены в базу данных!</h2>")
except sqlite3.Error as e:
    print("<h2>Произошла ошибка при добавлении данных в базу данных:</h2>")
    print("<p>{}</p>".format(str(e)))


con.close()

print("</body> </html>")

