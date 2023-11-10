import qrcode
import sqlite3


nombre = input("Ingrese el nombre del usuario: ")
id = input("Ingrese el id del usuario: ")

conn = sqlite3.connect('mybd.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO usuario (Nombre, id) VALUES (?, ?)", (nombre, id))
conn.commit()
conn.close()

qr = qrcode.QRCode(version=1, box_size=10,border=5)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill='black',back_color='white')
img.save(F'{nombre}.png')