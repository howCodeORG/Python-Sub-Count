import tkinter as tk
import base64
import os
from tkinter import ttk
from tkinter import messagebox as msgbox
import urllib.request
import json

def check(*args):
    name = varentry1.get()
    if not name:
        msgbox.showwarning("Error", "Please enter username!")
        return
    try:
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name + "&key=" + key).read()
    except urllib.error.HTTPError as err:
        msgbox.showerror("Error", "{}. Check if username does NOT contain spaces!".format(err))
        return
    try:
        jsondata = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    except IndexError as err:
        msgbox.showerror("Error", "{}. Check if you typed correct username!".format(str(err).capitalize()))
        return
    subs = name + " has " + "{:,d}".format(int(jsondata)) + " subscribers!"
    msgbox.showinfo("Subscriber Count", subs)

icon = """
AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAABMLAAATCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/BwAA/0cAAP+VAAD/vgAA/9gAAP/zAAD/8wAA/9gAAP++AAD/lQAA/0cAAP8HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/GgAA/5kAAP/zAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//MAAP+ZAAD/GgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/CAAA/4EAAP/1AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP/1AAD/gQAA/wcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/xgAAP/HAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/xgAA/xgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8uAAD/4wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/4wAA/y4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/GQAA/+QAAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/4wAA/xgAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/wgAAP/HAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/xgAA/wcAAAAAAAAAAAAAAAAAAAAAAAD/ggAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/gQAAAAAAAAAAAAAAAAAA/xoAAP/1AAD//wAA//8AAP//AAD//wQE//8cHP//MTH//0ZG//9bW///bW3//3Nz//92dv//enr//3p6//92dv//c3P//21t//9bW///Rkb//zEx//8cHP//BAT//wAA//8AAP//AAD//wAA//8AAP/1AAD/GQAAAAAAAAAAAAD/mgAA//8AAP//AAD//wAA//9FRf//4uL////////////////////////////////////////////////////////////////////////////////////////i4v//RET//wAA//8AAP//AAD//wAA//8AAP+ZAAAAAAAA/wcAAP/zAAD//wAA//8AAP//DQ3//+np///////////////////////////////////////////////////////////////////////////////////////////////////p6f//DQ3//wAA//8AAP//AAD//wAA//MAAP8HAAD/SAAA//8AAP//AAD//wAA//9BQf////////////////////////////////////////////////////////////////////////////////////////////////////////////9AQP//AAD//wAA//8AAP//AAD//wAA/0cAAP+VAAD//wAA//8AAP//AAD//2Bg////////////////////////////////////////+/v//////////////////////////////////////////////////////////////////19f//8AAP//AAD//wAA//8AAP//AAD/lQAA/78AAP//AAD//wAA//8AAP//f3/////////////////////////////////////////U1P//Ojr//8rK////////////////////////////////////////////////////////fn7//wAA//8AAP//AAD//wAA//8AAP++AAD/2QAA//8AAP//AAD//wAA//+Tk////////////////////////////////////////9TU//8AAP//AQH//15e///k5P////////////////////////////////////////////+Tk///AAD//wAA//8AAP//AAD//wAA/9gAAP/zAAD//wAA//8AAP//AAD//5yc////////////////////////////////////////1NT//wAA//8AAP//AAD//woK//+Bgf//9fX//////////////////////////////////5ub//8AAP//AAD//wAA//8AAP//AAD/8wAA//MAAP//AAD//wAA//8AAP//nJz////////////////////////////////////////U1P//AAD//wAA//8AAP//Cgr//4CA///19f//////////////////////////////////m5v//wAA//8AAP//AAD//wAA//8AAP/zAAD/2QAA//8AAP//AAD//wAA//+Tk////////////////////////////////////////9TU//8AAP//AQH//11d///k5P////////////////////////////////////////////+Tk///AAD//wAA//8AAP//AAD//wAA/9gAAP+/AAD//wAA//8AAP//AAD//39/////////////////////////////////////////1NT//zo6///Jyf///////////////////////////////////////////////////////39///8AAP//AAD//wAA//8AAP//AAD/vgAA/5UAAP//AAD//wAA//8AAP//YGD////////////////////////////////////////7+///////////////////////////////////////////////////////////////////YWH//wAA//8AAP//AAD//wAA//8AAP+VAAD/SAAA//8AAP//AAD//wAA//9BQf////////////////////////////////////////////////////////////////////////////////////////////////////////////9DQ///AAD//wAA//8AAP//AAD//wAA/0cAAP8IAAD/9AAA//8AAP//AAD//w0N///q6v//////////////////////////////////////////////////////////////////////////////////////////////////6+v//w8P//8AAP//AAD//wAA//8AAP/zAAD/BwAAAAAAAP+aAAD//wAA//8AAP//AAD//0VF///i4v///////////////////////////////////////////////////////////////////////////////////////+Li//9HR///AAD//wAA//8AAP//AAD//wAA/5kAAAAAAAAAAAAA/xoAAP/1AAD//wAA//8AAP//AAD//wUF//8dHf//MjL//0dH//9cXP//bm7//3R0//93d///enr//3p6//93d///dHT//25u//9cXP//R0f//zIy//8dHf//BQX//wAA//8AAP//AAD//wAA//8AAP/1AAD/GgAAAAAAAAAAAAAAAAAA/4IAAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA/4EAAAAAAAAAAAAAAAAAAAAAAAD/CAAA/8gAAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP/HAAD/BwAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/GQAA/+QAAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/4wAA/xgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/LgAA/+QAAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA/+MAAP8uAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/GQAA/8cAAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP/HAAD/GAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/CAAA/4IAAP/1AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP/1AAD/ggAA/wgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/xoAAP+aAAD/8wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP/zAAD/mgAA/xoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8HAAD/SAAA/5UAAP+/AAD/2QAA//MAAP/zAAD/2QAA/78AAP+VAAD/SAAA/wcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/8AD//8AAP/8AAA/+AAAH/AAAA/gAAAHwAAAA8AAAAOAAAABgAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAGAAAABwAAAA8AAAAPgAAAH8AAAD/gAAB/8AAA//wAA///AA/8=
"""
icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()
key = "INSERT KEY HERE"
root = tk.Tk()
root.wm_iconbitmap(tempFile)
root.title("Subscriber Count")
os.remove(tempFile)
varentry1 = tk.StringVar()
lbl_1 = tk.Label(root, text="Username")
entry_1 = ttk.Entry(root, textvariable=varentry1)
btn_1 = ttk.Button(root, text="Check subscribers!", command=check)
entry_1.bind("<Return>", check)
lbl_1.grid(row=0, column=0, padx=10, pady=10)
entry_1.grid(row=0, column=1, padx=(0, 10))
btn_1.grid(row=1, column=1, pady=(0,10))
root.mainloop()