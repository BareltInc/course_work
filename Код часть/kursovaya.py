from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar

white_color = '#ffffff'
black_color = '#000000'
gray_color = '#555555'
dark_gray_color = '#404040'
red_gray_color = '#e9928d'
red_color_day = '#db2b36'
red_color_night = '#800000'
main_color = white_color
red_color = red_color_day

font12 = 'Cuprum 12 normal'
font14 = 'Cuprum 14 normal'
font14b = 'Cuprum 14 bold'
font15b = 'Cuprum 15 bold'
font16 = 'Cuprum 16 normal'
font17 = 'Cuprum 17 normal'
font17b = 'Cuprum 17 bold'
font20 = 'Cuprum 20 normal'
font20b = 'Cuprum 20 bold'

main_window = Tk()
main_window.config(width=1280, height=747, bg=main_color)
main_window.resizable(False, False)
main_window.title('ЛУКОИЛ - Официальный сайт Компании «ЛУКОИЛ»')
main_window.iconbitmap('logo.ico')

red_header = Canvas(width=1280, height=40, bg=red_color, borderwidth=0, highlightthickness=0)
red_header.place(x=0, y=0)
red_header.create_polygon(210, 20, 220, 20, 215, 25, fill=white_color, activefill=red_gray_color)

def global_business_gray(event):
    global_business_lb['fg'] = red_gray_color
def global_business_white(event):
    global_business_lb['fg'] = white_color
global_business_lb = Label(text='Глобальный бизнес',font=font15b, fg=white_color, bg=red_color)
global_business_lb.place(x=30, y=7)
global_business_lb.bind('<Enter>', global_business_gray)
global_business_lb.bind('<Leave>', global_business_white)

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

def network_gray(event):
    network_lb['fg'] = red_gray_color
def network_white(event):
    network_lb['fg'] = white_color
network_lb = Label(text='Сеть АЗС',font=font15b, fg=white_color, bg=red_color)
network_lb.place(x=465, y=7)
network_lb.bind('<Enter>', network_gray)
network_lb.bind('<Leave>', network_white)

def tenders_gray(event):
    tenders_lb['fg'] = red_gray_color
def tenders_white(event):
    tenders_lb['fg'] = white_color
tenders_lb = Label(text='Тендеры',font=font15b, fg=white_color, bg=red_color)
tenders_lb.place(x=565, y=7)
tenders_lb.bind('<Enter>', tenders_gray)
tenders_lb.bind('<Leave>', tenders_white)

def vacancies_gray(event):
    vacancies_lb['fg'] = red_gray_color
def vacancies_white(event):
    vacancies_lb['fg'] = white_color
vacancies_lb = Label(text='Вакансии',font=font15b, fg=white_color, bg=red_color)
vacancies_lb.place(x=665, y=7)
vacancies_lb.bind('<Enter>', vacancies_gray)
vacancies_lb.bind('<Leave>', vacancies_white)

def contacts_gray(event):
    contacts_lb['fg'] = red_gray_color
def contacts_white(event):
    contacts_lb['fg'] = white_color
contacts_lb = Label(text='Контакты',font=font15b, fg=white_color, bg=red_color)
contacts_lb.place(x=765, y=7)
contacts_lb.bind('<Enter>', contacts_gray)
contacts_lb.bind('<Leave>', contacts_white)

def search_clear(event):
    search.delete(0, END)
def search_start(event):
    if search == '':
        search.insert(0, '  Поиск')

search = Entry(main_window, font=font15b, fg=red_gray_color, bg=main_color, borderwidth=0, highlightthickness=0)
search.place(x=875, y=8, width=265, height=25)
search.insert(0, '  Поиск')
search.bind('<ButtonPress>', search_clear)
search.bind('<FocusOut>', search_start)
div_search = Canvas(width=1, height=15, bg=red_color, borderwidth=0, highlightthickness=0, relief='flat')
div_search.place(x=1100, y=13)
search_img_day = PhotoImage(file='search_light.png')
search_img_night = PhotoImage(file='search_dark.png')
search_button = Button(image=search_img_day, bg=main_color, borderwidth=0, highlightthickness=0, relief='flat')
search_button.place(x=1112, y=13)

div_lang = Canvas(width=1, height=25, bg=main_color, borderwidth=0, highlightthickness=0)
div_lang.place(x=1150, y=8)
languages = ['RU', 'EN']
languages_default = StringVar(value=languages[0])
lang_style = ttk.Style()
lang_style.configure('TCombobox', selectbackground=white_color, selectforeground=red_color,
                                    background=white_color, foreground=red_color, fieldbackground=white_color,
                                    darkcolor=white_color,
                                    lightcolor=white_color)
languages_choose = ttk.Combobox(main_window, state='readonly', textvariable=languages_default, values=languages,
                                height=35, width=2, font=font14b)
languages_choose.place(x=1160, y=7)

black_header = Canvas(width=1280, height=100, bg=black_color, borderwidth=0, highlightthickness=0)
black_header.place(x=0, y=65)
logo_blackbg = PhotoImage(file='logo_blackbg.png')
logo_graybg = PhotoImage(file='logo_graybg.png')

lukoil_logo = Label(image=logo_blackbg, bg=black_color, borderwidth=0, highlightthickness=0)
lukoil_logo.place(x=30, y=85)

def company_red(event):
    company_lb['fg'] = red_color
def company_white(event):
    company_lb['fg'] = white_color
company_lb = Label(text='КОМПАНИЯ',font=font17, fg=white_color, bg=black_color)
company_lb.place(x=465, y=130)
company_lb.bind('<Enter>', company_red)
company_lb.bind('<Leave>', company_white)

def business_red(event):
    business_lb['fg'] = red_color
def business_white(event):
    business_lb['fg'] = white_color
business_lb = Label(text='БИЗНЕС',font=font17, fg=white_color, bg=black_color)
business_lb.place(x=580, y=130)
business_lb.bind('<Enter>', business_red)
business_lb.bind('<Leave>', business_white)

def investors_red(event):
    investors_lb['fg'] = red_color
def investors_white(event):
    investors_lb['fg'] = white_color
investors_lb = Label(text='ИНВЕСТОРЫ',font=font17, fg=white_color, bg=black_color)
investors_lb.place(x=660, y=130)
investors_lb.bind('<Enter>', investors_red)
investors_lb.bind('<Leave>', investors_white)

def press_red(event):
    press_lb['fg'] = red_color
def press_white(event):
    press_lb['fg'] = white_color
press_lb = Label(text='ПРЕСС-ЦЕНТР',font=font17, fg=white_color, bg=black_color)
press_lb.place(x=780, y=130)
press_lb.bind('<Enter>', press_red)
press_lb.bind('<Leave>', press_white)

def products_red(event):
    products_lb['fg'] = red_color
def products_white(event):
    products_lb['fg'] = white_color
products_lb = Label(text='ПРОДУКЦИЯ',font=font17, fg=white_color, bg=black_color)
products_lb.place(x=915, y=130)
products_lb.bind('<Enter>', products_red)
products_lb.bind('<Leave>', products_white)

def improvement_red(event):
    improvement_lb['fg'] = red_color
def improvement_white(event):
    improvement_lb['fg'] = white_color
improvement_lb = Label(text='УСТОЙЧИВОЕ РАЗВИТИЕ',font=font17, fg=white_color, bg=black_color)
improvement_lb.place(x=1035, y=130)
improvement_lb.bind('<Enter>', improvement_red)
improvement_lb.bind('<Leave>', improvement_white)

a1_lb = Label(text='А', font=font12, fg=red_color, bg=black_color)
a1_lb.place(x=1210, y=79)

def a2_red(event):
    if theme == 'light':
        a2_lb['fg'] = red_color_day
    if theme == 'dark':
        a2_lb['fg'] = red_color_night
def a2_white(event):
    a2_lb['fg'] = white_color
a2_lb = Label(text='А',font=font14, fg=white_color, bg=black_color)
a2_lb.place(x=1225, y=76)
a2_lb.bind('<Enter>', a2_red)
a2_lb.bind('<Leave>', a2_white)

def a3_red(event):
    if theme == 'light':
        a3_lb['fg'] = red_color_day
    if theme == 'dark':
        a3_lb['fg'] = red_color_night
def a3_white(event):
    a3_lb['fg'] = white_color
a3_lb = Label(text='А',font=font16, fg=white_color, bg=black_color)
a3_lb.place(x=1240, y=75)
a3_lb.bind('<Enter>', a3_red)
a3_lb.bind('<Leave>', a3_white)

poster1_img = PhotoImage(file='poster1_light.png')
poster2_img = PhotoImage(file='poster2_light.png')
poster3_img = PhotoImage(file='poster3_light.png')
poster4_img = PhotoImage(file='poster4_light.png')
poster5_img = PhotoImage(file='poster5_light.png')
poster6_img = PhotoImage(file='poster6_light.png')
poster = Label(image=poster4_img, bg=main_color, borderwidth=0, highlightthickness=0)
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

empty = PhotoImage(file='empty.png')
button1 = Button(image=empty, bg=red_color, borderwidth=0, highlightthickness=0, command=poster1)
button1.place(x=1121, y=202)
button2 = Button(image=empty, bg=red_color, borderwidth=0, highlightthickness=0, command=poster2)
button2.place(x=1139, y=202)
button3 = Button(image=empty, bg=red_color, borderwidth=0, highlightthickness=0, command=poster3)
button3.place(x=1158, y=202)
button4 = Button(image=empty, bg=red_color, borderwidth=0, highlightthickness=0, command=poster4)
button4.place(x=1177, y=202)
button5 = Button(image=empty, bg=red_color, borderwidth=0, highlightthickness=0, command=poster5)
button5.place(x=1195, y=202)
button6 = Button(image=empty, bg=red_color, borderwidth=0, highlightthickness=0, command=poster6)
button6.place(x=1214, y=202)

def sun_gray(event):
    theme_button['image'] = sun_gray_img
def sun_white(event):
    theme_button['image'] = sun_img
def moon_gray(event):
    theme_button['image'] = moon_gray_img
def moon_white(event):
    theme_button['image'] = moon_img

theme = 'light'
def dark_theme(event):
    global  main_color, red_color, theme
    theme = 'dark'
    main_color = dark_gray_color
    red_color = red_color_night
    main_window.configure(bg=main_color)
    red_header['bg'] = red_color_night
    global_business_lb['bg'] = red_color_night
    tg['bg'] = red_color_night
    vk['bg'] = red_color_night
    yt['bg'] = red_color_night
    network_lb['bg'] = red_color_night
    tenders_lb['bg'] = red_color_night
    vacancies_lb['bg'] = red_color_night
    contacts_lb['bg'] = red_color_night
    search_button['image'] = search_img_night
    div_search['bg'] = red_color_night
    lang_style.configure('TCombobox', selectforeground=red_color_night, foreground=red_color_night)
    theme_button['bg'] = red_color_night
    theme_button['image'] = moon_img
    account_button['bg'] = red_color_night
    account_button['activebackground'] = red_color_night
    black_header['bg'] = gray_color
    lukoil_logo['image'] = logo_graybg
    company_lb['bg'] = gray_color
    business_lb['bg'] = gray_color
    investors_lb['bg'] = gray_color
    press_lb['bg'] = gray_color
    products_lb['bg'] = gray_color
    improvement_lb['bg'] = gray_color
    a1_lb['bg'] = gray_color
    a1_lb['fg'] = red_color_night
    a2_lb['bg'] = gray_color
    a3_lb['bg'] = gray_color
    button1['bg'] = red_color_night
    button2['bg'] = red_color_night
    button3['bg'] = red_color_night
    button4['bg'] = red_color_night
    button5['bg'] = red_color_night
    button6['bg'] = red_color_night
    poster1_img['file'] = 'poster1_dark.png'
    poster2_img['file'] = 'poster2_dark.png'
    poster3_img['file'] = 'poster3_dark.png'
    poster4_img['file'] = 'poster4_dark.png'
    poster5_img['file'] = 'poster5_dark.png'
    poster6_img['file'] = 'poster6_dark.png'
    theme_button.bind('<Enter>', moon_gray)
    theme_button.bind('<Leave>', moon_white)
    theme_button.bind('<Button>', light_theme)

def light_theme(event):
    global main_color, red_color, theme
    theme = 'light'
    main_color = white_color
    red_color = red_color_day
    main_window.configure(bg=main_color)
    red_header['bg'] = red_color_day
    global_business_lb['bg'] = red_color_day
    tg['bg'] = red_color_day
    vk['bg'] = red_color_day
    yt['bg'] = red_color_day
    network_lb['bg'] = red_color_day
    tenders_lb['bg'] = red_color_day
    vacancies_lb['bg'] = red_color_day
    contacts_lb['bg'] = red_color_day
    search_button['image'] = search_img_day
    div_search['bg'] = red_color_day
    lang_style.configure('TCombobox', selectforeground=red_color_day, foreground=red_color_day)
    theme_button['bg'] = red_color_day
    theme_button['image'] = sun_img
    account_button['bg'] = red_color_day
    account_button['activebackground'] = red_color_day
    black_header['bg'] = black_color
    lukoil_logo['image'] = logo_blackbg
    company_lb['bg'] = black_color
    business_lb['bg'] = black_color
    investors_lb['bg'] = black_color
    press_lb['bg'] = black_color
    products_lb['bg'] = black_color
    improvement_lb['bg'] = black_color
    a1_lb['bg'] = black_color
    a1_lb['fg'] = red_color_day
    a2_lb['bg'] = black_color
    a3_lb['bg'] = black_color
    button1['bg'] = red_color_day
    button2['bg'] = red_color_day
    button3['bg'] = red_color_day
    button4['bg'] = red_color_day
    button5['bg'] = red_color_day
    button6['bg'] = red_color_day
    poster1_img['file'] = 'poster1_light.png'
    poster2_img['file'] = 'poster2_light.png'
    poster3_img['file'] = 'poster3_light.png'
    poster4_img['file'] = 'poster4_light.png'
    poster5_img['file'] = 'poster5_light.png'
    poster6_img['file'] = 'poster6_light.png'
    theme_button.bind('<Enter>', sun_gray)
    theme_button.bind('<Leave>', sun_white)
    theme_button.bind('<Button>', dark_theme)


sun_img = PhotoImage(file='sun.png')
sun_gray_img = PhotoImage(file='sun_gray.png')
moon_img = PhotoImage(file='moon.png')
moon_gray_img = PhotoImage(file='moon_gray.png')
theme_button = Label(image=sun_img, bg=red_color,
                        borderwidth=0, highlightthickness=0, activebackground=red_color)
theme_button.bind('<Enter>', sun_gray)
theme_button.bind('<Leave>', sun_white)
theme_button.bind('<Button>', dark_theme)
theme_button.place(x=1212, y=9)

def account_gray(event):
    account_button['image'] = account_image_gray
def account_white(event):
    account_button['image'] = account_image_white
account_image_white = PhotoImage(file='user_white.png')
account_image_gray = PhotoImage(file='user_gray.png')

user_logo_img = PhotoImage(file='user_big_light.png')
add_image = PhotoImage(file='add_light.png')
add_image_gray = PhotoImage(file='add_gray.png')
coin_img = PhotoImage(file='coin_light.png')
user = []
authorise_status = False
reg_log = 'reg'
transactions = []
bonuses = 0

def account_window():
    global authorise_status
    if theme == 'light':
        main_color = white_color
        red_color = red_color_day
        user_logo_img['file'] = 'user_big_light.png'
    if theme == 'dark':
        main_color = dark_gray_color
        red_color = red_color_night
        user_logo_img['file'] = 'user_big_dark.png'

    acc_window = Toplevel(main_window)
    acc_window.title('Личный кабинет')
    acc_window.config(width=400, height=480, bg=main_color)
    acc_window.resizable(False, False)
    acc_window.iconbitmap('logo.ico')

    user_logo = Label(acc_window, image=user_logo_img, bg=main_color, highlightthickness=0)
    user_logo.place(x=136, y=0)
    welcome_lb = Label(acc_window, text='', width=31, justify='center', font=font20b, bg=black_color, fg=white_color)
    welcome_lb.place(x=0, y=135)

    def unauthorised():
        if theme == 'light':
            main_color = white_color
            red_color = red_color_day
        if theme == 'dark':
            main_color = dark_gray_color
            red_color = red_color_night
        global reg_log
        welcome_lb['text'] = 'Добро пожаловать!'
        reg_log_lb = Label(acc_window, text='Регистрация', font=font17b, bg=main_color, fg=red_color)
        reg_log_lb.place(x=35, y=175)

        def authorise():
            acc_window.config(width=400, height=480)
            global user, authorise_status
            if reg_log == 'reg':
                u_name = user_name_entry.get()
                u_login = login_entry.get()
                u_password = password_entry.get()
                if u_name != 'Введите ваше имя' and u_login != 'Придумайте логин' and u_password != 'Придумайте пароль':
                    user = [u_name, u_login, u_password]
                    authorise_status = True
                    reg_log_lb.destroy()
                    user_name_entry.destroy()
                    login_entry.destroy()
                    password_entry.destroy()
                    authorise_button.destroy()
                    reg_log_button.destroy()
                    authorised()
                else:
                    authorise_button['text'] = 'Ошибка'

            if reg_log == 'log':
                u_login = login_entry.get()
                u_password = password_entry.get()
                if user!=[] and user[1] == u_login and user[2] == u_password:
                    authorise_status = True
                    reg_log_lb.destroy()
                    user_name_entry.destroy()
                    login_entry.destroy()
                    password_entry.destroy()
                    authorise_button.destroy()
                    reg_log_button.destroy()
                    authorised()
                else:
                    acc_window.configure(width=400, height=420)
                    authorise_button['text'] = 'Ошибка'

        def user_name_clear(event):
            if user_name_entry.get() and user_name_entry.get() != 'Введите ваше имя' and user_name_entry.get() != (
                    '*' * 17):
                authorise_button['text'] = 'Ошибка'
            else:
                user_name_entry.delete(0, END)
        def user_name_start(event):
            if user_name_entry.get():
                authorise_button['text'] = 'Ошибка'
            else:
                user_name_entry.delete(0, END)
                user_name_entry.insert(0, 'Введите ваше имя')
        user_name = StringVar()
        user_name_entry = Entry(acc_window, textvariable=user_name, width=28, fg=black_color, font=font17,
                                justify='center',
                                relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0,
                                selectbackground=red_color)
        user_name_entry.bind('<FocusIn>', user_name_clear)
        user_name_entry.bind('<FocusOut>', user_name_start)

        def login_clear(event):
            if login_entry.get() and login_entry.get() != 'Придумайте логин' and login_entry.get() != 'Введите логин':
                if reg_log == 'log':
                    authorise_button['text'] = 'Войти'
                if reg_log == 'reg':
                    authorise_button['text'] = 'Зарегистрироваться'
            else:
                login_entry.delete(0, END)
                if reg_log == 'log':
                    authorise_button['text'] = 'Войти'
                if reg_log == 'reg':
                    authorise_button['text'] = 'Зарегистрироваться'
        def login_start(event):
            if login_entry.get():
                if reg_log == 'log':
                    authorise_button['text'] = 'Войти'
                if reg_log == 'reg':
                    authorise_button['text'] = 'Зарегистрироваться'
            else:
                login_entry.delete(0, END)
                if reg_log == 'reg':
                    login_entry.insert(0, 'Придумайте логин')
                if reg_log == 'log':
                    login_entry.insert(0, 'Введите логин')

        login = StringVar()
        login_entry = Entry(acc_window, textvariable=login, width=28, fg=black_color, font=font17, justify='center',
                            relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0,
                            selectbackground=red_color)
        login_entry.bind('<FocusIn>', login_clear)
        login_entry.bind('<FocusOut>', login_start)

        def password_clear(event):
            if password_entry.get() and password_entry.get() != 'Придумайте пароль' and password_entry.get() != 'Введите пароль':
                if reg_log == 'log':
                    authorise_button['text'] = 'Войти'
                if reg_log == 'reg':
                    authorise_button['text'] = 'Зарегистрироваться'
            else:
                password_entry.delete(0, END)
                if reg_log == 'log':
                    authorise_button['text'] = 'Войти'
                if reg_log == 'reg':
                    authorise_button['text'] = 'Зарегистрироваться'
        def password_start(event):
            if password_entry.get():
                if reg_log == 'log':
                    authorise_button['text'] = 'Войти'
                if reg_log == 'reg':
                    authorise_button['text'] = 'Зарегистрироваться'
            else:
                password_entry.delete(0, END)
                if reg_log == 'reg':
                    password_entry.insert(0, 'Придумайте пароль')
                if reg_log == 'log':
                    password_entry.insert(0, 'Введите пароль')
        def password_enter(event):
            password_entry['show'] = '*'
        password = StringVar()
        password_entry = Entry(acc_window, textvariable=password, width=28, fg=black_color, font=font17,
                               justify='center', show='',
                               relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0,
                               selectbackground=red_color)
        password_entry.bind('<FocusIn>', password_clear)
        password_entry.bind('<FocusOut>', password_start)
        password_entry.bind('<KeyPress>', password_enter)

        authorise_button = Button(acc_window, text='Зарегистрироваться', font=font20, bg=red_color, fg=white_color,
                                  width=28, height=2, relief='flat', borderwidth=0, command=authorise,
                                  activebackground=red_gray_color, activeforeground=white_color)

        def reg(event):
            global reg_log
            reg_log = 'reg'
            reg_log_lb['text'] = 'Регистрация'
            reg_log_button['text'] = 'Уже есть аккаунт?'
            reg_log_button.place(x=225, y=177)
            reg_log_button.bind('<Button>', log)
            acc_window.config(width=400, height=480, bg=main_color)
            registration()
        def registration():
            user_name_entry.place(x=35, y=210)
            user_name_entry.delete(0, END)
            user_name_entry.insert(0, 'Введите ваше имя')
            login_entry.place(x=35, y=260)
            login_entry.delete(0, END)
            login_entry.insert(0, 'Придумайте логин')
            password_entry.place(x=35, y=310)
            password_entry.delete(0, END)
            password_entry['show'] = ''
            password_entry.insert(0, 'Придумайте пароль')
            authorise_button['text'] = 'Зарегистрироваться'
            authorise_button.place(x=35, y=375)

        def log(event):
            global reg_log
            reg_log = 'log'
            reg_log_lb['text'] = 'Войдите в аккаунт'
            reg_log_button['text'] = 'Нет аккаунта?'
            reg_log_button.place(x=260, y=177)
            reg_log_button.bind('<Button>', reg)
            acc_window.config(width=400, height=420, bg=main_color)
            log_in()
        def log_in():
            user_name_entry.place(x=10000, y=10000)
            login_entry.place(x=35, y=210)
            login_entry.delete(0, END)
            login_entry.insert(0, 'Введите логин')
            password_entry.place(x=35, y=260)
            password_entry.delete(0, END)
            password_entry.insert(0, 'Введите пароль')
            authorise_button['text'] = 'Войти'
            authorise_button.place(x=35, y=310)

        if reg_log == 'reg':
            registration()
        if reg_log == 'log':
            log_in()

        def login_gray(event):
            reg_log_button['fg'] = red_gray_color
        def login_red(event):
            if theme == 'light':
                reg_log_button['fg'] = red_color_day
            if theme == 'dark':
                reg_log_button['fg'] = red_color_night
        reg_log_button = Label(acc_window, text='Уже есть аккаунт?', font=font16, bg=main_color, fg=red_color)
        reg_log_button.place(x=225, y=177)
        reg_log_button.bind('<Enter>', login_gray)
        reg_log_button.bind('<Leave>', login_red)
        reg_log_button.bind('<Button>', log)

    def authorised():
        def log_out():
            global authorise_status, reg_log
            authorise_status = False
            expenses_img_lb.destroy()
            expenses_lb.destroy()
            bonuses_img_lb.destroy()
            bonuses_lb.destroy()
            log_out_button.destroy()
            reg_log = 'reg'
            unauthorised()

        def expenses_window():
            if theme == 'light':
                main_color = white_color
                sec_color = black_color
                red_color = red_color_day
                add_image['file'] = 'add_light.png'
            if theme == 'dark':
                main_color = dark_gray_color
                sec_color = white_color
                red_color = red_color_night
                add_image['file'] = 'add_dark.png'

            def add_transaction(event):
                if theme == 'light':
                    main_color = white_color
                    sec_color = black_color
                    red_color = red_color_day
                if theme == 'dark':
                    main_color = dark_gray_color
                    sec_color = white_color
                    red_color = red_color_night

                def get_transaction():
                    global bonuses
                    price = 0
                    add_button['text'] = 'Добавить транзакцию'
                    date = calendar.get_date()
                    try:
                        litres = int(litres_entry.get())
                    except:
                        add_button['text'] = 'Ошибка'
                    gas = gas_choose.get()
                    if gas and date:
                        match gas:
                            case '92':
                                price = 53
                            case '95':
                                price = 57
                            case '100':
                                price = 82
                            case 'ДТ':
                                price = 68
                        summ = price*litres
                        transactions.append({'Дата': date, 'Литры': litres, 'Бензин': gas, 'Сумма': summ, 'Бонусы': round(summ*0.1, 2)})
                        bonuses += round(summ*0.1, 2)
                        print(date, litres, gas, bonuses)
                        transactions_list.insert('', END, values=(transactions[-1]['Дата'],
                                                                  transactions[-1]['Литры'],
                                                                  transactions[-1]['Бензин'],
                                                                  transactions[-1]['Сумма'],
                                                                  transactions[-1]['Бонусы'],))
                    else:
                        add_button['text'] = 'Ошибка'


                add_window = Toplevel(exp_window)
                add_window.title('Добавление транзакции')
                add_window.config(width=275, height=360, bg=main_color)
                add_window.resizable(False, False)
                add_window.iconbitmap('logo.ico')

                date_label = Label(add_window, text="Дата:", font=font16, bg=main_color, fg=red_color)
                date_label.place(x=10, y=5)
                calendar = Calendar(add_window, selectmode='day', year=2024, background=red_color, foreground=white_color,
                                    selectbackground=red_color, selectforeground=sec_color)
                calendar.place(x=10, y=30)

                litres_label = Label(add_window, text="Литры:", font=font16, bg=main_color, fg=red_color)
                litres_label.place(x=10, y=210)
                litres_entry = Entry(add_window, width=10, fg=black_color, font=font17, justify='center',
                                     relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0,
                                     selectbackground=black_color, highlightbackground=red_color)
                litres_entry.place(x=10, y=235)

                gas_label = Label(add_window, text="Бензин:", font=font16, bg=main_color, fg=red_color)
                gas_label.place(x=185, y=210)
                gas_types = ['92', '95', '100', 'ДТ']
                gas_var = StringVar()
                gas_style = ttk.Style()
                gas_style.configure('TCombobox', selectbackground=white_color, selectforeground=red_color,
                                    background=white_color, foreground=red_color, fieldbackground=white_color,
                                    darkcolor=red_color,
                                    lightcolor=white_color)
                gas_choose = ttk.Combobox(add_window, state='readonly', textvariable=gas_var, font=font17b, values=gas_types, width=4)
                gas_choose.place(x=185, y=235)

                add_button = Button(add_window, text="Добавить транзакцию", font=font17b, width=20, bg=red_color, fg=white_color,
                                     height=2, relief='flat', borderwidth=0, command=get_transaction,
                                     activebackground=red_gray_color, activeforeground=white_color)
                add_button.place(x=12, y=280)

            def add_tr_gray(event):
                add_transact_lb['fg'] = red_gray_color
                add_image_lb['image'] = add_image_gray
            def add_tr_red(event):
                add_transact_lb['fg'] = red_color
                add_image_lb['image'] = add_image

            exp_window = Toplevel(main_window)
            exp_window.title('История транзакций')
            exp_window.config(width=500, height=500, bg=main_color)
            exp_window.resizable(False, False)
            exp_window.iconbitmap('logo.ico')

            user_logo = Label(exp_window, image=user_logo_img, bg=main_color, highlightthickness=0)
            user_logo.place(x=186, y=0)
            name_lb = Label(exp_window, text=user[0], width=38, justify='center', font=font20b, bg=black_color, fg=white_color)
            name_lb.place(x=0, y=135)

            transactions_lb = Label(exp_window, text='История транзакций', font=font17, bg=main_color, fg=red_color)
            transactions_lb.place(x=5, y=175)
            add_image_lb = Label(exp_window, image=add_image, bg=main_color, activebackground=sec_color)
            add_image_lb.place(x=275, y=178)
            add_transact_lb = Label(exp_window, text='Добавить транзакцию', font=font14b, bg=main_color, fg=red_color)
            add_transact_lb.place(x=303, y=178)
            add_transact_lb.bind('<Enter>', add_tr_gray)
            add_transact_lb.bind('<Leave>', add_tr_red)
            add_transact_lb.bind('<Button>', add_transaction)
            add_image_lb.bind('<Enter>', add_tr_gray)
            add_image_lb.bind('<Leave>', add_tr_red)
            add_image_lb.bind('<Button>', add_transaction)

            headerstyle = ttk.Style()
            headerstyle.configure('Treeview.Heading', font=font17b)
            columnstyle = ttk.Style()
            columnstyle.configure('Treeview', font=font16, background=main_color, foreground=sec_color, fieldbackground=main_color)
            columnstyle.map('Treeview', background=[('selected', red_color)])
            transactions_list = ttk.Treeview(exp_window, columns=('Дата', 'Литры', 'Бензин', 'Сумма', 'Бонусы'), show="headings", height=12)
            transactions_list.column('#1', anchor=CENTER, stretch=NO, width=100)
            transactions_list.heading('#1', text='Дата')
            transactions_list.column('#2', anchor=CENTER, stretch=NO, width=95)
            transactions_list.heading('#2', text="Литры")
            transactions_list.column('#3', anchor=CENTER, stretch=NO, width=95)
            transactions_list.heading('#3', text="Бензин")
            transactions_list.column('#4', anchor=CENTER, stretch=NO, width=100)
            transactions_list.heading('#4', text="Сумма")
            transactions_list.column('#5', anchor=CENTER, stretch=NO, width=95)
            transactions_list.heading('#5', text="Бонусы")
            for transaction in transactions:
                transactions_list.insert('', END, values=(transaction['Дата'],
                                                         transaction['Литры'],
                                                         transaction['Бензин'],
                                                         transaction['Сумма'],
                                                         transaction['Бонусы'],))
            transactions_list.place(x=7, y=210)

        def bonuses_window():
            if theme == 'light':
                main_color = white_color
                sec_color = black_color
                red_color = red_color_day
                coin_img['file'] = 'coin_light.png'
            if theme == 'dark':
                main_color = dark_gray_color
                sec_color = white_color
                red_color = red_color_night
                coin_img['file'] = 'coin_dark.png'
            bonus_window = Toplevel(main_window)
            bonus_window.title('Бонусы')
            bonus_window.config(width=500, height=500, bg=main_color)
            bonus_window.resizable(False, False)
            bonus_window.iconbitmap('logo.ico')

            user_logo = Label(bonus_window, image=user_logo_img, bg=main_color, highlightthickness=0)
            user_logo.place(x=186, y=0)
            name_lb = Label(bonus_window, text=user[0], width=38, justify='center', font=font20b, bg=black_color,
                               fg=white_color)
            name_lb.place(x=0, y=135)

            coin_img_lb = Label(bonus_window, image=coin_img, bg=main_color)
            coin_img_lb.place(x=50, y=220)
            user_bonuses_lb = Label(bonus_window, text=f'Вы накопили \n{bonuses} бонусов', fg=red_color, bg=main_color, font=font17b)
            user_bonuses_lb.place(x=50, y=370)

            promocodes = ['LUKOIL-DRIVE20: \nСкидка 20% на топливо \nпри заправке от 1000 рублей',
                          'LUKOIL-BONUS100: \n100 бонусных баллов \nпри первой заправке.',
                          'LUKOIL-WEEKEND5: \nСкидка 5% на все товары \nв магазинах сети "Лукойл" \nпо выходным дням.']
            y_pos = 185
            for promocode in promocodes:
                promolabel = Label(bonus_window, text=promocode, width=25, font=font16, bg=main_color, fg=sec_color,
                                   relief='solid', highlightthickness=2, borderwidth=0, highlightbackground=red_color)
                promolabel.place(x=225, y=y_pos)
                y_pos += 100

        welcome_lb['text'] = user[0]
        acc_window.expenses_img = PhotoImage(file='expenses_light.png')
        acc_window.bonuses_img = PhotoImage(file='bonuses_dark.png')

        if theme == 'light':
            main_color = white_color
            sec_color = black_color
            red_color = red_color_day
            acc_window.expenses_img['file'] = 'expenses_light.png'
            acc_window.bonuses_img['file'] = 'bonuses_light.png'
        if theme == 'dark':
            main_color = dark_gray_color
            sec_color = white_color
            red_color = red_color_night
            acc_window.expenses_img['file'] = 'expenses_dark.png'
            acc_window.bonuses_img['file'] = 'bonuses_dark.png'

        expenses_img_lb = Button(acc_window, image=acc_window.expenses_img, bg=main_color, relief='flat',
                                 borderwidth=0, activebackground=main_color, command=expenses_window)
        expenses_img_lb.place(x=54, y=225)
        expenses_lb = Label(acc_window, text='Транзакции', font=font17, fg=red_color, bg=main_color, justify='center',
                            width=11)
        expenses_lb.place(x=54, y=365)
        bonuses_img_lb = Button(acc_window, image=acc_window.bonuses_img, bg=main_color, relief='flat',
                                borderwidth=0, activebackground=main_color, command=bonuses_window)
        bonuses_img_lb.place(x=219, y=225)
        bonuses_lb = Label(acc_window, text='Бонусы и скидки', font=font17, fg=red_color, bg=main_color,
                           width=13)
        bonuses_lb.place(x=209, y=365)

        log_out_button = Button(acc_window, text='Выйти', bg=main_color, fg=sec_color, font=font16,
                                relief='flat', borderwidth=0, activebackground=main_color, command=log_out)
        log_out_button.place(x=170, y=430)

    if authorise_status == False:
        unauthorised()
    if authorise_status == True:
        authorised()

account_button = Button(image=account_image_white, bg=red_color,
                        borderwidth=0, highlightthickness=0, activebackground=red_color_day,
                        command=account_window)
account_button.place(x=1245, y=9)
account_button.bind('<Enter>', account_gray)
account_button.bind('<Leave>', account_white)



main_window.mainloop()