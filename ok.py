from tkinter import *
from random import choice

K, N, B = range(3)
win = 0
loose = 0


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        bth = Button(root, text="Камень", font=("Calibri", 15), command=lambda x=K: self.hod(x), bg="#F39DF3")
        bth1 = Button(root, text="Ножницы", font=("Calibri", 15), command=lambda x=N: self.hod(x), bg='#F39DF3')
        bth2 = Button(root, text="Бумага", font=("Calibri", 15), command=lambda x=B: self.hod(x), bg='#F39DF3')

        bth.place(x=10, y=100, width=100, height=50)
        bth1.place(x=190, y=100, width=120, height=50)
        bth2.place(x=390, y=100, width=100, height=50)

        self.label = Label(root, text="Начало игры", bg="#DB7093", font=("Calibri", 20))
        self.label.place(x=156, y=10)

        self.score_label = Label(text=f"Счет:\nwin: {win} \nloose: {loose}")
        self.score_label.place(x=16, y=10)

    def hod(self, button):
        global win, loose

        txt = ["Камень", "Ножницы", "Бумага"]
        number = choice([K, N, B])
        print("Пользователь нажал" + txt[button])
        print("Робот нажал" + txt[button])

        if (button == K and number == N) or (button == N and number == B) or (button == B and number == K):
            print('Победа')
            self.label.configure(text="Победа")
            win += 1
        elif (button == K and number == B) or (button == N and number == K) or (button == B and number == N):
            print('Поражение')
            loose += 1
            self.label.configure(text="Поражение")
        elif button == number:
            print('Ничья')
            self.label.configure(text="Ничья")
        self.score_label.configure(text=f"Счет:\nwin: {win} \nloose: {loose}")


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x200+200+200")
    root.title("Камень, Ножницы, Бумага")
    root.resizable(False, False)
    root["bg"] = "#D8BFD8"
    app = Main(root)
    app.pack()
    root.mainloop()
