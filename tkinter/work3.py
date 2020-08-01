import tkinter as tk


def main():
    window = tk.Tk()
    window.title('计算器')
    window.geometry('500x300')
    e = tk.StringVar()

    def jafa():
        a = int(e1.get())
        b = int(e2.get())
        e.set(a+b)

    e1 = tk.Entry(window, show=None)
    e2 = tk.Entry(window, show=None)
    e3 = tk.Entry(window, textvariable=e)
    b1 = tk.Button(window, text='+', width=3,height=1, command=jafa)

    e1.pack()
    e2.pack()
    b1.pack()
    e3.pack()


    tk.mainloop()


if __name__ == '__main__':
    main()