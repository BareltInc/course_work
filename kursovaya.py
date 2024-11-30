from tkinter import *
from tkinter import ttk

# Определение цветов и шрифтов
white_color = '#ffffff'
black_color = '#000000'
gray_color = '#e9928d'
red_color = '#db2b36'
font15 = 'Cuprum 15 bold'
font17 = 'Cuprum 17 bold'


# Определение параметров окна
main_window = Tk()
main_window.config(width=1280, height=720, bg=white_color)
main_window.resizable(False, False)
main_window.title('ЛУКОИЛ - Официальный сайт Компании «ЛУКОИЛ»')


# Красный заголовок
red_header = Canvas(width=1280, height=40, bg=red_color, borderwidth=0, highlightthickness=0)
red_header.place(x=0, y=0)

# Глобальный бизнес
global_business_lb = Label(text='Глобальный бизнес',font=font15, fg=white_color, bg=red_color)
global_business_lb.place(x=30, y=7)

# Телеграмм
tg_logo = PhotoImage(file='tg_logo.png')
tg = Label(image=tg_logo, bg=red_color, borderwidth=0, highlightthickness=0)
tg.place(x=240, y=9)
# ВК
vk_logo = PhotoImage(file='vk_logo.png')
vk = Label(image=vk_logo, bg=red_color, borderwidth=0, highlightthickness=0)
vk.place(x=280, y=9)
# Ютуб
yt_logo = PhotoImage(file='yt_logo.png')
yt = Label(image=yt_logo, bg=red_color, borderwidth=0, highlightthickness=0)
yt.place(x=320, y=9)

# Сеть АЗС
def network_gray(event):
    network_lb['fg'] = gray_color
def network_white(event):
    network_lb['fg'] = white_color
network_lb = Label(text='Сеть АЗС',font=font15, fg=white_color, bg=red_color)
network_lb.place(x=525, y=7)
network_lb.bind('<Enter>', network_gray)
network_lb.bind('<Leave>', network_white)

# Тендеры
def tenders_gray(event):
    tenders_lb['fg'] = gray_color
def tenders_white(event):
    tenders_lb['fg'] = white_color
tenders_lb = Label(text='Тендеры',font=font15, fg=white_color, bg=red_color)
tenders_lb.place(x=625, y=7)
tenders_lb.bind('<Enter>', tenders_gray)
tenders_lb.bind('<Leave>', tenders_white)

# Вакансии
def vacancies_gray(event):
    vacancies_lb['fg'] = gray_color
def vacancies_white(event):
    vacancies_lb['fg'] = white_color
vacancies_lb = Label(text='Вакансии',font=font15, fg=white_color, bg=red_color)
vacancies_lb.place(x=725, y=7)
vacancies_lb.bind('<Enter>', vacancies_gray)
vacancies_lb.bind('<Leave>', vacancies_white)

# Контакты
def contacts_gray(event):
    contacts_lb['fg'] = gray_color
def contacts_white(event):
    contacts_lb['fg'] = white_color
contacts_lb = Label(text='Контакты',font=font15, fg=white_color, bg=red_color)
contacts_lb.place(x=825, y=7)
contacts_lb.bind('<Enter>', contacts_gray)
contacts_lb.bind('<Leave>', contacts_white)


# Поиск
def search_clear(event):
    search.delete(0, END)
def search_start(event):
    search.insert(0, '  Поиск')

search = Entry(main_window, font=font15, fg=gray_color, bg=white_color)
search.place(x=935, y=9, width=265, height=25)
search.insert(0, '  Поиск')
search.bind('<ButtonPress>', search_clear)
search.bind('<Deactivate>', search_start)
div_search = Canvas(width=1, height=15, bg=red_color, borderwidth=0, highlightthickness=0, relief='flat')
div_search.place(x=1160, y=13)
search_img = PhotoImage(file='search.png')
search_button = Button(image=search_img, bg=white_color, borderwidth=0, highlightthickness=0, relief='flat')
search_button.place(x=1172, y=13)

# Выбор языка
div_lang = Canvas(width=1, height=25, bg=white_color, borderwidth=0, highlightthickness=0)
div_lang.place(x=1210, y=9)
languages = ['RU', 'EN']
languages_default = StringVar(value=languages[0])
languages_choose = ttk.Combobox(textvariable=languages_default, values=languages, height=35, width=2, font=font17)
languages_choose.place(x=1222, y=7)


# Черный заголовок
black_header = Canvas(width=1280, height=100, bg=black_color, borderwidth=0, highlightthickness=0)
black_header.place(x=0, y=65)
logo = PhotoImage(file='logo.png')
lukoil_logo = Label(image=logo, bg=black_color, borderwidth=0, highlightthickness=0)
lukoil_logo.place(x=30, y=85)

# Компания
def company_red(event):
    company_lb['fg'] = red_color
def company_white(event):
    company_lb['fg'] = white_color
company_lb = Label(text='КОМПАНИЯ',font=font17, fg=white_color, bg=black_color)
company_lb.place(x=465, y=130)
company_lb.bind('<Enter>', company_red)
company_lb.bind('<Leave>', company_white)

# Бизнес
def business_red(event):
    business_lb['fg'] = red_color
def business_white(event):
    business_lb['fg'] = white_color
business_lb = Label(text='БИЗНЕС',font=font17, fg=white_color, bg=black_color)
business_lb.place(x=580, y=130)
business_lb.bind('<Enter>', business_red)
business_lb.bind('<Leave>', business_white)

# Инвесторы
def investors_red(event):
    investors_lb['fg'] = red_color
def investors_white(event):
    investors_lb['fg'] = white_color
investors_lb = Label(text='ИНВЕСТОРЫ',font=font17, fg=white_color, bg=black_color)
investors_lb.place(x=660, y=130)
investors_lb.bind('<Enter>', investors_red)
investors_lb.bind('<Leave>', investors_white)

# Пресс-центр
def press_red(event):
    press_lb['fg'] = red_color
def press_white(event):
    press_lb['fg'] = white_color
press_lb = Label(text='ПРЕСС-ЦЕНТР',font=font17, fg=white_color, bg=black_color)
press_lb.place(x=780, y=130)
press_lb.bind('<Enter>', press_red)
press_lb.bind('<Leave>', press_white)

# Продукция
def products_red(event):
    products_lb['fg'] = red_color
def products_white(event):
    products_lb['fg'] = white_color
products_lb = Label(text='ПРОДУКЦИЯ',font=font17, fg=white_color, bg=black_color)
products_lb.place(x=915, y=130)
products_lb.bind('<Enter>', products_red)
products_lb.bind('<Leave>', products_white)

# Устойчивое развитие
def improvement_red(event):
    improvement_lb['fg'] = red_color
def improvement_white(event):
    improvement_lb['fg'] = white_color
improvement_lb = Label(text='УСТОЙЧИВОЕ РАЗВИТИЕ',font=font17, fg=white_color, bg=black_color)
improvement_lb.place(x=1035, y=130)
improvement_lb.bind('<Enter>', improvement_red)
improvement_lb.bind('<Leave>', improvement_white)








main_window.mainloop()