from tkinter import *
from tkinter import ttk

# Определение цветов и шрифтов
white_color = '#ffffff'
black_color = '#000000'
gray_color = '#e9928d'
red_color = '#db2b36'
font12 = 'Cuprum 12 normal'
font14 = 'Cuprum 14 normal'
font14b = 'Cuprum 14 bold'
font15b = 'Cuprum 15 bold'
font16 = 'Cuprum 16 normal'
font17 = 'Cuprum 17 normal'
font17b = 'Cuprum 17 bold'
font20 = 'Cuprum 20 normal'
font20b = 'Cuprum 20 bold'

# Определение параметров окна
main_window = Tk()
main_window.config(width=1280, height=720, bg=white_color)
main_window.resizable(False, False)
main_window.title('ЛУКОИЛ - Официальный сайт Компании «ЛУКОИЛ»')


# Красный заголовок
red_header = Canvas(width=1280, height=40, bg=red_color, borderwidth=0, highlightthickness=0)
red_header.place(x=0, y=0)
red_header.create_polygon(210, 20, 220, 20, 215, 25, fill=white_color, activefill=gray_color)

# Глобальный бизнес
def global_business_gray(event):
    global_business_lb['fg'] = gray_color
def global_business_white(event):
    global_business_lb['fg'] = white_color
global_business_lb = Label(text='Глобальный бизнес',font=font15b, fg=white_color, bg=red_color)
global_business_lb.place(x=30, y=7)
global_business_lb.bind('<Enter>', global_business_gray)
global_business_lb.bind('<Leave>', global_business_white)

# Телеграмм
def tg_red(event):
    tg['image'] = tg_logo2
def tg_white(event):
    tg['image'] = tg_logo1
tg_logo1 = PhotoImage(file='tg_logo1.png')
tg_logo2 = PhotoImage(file='tg_logo2.png')
tg = Label(image=tg_logo1, bg=red_color, borderwidth=0, highlightthickness=0)
tg.place(x=240, y=9)
tg.bind('<Enter>', tg_red)
tg.bind('<Leave>', tg_white)

# ВК
def vk_red(event):
    vk['image'] = vk_logo2
def vk_white(event):
    vk['image'] = vk_logo1
vk_logo1 = PhotoImage(file='vk_logo1.png')
vk_logo2 = PhotoImage(file='vk_logo2.png')
vk = Label(image=vk_logo1, bg=red_color, borderwidth=0, highlightthickness=0)
vk.place(x=280, y=9)
vk.bind('<Enter>', vk_red)
vk.bind('<Leave>', vk_white)

# Ютуб
def yt_red(event):
    yt['image'] = yt_logo2
def yt_white(event):
    yt['image'] = yt_logo1
yt_logo1 = PhotoImage(file='yt_logo1.png')
yt_logo2 = PhotoImage(file='yt_logo2.png')
yt = Label(image=yt_logo1, bg=red_color, borderwidth=0, highlightthickness=0)
yt.place(x=320, y=9)
yt.bind('<Enter>', yt_red)
yt.bind('<Leave>', yt_white)

# Сеть АЗС
def network_gray(event):
    network_lb['fg'] = gray_color
def network_white(event):
    network_lb['fg'] = white_color
network_lb = Label(text='Сеть АЗС',font=font15b, fg=white_color, bg=red_color)
network_lb.place(x=495, y=7)
network_lb.bind('<Enter>', network_gray)
network_lb.bind('<Leave>', network_white)

# Тендеры
def tenders_gray(event):
    tenders_lb['fg'] = gray_color
def tenders_white(event):
    tenders_lb['fg'] = white_color
tenders_lb = Label(text='Тендеры',font=font15b, fg=white_color, bg=red_color)
tenders_lb.place(x=595, y=7)
tenders_lb.bind('<Enter>', tenders_gray)
tenders_lb.bind('<Leave>', tenders_white)

# Вакансии
def vacancies_gray(event):
    vacancies_lb['fg'] = gray_color
def vacancies_white(event):
    vacancies_lb['fg'] = white_color
vacancies_lb = Label(text='Вакансии',font=font15b, fg=white_color, bg=red_color)
vacancies_lb.place(x=695, y=7)
vacancies_lb.bind('<Enter>', vacancies_gray)
vacancies_lb.bind('<Leave>', vacancies_white)

# Контакты
def contacts_gray(event):
    contacts_lb['fg'] = gray_color
def contacts_white(event):
    contacts_lb['fg'] = white_color
contacts_lb = Label(text='Контакты',font=font15b, fg=white_color, bg=red_color)
contacts_lb.place(x=795, y=7)
contacts_lb.bind('<Enter>', contacts_gray)
contacts_lb.bind('<Leave>', contacts_white)


# Поиск
def search_clear(event):
    search.delete(0, END)
def search_start(event):
    search.insert(0, '  Поиск')

search = Entry(main_window, font=font15b, fg=gray_color, bg=white_color, borderwidth=0, highlightthickness=0)
search.place(x=905, y=8, width=265, height=25)
search.insert(0, '  Поиск')
search.bind('<ButtonPress>', search_clear)
search.bind('<Deactivate>', search_start)
div_search = Canvas(width=1, height=15, bg=red_color, borderwidth=0, highlightthickness=0, relief='flat')
div_search.place(x=1130, y=13)
search_img = PhotoImage(file='search.png')
search_button = Button(image=search_img, bg=white_color, borderwidth=0, highlightthickness=0, relief='flat')
search_button.place(x=1142, y=13)

# Выбор языка
div_lang = Canvas(width=1, height=25, bg=white_color, borderwidth=0, highlightthickness=0)
div_lang.place(x=1180, y=8)
languages = ['RU', 'EN']
languages_default = StringVar(value=languages[0])
languages_choose = ttk.Combobox(main_window, textvariable=languages_default, values=languages,
                                height=35, width=2, font=font14b)
languages_choose.place(x=1190, y=7)

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

# Шрифты

# A1
a1_lb = Label(text='А',font=font12, fg=red_color, bg=black_color)
a1_lb.place(x=1210, y=79)

# A2
def a2_red(event):
    a2_lb['fg'] = red_color
def a2_white(event):
    a2_lb['fg'] = white_color
a2_lb = Label(text='А',font=font14, fg=white_color, bg=black_color)
a2_lb.place(x=1225, y=76)
a2_lb.bind('<Enter>', a2_red)
a2_lb.bind('<Leave>', a2_white)

# A3
def a3_red(event):
    a3_lb['fg'] = red_color
def a3_white(event):
    a3_lb['fg'] = white_color
a3_lb = Label(text='А',font=font16, fg=white_color, bg=black_color)
a3_lb.place(x=1240, y=75)
a3_lb.bind('<Enter>', a3_red)
a3_lb.bind('<Leave>', a3_white)


# Постеры
poster1_img = PhotoImage(file='poster1.png')
poster2_img = PhotoImage(file='poster2.png')
poster3_img = PhotoImage(file='poster3.png')
poster4_img = PhotoImage(file='poster4.png')
poster5_img = PhotoImage(file='poster5.png')
poster6_img = PhotoImage(file='poster6.png')


poster = Label(image=poster1_img, bg=white_color, borderwidth=0, highlightthickness=0)
poster.place(x=27, y=190)

def poster1():
    global poster
    poster['image'] = poster1_img
def poster2():
    global poster
    poster['image'] = poster2_img
def poster3():
    global poster
    poster['image'] = poster3_img
def poster4():
    global poster
    poster['image'] = poster4_img
def poster5():
    global poster
    poster['image'] = poster5_img
def poster6():
    global poster
    poster['image'] = poster6_img

empty_png = PhotoImage(file='empty.png')
button1 = Button(image=empty_png, bg=red_color, borderwidth=0, highlightthickness=0, command=poster1)
button1.place(x=1121, y=202)
button2 = Button(image=empty_png, bg=red_color, borderwidth=0, highlightthickness=0, command=poster2)
button2.place(x=1139, y=202)
button3 = Button(image=empty_png, bg=red_color, borderwidth=0, highlightthickness=0, command=poster3)
button3.place(x=1158, y=202)
button4 = Button(image=empty_png, bg=red_color, borderwidth=0, highlightthickness=0, command=poster4)
button4.place(x=1177, y=202)
button5 = Button(image=empty_png, bg=red_color, borderwidth=0, highlightthickness=0, command=poster5)
button5.place(x=1195, y=202)
button6 = Button(image=empty_png, bg=red_color, borderwidth=0, highlightthickness=0, command=poster6)
button6.place(x=1214, y=202)

# Личный кабинет
def account_gray(event):
    account_button['image'] = account_image_gray
def account_white(event):
    account_button['image'] = account_image_white

def account_window():
    # Окно личного кабинета
    acc_window = Toplevel(main_window)
    acc_window.title('Личный кабинет пользователя')
    acc_window.config(width=500, height=600, bg=white_color)
    acc_window.resizable(False, False)

    acc_window.user_logo_img = PhotoImage(file='user_big.png')
    user_logo = Label(acc_window, image=acc_window.user_logo_img, bg=white_color, highlightthickness=0)
    user_logo.place(x=186, y=0)
    welcome_lb = Label(acc_window, text='Добро пожаловать!', font=font20b, bg=white_color, fg=black_color)
    welcome_lb.place(x=140, y=130)
    # Регистрация
    registration_lb = Label(acc_window, text='Регистрация', font=font17, bg=white_color, fg=red_color)
    registration_lb.place(x=200, y=170)
    # Имя
    user_name_entry = Entry(acc_window, width=28, font=font17, justify='center', relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0)
    user_name_entry.place(x=85, y=210)
    user_name_entry.insert(0, 'Введите ваше имя')
    # Логин
    login_entry = Entry(acc_window, width=28, font=font17, justify='center', relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0)
    login_entry.place(x=85, y=260)
    login_entry.insert(0, 'Придумайте логин')
    # Пароль
    password_entry = Entry(acc_window, width=28, font=font17, justify='center', relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0)
    password_entry.place(x=85, y=310)
    password_entry.insert(0, 'Придумайте пароль')

    def user_name_clear(event):
        user_name_entry.delete(0, END)
    user_name_entry.bind('<ButtonPress>', user_name_clear)
    def user_name_start(event):
        user_name_entry.insert(0, '  Поиск')
    user_name_entry.bind('<Deactivate>', user_name_start)

    def login_clear(event):
        login_entry.delete(0, END)
    login_entry.bind('<ButtonPress>', login_clear)
    def password_clear(event):
        password_entry.delete(0, END)
    password_entry.bind('<ButtonPress>', password_clear)

    registration_button = Button(acc_window, text='Зарегистрироваться', font=font20, bg=red_color, fg=white_color, width=27, height=2)
    registration_button.place(x=87, y=370)




account_image_white = PhotoImage(file='user_white.png')
account_image_gray = PhotoImage(file='user_gray.png')

account_button = Button(image=account_image_white, bg=red_color, borderwidth=0, highlightthickness=0, command=account_window)
account_button.place(x=1245,y=9)
account_button.bind('<Enter>', account_gray)
account_button.bind('<Leave>', account_white)



main_window.mainloop()