import tkinter as tk


# import tkinter.messagebox

def main():

    # 创建顶层窗口
    window = tk.Tk()
    # 设置窗口大小
    window.geometry('800x600')  # 小写eiks
    # 设置窗口标题
    window.title('私人定制')
    l = tk.Label(window, text='你好！this is Tkinter', bg='green', fg='white', font=('Arial', 12), width=30, height=2)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    # Label内容content区域放置位置，自动调节尺寸
    # l.pack()
    var = tk.StringVar()
    l1 = tk.Label(window, textvariable=var, bg='red', fg='white', font=('Arial', 12), width=30, height=2)
    l1.pack()
    on_hit = False

    def hit_me():
        nonlocal on_hit
        if on_hit == False:
            on_hit = True
            var.set('you hit me')
        else:
            on_hit = False
            var.set('')

    b = tk.Button(window, text="按钮", command=hit_me)

    b.pack()
    # 开启主事件循环
    # 放到main()的末尾
    tk.mainloop()



if __name__ == '__main__':
    main()