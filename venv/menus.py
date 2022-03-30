from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
import csv

# Data pentru fisierul csv
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
        # addBook(p)
        add_book_window(p)
    elif (button_press == "3"):
        print("Ai apasat butonul: Edit a book")
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


def addBook(self):
    import tkinter as tk
    from tkinter import ttk

    class App(tk.Tk):
        def __init__(self):
            super().__init__()

            self.title('Treeview demo')
            self.geometry('620x200')

            self.tree = self.create_tree_widget()

        # def create_tree_widget(self):
        #     columns = ('first_name', 'last_name', 'email')
        #     tree = ttk.Treeview(self, columns=columns, show='headings')
        #
        #     # define headings
        #     tree.heading('first_name', text='First Name')
        #     tree.heading('last_name', text='Last Name')
        #     tree.heading('email', text='Email')
        #
        #     tree.grid(row=0, column=0, sticky=tk.NSEW)
        #
        #     # adding an item
        #     tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))
        #
        #     # insert a the end
        #     tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))
        #
        #     # insert at the beginning
        #     tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))
        #
        #     return tree

    if __name__ == '__main__':
        app = App()
        app.mainloop()


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


def editBook(self):
    print("Test commit1")
    book_name = input("Enter book name: ")
    import csv
    rows = []
    rows_list_rom = []
    rows_list_eng = []
    try:
        with open('booksDBElena.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview")))
            for row in rows:
                print(f'Aici printam prima oara ce valoarea avem pentru book name ' + book_name)
                rows_list_rom.append(row["BookNameRom"])  # we store every rom book name in a list
                print(f'Aici printam in romana ce valoari avem pentru book name rom ' + rows_list_rom)
                rows_list_eng.append(row["BookNameEng"])  # we store every eng book name in a list
                print(f'Aici printam in engleza ce valoari avem pentru book name eng ' + rows_list_eng)

            if ((book_name not in rows_list_rom) or (
                    book_name not in rows_list_eng)):  # we search the book the user typed in our list
                add_new_book = input(f' The {book_name} book does not exits. Would you like to add it? (Y/N)? ')
                if add_new_book.upper() == "N":
                    return
                else:
                    addBook()
                    return
            else:
                book_read = input("Is the book read? (Y/N)? ")
                if book_read.upper() == 'Y':
                    book_read = True
                else:
                    book_read = False
                book_own = input("Is the book own? (Y/N)? ")
                if book_own.upper() == 'Y':
                    book_own = True
                else:
                    book_own = False
                instagram_review = input("Does it have a review on Instagram? (Y/N)? ")
                if instagram_review.upper() == 'Y':
                    instagram_review = True
                else:
                    instagram_review = False
                rows = []

        with open('booksDBElena.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview")))
            for row in rows:
                if ((row["BookNameRom"] == book_name) or ((row["BookNameEng"] == book_name))):
                    row["Read"] = book_read
                    row["Own"] = book_own
                    row["InstagramReview"] = instagram_review
                    break
        with open('booksDBElena.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=
            ["BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview"])
            csv_writer.writerows(rows)
        print("Book was updated successfully!")
    except IOError:
        print("Unable to read the file! ")


def add_book_window(self):
    def close_window():
        top.destroy()

    import tkinter as tk


    fields = 'Numele cartii in romana',\
             'Numele cartii in engleza',\
             'Autor', \
             'Ai citit cartea? Y/N', \
             'Este cumparata? Y/N', \
             'Are review pe Instagram? Y/N'
    

    def fetch(entries): # luam raspunsurile si le scriem in baza de date
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

        txt.tag_remove('found', '1.0', END)
        ser = modify.get()

        book_name = ser.lower() # salvam cuvantul cautat pentru a cauta in baza de date
        with open('booksDBElena.csv', mode='r') as file:
            rows = list(csv.DictReader(file, fieldnames=(
                "BookNameRom", "BookNameEng", "AuthorName", "Read", "Own", "InstagramReview")))
            for row in rows:
                if ((book_name in row["BookNameRom"].lower()) or (book_name in row["BookNameEng"].lower()) or (book_name in row["AuthorName"].lower())):
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
                                        if ((book_name in row["BookNameRom"].lower()) or (book_name in row["BookNameEng"].lower()) or (book_name in row["AuthorName"].lower())):
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


# def search_books(self):
#     import tkinter as tk
#     from tkinter import ttk
#     import csv
#
#     app = tk.Tk()
#     app.title('Search book')
#     app.geometry('800x500')
#     x = StringVar()
#     y = StringVar()
#     z = StringVar()
#
#     file = r'booksDBElena.csv'
#
#     f = open(file, 'r')
#     csvreader = csv.reader(f)
#     csvreader_list = list(csvreader)
#
#     # print(csvreader_list)
#
#     label1 = tk.Label(app, text="Cauta numele cartii in romana: ", font="Helvetica 12", fg="white", bg="#460B05")
#     label1.place(x=10, y=10)
#     search1 = tk.Entry(app, textvariable=x)
#     search1.place(x=80, y=10, height=23, width=200)
#
#     label2 = tk.Label(app, text="Cauta numele cartii in engleza ", font="Helvetica 12", fg="white", bg="#460B05")
#     label2.place(x=300, y=10)
#     search2 = tk.Entry(app, textvariable=y)
#     search2.place(x=370, y=10, height=23, width=200)
#
#     label3 = tk.Label(app, text="Cauta dupa autor", font="Helvetica 12", fg="white", bg="#460B05")
#     label3.place(x=580, y=10)
#     search3 = tk.Entry(app, textvariable=z)
#     search3.place(x=630, y=10, height=23, width=200)
#
#     tv = ttk.Treeview(app, columns=('col_1', 'col_2', 'col_3'), show='headings')
#     tv.column('col_1', minwidth=0, width=400)
#     tv.column('col_2', minwidth=0, width=100)
#     tv.column('col_3', minwidth=0, width=100)
#
#     tv.heading('col_1', text='BookNameRom')
#     tv.heading('col_2', text='BookNameEng')
#     tv.heading('col_3', text='AuthorName')
#
#     tv.place(x=100, y=200)
#
#     def search():
#
#         tv.delete(*tv.get_children())
#         word = x.get().title()
#         print(f'ce este word? {word}')
#         word1 = y.get()
#         print(f'ce este word1? {word1}')
#
#         word2 = z.get()
#         print(f'ce este word2? {word2}')
#
#         if x.get():
#             for (i, n, f) in csvreader_list:
#                 if word in i:
#                     tv.insert('', 'end', values=(i, n, f))
#         elif y.get():
#             for (i, n, f) in csvreader_list:
#                 if word1 in n:
#                     tv.insert('', 'end', values=(i, n, f))
#         elif z.get():
#             for (i, n, f) in csvreader_list:
#                 if word2 in f:
#                     tv.insert('', 'end', values=(i, n, f))
#         else:
#             for (i, n, f) in csvreader_list:
#                 tv.insert('', 'end', values=(i, n, f))
#         search1.delete(0, 'end')
#         search2.delete(0, 'end')
#         search3.delete(0, 'end')
#
#     searchbutton = tk.Button(app, text="Search", fg="black", command=search, anchor="center", justify=CENTER)
#     searchbutton.place(x=1, y=50, width=298)


root = Tk()
app = Window(root)
root.wm_title("Book Library")
root.geometry("800x360")
root.mainloop()