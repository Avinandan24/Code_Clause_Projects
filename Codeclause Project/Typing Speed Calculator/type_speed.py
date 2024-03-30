from tkinter import *
from tkinter import ttk
import time
import random
import difflib


class MainWindow:

    def __init__(self, root):
        self.text = ["The greatest glory in living lies not in never falling, but in rising every time we fall.",
                     "The way to get started is to quit talking and begin doing.",
                     "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
                     "If life were predictable it would cease to be life, and be without flavor.",
                     "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
                     "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
                     "Life is what happens when you're busy making other plans.",
                     "One day the people that don’t even believe in you will tell everyone how they met you.",
                     "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
                     "The quick brown fox jumps over the lazy dog."]
        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0
        root.title("Typing Speed")
        root.geometry("550x950")
        root.configure(bg="#f2f2f2")

        self.frame = Frame(root, bg="#f2f2f2")
        self.frame.pack(fill=BOTH, expand=True)

        self.label_text = Label(
            self.frame, text="Welcome to Typing Speed Calculator", wraplength=400, font=("Helvetica", 14), bg="#f2f2f2")
        self.label_text.pack(pady=(20, 10))

        self.user_text = Text(self.frame, font=("Helvetica", 12))
        self.user_text.pack(fill=BOTH, padx=50, pady=(0, 20))

        self.btn_frame = Frame(self.frame, bg="#f2f2f2")
        self.btn_frame.pack(pady=(0, 20))

        self.btn_toggle = Button(self.btn_frame, text="Start", command=self.toggle_start_stop, width=15, height=2, bg="#1976D2", fg="white", font=("Helvetica", 12))
        self.btn_toggle.grid(row=0, column=0, padx=(0, 10))

        self.btn_newtext = Button(self.btn_frame, text="New Text", command=self.new_text, bg="#388E3C", fg="white", font=("Helvetica", 12))
        self.btn_newtext.grid(row=0, column=1, padx=(10, 0))

        self.label_speed = Label(
            self.frame, text=f"Your typing speed is {self.speed} WPM", font=("Helvetica", 12), bg="#f2f2f2")
        self.label_speed.pack()

        self.label_accuracy = Label(
            self.frame, text=f"Your typing accuracy is {self.accuracy} %", font=("Helvetica", 12), bg="#f2f2f2")
        self.label_accuracy.pack()

        self.started = False

    def toggle_start_stop(self):
        if not self.started:
            self.start()
            self.btn_toggle.config(text="Stop", bg="#D32F2F")
        else:
            self.stop()
            self.btn_toggle.config(text="Start", bg="#1976D2")

    def start(self):
        self.started = True
        self.time_start = time.time()

    def stop(self):
        self.started = False
        self.time_end = time.time()
        words = self.label_text.cget("text").split(' ')
        self.speed = round(len(words)/((self.time_end - self.time_start)/60))
        self.label_speed.config(
            text=f"Your typing speed is {self.speed} WPM")
        self.accuracy = round(difflib.SequenceMatcher(None, self.label_text.cget(
            "text"), self.user_text.get("1.0", 'end-1c')).ratio()*100)
        self.label_accuracy.config(
            text=f"Your typing accuracy is {self.accuracy} %")

    def new_text(self):
        self.label_text.config(
            text=self.text[random.randint(0, len(self.text)-1)])
        self.user_text.delete('1.0', END)


def main():
    root = Tk()
    myapp = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
