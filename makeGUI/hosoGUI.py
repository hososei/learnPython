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

""" 画面描画関数
"""
def run():
    global entry, response_area,lb,action

    root = tk.TK()
    root.geometry("880*560")
    root.title("Intelligent Agent : ")
    font = ("Helevetica",14)
    font_log=("Helevetica",11)

    menubar = tk.Menu(root)
    root.config(menu=menubar)
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label="ファイル", menu=filemenu)
    filemenu.add_command(label="閉じる", command=root.destroy)
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label="オプション", menu=optionmenu)
    optionmenu.add_radiobutton(
        label="Responderを表示",
        variable = action,
        value = 0
    )
