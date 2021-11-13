import tkinter as tk
from ptna import *

""" グローバル変数の定義
"""
entry = None
response_area = None
lb = None
action = None
hoso = Hoso('hoso')

""" リストボックスに追加する関数
"""
def putlog(str):
    lb.insert(tkEND, str)

def prompt():
    h = hoso.name
    if (action.get()) == 0:
        h += ":" + hoso.responder.name
        return h + "> "

def talk():
    value = entry.get()
    if not value:
        response_area.configure(text="何？")
    else:
        response = hoso.dialogue(value)
        response_area.configure(text=response)
        putlog(">" + value)
        putlog(prompt() + response)
        entry.delete(0, tk.END)
