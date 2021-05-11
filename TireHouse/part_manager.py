from tkinter import *
from db import Database
from tkinter import messagebox
from datetime import datetime

db = Database('store.db')


iesireintrare = bool()


def populate_list():
    tires_list.delete(0, END)
    for row in db.fetch():
      tires_list.insert(END, row) 


def populate_list_iesiri():
    iesiri_list.delete(0, END)
    for row in db.fetch_iesiri():
      iesiri_list.insert(END, row) 


def add_item():
    if serieSasiu_text.get() == ''  or client_text.get() == '' or cantitate_text.get() == '' or produs_text.get() == '':
        messagebox.showerror('Campuri necesare', 'Date insuficiente.')
        return
    dataLive = timeRead()
    db.insert(
        serieSasiu_text.get(), 
        nrInmatriculare_text.get(), 
        client_text.get(), 
        dimFata_text.get(), 
        dimSpate_text.get(), 
        profil_text.get(), 
        produs_text.get(), 
        cantitate_text.get(),
        dataLive)


    db.insert_iesiri(
        serieSasiu_text.get(), 
        nrInmatriculare_text.get(), 
        client_text.get(), 
        dimFata_text.get(), 
        dimSpate_text.get(), 
        profil_text.get(), 
        produs_text.get(), 
        cantitate_text.get(),
        dataLive)


    tires_list.delete(0,END)
    iesiri_list.delete(0,END)


    tires_list.insert(END, (
        serieSasiu_text.get(), 
        nrInmatriculare_text.get(), 
        client_text.get(), 
        dimFata_text.get(), 
        dimSpate_text.get(), 
        profil_text.get(), 
        produs_text.get(), 
        cantitate_text.get(),
        dataLive))


    iesiri_list.insert(END, (
        serieSasiu_text.get(), 
        nrInmatriculare_text.get(), 
        client_text.get(), 
        dimFata_text.get(), 
        dimSpate_text.get(), 
        profil_text.get(), 
        produs_text.get(), 
        cantitate_text.get(),
        dataLive))


    clear_text()
    populate_list()


def select_item(event):
    try:
     global selected_item
     index = tires_list.curselection()[0]
     selected_item = tires_list.get(index)

     serieSasiu_entry.delete(0,END)
     serieSasiu_entry.insert(END,selected_item[1])

     nrInmatriculare_entry.delete(0,END)
     nrInmatriculare_entry.insert(END,selected_item[2])

     client_entry.delete(0,END)
     client_entry.insert(END,selected_item[3])

     dimFata_entry.delete(0,END)
     dimFata_entry.insert(END,selected_item[4])

     dimSpate_entry.delete(0,END)
     dimSpate_entry.insert(END,selected_item[5])

     profil_entry.delete(0,END)
     profil_entry.insert(END,selected_item[6])

     produs_entry.delete(0,END)
     produs_entry.insert(END,selected_item[7])

     cantitate_entry.delete(0,END)
     cantitate_entry.insert(END,selected_item[8])
    except IndexError:
        pass



def remove_item():
    response_remove = messagebox.askokcancel('Esti sigur?','Doresti sa stergi acest obiect?')
    if response_remove:
        adauga_iesiri()
        db.remove(selected_item[0])
        clear_text()
        populate_list()
    else:
        return


def clear_text():
    serieSasiu_entry.delete(0,END)
    nrInmatriculare_entry.delete(0,END)
    client_entry.delete(0,END)
    dimFata_entry.delete(0,END)
    dimSpate_entry.delete(0,END)
    profil_entry.delete(0,END)
    produs_entry.delete(0,END)
    cantitate_entry.delete(0,END)
    


def update_item():
    if serieSasiu_text.get() == ''  or client_text.get() == '' or cantitate_text.get() == '' or produs_text.get() == '':
        messagebox.showerror('Campuri necesare', 'Date insuficiente.')
        return
    response_update = messagebox.askokcancel('Esti sigur?','Doresti sa actualizezi acest obiect?')
    if response_update:

        dataLive = timeRead() 

        db.update(selected_item[0], 
            serieSasiu_text.get(), 
            nrInmatriculare_text.get(), 
            client_text.get(), 
            dimFata_text.get(), 
            dimSpate_text.get(), 
            profil_text.get(), 
            produs_text.get(), 
            cantitate_text.get(),
            dataLive)
        populate_list()
    else:
        return

def clear_item():
    clear_text()





def adauga_iesiri():
    if serieSasiu_text.get() == ''  or client_text.get() == '' or cantitate_text.get() == '' or produs_text.get() == '':
        messagebox.showerror('Campuri necesare', 'Date insuficiente.')
        return
    dataLive = timeRead()

    db.insert_iesiri(
        serieSasiu_text.get(), 
        nrInmatriculare_text.get(), 
        client_text.get(), 
        dimFata_text.get(), 
        dimSpate_text.get(), 
        profil_text.get(), 
        produs_text.get(), 
        cantitate_text.get(),
        dataLive)



    iesiri_list.delete(0,END)


    iesiri_list.insert(END, (
        serieSasiu_text.get(), 
        nrInmatriculare_text.get(), 
        client_text.get(), 
        dimFata_text.get(), 
        dimSpate_text.get(), 
        profil_text.get(), 
        produs_text.get(), 
        cantitate_text.get(),
        dataLive))


    clear_text()
    populate_list_iesiri()






#Create window
app = Tk()

###################################################################################################################################################################################
#Layout BONURI IESIRE

top = Toplevel()
top.geometry('865x575')



#Frame label
titlu_frame = Frame(top)
titlu_frame.grid(row = 0, column = 0, columnspan = 2)


#Label titlu
titlu_label = Label(titlu_frame,text='Bonuri de Iesire', font=('bold',14), pady=20)
titlu_label.grid(row  = 0, column = 1)

#Iesiri frame
iesiri_frame = Frame(top)
iesiri_frame.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = 20)


scrollbar_iesiri = Scrollbar(iesiri_frame)
scrollbar_iesiri.pack(side = RIGHT, fill = Y)


#ListBox + scrollbar  iesiri
iesiri_list = Listbox(iesiri_frame, height = 25, width = 90, border = 0, justify = LEFT, font = 14)
iesiri_list.pack()


iesiri_list.configure(yscrollcommand=scrollbar_iesiri.set)
scrollbar_iesiri.configure(command = iesiri_list.yview)
iesiri_list.pack(expand = TRUE, fill = BOTH)



def openIesiri():
    return True



##################################################################################################################################################################################


#Frame Labels + Entry
frame_label_entry = Frame(app)
frame_label_entry.grid(row = 0, column = 0, rowspan = 7, columnspan = 2)


#Serie Sasiu  Label+Entry
serieSasiu_text = StringVar()
serieSasiu_label = Label(frame_label_entry, text='Serie sasiu:', font=('bold',14), pady=20)
serieSasiu_label.grid(row=0,column=0, padx = 5, columnspan=1)
serieSasiu_entry = Entry(frame_label_entry,textvariable=serieSasiu_text)
serieSasiu_entry.grid(row=0,column=1, padx = 5)



#Numar Inmariculare Label+Entry
nrInmatriculare_text = StringVar()
nrInmatriculare_label = Label(frame_label_entry, text='Numar inmatriculare:', font=('bold',14),pady=20)
nrInmatriculare_label.grid(row=1,column=0)
nrInmatriculare_entry = Entry(frame_label_entry,textvariable=nrInmatriculare_text)
nrInmatriculare_entry.grid(row=1, column=1)




#Client Label+Entry
client_text = StringVar()
client_label = Label(frame_label_entry, text='Client:', font=('bold',14), pady=20)
client_label.grid(row=2,column=0)
client_entry = Entry(frame_label_entry,textvariable=client_text)
client_entry.grid(row=2,column=1)


#Dimensiune Fata Label+Entry
dimFata_text = StringVar()
dimFata_label = Label(frame_label_entry, text='Dimensiune Fata:', font=('bold',14), pady=20)
dimFata_label.grid(row=3,column=0)
dimFata_entry = Entry(frame_label_entry,textvariable=dimFata_text)
dimFata_entry.grid(row=3,column=1)





#Dimensiune Spate  Label+Entry
dimSpate_text = StringVar()
dimSpate_label = Label(frame_label_entry, text='Dimensiune Spate:', font=('bold',14), pady=20)
dimSpate_label.grid(row=4,column=0)
dimSpate_entry = Entry(frame_label_entry,textvariable=dimSpate_text)
dimSpate_entry.grid(row=4,column=1)



#Profil Label+Entry
profil_text = StringVar()
profil_label = Label(frame_label_entry, text='Profil:', font=('bold',14), pady=20)
profil_label.grid(row=5,column=0)
profil_entry = Entry(frame_label_entry,textvariable=profil_text)
profil_entry.grid(row=5,column=1)



#Produs Label+Entry
produs_text = StringVar()
produs_label = Label(frame_label_entry, text='Produs:', font=('bold',14), pady=20)
produs_label.grid(row=6,column=0)
produs_entry = Entry(frame_label_entry,textvariable=produs_text)
produs_entry.grid(row=6,column=1)


#Cantitate Label+Entry
cantitate_text = StringVar()
cantitate_label = Label(frame_label_entry, text='Cantitate:', font=('bold',14), pady=20)
cantitate_label.grid(row=7,column=0)
cantitate_entry = Entry(frame_label_entry,textvariable=cantitate_text)
cantitate_entry.grid(row=7,column=1)





#Frame pentru lista
frame_list = Frame(app, padx = 5, pady = 5)
frame_list.grid(row = 0, column = 2, columnspan = 4, rowspan = 8, pady = 20, padx = 20, sticky = NSEW)


#Scroll Bar
scrollbar = Scrollbar(frame_list)
#scrollbar.grid(row = 0, column = 5, rowspan = 8, sticky = N+S)
scrollbar.pack(side = RIGHT, fill = Y)

#Tire list
tires_list = Listbox(frame_list, height = 35, width = 100, border = 0, justify = LEFT, font = 14)
#tires_list.grid(row = 0, column = 2, columnspan = 3, rowspan = 8, pady = 20, padx = 20)
app.grid_columnconfigure(2,weight = 1)
app.grid_rowconfigure(0,weight = 1)
tires_list.pack(expand = TRUE, fill = BOTH)
#Set scroll to listbox
tires_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command = tires_list.yview)

#Bind select
tires_list.bind('<<ListboxSelect>>', select_item)


#Frame buttons
frame_buttons = Frame(app)
frame_buttons.grid(row = 0, column = 6, rowspan = 5, columnspan = 1, padx = 20)

#Buttons
add_btn = Button(frame_buttons, text = 'Add Tire', width = 12, command = add_item)
add_btn.grid(row = 0, column = 6, pady = 20)

remove_btn = Button(frame_buttons, text = 'Remove Tire', width = 12, command = remove_item)
remove_btn.grid(row = 1, column = 6, pady = 20)

update_btn = Button(frame_buttons, text = 'Update Tire', width = 12, command = update_item)
update_btn.grid(row = 2, column = 6, pady = 20)

clear_btn = Button(frame_buttons, text = 'Clear Tire', width = 12, command = clear_item)
clear_btn.grid(row = 3, column = 6, pady = 20)

iesiri_btn = Button(frame_buttons, text = "Bonuri de Iesire", width = 12, command = openIesiri)
iesiri_btn.grid(row = 4, column = 6, pady = 40)






#Data live
def timeRead():
    now = datetime.now()
    t = now.strftime("%d/%m/%Y, %H:%M:%S")
    app.after(1000, timeRead)
    return t


def clock():
    now = datetime.now()
    t = now.strftime("%d/%m/%Y, %H:%M:%S, %m%m")
    app.after(500, clock)
    return print(t)



app.title('TireHouse')
app.geometry('1500x725')
app.minsize(width = 1500, height = 700)
app.config(bg = 'lightgray')
#Populate with tires ^.^
populate_list()
populate_list_iesiri()


#start 
app.mainloop()
