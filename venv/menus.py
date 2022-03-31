from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
import csv

# Data pentru fisierul csv
# BookNameRom,BookNameEng,AuthorName,Read,Own,InstagramReview
#
# A treia fata,-,Agatha Cristie,Y,Y,N
# Noapte Nesfarsita,-,Agatha Cristie,Y,Y,N
# Ceasurile,-,Agatha Cristie,Y,Y,N
# Adversarul secret,-,Agatha Cristie,Y,Y,N
# La Hotelul Bertram,-,Agatha Cristie,Y,Y,N
# Cei cinci purcelusi,-,Agatha Cristie,Y,Y,N
# Conacul dintre dealuri,-,Agatha Cristie,Y,Y,N
# Crima din Mesopotamia,-,Agatha Cristie,Y,Y,N
# Cu cartile pe fata,-,Agatha Cristie,Y,Y,N
# -,And then there were none,Agatha Cristie,Y,Y,N
# Primele cazuri ale lui Poirot,-,Agatha Cristie,Y,Y,N
# 13 la cina,-,Agatha Cristie,Y,Y,N
# Luceafarul,,Mihai Eminescu,Da,Nu,Nu
# Gradina secreta,The secret garden,Frances Hodgson Burnett,Y,Y,Y

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        button1 = Button(master, text="Find books", command=lambda m="1": which_button(m))
        button1.place(relx=0.5, rely=0.15, anchor = "center")

        button2 = Button(master, text="Add a book", command=lambda m="2": which_button(m))
        button2.place(relx=0.5, rely=0.30, anchor="center")


        button3 = Button(master, text="Edit a book", command=lambda m="3": which_button(m))
        button3.place(relx=0.5, rely=0.45, anchor="center")

        button4 = Button(master, text="List all books", command=lambda m="4": which_button(m))
        button4.place(relx=0.5, rely=0.60, anchor="center")

        exitButton = Button(master, text="Exit", command=lambda m="5": which_button(m))
        exitButton.place(relx=0.5, rely=0.75, anchor="center")


    def confirmation(selfs):
        root.title('Exit')
        root.geometry('300x150')

        # click event handler
        def confirm():
            answer = askyesno(title='confirmation',
                              message='Are you sure that you want to quit?')
            if answer:
                root.destroy()

        ttk.Button(
            root,
            text='Exit',
            command=confirm).pack(expand=True)


def which_button(button_press):
    # Printing the text when a button is clicked

    print(button_press)
    p = Window

    if (button_press == "1"):
        print("Ai apasat butonul: Find Books")
        search_books(p)
    elif (button_press == "2"):
        print("Ai apasat butonul: Add a book")
        add_book_window(p)
    elif (button_press == "3"):
        print("Ai apasat butonul: Edit a book")
        edit_book(p)
    elif (button_press == "4"):
        print("Ai apasat butonul: List Books")
        listBooks(p)
        # list_books_window(p)
    elif (button_press == "5"):
        print("Ai apasat butonul: Exit")
        exit()
    elif (button_press == "6"):
        print("Ai apasat butonul: Lista cartilor gasite")
        listBooks(p)


def search_books(self):
    from tkinter import ttk
    from tkinter import messagebox
    import sqlite3
    from tkinter import colorchooser
    import tkinter.ttk as ttk
    import csv
    import os

#     search menu
    ws = Tk()
    Frm = Frame(ws)
    Label(Frm, text='Enter Word to Find:').pack(side=LEFT)
    modify = Entry(Frm)
    modify.pack(side=LEFT, fill=BOTH, expand=2)

    modify.focus_set()

    buttn = Button(Frm, text='Find')
    buttn.pack(side=RIGHT)
    Frm.pack(side=TOP)

    txt = Text(ws)


    def find():
        import tkinter.ttk as ttk
        import csv
        import os

        book_found = False

        txt.tag_remove('found', '1.0', END)
        ser = modify.get()

        book_name = ser.lower() # salvam cuvantul cautat pentru a cauta in baza de date
        with open('booksDBElena.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview")))
            for row in rows:
                if ((book_name in row["BookNameRom"].lower()) or (book_name in row["BookNameEng"].lower()) or (book_name in row["AuthorName"].lower())):
                    book_found = True

        if not book_found:
            import tkinter
            from tkinter import messagebox
            # message box display
            messagebox.showerror("Not found", f"The book '{ser}' is not present in your list!")
        else:
            book_found = False
            import tkinter.ttk as ttk
            import csv
            import os

            root = Tk()

            root.title("Lista tuturor cartilor")
            width = 1430
            height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 1.2) - (width / 1.2)
            y = (screen_height / 1.2) - (height / 1.2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(1, 1)

            TableMargin = Frame(root, width=1800)
            TableMargin.pack(side=TOP)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"), height=700,
                                selectmode="extended",
                                yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('BookNameRom', text="Numele cartii in romana", anchor="c")
            tree.heading('BookNameEng', text="Numele cartii in engleza", anchor="c")
            tree.heading('AuthorName', text="Autor", anchor="c")
            tree.heading('Read', text="Ai citit cartea?", anchor="c")
            tree.heading('Own', text="Este cumparata?", anchor="c")
            tree.heading('InstagramReview', text="Are review pe Instagram?", anchor="c")
            tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
            tree.column('#1', stretch=NO, minwidth=0, width=300, anchor=CENTER)
            tree.column('#2', stretch=NO, minwidth=0, width=300, anchor=CENTER)
            tree.column('#3', stretch=NO, minwidth=0, width=200, anchor=CENTER)
            tree.column('#4', stretch=NO, minwidth=0, width=200, anchor=CENTER)
            tree.column('#5', stretch=NO, minwidth=0, width=200, anchor=CENTER)
            tree.column('#6', stretch=NO, minwidth=0, width=200, anchor=CENTER)

            tree.pack()

            with open("booksDBElena.csv", mode="r") as file:
                rows = csv.DictReader(file, fieldnames=
                ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                for row in rows:
                    if ((row.get("BookNameRom") == "BookNameRom") or (
                            row.get(
                                "BookNameEng") == "BookNameEng")):  # skipping the header row when printing data
                        pass
                    else:
                        # print(
                        #     f"Book name(rom): {row.get('BookNameRom')}, Book name(eng): {row.get('BookNameEng')}, Author: {row.get('AuthorName')}, Read: {row.get('Read')}, Own: {row.get('Own')}, InstagramReview: {row.get('InstagramReview')}.")
                        reader = csv.DictReader(file, fieldnames=
                        ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                        for row in reader:
                            if ((book_name in row["BookNameRom"].lower()) or (
                                    book_name in row["BookNameEng"].lower()) or (
                                    book_name in row["AuthorName"].lower())):
                                book_name_rom = row['BookNameRom']
                                book_name_en = row['BookNameEng']
                                author = row['AuthorName']
                                read = row['Read']
                                own = row['Own']
                                insta = row['InstagramReview']
                                tree.insert("", 0, values=(book_name_rom, book_name_en, author, read, own, insta))


        if ser:
            idx = '1.0'
            while 1:
                idx = txt.search(ser, idx, nocase=1,
                                 stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(ser))

                txt.tag_add('found', idx, lastidx)
                idx = lastidx
            txt.tag_config('found', foreground='blue')
        modify.focus_set()

    buttn.config(command=find)


def add_book_window(self):
    import tkinter as tk

    fields = 'Numele cartii in romana', \
             'Numele cartii in engleza', \
             'Autor', \
             'Ai citit cartea? Y/N', \
             'Este cumparata? Y/N', \
             'Are review pe Instagram? Y/N'

    def fetch(entries):  # luam raspunsurile si le scriem in baza de date
        raspunsuri = []
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            raspunsuri.append(text)
            # print('%s: "%s"' % (field, text))

        book_name_rom = raspunsuri[0]
        book_name_eng = raspunsuri[1]
        author_name = raspunsuri[2]
        is_read = raspunsuri[3]
        is_own = raspunsuri[4]
        instagram_review = raspunsuri[5]

        import csv
        try:
            with open('booksDBElena.csv', mode='r', newline='') as readFile:
                rows = csv.DictReader(readFile, fieldnames=
                ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                # we first check to see if header exists
                try:
                    test_bytes = readFile.read(1024)
                    readFile.seek(0)
                    has_header = csv.Sniffer().has_header(test_bytes)
                # treating the exception where the headers don't exist
                except csv.Error:
                    with open('booksDBElena.csv', mode='w') as writeFile:
                        writer = csv.DictWriter(writeFile, fieldnames=
                        ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                        writer.writeheader()
                    writeFile.close()
                else:
                    print()

            with open('booksDBElena.csv', mode='a', ) as file:  # mode = 'a' appends to the existing list
                writer = csv.DictWriter(file, fieldnames=
                ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                writer.writerow({'BookNameRom': book_name_rom,
                                 'BookNameEng': book_name_eng,
                                 'AuthorName': author_name,
                                 'Read': is_read,
                                 'Own': is_own,
                                 'InstagramReview': instagram_review})
        except IOError:
            print("Unable to read the file!")

    def makeform(root, fields):
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=30, text=field, anchor='e')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))

        return entries

    if __name__ == '__main__':
        root = tk.Tk()
        ents = makeform(root, fields)
        root.bind('<Return>', (lambda event, e=ents: fetch(e)))
        b2 = tk.Button(root, text='Quit', command=root.quit)
        b2.pack(side=tk.RIGHT, padx=5, pady=5)
        b1 = tk.Button(root, text='Adauga',
                       command=(lambda e=ents: fetch(e)))
        b1.pack(side=tk.RIGHT, padx=5, pady=5)
        # root.mainloop()


def edit_book(self):
    from tkinter import ttk
    from tkinter import messagebox
    import sqlite3
    from tkinter import colorchooser
    import tkinter.ttk as ttk
    import csv
    import os

    ws = Tk()
    Frm = Frame(ws)
    Label(Frm, text='Search for a book:').pack(side=LEFT)
    modify = Entry(Frm)
    modify.pack(side=LEFT, fill=BOTH, expand=2)

    modify.focus_set()

    buttn = Button(Frm, text='Find')
    buttn.pack(side=RIGHT)
    Frm.pack(side=TOP)

    txt = Text(ws)

    def find():
        import tkinter.ttk as ttk
        import csv
        import os

        book_found = False

        txt.tag_remove('found', '1.0', END)
        ser = modify.get()

        book_name = ser.lower()  # salvam cuvantul cautat pentru a cauta in baza de date
        with open('booksDBElena.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview")))
            for row in rows:
                if ((book_name in row["BookNameRom"].lower()) or (book_name in row["BookNameEng"].lower()) or (
                        book_name in row["AuthorName"].lower())):
                    book_found = True
                    book_name_rom = row['BookNameRom']
                    book_name_en = row['BookNameEng']
                    author = row['AuthorName']
                    read = row['Read']
                    own = row['Own']
                    insta = row['InstagramReview']


        if not book_found:
            import tkinter
            from tkinter import messagebox

            # hide main window
            root = tkinter.Tk()
            root.withdraw()

            # message box display
            messagebox.showerror("Not found", f"The book '{ser}' is not present in your list!")


        if book_found:
            book_found = False
            import tkinter.ttk as ttk
            import csv
            import os

            root = Tk()

            root.title("Lista tuturor cartilor")
            width = 1430
            height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width / 1.2) - (width / 1.2)
            y = (screen_height / 1.2) - (height / 1.2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.resizable(1, 1)

            TableMargin = Frame(root, width=1800)
            TableMargin.pack(side=TOP)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"), height=700,
                                selectmode="extended",
                                yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('BookNameRom', text="Numele cartii in romana", anchor="c")
            tree.heading('BookNameEng', text="Numele cartii in engleza", anchor="c")
            tree.heading('AuthorName', text="Autor", anchor="c")
            tree.heading('Read', text="Ai citit cartea?", anchor="c")
            tree.heading('Own', text="Este cumparata?", anchor="c")
            tree.heading('InstagramReview', text="Are review pe Instagram?", anchor="c")
            tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
            tree.column('#1', stretch=NO, minwidth=0, width=300, anchor=CENTER)
            tree.column('#2', stretch=NO, minwidth=0, width=300, anchor=CENTER)
            tree.column('#3', stretch=NO, minwidth=0, width=200, anchor=CENTER)
            tree.column('#4', stretch=NO, minwidth=0, width=200, anchor=CENTER)
            tree.column('#5', stretch=NO, minwidth=0, width=200, anchor=CENTER)
            tree.column('#6', stretch=NO, minwidth=0, width=200, anchor=CENTER)

            tree.pack()

            with open("booksDBElena.csv", mode="r") as file:
                rows = csv.DictReader(file, fieldnames=
                ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                for row in rows:
                    if ((row.get("BookNameRom") == "BookNameRom") or (
                            row.get(
                                "BookNameEng") == "BookNameEng")):  # skipping the header row when printing data
                        pass
                    else:
                        # print(
                        #     f"Book name(rom): {row.get('BookNameRom')}, Book name(eng): {row.get('BookNameEng')}, Author: {row.get('AuthorName')}, Read: {row.get('Read')}, Own: {row.get('Own')}, InstagramReview: {row.get('InstagramReview')}.")
                        reader = csv.DictReader(file, fieldnames=
                        ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                        for row in reader:
                            if ((book_name in row["BookNameRom"].lower()) or (
                                    book_name in row["BookNameEng"].lower()) or (
                                    book_name in row["AuthorName"].lower())):
                                book_name_rom = row['BookNameRom']
                                book_name_en = row['BookNameEng']
                                author = row['AuthorName']
                                read = row['Read']
                                own = row['Own']
                                insta = row['InstagramReview']
                                tree.insert("", 0, values=(book_name_rom, book_name_en, author, read, own, insta))

        if ser:
            idx = '1.0'
            while 1:
                idx = txt.search(ser, idx, nocase=1,
                                 stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(ser))

                txt.tag_add('found', idx, lastidx)
                idx = lastidx
            txt.tag_config('found', foreground='blue')
        modify.focus_set()

    buttn.config(command=find)

    def fin2222():
        import tkinter.ttk as ttk
        import csv
        import os

        book_found = False

        txt.tag_remove('found', '1.0', END)
        ser = modify.get()

        book_name = ser.lower() # salvam cuvantul cautat pentru a cauta in baza de date
        with open('booksDBElena.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview")))
            for row in rows:
                if ((book_name in row["BookNameRom"].lower()) or (book_name in row["BookNameEng"].lower()) or (book_name in row["AuthorName"].lower())):
                    book_name_rom = row['BookNameRom']
                    book_name_en = row['BookNameEng']
                    author = row['AuthorName']
                    read = row['Read']
                    own = row['Own']
                    insta = row['InstagramReview']
                    # tree.insert("", 0, values=(book_name_rom, book_name_en, author, read, own, insta))
                    book_found = True

        import tkinter as tk

        fields = 'Numele cartii in romana', \
                 'Numele cartii in engleza', \
                 'Autor', \
                 'Ai citit cartea? Y/N', \
                 'Este cumparata? Y/N', \
                 'Are review pe Instagram? Y/N'

        entries = book_name, \
                book_name_en, \
                author, \
                read, \
                own, \
                insta

        i = 0;
        while (i < 6):
            print(f'{fields[i], entries[i]}')
            i += 1;

        def fetch(entries):  # luam raspunsurile si le scriem in baza de date
            raspunsuri = [book_name_rom, book_name_en, author, read, own, insta]
            for raspuns in raspunsuri:
                field = entry[0]
                text = entry[1].get()
                raspunsuri.append(text)
                # print('%s: "%s"' % (field, text))

            book_name_rom = raspunsuri[0]
            book_name_eng = raspunsuri[1]
            author_name = raspunsuri[2]
            is_read = raspunsuri[3]
            is_own = raspunsuri[4]
            instagram_review = raspunsuri[5]

            import csv
            try:
                with open('booksDBElena.csv', mode='r', newline='') as readFile:
                    rows = csv.DictReader(readFile, fieldnames=
                    ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                    # we first check to see if header exists
                    try:
                        test_bytes = readFile.read(1024)
                        readFile.seek(0)
                        has_header = csv.Sniffer().has_header(test_bytes)
                    # treating the exception where the headers don't exist
                    except csv.Error:
                        with open('booksDBElena.csv', mode='w') as writeFile:
                            writer = csv.DictWriter(writeFile, fieldnames=
                            ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                            writer.writeheader()
                        writeFile.close()
                    else:
                        print()

                with open('booksDBElena.csv', mode='a', ) as file:  # mode = 'a' appends to the existing list
                    writer = csv.DictWriter(file, fieldnames=
                    ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                    writer.writerow({'BookNameRom': book_name_rom,
                                     'BookNameEng': book_name_eng,
                                     'AuthorName': author_name,
                                     'Read': is_read,
                                     'Own': is_own,
                                     'InstagramReview': instagram_review})
            except IOError:
                print("Unable to read the file!")

        def makeform(root, fields):
            entries = []
            for field in fields:
                row = tk.Frame(root)
                lab = tk.Label(row, width=30, text=field, anchor='e')
                ent = tk.Entry(row)
                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                lab.pack(side=tk.LEFT)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
                entries.append((field, ent))

            return entries

        if __name__ == '__main__':
            root = tk.Tk()
            ents = makeform(root, fields)
            root.bind('<Return>', (lambda event, e=ents: fetch(e)))
            b2 = tk.Button(root, text='Quit', command=root.quit)
            b2.pack(side=tk.RIGHT, padx=5, pady=5)
            b1 = tk.Button(root, text='Adauga',
                           command=(lambda e=ents: fetch(e)))
            b1.pack(side=tk.RIGHT, padx=5, pady=5)
            # root.mainloop()


def listBooks(self):
    import tkinter.ttk as ttk
    import csv
    import os

    root = Tk()

    root.title("Lista tuturor cartilor")
    width = 1430
    height = 800


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 1.2) - (width / 1.2)
    y = (screen_height / 1.2) - (height / 1.2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(1, 1)

    TableMargin = Frame(root, width=1800)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"), height=700, selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('BookNameRom', text="Numele cartii in romana", anchor="c")
    tree.heading('BookNameEng', text="Numele cartii in engleza", anchor="c")
    tree.heading('AuthorName', text="Autor", anchor="c")
    tree.heading('Read', text="Ai citit cartea?", anchor="c")
    tree.heading('Own', text="Este cumparata?", anchor="c")
    tree.heading('InstagramReview', text="Are review pe Instagram?", anchor="c")
    tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    tree.column('#1', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    tree.column('#2', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    tree.column('#3', stretch=NO, minwidth=0, width=200, anchor=CENTER)
    tree.column('#4', stretch=NO, minwidth=0, width=200, anchor=CENTER)
    tree.column('#5', stretch=NO, minwidth=0, width=200, anchor=CENTER)
    tree.column('#6', stretch=NO, minwidth=0, width=200, anchor=CENTER)



    tree.pack()



    try:
        with open("booksDBElena.csv", mode="r") as file:
            rows = csv.DictReader(file, fieldnames=
            ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
            for row in rows:
                if ((row.get("BookNameRom") == "BookNameRom") or (
                        row.get("BookNameEng") == "BookNameEng")):  # skipping the header row when printing data
                    pass
                else:
                    # print(
                    #     f"Book name(rom): {row.get('BookNameRom')}, Book name(eng): {row.get('BookNameEng')}, Author: {row.get('AuthorName')}, Read: {row.get('Read')}, Own: {row.get('Own')}, InstagramReview: {row.get('InstagramReview')}.")
                    reader = csv.DictReader(file, fieldnames=
            ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
                    for row in reader:
                        book_name_rom = row['BookNameRom']
                        book_name_en = row['BookNameEng']
                        author = row['AuthorName']
                        read = row['Read']
                        own = row['Own']
                        insta = row['InstagramReview']
                        tree.insert("", 0, values=(book_name_rom, book_name_en, author, read, own, insta))




    except IOError:
        print("Unable to read the file!")




root = Tk()
app = Window(root)
root.wm_title("Book Library")
root.geometry("800x360")
root.mainloop()