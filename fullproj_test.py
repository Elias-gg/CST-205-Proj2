import tkinter as tk
from tkinter import ttk
from MyQR import myqr
from tkinter import filedialog
import os

LARGE_FONT = ("Verdana", 12)

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

def qr_2(size,url_in,path):
    print('\n\n\n\n1  being smaller \n40 being bigger')
    num = size
    # url = 'https://www.instagram.com/jayrfitz/?hl=en'
    url = url_in
    pic = path

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
        URLin = ' '
        Size = 1
        filePath = ' '
        
        def submit():
            content = url_entry.get()
            URLin = content
            print(URLin)
        def submit2():
            content = size_entry.get()
            Size = content
            print(Size)

        def Browse():
            filename = filedialog.askopenfilename()
            filePath = filename
            print(filePath)
            
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "start page", font = LARGE_FONT)
        label.pack()

        label = ttk.Label(self,text = "start page", font = LARGE_FONT)
        button1 = ttk.Button(self,text = "Page 1", command = lambda: controller.show_frame(PageOne))
        button1.place(x = 0, y = 450)

        url_label = ttk.Label(self,text = "Enter URL in box", font = LARGE_FONT)
        url_label.place(x = 100, y = 25)
        
        submit1 = ttk.Button(self,text = "submit", command = submit)
        submit1.place(x = 0, y = 25)

        url_entry = ttk.Entry(self,width = 50)
        url_entry.place(x = 0, y = 100)

        submit2 = ttk.Button(self,text = "submit", command = submit2)
        submit2.place(x = 0, y = 150)

        size_label = ttk.Label(self,text = "Enter the size of the QR code", font = LARGE_FONT)
        size_label.place(x = 100, y = 150)
        
        size_entry = ttk.Entry(self,width = 50)
        size_entry.place(x = 0, y = 200)

        file_label = ttk.Label(self,text = filePath, font = LARGE_FONT)
        file_label.place(x = 0, y = 350)
        FileBrowse = ttk.Button(self,text = "Browse",command = Browse,)
        FileBrowse.place(x = 0, y= 250)

        file_ent = ttk.Entry(self,width = 50, text = filePath)
        file_ent.place(x = 0, y = 300)


            
        run = ttk.Button(self,text = "Run", command = lambda: qr_2(Size,URLin,filePath))
        run.place(x = 0, y = 400)



        
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
