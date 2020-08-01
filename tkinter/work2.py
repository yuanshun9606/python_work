import tkinter as tk

def main():
    window = tk.Tk()
    window.title('work2')
    window.geometry('500x300')
    e = tk.Entry(window,show = None, font = ('Arial',14))
    e.pack()

    # 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
    def insert_point():  # 在鼠标焦点处插入输入内容
        var = e.get()
        t.insert('insert', var)

    def insert_end():  # 在文本框内容最后接着插入输入内容
        var = e.get()
        t.insert('end', var)

    # 第6步，创建并放置两个按钮分别触发两种情况
    b1 = tk.Button(window, text='insert point', width=10,
                   height=2, command=insert_point)
    b1.pack()
    b2 = tk.Button(window, text='insert end', width=10,
                   height=2, command=insert_end)
    b2.pack()

    # 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
    t = tk.Text(window, height=3)
    t.pack()

    tk.mainloop()



if __name__ == '__main__':
    main()