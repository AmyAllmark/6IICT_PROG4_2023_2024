"""
Maak een YTB 2 MP4 app. 
Hier kan je een URL ingeven, een resolutie kiezen en deze video naar je toestel downloaden. 
Hiernaast kan je ook extra info ophalen van de URL.

"""
from pytube import YouTube



def download_video():
    url = Entry_URL.get()
    print(url)
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4", progressive=True, resolution="720p").first()
    stream.download(output_path=r"C:\Users\AlAm271206\Downloads")

import tkinter as tk
app = tk.Tk()



label_URL= tk.Label(master=app, text= "Geef een URL in van YouTube:")
label_URL.grid(row=0,column=0,columnspan=2)

Entry_URL= tk.Entry(master=app, width=50)
Entry_URL.grid(row=1,column=0,columnspan=2, padx= 20)


Rezolutie_tekst= tk.Label(master=app, text= "Welke rezolutie downloaden:")
Rezolutie_tekst.grid(row=2,column=0,columnspan=2)


resoluties= ["720p", "360p"]
resolutie_var=tk.StringVar(app)
resolutie_var.set(resoluties[0])
resolutie_menu = tk.OptionMenu(app, resolutie_var, *resoluties)
resolutie_menu.grid(row=3,column=0, columnspan=2)

Downloaden=tk.Button(master=app,text= "Download", command=download_video)
Downloaden.grid(row=4, column=0,columnspan=2,pady=10)





















app.mainloop()
