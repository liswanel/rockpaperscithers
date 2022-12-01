from tkinter import *
from random import choice

K, N, B = range(3)

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        bth = Button(root, text="Камень", font=("Calibri", 15), command=lambda x=K: self.hod(x))
        bth1 = Button(root, text="Ножницы", font=("Calibri", 15), command=lambda x=N: self.hod(x))
        bth2 = Button(root, text="Бумага", font=("Calibri", 15), command=lambda x=B: self.hod(x))

        bth.place(x=10, y=100, width=100, height=20)
        bth1.place(x=210, y=100, width=100, height=20)
        bth2.place(x=410, y=100, width=100, height=20)

        self.label = Label(root, text="Начало игры", bg="#DB7093", font=("Calibri", 20))
        self.label.place(x=156, y=10)

    def hod(self, button):
        txt = ["Камень", "Ножницы", "Бумага"]
        number = choice([K, N, B])
        print("Пользователь нажал" + txt[button])
        print("Робот нажал" + txt[button])

        if (button == K and number == N) or (button == N and number == B) or (button == B and number == K):
            print('Победа')
        elif (button == K and number == B) or (button == N and number == K) or (button == B and number == N):
            print('Поражение')
        elif button == number:
            print('Ничья')

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500+200+200")
    root.title("Камень, Ножницы, Бумага")
    root.resizable(False, False)
    root["bg"] = "#D8BFD8"
    app = Main(root)
    app.pack()
    root.mainloop()


