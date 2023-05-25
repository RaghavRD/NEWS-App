import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
from io import BytesIO
import webbrowser

class NewsApp:
    def __init__(self):
        # Fatch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=7f6551038abb425990c95bcc1af0a549').json()
        # Load GUI
        self.load_gui()
        # Load NEWS
        self.load_news(0)
        
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.title("My NEWS")
        self.root.iconbitmap("./images/main_icon.ico")
        self.root.resizable(0,0)
        self.root.configure(background='white')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def open_link(self, url):
        webbrowser.open(url)

    def load_news(self, index):
        self.clear()

        try:
            # Try original image for the NEWS shon in the below diagram from the uppermost digit to the 
            # lower stack using the stack.
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            img = Image.open(BytesIO(raw_data)).resize((350,210))
            photo = ImageTk.PhotoImage(img)
            Labell = Label(self.root, image=photo)
            Labell.pack()
        except:
            # this is backup image for the NEWS
            raw_data = Image.open("./images/not found.png")
            img = Image.open("./images/not found.png").resize((350,210))
            photo = ImageTk.PhotoImage(img)
            Labell = Label(self.root, image=photo)
            Labell.pack()

        # Heading
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='white', fg='black', wraplength=350, justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('vardana',14))

        # Description
        description = Label(self.root, text=self.data['articles'][index]['description'], bg='white', fg='black', wraplength=350, justify='left')
        description.pack(pady=(2,20))
        description.config(font=('vardana',11))

        # Frame
        frame = Frame(self.root, bg='white')
        frame.pack(expand=True, fill=BOTH)

        # Buttons for Navigation
        if index == 0:
            # prev = Button(frame, text='Prev', background='black', fg='white', width=24, height=2, command=lambda :self.load_news(index-1))
            # prev.pack(side=LEFT)
            read = Button(frame, text='Read More', background='black', fg='white', width=24, height=2, command=lambda :self.open_link(self.data['articles'][index]['url']))
            read.pack(side=LEFT)
            next = Button(frame, text='Next', background='black', fg='white', width=24, height=2, command=lambda :self.load_news(index+1))
            next.pack(side=LEFT)
        else:
            prev = Button(frame, text='Prev', background='black', fg='white', width=16, height=2, command=lambda :self.load_news(index-1))
            prev.pack(side=LEFT)
            read = Button(frame, text='Read More', background='black', fg='white', width=16, height=2, command=lambda :self.open_link(self.data['articles'][index]['url']))
            read.pack(side=LEFT)
            next = Button(frame, text='Next', background='black', fg='white', width=16, height=2, command=lambda :self.load_news(index+1))
            next.pack(side=LEFT)

        # if index == 0 or index == len(self.data['articles'])-1:
        #     read = Button(frame, text='Read More', background='black', fg='white', width=24, height=2, command=lambda :self.open_link(self.data['articles'][index]['url']))
        #     read.pack(side=LEFT)
        # else:
        #     read = Button(frame, text='Read More', background='black', fg='white', width=16, height=2, command=lambda :self.open_link(self.data['articles'][index]['url']))
        #     read.pack(side=LEFT)

        if index == len(self.data['articles'])-1:
            prev = Button(frame, text='Prev', background='black', fg='white', width=24, height=2, command=lambda :self.load_news(index-1))
            prev.pack(side=LEFT)
            read = Button(frame, text='Read More', background='black', fg='white', width=24, height=2, command=lambda :self.open_link(self.data['articles'][index]['url']))
            read.pack(side=LEFT)
        else:
            prev = Button(frame, text='Prev', background='black', fg='white', width=16, height=2, command=lambda :self.load_news(index-1))
            prev.pack(side=LEFT)
            read = Button(frame, text='Read More', background='black', fg='white', width=16, height=2, command=lambda :self.open_link(self.data['articles'][index]['url']))
            read.pack(side=LEFT)
            next = Button(frame, text='Next', background='black', fg='white', width=16, height=2, command=lambda :self.load_news(index+1))
            next.pack(side=LEFT)

        # Mainloop
        self.root.mainloop()

obj = NewsApp()