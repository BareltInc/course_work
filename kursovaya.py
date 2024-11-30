from tkinter import *
from tkinter import font

# Определение цветов и шрифтов
white_color = '#ffffff'
black_color = '#000000'
red_color = '#db2b36'
font15 = 'Cuprum 15 normal'
font17 = 'Cuprum 17 bold'


# Определение параметров окна
main_window = Tk()
main_window.config(width=1280, height=720, bg=white_color)
main_window.resizable(False, False)
main_window.title('ЛУКОИЛ - Официальный сайт Компании «ЛУКОИЛ»')


# Красный заголовок
red_header = Canvas(width=1280, height=40, bg=red_color, borderwidth=0)
red_header.place(x=0, y=0)

# Глобальный бизнес
global_business_lb = Label(text='Глобальный бизнес',font=font15, fg=white_color, bg=red_color)
global_business_lb.place(x=30, y=7)
# Телеграмм
tg_logo = PhotoImage(file='tg_logo.png')
tg = Label(image=tg_logo, bg=red_color, borderwidth=0)
tg.place(x=240, y=10)
# ВК
vk_logo = PhotoImage(file='vk_logo.png')
vk = Label(image=vk_logo, bg=red_color, borderwidth=0)
vk.place(x=280, y=10)
# Ютуб
yt_logo = PhotoImage(file='yt_logo.png')
yt = Label(image=yt_logo, bg=red_color, borderwidth=0)
yt.place(x=320, y=10)
# Сеть АЗС
network_lb = Label(text='Сеть АЗС',font=font15, fg=white_color, bg=red_color)
network_lb.place(x=525, y=7)
# Тендеры
tenders_lb = Label(text='Тендеры',font=font15, fg=white_color, bg=red_color)
tenders_lb.place(x=625, y=7)
# Вакансии
vacancies_lb = Label(text='Вакансии',font=font15, fg=white_color, bg=red_color)
vacancies_lb.place(x=725, y=7)
# Контакты
contacts_lb = Label(text='Контакты',font=font15, fg=white_color, bg=red_color)
contacts_lb.place(x=825, y=7)


# Черный заголовок
black_header = Canvas(width=1280, height=100, bg=black_color, borderwidth=0)
black_header.place(x=0, y=65)
logo = PhotoImage(file='logo.png')
lukoil_logo = Label(image=logo, bg=black_color, borderwidth=0)
lukoil_logo.place(x=30, y=85)
# Компания
network_lb = Label(text='КОМПАНИЯ',font=font17, fg=white_color, bg=black_color)
network_lb.place(x=465, y=130)
# Бизнес
network_lb = Label(text='БИЗНЕС',font=font17, fg=white_color, bg=black_color)
network_lb.place(x=580, y=130)
# Инвесторы
network_lb = Label(text='ИНВЕСТОРЫ',font=font17, fg=white_color, bg=black_color)
network_lb.place(x=660, y=130)
# Пресс-центр
network_lb = Label(text='ПРЕСС-ЦЕНТР',font=font17, fg=white_color, bg=black_color)
network_lb.place(x=780, y=130)
# Продукция
network_lb = Label(text='ПРОДУКЦИЯ',font=font17, fg=white_color, bg=black_color)
network_lb.place(x=915, y=130)
# Устойчивое развитие
network_lb = Label(text='УСТОЙЧИВОЕ РАЗВИТИЕ',font=font17, fg=white_color, bg=black_color)
network_lb.place(x=1035, y=130)







main_window.mainloop()