__author__ = 'Manu'
'''
Created on Feb 5, 2015

@author: manubhat
'''

from Tkinter import *
from ttk import *
from tkFileDialog import *
from dropbox_auth import *

def browsefile():
    myfile = askopenfile(parent = tab1,mode = 'rb')
#     myobj = dropbox_auth.mydropbox1
    myobj2.encrypt(myfile.name)

def downloadfile():
    fileitem = list_drop.curselection()
    fileitemsel = list_drop.get(fileitem)
    myobj2.downloaddropbox(fileitemsel)


def refreshfile():
    list_drop.delete(0, END)
    filelist = myobj2.listdropbox()
    for fileitem in filelist:
        list_drop.insert(END, str(fileitem).replace('/', ''))

myobj2 = mydropbox1()

root = Tk()
root.title('One stop cloud synchronization')
#Create a notebook
note = Notebook(root)
tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
#Create Buttons
upload_drop = Button(tab1, text='Upload', command=browsefile)
exit_drop1 = Button(tab1, text='Exit', command=root.destroy)
upload_drop.pack(padx = 10,pady=5)
exit_drop1.pack(padx=10,pady=50)

download_drop = Button(tab2, text='Download', command=downloadfile)
exit_drop2 = Button(tab2, text='Refresh', command=refreshfile)
download_drop.pack(padx = 10,pady=5)
exit_drop2.pack(padx=10,pady=5)

list_drop = Listbox(tab2, width=10,height=10)
list_drop.pack(pady=10, fill=BOTH, expand=True)
scroll_drop = Scrollbar(list_drop)
scroll_drop.pack(side=RIGHT, fill=Y)
scroll_drop.config(command=list_drop.yview)

download_gd = Button(tab3, text='Download', command=root.destroy)
exit_gd = Button(tab3, text='Refresh', command=root.destroy)
download_gd.pack(padx = 10,pady=5)
exit_gd.pack(padx=10,pady=5)

note.add(tab1, text = "Upload to Dropbox/Google Drive")
note.add(tab2, text = "Download from Dropbox")
note.add(tab3, text = "Download from Google Drive")
note.pack(fill='both', expand='yes')

refreshfile()

root.geometry("500x500")

root.mainloop()