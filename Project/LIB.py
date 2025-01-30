from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from tkinter import Toplevel
import csv


class Library_Management_System:
    
    def __init__(self):
        
                            #############################    Window SETUP   ############################################ 
                            
                                                        #Create the main window
        self.root = Tk()
                
                                    #Set the width and height of the window using the screen's dimensions
                                    
        Screen_Width = self.root.winfo_screenheight()
        Screen_Height = self.root.winfo_screenwidth()
        self.root.geometry(f"{Screen_Height}x{Screen_Width}")
        self.root.title("Group 1 Library Management System")
        self.root.resizable(False, False)
        self.root.state("zoomed")
        
                                                    #Setting the icon of the window
                
        icon_image = PhotoImage(file = "D:\\Documents\\Programming\\Tkinter\\Tkinter Project\\Project\\PL.png")
        self.root.iconphoto(True, icon_image) 
        
                    ##################################      HEADER SETUP     ###########################################
        
                                                    #setting the header and image
                                                    
        HeadImage = ImageTk.PhotoImage(Image.open("D:\\Documents\\Programming\\Tkinter\\Tkinter Project\\Project\\PL.png"))
        self.Label = Label(self.root, text = "Library Management System", image = HeadImage, fg = "#C50F10", font = ("Arial", 27, "bold"), compound = "left", relief = "groove", bd = 10, pady = 10)
        self.Label.pack(fill = 'x')
        
        
                    ##################################      MAIN PAGE SETUP     ###########################################
        
                                                            #Variables
                                                
        global Tree
        Tree = None
        MType = StringVar()
        RNumber = StringVar()
        Title = StringVar()
        FName = StringVar()
        SName = StringVar()
        Telephone = StringVar()
        BiD = StringVar()
        BTitle = StringVar()
        Author = StringVar()
        DBorrowed = StringVar()
        DDate = StringVar()
        LRFine = StringVar()
        self.ListOfBooks = {}

                                                                #Functions  
                                                                      
        def LoadBooks():
            with open("BookList.csv", mode='r', newline = '') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    self.ListOfBooks[row[0]] = row[1]
        LoadBooks()

        def SaveBooks(Title, Author, filename = "BookList.csv"):
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([Title, Author])

        def DisplayData():
            
            Administrator_Code = "Libarian"
            AdminSubmit = StringVar()
            SelectedValue = self.Combo1.get()
            
            if SelectedValue == "Administrator":
                
                def Submit():
                    
                    GetValue = AdminSubmit.get()
                    
                    if GetValue == Administrator_Code:
                        messagebox.showinfo("Message", "Login Success")
                        
                        TableWindow = Toplevel(self.root)
                        TableWindow.geometry("500x500")
                        TableWindow.title("Records")
                        TableWindow.state("zoomed")
                        
                        global Tree
                        Tree = ttk.Treeview(TableWindow, columns=("MType", "RNumber", "Title", "FName", "SName", "Telephone", "BTitle", "DBorrowed", "DDue"), show = "headings")
                        Tree.pack(expand = True, fill = "both")   
                        
                        Tree.heading("MType", text="Membership Type")
                        Tree.heading("RNumber", text="Reference Number")
                        Tree.heading("Title", text="Title")
                        Tree.heading("FName", text="First Name")
                        Tree.heading("SName", text="Surname")
                        Tree.heading("Telephone", text="Telephone")
                        Tree.heading("BTitle", text="Book Title")
                        Tree.heading("DBorrowed", text="Date Borrowed")
                        Tree.heading("DDue", text="Date Due")
                        
                        for col in Tree["columns"]:
                            Tree.column(col, anchor="center")
                            
                        with open('Borrowed Books.csv', newline = '') as csvfile:
                            reader = csv.reader(csvfile)
                            for row in reader:
                                Tree.insert("", "end", values = row)
                    else:
                        messagebox.showerror("Message", "Wrong Password")
                    
                def OpenNewWindow():
                
                    NewWindow = Toplevel(self.root)
                    NewWindow.title("Confirmation")
                    NewWindow.geometry("220x200")
                    NewWindow.resizable(False, False)
                        
                    Label1 = Label(NewWindow, text = "Enter Admin Password to proceed")
                    Label1.grid(row = 0, column = 0, pady = 20, padx = 20)
                    
                    Entry1 = Entry(NewWindow, textvariable = AdminSubmit, show = "*")
                    Entry1.grid(row = 1, column = 0)
                    
                    Button1 = Button(NewWindow, text = "Submit", pady = 2, padx = 2, command = Submit)
                    Button1.grid(row = 2, column = 0, pady = 20)
                        
                OpenNewWindow()
            
        def Reset():
            
            MType.set("")
            RNumber.set("")
            Title.set("")
            FName.set("")
            SName.set("")
            Telephone.set("")
            BiD.set("")
            BTitle.set("")
            Author.set("")
            DBorrowed.set("")
            DDate.set("")
            LRFine.set("")
        
        def ComboValue(event):
            
            SelectedValue = self.Combo1.get()
            
            if SelectedValue == "Student":
                self.Entry22.config(state = "normal")
                self.Label1.config(text = "Reference Number:", state = "normal")
                self.Button1.config(state = "normal")
                self.Button2.config(state = "disabled")
                self.Button3.config(state = "disabled")
                self.Button4.config(state = "normal")
                self.Button5.config(state = "disabled")
                
            elif SelectedValue == "Administrator":
                self.Entry22.config(state = "disabled")
                RNumber.set("")
                self.Label1.config(text = "Disabled", state = "disabled")
                self.Button1.config(state = "normal")
                self.Button2.config(state = "normal")
                self.Button3.config(state = "normal")
                self.Button4.config(state = "normal")
                self.Button5.config(state = "normal")
                
            elif SelectedValue == "Guest":
                self.Entry22.config(state = "disabled")
                RNumber.set("")
                self.Label1.config(text = "Disabled", state = "disabled")
                self.Button1.config(state = "normal")
                self.Button2.config(state = "disabled")
                self.Button3.config(state = "disabled")
                self.Button4.config(state = "normal")
                self.Button5.config(state = "disabled")
                
            else:
                self.Entry22.config(state = "disabled")
                RNumber.set("")
                self.Label1.config(text = "Disabled", state = "disabled")
                self.Button1.config(state = "normal")
                self.Button2.config(state = "disabled")
                self.Button3.config(state = "disabled")
                self.Button4.config(state = "normal")
                self.Button5.config(state = "disabled")
                
        def Exit():
            
            Message = messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
            
            if Message:
                print("User chose Yes")
                self.root.destroy()
            else:
                print("User chose No")
                
        def On_Select(event):
            
            Selected_Index = self.BookList.curselection()
            
            if Selected_Index:    
                         
                Index = 1 + Selected_Index[0]   
                Selected_List = self.BookList.get(Selected_Index)
                
                Aut = self.ListOfBooks[Selected_List]
                Now = datetime.now()
                
                CurrentDate = Now.strftime("%A, %B %d, %Y %H:%M")
                Future = Now + timedelta(days = 7)
                FutureDate = Future.strftime("%A, %B %d, %Y %H:%M")
                
                BTitle.set(Selected_List)
                BiD.set(f"000{Index}")
                Author.set(Aut)
                LRFine.set("GH₵ 20")
                DBorrowed.set(CurrentDate)
                DDate.set(FutureDate)
                
        def Submit():
            
            Administrator_Code = "Libarian"
            AdminSubmit = StringVar()
                        
            def Submit():
                    
                    GetValue = AdminSubmit.get()
                    
                    if GetValue == Administrator_Code:
                                                
                        CB1 = Telephone.get()
                        CB2 = MType.get()
                        CB3 = Title.get()
                        CB4 = FName.get()
                        CB5 = SName.get()
                        CB6 = BTitle.get()
                    
                        if CB1 and CB2 and CB3 and CB4 and CB5 and CB6:
                            self.Button.config(state = "normal")
                            Message = messagebox.showinfo("Congratulations", "Book Borrowed Successfully")
                            
                            if not RNumber.get():
                                    RNumber.set("None")
                            
                            DataEntries = [
                                MType.get(),
                                RNumber.get(),
                                Title.get(),
                                FName.get(),
                                SName.get(),
                                Telephone.get(),
                                BTitle.get(),
                                DBorrowed.get(),
                                DDate.get()
                            ]
                            
                            with open('Borrowed Books.csv', mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(DataEntries)
                            
                            Reset()
                            
                            self.Entry22.config(state = "disabled")
                            self.Label1.config(text = "Disabled", state = "disabled")
                
                
                        else:
                            Message = messagebox.showerror("Error", "Please Fill in all the Form to proceed")
                    
                    else:
                            Message = messagebox.showerror("Error", "Wrong Password")

                        
                        
            def OpenNewWindow():
                
                    NewWindow = Toplevel(self.root)
                    NewWindow.title("Confirmation")
                    NewWindow.geometry("220x200")
                    NewWindow.resizable(False, False)
                        
                    Label1 = Label(NewWindow, text = "Enter Admin Password to proceed")
                    Label1.grid(row = 0, column = 0, pady = 20, padx = 20)
                    
                    Entry1 = Entry(NewWindow, textvariable = AdminSubmit, show = "*")
                    Entry1.grid(row = 1, column = 0)
                    
                    Button1 = Button(NewWindow, text = "Submit", pady = 2, padx = 2, command = Submit)
                    Button1.grid(row = 2, column = 0, pady = 20)
                        
            OpenNewWindow()
            
                
        def Delete():
            
            Administrator_Code = "Libarian"
            AdminSubmit = StringVar()
            SelectedValue = self.Combo1.get()
            
            if SelectedValue == "Administrator":
                
                def Submit():
                    
                    GetValue = AdminSubmit.get()
                    
                    if GetValue == Administrator_Code:
                    
                        Selected_Index = self.BookList.curselection() 
                        
                        if Selected_Index:  
                            AboutDeleting = self.BookList.get(Selected_Index[0])  
                            self.BookList.delete(Selected_Index[0])
                            
                            Updatecsv(AboutDeleting)
                        
                            messagebox.showinfo("Message", "Book Deleted Successfully")     
                            Reset()  
                        else:
                            messagebox.showerror("Message", "Please select book and retry")
                            
                    else:
                        messagebox.showerror("Message", "Wrong Password")
                     
                
                def Updatecsv(AboutDeleting, filename = "BookList.csv"):
                    with open(filename, newline = '') as csvfile:
                        reader = csv.reader(csvfile)
                        books = list(reader)
    
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        for book in books:
                            if book[0] != AboutDeleting:
                                writer.writerow(book)
                            
                def OpenNewWindow():
                
                    NewWindow = Toplevel(self.root)
                    NewWindow.title("Confirmation")
                    NewWindow.geometry("220x200")
                    NewWindow.resizable(False, False)
                        
                    Label1 = Label(NewWindow, text = "Enter Admin Password to proceed")
                    Label1.grid(row = 0, column = 0, pady = 20, padx = 20)
                        
                    Entry1 = Entry(NewWindow, textvariable = AdminSubmit, show = "*")
                    Entry1.grid(row = 1, column = 0)
                        
                    Button1 = Button(NewWindow, text = "Submit", pady = 2, padx = 2, command = Submit)
                    Button1.grid(row = 2, column = 0, pady = 20)
                        
                    NewWindow.mainloop()
                        
                OpenNewWindow()
            
        def Action():
            
            Administrator_Code = "Libarian"
            AdminSubmit = StringVar()
            SelectedValue = self.Combo1.get()
            
            if SelectedValue == "Administrator":
                
                def Submit():
                    
                    GetValue = AdminSubmit.get()
                    
                    if GetValue == Administrator_Code:
                        messagebox.showinfo("Message", "Login Success")
                        
                        def OpenNewWindow():
                            
                            def AddBooks():
                                BookTitle = BookTit.get()
                                BookAuthor = BookAut.get()
                    
                                if BookTitle and BookAuthor:
                                    
                                    SaveBooks(BookTitle, BookAuthor)
                                    
                                    self.ListOfBooks[BookTitle] = BookAuthor
                                    
                                    self.BookList.insert(END, BookTitle)
                                    
                                    messagebox.showinfo("Congratulations", "Book added successfully")
                                    Reset()
                
                            
                            NewWindow = Toplevel(self.root)
                            NewWindow.title("Administrator Settings")
                            NewWindow.geometry("400x250")
                            NewWindow.resizable(False, False)
                            
                            Label1 = Label(NewWindow, text = "Enter Book Title:")
                            Label1.grid(row = 0, column = 0, pady = (70,0), padx = 20, sticky = "w")
                    
                            BookTit = Entry(NewWindow, width = 35)
                            BookTit.grid(row = 0, column = 1, pady = (70,0))
                            
                            Label1 = Label(NewWindow, text = "Enter Book Author:")
                            Label1.grid(row = 1, column = 0, pady = 20, padx = 20, sticky = "w")
                    
                            BookAut = Entry(NewWindow, width = 35)
                            BookAut.grid(row = 1, column = 1)
                            
                            Button1 = Button(NewWindow, text = "Submit", pady = 2, padx = 2, command = AddBooks)
                            Button1.grid(row = 2, column = 0, pady = 20, columnspan = 2, padx = (20, 0))
                    
                        OpenNewWindow()
                        
                    else:
                        Message = messagebox.showerror("Error", "Wrong Password")
            
                def OpenNewWindow():
            
                    NewWindow = Toplevel(self.root)
                    NewWindow.title("Confirmation")
                    NewWindow.geometry("220x200")
                    NewWindow.resizable(False, False)
                    
                    Label1 = Label(NewWindow, text = "Enter Admin Password to proceed")
                    Label1.grid(row = 0, column = 0, pady = 20, padx = 20)
                    
                    Entry1 = Entry(NewWindow, textvariable = AdminSubmit, show = "*")
                    Entry1.grid(row = 1, column = 0)
                    
                    Button1 = Button(NewWindow, text = "Submit", command = Submit, pady = 2, padx = 2)
                    Button1.grid(row = 2, column = 0, pady = 20)
                    
                    NewWindow.mainloop()
                    
                OpenNewWindow()
                   
        
                                                                # Page Frame Setup
                                             
        self.BodyFrame = Frame(self.root, relief = "groove", bd = 3)
        self.BodyFrame.pack(fill = 'both', expand = True, pady = 10)
        
        
                                                    # Membership and Book Details Frame Label
                                    
        self.MembershipLabel = LabelFrame(self.BodyFrame, relief = "ridge", bd = 10, fg = "blue", font = ("Arial", 10, "bold"), text = "Library Membership Form", width = (0.6 * Screen_Width), height = 400)
        self.MembershipLabel.grid(row = 0, column = 0, pady = (27,0), padx = (20,0), sticky = "nw")

        self.BookInfoLabel = LabelFrame(self.BodyFrame, relief = "ridge", bd = 10, fg = "blue", font = ("Arial", 10, "bold"), text = "Book Details", width = 500, height = 269)
        self.BookInfoLabel.grid(row = 0, column = 1, pady = (27,0), padx = (10,27), sticky = "nw")
        
    
                                                                # Membership Form 
            
        
                                                                    #Row1 
        self.Label = Label (self.MembershipLabel, text = "Member Type:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 0, column = 0, sticky = 'W')
        
        self.Combo1 = ttk.Combobox (self.MembershipLabel, font = ("Arial", 10), state = "readonly", width = 27, textvariable = MType)
        self.Combo1['value'] = ("", "Student", "Lecturer", "Administrator", "Guest")
        self.Combo1.current(0)
        self.Combo1.grid(row = 0, column = 2, padx = (20, 0), sticky = "w")
        self.Combo1.bind("<<ComboboxSelected>>", ComboValue)
              
        self.Label = Label(self.MembershipLabel, text = "Book ID:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 0, column = 3, sticky = 'W')

        self.Entry1 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, state = "readonly", textvariable = BiD)
        self.Entry1.grid(row = 0, column = 4, padx = (20, 20))

                                                                    #Row2
        self.Label1 = Label (self.MembershipLabel, text = "Disabled", padx = 10, pady = 10, font = ("Arial", 10,"bold"), state = "disabled")
        self.Label1.grid(row = 1, column = 0, sticky = 'W')
        
        self.Entry22 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, state = "disabled", textvariable = RNumber)
        self.Entry22.grid(row = 1, column = 2, padx = (20, 20), sticky = "w")
        
        
        self.Label = Label(self.MembershipLabel, text = "Book Title:", padx = 10, pady = 10, font = ("Arial", 10,"bold") )
        self.Label.grid(row = 1, column = 3, sticky = 'W')

        self.Entry2 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, state = "readonly", textvariable = BTitle)
        self.Entry2.grid(row = 1, column = 4, padx = (20, 20))
        
        
                                                                 #Row3
        self.Label = Label (self.MembershipLabel, text = "Title:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 2, column = 0, sticky = 'W')

        self.Combo = ttk.Combobox (self.MembershipLabel, font = ("Arial", 10), state = "readonly", width = 27, textvariable = Title)
        self.Combo['value'] = ("", "Mr", "Miss", "Mrs", "Dr", "Prof")
        self.Combo.current(0)
        self.Combo.grid(row = 2, column = 2, padx = (20, 0), sticky = "w")
        
        self.Label = Label(self.MembershipLabel, text = "Author:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 2, column = 3, sticky = 'W')

        self.Entry3 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, state = "readonly", textvariable = Author)
        self.Entry3.grid(row = 2, column = 4, padx = (20, 20))

                                                                    #Row4
        self.Label = Label (self.MembershipLabel, text = "First Name:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 3, column = 0, sticky = 'W')
        
        self.Entry5 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, textvariable = FName)
        self.Entry5.grid(row = 3, column = 2, padx = (20, 20), sticky = "w")
        
        self.Label = Label(self.MembershipLabel, text = "Date Borrowed:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 3, column = 3, sticky = 'W')

        self.Entry4 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, state = "readonly", textvariable = DBorrowed)
        self.Entry4.grid(row = 3, column = 4, padx = (20, 20))
        
                                                                    #Row5
        self.Label = Label (self.MembershipLabel, text = "Surname:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 4, column = 0, sticky = 'W')
        
        self.Entry = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, textvariable = SName)
        self.Entry.grid(row = 4, column = 2, padx = (20, 20), sticky = "w")
        
        self.Label = Label(self.MembershipLabel, text = "Due Date:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 4, column = 3, sticky = 'W')

        self.Entry5 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, state = "readonly", textvariable = DDate)
        self.Entry5.grid(row = 4, column = 4, padx = (20, 20))
        
                                                                        #Row6
        self.Label = Label (self.MembershipLabel, text = "Telephone Number:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 5, column = 0, sticky = 'W')
        
        self.Entry = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, textvariable = Telephone)
        self.Entry.grid(row = 5, column = 2, padx = (20, 20), sticky = "w")
        
        self.Label = Label(self.MembershipLabel, text = "Late Return Fine:", padx = 10, pady = 10, font = ("Arial", 10,"bold"))
        self.Label.grid(row = 5, column = 3, sticky = 'W')

        self.Entry6 = Entry(self.MembershipLabel, font = ("Arial", 10), width = 30, state = "readonly", textvariable = LRFine)
        self.Entry6.grid(row = 5, column = 4, padx = (20, 20))
        
                                                                    ##Sumbit##

        self.Button = Button (self.MembershipLabel, width = 20, font = ("Arial", 10, "bold"), text = "Borrow Book" , pady = 5, command = Submit)
        self.Button.grid(row = 6, columnspan = 5, pady = (30, 20))
        
        
                                ###############################  Actions Frame  #########################
        
        self.SubReset = LabelFrame(self.BodyFrame, relief = "ridge", bd = 5, fg = "blue", font = ("Arial", 10, "bold"), text = "Actions", height = 80)
        self.SubReset.grid(row = 1, column = 0, pady = (27,0), padx = (20,28), sticky = "we", columnspan = 2)
        self.SubReset.grid_propagate(False)
        self.SubReset.rowconfigure(0, weight = 1)
        self.SubReset.columnconfigure(0, weight = 1)
        
        
                             ###############################  Actions Frame Body  #########################

        self.Button1 = Button(self.SubReset, text = "Reset Membership Info", font = ('Arial', 10, "bold"), command = Reset)
        self.Button1.grid(row = 0, column = 0, sticky = "w", padx = (40,0))
        self.Button2 = Button(self.SubReset, text = "Delete Book", font = ('Arial', 10, "bold"), state = "disabled", command = Delete)
        self.Button2.grid(row = 0, column = 2, sticky = "w", padx = (10,0))
        self.Button3 = Button(self.SubReset, text = "Display Data", font = ('Arial', 10, "bold"), state = "disabled", command = DisplayData)
        self.Button3.grid(row = 0, column = 3, sticky = "w", padx = (10,0))
        self.Button4 = Button(self.SubReset, text = "Exit", font = ('Arial', 10, "bold"), fg ="white", bg = "#C50F10", command = Exit)
        self.Button4.grid(row = 0, column = 4, sticky = "w", padx = (10,40))
        self.Button5 = Button(self.SubReset, text = "Add Book", font = ('Arial', 10, "bold"), state = "disabled", command = Action)
        self.Button5.grid(row = 0, column = 1, sticky = "w", padx = (0,0))
        
        
        
                                        ###############################  Books Body #########################
                
    
        self.Scrollbar = Scrollbar(self.BookInfoLabel)
        self.Scrollbar.grid(row = 0, column = 1, sticky = "ns")
        
        self.BookList = Listbox(self.BookInfoLabel, width = 70, height = 20)
        self.BookList.bind("<<ListboxSelect>>", On_Select)
        self.BookList.grid(row = 0, column = 0, padx = (20, 0))
        
        self.Scrollbar.config(command = self.BookList.yview)
        
        for Book in self.ListOfBooks:
            self.BookList.insert(END, Book)
            
            
        self.root.mainloop()
        
Library_Management_System()