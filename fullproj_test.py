import tkinter as tk
from tkinter import ttk
from MyQR import myqr
from tkinter import filedialog
import os

LARGE_FONT = ("Verdana", 12)
filePath = ''
version = ""
class QRgenerator(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.wm_title(self,"CST-205-Project2")
        container.pack(side = "top", fill  = "both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        for f in (StartPage,PageOne,QR1,QR2):

            frame = f(container, self)

            self.frames[f] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

def qr_2(file,newurl,vers):
    print('\n\ndone check file for qr\n\n')
    num = vers
    # url =
    url = newurl
    pic = file

    version, level, qr_name = myqr.run(
        words=url,
        version=num,
        level='H',
        picture=pic,
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=None,
    #outputdirectory I deleted but we can set it here
        )

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "start page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self,text = "next page", command = lambda: controller.show_frame(PageOne))
        button1.pack()
class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Page One", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self,text = "Option1", command = lambda: controller.show_frame(QR1))
        button1.place(x = 0, y = 0)

        button2 = ttk.Button(self,text = "Option2", command = lambda: controller.show_frame(QR2))
        button2.place(x = 425, y = 0)
class QR1(tk.Frame):

    def __init__(self,parent,controller):

        def submit():
            global URLin
            URLin = url_entry.get()
            print(URLin)

        def submit2():
            global version
            version = int(size_entry.get())
            print(version)


        def Browse():
            global filePath
            filename = filedialog.askopenfilename()
            filePath = filename
            file_label = ttk.Label(self,text = filePath, font = LARGE_FONT)
            file_label.place(x = 0, y = 325)

            print(filePath)


        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "start page", font = LARGE_FONT)
        label.pack()

        label = ttk.Label(self,text = "start page", font = LARGE_FONT)


        submit1 = ttk.Button(self,text = "submit", command = submit)
        submit1.place(x = 0, y = 25)

        url_label = ttk.Label(self,text = "Enter URL in box", font = LARGE_FONT)
        url_label.place(x = 100, y = 25)



        url_entry = ttk.Entry(self,width = 50)
        url_entry.place(x = 0, y = 100)

        submit2 = ttk.Button(self,text = "submit", command = submit2)
        submit2.place(x = 0, y = 150)

        size_label = ttk.Label(self,text = "Enter the size of the QR code", font = LARGE_FONT)
        size_label.place(x = 100, y = 150)

        size_entry = ttk.Entry(self,width = 50)
        size_entry.place(x = 0, y = 200)


        FileBrowse = ttk.Button(self,text = "Browse",command = Browse)
        FileBrowse.place(x = 0, y= 250)


        run = ttk.Button(self,text = "Run", command = lambda: qr_2(filePath,URLin,version))
        run.place(x = 0, y = 400)

        button1 = ttk.Button(self,text = "Page 1", command = lambda: controller.show_frame(PageOne))
        button1.place(x = 0, y = 450)




class QR2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "start page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self,text = "next page", command = lambda: controller.show_frame(PageOne))
        button1.pack()


app = QRgenerator()
app.geometry("500x500")
app.mainloop()
