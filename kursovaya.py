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
main_window.iconbitmap('logo.ico')


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
                                height=35, width=2, font=font14b, foreground=red_color,
                                state='readonly')
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


# Личный кабинет

user = []
authorized = False
transactions = [
    {'Дата': '2024-10-26', 'Литры': 23, 'Бензин': '92', 'Сумма': '2300', 'Бонусы' : '23'},
    {'Дата': '2024-10-27', 'Литры': 15, 'Бензин': '95', 'Сумма': '1500', 'Бонусы' : '15'}
]

def account_gray(event):
    account_button['image'] = account_image_gray
def account_white(event):
    account_button['image'] = account_image_white

user_logo_img = PhotoImage(file='user_big.png')
add_image = PhotoImage(file='add.png')
add_image_gray = PhotoImage(file='add_gray.png')

def account_window():
    # Окно личного кабинета
    acc_window = Toplevel(main_window)
    acc_window.title('Личный кабинет пользователя')
    acc_window.config(width=400, height=480, bg=white_color)
    acc_window.resizable(False, False)
    acc_window.iconbitmap('logo.ico')

    user_logo = Label(acc_window, image=user_logo_img, bg=white_color, highlightthickness=0)
    user_logo.place(x=136, y=0)
    welcome_lb = Label(acc_window, text='', width=31, justify='center', font=font20b, bg=black_color, fg=white_color)
    welcome_lb.place(x=0, y=135)

    # Регистрация
    def logged_out():
        welcome_lb['text'] = 'Добро пожаловать!'
        registration_lb = Label(acc_window, text='Регистрация', font=font17, bg=white_color, fg=red_color)
        registration_lb.place(x=150, y=175)
        # Имя
        user_name = StringVar()
        user_name_entry = Entry(acc_window, textvariable=user_name, width=28, fg=black_color, font=font17,
                                justify='center',
                                relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0,
                                selectbackground=red_color)
        user_name_entry.place(x=35, y=210)
        user_name_entry.insert(0, 'Введите ваше имя')
        # Логин
        login = StringVar()
        login_entry = Entry(acc_window, textvariable=login, width=28, fg=black_color, font=font17, justify='center',
                            relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0,
                            selectbackground=red_color)
        login_entry.place(x=35, y=260)
        login_entry.insert(0, 'Придумайте логин')
        # Пароль
        password = StringVar()
        password_entry = Entry(acc_window, textvariable=password, width=28, fg=black_color, font=font17,
                               justify='center', show='',
                               relief='groove', highlightcolor=red_color, highlightthickness=2, borderwidth=0,
                               selectbackground=red_color)
        password_entry.place(x=35, y=310)
        password_entry.insert(0, 'Придумайте пароль')

        # Ввод имени
        def user_name_clear(event):
            if user_name_entry.get() and user_name_entry.get() != 'Введите ваше имя' and user_name_entry.get() != (
                    '*' * 17):
                pass
            else:
                user_name_entry.delete(0, END)
        def user_name_start(event):
            if user_name_entry.get():
                pass
            else:
                user_name_entry.delete(0, END)
                user_name_entry.insert(0, 'Введите ваше имя')
        user_name_entry.bind('<FocusIn>', user_name_clear)
        user_name_entry.bind('<FocusOut>', user_name_start)

        # Ввод логина
        def login_clear(event):
            if login_entry.get() and login_entry.get() != 'Придумайте логин':
                pass
            else:
                login_entry.delete(0, END)
        def login_start(event):
            if login_entry.get():
                pass
            else:
                login_entry.delete(0, END)
                login_entry.insert(0, 'Придумайте логин')
        login_entry.bind('<FocusIn>', login_clear)
        login_entry.bind('<FocusOut>', login_start)

        # Ввод пароля
        def password_clear(event):
            if password_entry.get() and password_entry.get() != 'Придумайте пароль':
                pass
            else:
                password_entry.delete(0, END)
        def password_start(event):
            if password_entry.get():
                pass
            else:
                password_entry.delete(0, END)
                password_entry.insert(0, 'Придумайте пароль')
        def password_enter(event):
            password_entry['show'] = '*'

        password_entry.bind('<FocusIn>', password_clear)
        password_entry.bind('<FocusOut>', password_start)
        password_entry.bind('<KeyPress>', password_enter)

        # Получение данных о регистрации
        def log_in():
            global user, authorized
            u_name = user_name_entry.get()
            u_login = login_entry.get()
            u_password = password_entry.get()
            user = [u_name, u_login, u_password]
            authorized = True
            if authorized:
                logged_in()
                registration_lb.destroy()
                user_name_entry.destroy()
                login_entry.destroy()
                password_entry.destroy()
                registration_button.destroy()

        registration_button = Button(acc_window, text='Зарегистрироваться', font=font20, bg=red_color, fg=white_color,
                                     width=28, height=2, relief='flat', borderwidth=0, command=log_in,
                                     activebackground=gray_color, activeforeground=white_color)
        registration_button.place(x=35, y=375)


    def logged_in():
        def log_out():
            global authorized
            authorized = False
            expenses_img_lb.destroy()
            expenses_lb.destroy()
            bonuses_img_lb.destroy()
            bonuses_lb.destroy()
            log_out_button.destroy()
            logged_out()

        def expenses_window():

            def add_transaction(event):
                add_window = Toplevel(main_window)
                add_window.title('Добавление транзакции')
                add_window.config(width=500, height=100, bg=white_color)
                add_window.resizable(False, False)
                add_window.iconbitmap('logo.ico')

                date_label = Label(add_window, text="Дата:", font=font16, bg=white_color, fg=red_color)
                date_label.place(x=0, y=5)
                date_entry = Entry(add_window)
                date_entry.place(x=0, y=30)

                litres_label = Label(add_window, text="Литры:", font=font16, bg=white_color, fg=red_color)
                litres_label.place(x=100, y=5)
                litres_entry = Entry(add_window)
                litres_entry.place(x=100, y=30)

                gas_label = Label(add_window, text="Бензин:", font=font16, bg=white_color, fg=red_color)
                gas_label.place(x=200, y=5)
                gas_entry = Entry(add_window)
                gas_entry.place(x=200, y=30)

                add_button = Button(add_window, text="Добавить \n транзакцию", font=font16, bg=white_color, fg=red_color)
                add_button.place(x=375, y=15)

                print('Добавить транзакцию')
            def add_tr_gray(event):
                add_transact_lb['fg'] = gray_color
                add_image_lb['image'] = add_image_gray
            def add_tr_red(event):
                add_transact_lb['fg'] = red_color
                add_image_lb['image'] = add_image

            exp_window = Toplevel(main_window)
            exp_window.title('История транзакций')
            exp_window.config(width=500, height=500, bg=white_color)
            exp_window.resizable(False, False)
            exp_window.iconbitmap('logo.ico')

            user_logo = Label(exp_window, image=user_logo_img, bg=white_color, highlightthickness=0)
            user_logo.place(x=186, y=0)
            name_lb = Label(exp_window, text=user[0], width=38, justify='center', font=font20b, bg=black_color, fg=white_color)
            name_lb.place(x=0, y=135)

            transactions_lb = Label(exp_window, text='История транзакций', font=font17, bg=white_color, fg=red_color)
            transactions_lb.place(x=5, y=175)
            add_image_lb = Label(exp_window, image=add_image, bg=white_color, activebackground=white_color)
            add_image_lb.place(x=275, y=178)
            add_transact_lb = Label(exp_window, text='Добавить транзакцию', font=font14b, bg=white_color, fg=red_color)
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
            columnstyle.configure('Treeview', font=font16, background=white_color, foreground=black_color, fieldbackground="#E1E1E1")
            columnstyle.map('Treeview', background=[('selected', red_color)])
            transactions_list = ttk.Treeview(exp_window, columns=('Дата', 'Литры', 'Бензин', 'Сумма', 'Бонусы'), show="headings")
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

            # date = '04/05/2023'
            # litres = 20
            # gas = '92'
            # gas92 = 40
            # summ = litres * gas92
            # bonus = summ * 0.1

            for transaction in transactions:
                transactions_list.insert('', END, values=(transaction['Дата'],
                                                         transaction['Литры'],
                                                         transaction['Бензин'],
                                                         transaction['Сумма'],
                                                         transaction['Бонусы'],))

            # transactions_list.insert('', END, values=(date, litres, gas, summ, bonus))

            transactions_list.place(x=7, y=210)


        def bonuses_window():
            bonus_window = Toplevel(main_window)
            bonus_window.title('Бонусы')
            bonus_window.config(width=400, height=500, bg=white_color)
            bonus_window.resizable(False, False)
            bonus_window.iconbitmap('logo.ico')

            user_logo = Label(bonus_window, image=user_logo_img, bg=white_color, highlightthickness=0)
            user_logo.place(x=136, y=0)
            name_lb = Label(bonus_window, text=user[0], width=31, justify='center', font=font20b, bg=black_color,
                               fg=white_color)
            name_lb.place(x=0, y=135)


        welcome_lb['text'] = user[0]

        acc_window.expenses_img = PhotoImage(file='expenses.png')
        acc_window.bonuses_img = PhotoImage(file='bonuses.png')
        expenses_img_lb = Button(acc_window, image=acc_window.expenses_img, bg=white_color, relief='flat',
                                 borderwidth=0, activebackground=white_color, command=expenses_window)
        expenses_img_lb.place(x=54, y=225)
        expenses_lb = Label(acc_window, text='Транзакции', font=font17, fg=red_color, bg=white_color, justify='center',
                            width=11)
        expenses_lb.place(x=54, y=365)
        bonuses_img_lb = Button(acc_window, image=acc_window.bonuses_img, bg=white_color, relief='flat',
                                borderwidth=0, activebackground=white_color, command=bonuses_window)
        bonuses_img_lb.place(x=219, y=225)
        bonuses_lb = Label(acc_window, text='Бонусы и скидки', font=font17, fg=red_color, bg=white_color,
                           width=13)
        bonuses_lb.place(x=209, y=365)

        log_out_button = Button(acc_window, text='Выйти', bg=white_color, fg=black_color, font=font16,
                                relief='flat', borderwidth=0, activebackground=white_color, command=log_out)
        log_out_button.place(x=170, y=430)


    if authorized == False:
        logged_out()

    if authorized == True:
        logged_in()


account_image_white = PhotoImage(file='user_white.png')
account_image_gray = PhotoImage(file='user_gray.png')

account_button = Button(image=account_image_white, bg=red_color,
                        borderwidth=0, highlightthickness=0, activebackground=red_color,
                        command=account_window)
account_button.place(x=1245, y=9)
account_button.bind('<Enter>', account_gray)
account_button.bind('<Leave>', account_white)



main_window.mainloop()