import pytest

from whatsappy import Whatsapp
from whatsappy.chat import Group, Chat
from whatsappy.util import Me
from whatsappy.messages import UnreadMessage

whatsapp: Whatsapp = None

def test_login() -> None:
    global whatsapp
    whatsapp = Whatsapp(data_path=r"C:\Users\Italo Seara\AppData\Local\Google\Chrome\User Data\Default", visible=False)

    @whatsapp.event
    def on_message(message: UnreadMessage) -> None:
        pass

    @whatsapp.event
    def on_ready() -> None:
        pass

    whatsapp.run()
    assert whatsapp._is_loaded()

def test_chat() -> None:
    chat = whatsapp.open("Gordelicia")
    assert isinstance(chat, Chat)
    assert chat.name == "Gordelicia"

    chat = whatsapp.open("fabricio da moita")
    assert isinstance(chat, Chat)
    assert chat.name == "Fabrício Da Moita"
    
    group = whatsapp.open("Console")
    assert isinstance(group, Group)

    assert group.name == "Console"
    assert group.description == "A group for testing purposes."
    assert group.participants == 1
    assert group.profile_picture is not None
    
    group.send("Hello, World!", attatchments=[
        r"C:\Users\Italo Seara\Downloads\Atividade 3.pdf", 
        r"C:\Users\Italo Seara\Downloads\planilha.xlsx", 
        r"C:\Users\Italo Seara\Downloads\Calculo_Aplicado_II_-_Italo_Seara.pdf", 
        r"C:\Users\Italo Seara\Downloads\Powerful Leelo.png"
    ], type="auto")
    group.send("Hello, World!\n\nmultiline")

    assert whatsapp.current_chat == group.name

def test_chat_mute() -> None:
    chat = whatsapp.open("Felpudo")
    chat.mute("8 hours")
    assert chat.is_muted
    
    chat.mute("1 week")
    assert chat.is_muted

    chat.mute("Always")
    assert chat.is_muted

    chat.unmute()
    assert not chat.is_muted

    chat.unmute()
    assert not chat.is_muted

def test_me() -> None:
    me = whatsapp.me
    assert isinstance(me, Me)
    assert me.name == "Italo Seara"

def test_unread() -> None:
    unread = whatsapp.unread_messages
    assert isinstance(unread, list)
    
def test_close() -> None:
    whatsapp.close()