import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title('Welcome to Website')
window.geometry('400x300')


canvas = tk.Canvas(window, width=400, height=135, bg='green')   # 画布
image_file = tk.PhotoImage(file='pc.gif')  # 图片文件
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')

tk.Label(window, text='Welcome', font=('Arial', 16)).pack()
tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=175)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120, y=215)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='Welcome', message='How are you？')
        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tkinter.messagebox.askyesno('Welcome! ', 'You have not sign up yet.Sign up now?')
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_Website():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign uo window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=130, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=130, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_new_pwd_confirm.place(x=130, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Website)
    btn_confirm_sign_up.place(x=180, y=120)


btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=200,y=240)
tk.mainloop()
