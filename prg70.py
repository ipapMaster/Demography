# Обработчик изображений

from tkinter import *  # подключаем все элементы Tkinter
from tkinter import filedialog  # файловый диалог
from PIL import Image, ImageTk, ImageFilter, ImageEnhance


class App:  # класс нашего приложения
    def __init__(self):  # Конструктор
        self.root = Tk()  # корневой элемент
        self.root.title('Обработка изображений')
        self.root.geometry('800x600')  # Размеры окна
        self.root.resizable(False, False)  # Фиксируем габариты
        self.root.iconphoto(False, PhotoImage(file='icon.png'))
        self.label = Label(text='Работаем с картинками',
                           background='#ffff00',
                           foreground='red',
                           font=('Verdana', 16))
        self.label.pack()  # Размещение надписи
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)
        # Кнопка загрузки
        self.btn = Button(text='Загрузить', command=self.load)
        self.btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # Кнопка размытия
        self.blur = Button(text='Размыть', command=self.blur)
        self.blur.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # Кнопка резкости
        self.shrp = Button(text='Резкость', command=self.sharp)
        self.shrp.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # Кнопка отражения по горизонтали
        self.flp = Button(text='Отразить', command=self.flip)
        self.flp.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # Кнопка возврата к оригиналу
        self.orig = Button(text='Оригинал', command=self.back)
        self.orig.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # Кнопка очистки
        self.rect_btn = Button(text='Очистить', command=self.make_rect)
        self.rect_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # Кнопка сохранения
        self.save_btn = Button(text='Сохранить', command=lambda: self.load_save('save'))
        self.save_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.save_btn['state'] = DISABLED
        # self.btn.bind('<ButtonPress-1>', self.load)
        self.left, self.top = 0, 0  # точки привязки к холсту
        self.ext = ''  # Расширение файла картинки
        self.image = None
        self.empty = Image.new('RGB', (600, 400), (255, 255, 255))  # пустышка
        self.root.mainloop()

    def load(self):
        try:
            fullpath = filedialog.askopenfilename(initialdir='./',
                                                  filetypes=(
                                                      ('All', '*.*'),
                                                      ('JPEG', '*.jpg'),
                                                      ('PNG', '*.png')
                                                  ))  # диалог открытия картинки
            self.ext = fullpath.split('.')[-1]  # получаем расширение из пути
            # print(self.ext)
            self.empty = Image.open(fullpath)
            mode = self.empty.mode  # получаем цветовую схему
            if mode == 'P':  # 256-color indexed image
                self.empty = self.empty.convert('RGB')
            w, h = self.empty.size
            self.left, self.top = 0, 0

            if w > 600:
                ratio = w / 600
                h = int(h / ratio)
                w = 600
                self.empty = self.empty.resize((w, h))
                if h < 400:
                    self.left, self.top = 0, (400 - h) // 2
                else:
                    self.left, self.top = 0, 0
            else:
                self.left = (600 - w) // 2
                self.top = (400 - h) // 2

            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        except AttributeError:  # если не удалось подгрузить
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    # Функционал кнопки "Размытия"
    def blur(self):
        blur_img = self.empty.filter(ImageFilter.GaussianBlur(5))
        self.image = ImageTk.PhotoImage(blur_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    # Функционал кнопки "Резкость"
    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.empty)
        sharp_img = sharper.enhance(5.0)
        self.image = ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    # Функционал кнопки "Отразить"
    def flip(self):
        flp_img = self.empty.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.image = ImageTk.PhotoImage(flp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    # Функционал кнопки возврата к оригиналу
    def back(self):
        self.image = ImageTk.PhotoImage(self.empty)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = DISABLED

    def load_save(self, *args):
        if len(args) == 1 and args[0] == 'save':
            # print(args[0])
            fullpath = filedialog.asksaveasfilename(initialfile=f'result.{self.ext}')
            if fullpath != '':
                if f'.{self.ext}' not in fullpath:
                    fullpath += f'.{self.ext}'
                res = ImageTk.getimage(self.image)
                if res.mode == 'RGBA' and 'jp' in self.ext:
                    res = res.convert('RGB')
                res.save(fullpath)
                self.save_btn['state'] = DISABLED


    # Функционал кнопки "Очистить"
    def make_rect(self):
        self.canvas.create_rectangle(0, 0, 600, 400, fill='#ffffff')


app = App()
