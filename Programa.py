import cv2
import sqlite3
import pyautogui, webbrowser
import time
from time import sleep


numero="+525613726213"

conn = sqlite3.connect('mybd.db')
cursor = conn.cursor()

capture= cv2.VideoCapture(0)

while(capture.isOpened):
    ret, frame = capture.read()

    if(cv2.waitKey(1)==ord('s')):
        break

    qrDetector = cv2.QRCodeDetector()

    data, bbox,rectificarImage = qrDetector.detectAndDecode(frame)

    if len(data) > 0:
        cursor.execute("SELECT Nombre FROM usuario WHERE id = ?", (data,))
        resultado = cursor.fetchone()
        if resultado is not None:
            webbrowser.open(F'https://web.whatsapp.com/send?phone={numero}')
            hora_actual = time.localtime()
            sleep(20)
            texto=f"el usuario {resultado}, acaba de llegar a las {hora_actual.tm_hour}:{hora_actual.tm_min}:{hora_actual.tm_sec}"
            pyautogui.typewrite(texto)
            pyautogui.press('enter')
        else:
            print(f"El valor '{data}' no existe.")
    else:
        cv2.imshow('webCam', frame)
    resultado=None
    data=None

capture.release()
cv2.destroyAllWindows