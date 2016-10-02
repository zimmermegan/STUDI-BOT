from Tkinter import *
from PIL import Image
import datetime
import time
import threading
import serial
ser = serial.Serial('/dev/ttyACM0',9600)
class pomodoro(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=500, height=500)
        
        self.num = 2
        self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
        self.label_back = Label(self, image=self.image)
        self.label_back.pack()

        self.button = Button(self, text="Start", font = ("Verdana",22),
                             bg="Orange",command=self.handle_work)
        self.button.pack(side=LEFT, padx=10)
        self.slogan = Button(self,text="Stop", font = ("Verdana",22),
                             bg = "Cyan" ,command=self.reset)
        self.slogan.pack(side=LEFT, padx=10)

        #FOR TESTING

        self.pause_button = Button(self, text="Pause", font = ("Verdana",22),
                            bg="Green",command=self.pause)
        self.pause_button.pack(side=LEFT, padx=10)

        self.candy = Button(self, text="Candy", font = ("Verdana",22),fg = "white",
                            bg="Purple",command=self.feed_me)
        self.candy.pack(side=LEFT, padx=10)

        self.label = Label(self, text="", font = ("Verdana",22), width=16)
        self.label.pack(side=RIGHT)

        self.spacing = Label(self, text="Timer :", font = ("Verdana",22), width=16)
        self.spacing.pack(side=RIGHT)
        
        self.title("STUDI-BOT")
        self.label.pack()
        self.minute = 0
        self.second = 0
        self.dispense = True
        self.pause = False
        self.setup()


#        self.image2 = Image.open("/home/jacob/Downloads/StudiBot/image2.png")
#        self.image3 = Image.open("/home/jacob/Downloads/StudiBot/image3.png")
#        self.image4 = Image.open("/home/jacob/Downloads/StudiBot/image4.png")

        

    def updateString(self):
        self.label.configure(text="%d m %d s" % (self.minute, self.second))

    def setup(self):
        self.minute = 25
        self.second = 0
        self.updateString()

    def handle_work(self):
        self.w = threading.Thread(target=self.work_thread)
        self.w.start()

    def work_thread(self):
        try:
            self.work()
        except:
            print("Caught")
            self.minute = 25
            self.second = 0
            self.updateString()
            
        return

    def work(self):
        print("Started...")

        self.num = 1
        self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
        self.label_back.configure(image=self.image)

        self.stop = False
        minutes = 1
        counter = 1
        current = minutes
        for i in range(minutes * 60):
            time.sleep(1)
            counter -= 1
            if counter == 0:
                counter = 60
                current -= 1
                print("Minute:",current)
            self.minute = current
            self.second = counter
            self.updateString()
            if self.stop == True:
                raise Exception
            while self.pause:
                    continue


        print("Break time!")
  #      self.beeps()




        self.dispense = True
        self.feed_me()

        minutes = 4
        counter = 60
        current = minutes

        time.sleep(2)

        self.num = 3
        self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
        self.label_back.configure(image=self.image)

        for i in range(minutes * 60):
            time.sleep(1)
            counter -= 1
            if counter == 0:
                current -= 1
                counter = 60
            self.minute = current
            self.second = counter
            self.updateString()
            if self.stop == True:
                raise Exception
            while self.pause:
                continue

        self.num = 2
        self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
        self.label_back.configure(image=self.image)

        print("Work time!")
#        self.beeps()


        return

    def pause(self):
        
        if self.pause:
            self.num = 1
            self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
            self.label_back.configure(image=self.image)
            self.pause_button.configure(text = "Pause")
        else:
            self.num = 2
            self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
            self.label_back.configure(image=self.image)
            self.pause_button.configure(text = "Unpause")

        self.pause = not(self.pause)
        

        return

    def reset(self):
        self.num = 2
        self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
        self.label_back.configure(image=self.image)
        self.stop = True
        self.minute = 25
        self.second = 0
        self.updateString()
        return
        
    def feed_me(self):

        self.num = 0
        self.image = PhotoImage(file="/home/jacob/Downloads/StudiBot/image.gif", format = "gif -index %d" %self.num)
        self.label_back.configure(image=self.image)

        if self.dispense == True:
            print("Feed meee")
            self.dispense = False
            ser.write("1")
        return

if __name__ == "__main__":
    app = pomodoro()
    app.mainloop()
