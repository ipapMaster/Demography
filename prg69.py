# GUI - Graphic User Interface
# PyQt6 - на самостоятельное
import tkinter
from PIL import Image, ImageTk


class App:
    def __init__(self):
        # корневой элемент приложения
        self.root = tkinter.Tk()

        # рабочая область
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        # Добавляем ярлык
        self.label = tkinter.Label(self.frame,
                                   text='Меняем изображение').grid(row=1, column=1)

        self.but = tkinter.Button(self.frame,
                                  text='Заменить',
                                  command=self.change).grid(row=2, column=1)

        # Добавим холст
        self.canvas = tkinter.Canvas(self.root, height=400, width=600)

        # Добавляем изображение на холст
        self.image = Image.open('original.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=3, column=1)
        self.root.mainloop()  # ожидание действий пользователя

    # Метод change
    def change(self):
        print('Кнопка нажата')
        self.image = Image.open('inverted.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=3, column=1)


app = App()
