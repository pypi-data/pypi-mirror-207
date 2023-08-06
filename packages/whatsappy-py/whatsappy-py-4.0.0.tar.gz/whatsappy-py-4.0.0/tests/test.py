from whatsappy import Whatsapp
from time import sleep

whatsapp = Whatsapp(
    data_path=r"C:\Users\Italo Seara\AppData\Local\Google\Chrome\User Data\Default"
).run()

chat = whatsapp.open("Console")
chat.send("teste", attatchments=[
    "Adson", "Gordelicia", "Fabricio da moita", "Mae linda"
])
sleep(10)

whatsapp.close()