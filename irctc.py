from tkinter import*
import requests

class Irctc:

    def __init__(self):
        self.root=Tk()
        self.root.title("IRCTC V2.0")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#0089ae")

        self.label1=Label(self.root, text="Train Route",bg="#0089ae",fg="#ffffff")
        self.label1.configure(font=("Arial",22,"bold","underline"))
        self.label1.pack(pady=(30,10))

        self.trainNo=Entry(self.root)
        self.trainNo.pack(ipadx=40,ipady=10)
        click=Button(self.root,text="Fetch Stations",width=29, height=2,command=lambda: self.fetch())
        click.pack(pady=(15,15))

        self.result=Label(self.root, bg="#0089ae",fg="#ffffff")
        self.result.configure(font=("Arial",12))
        self.result.pack(pady=(5,10))

        self.root.mainloop()

    def fetch(self):
        train_no=self.trainNo.get()
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/6y10lt09no/".format(train_no)
        data=requests.get(url)
        response=data.json()
        station=""
        for i in response['route']:
           station=station+i['station']['name']+" | "+i['scharr']+" | "+i['schdep']+" | "+str(i['distance'])+"KM"+ "\n"
           
        self.result.configure(text=station)
        
        
obj=Irctc()
