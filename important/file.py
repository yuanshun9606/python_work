import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import threading
import os

#选择文件按钮的处理
def selectFile():
    resultlabel.configure(text="", wraplength=600)
    selectfile = tkinter.filedialog.askopenfilename()
    if selectfile != '':
        s_entry.delete(0,tk.END)
        s_entry.insert(0,selectfile)

    src_file=s_entry.get()
    if src_file != '':
        target_file=src_file+".txt"
        t_entry.delete(0, tk.END)
        t_entry.insert(0,target_file)
        convert_button.configure(state="enable")
    else:
        t_entry.delete(0, tk.END)
        convert_button.configure(state="disabled")


def bin2hextext(srcfile,targetfile):
#二进制文件srcfile 转换成文本文件 targetfile，16进制显示，带偏移
    i=1
    try:
        fsrc=open(srcfile,mode='rb')
        ftarget= open(targetfile, mode='w')
        iBytes = fsrc.read()
        print("%08x:" % 0, file=ftarget, end='')
        for s_byte in iBytes:
            print("%02x" % s_byte,file = ftarget,end='')

            if i%16 == 0:
                print("" , file=ftarget)
                print("%08x:" % i, file=ftarget,end='')
            #刷新文件缓存 显示进度
            if i%(128*1024) == 0:
                status = ('%.2f%%' % ((i/(os.path.getsize(srcfile)) * 100)) )
                ftarget.flush()
                resultlabel.configure(text=status)
            i += 1
        fsrc.close()
        ftarget.close()
        return "Convert file successfully"
    except (OSError,TypeError) as reason:
        return "Error"+str(reason)

#创建线程进行处理 防止界面卡死
def convert_thread_func(src,target):
    res = bin2hextext(src, target)
    resultlabel.configure(text=res, wraplength=600)
    convert_button.configure(state="enable")

#转换按键的处理
def convert_func():
    convert_button.configure(state="disabled")
    resultlabel.configure(text="Processing ... ", wraplength=600)
    sf = s_entry.get()
    tf = t_entry.get()
    t=threading.Thread(target=convert_thread_func,args=(sf,tf))
    t.start()


root=tk.Tk()
root.title("bin2text V0.1 by: deep_pro") #第一个版本 2018-10-04
tkinter.Label(root,text="source file:").grid(row=0,column=0)
tkinter.Label(root,text="target file:").grid(row=1,column=0)
tkinter.Label(root,text=" result :").grid(row=2,column=0)
resultlabel=tkinter.Label(root,fg="red",text=" ")
resultlabel.grid(row=2,column=1)
s_entry=tkinter.Entry(width=99)
t_entry=tkinter.Entry(width=99)
s_entry.grid(row=0,column=1)
t_entry.grid(row=1,column=1)

ttk.Label(root,text=" ").grid(row=0,column=2)
ttk.Label(root,text=" ").grid(row=1,column=2)
src_button=ttk.Button(root,text="open",width=8,command = selectFile).grid(row=0,column=3)
convert_button=ttk.Button(root,text="convert",width=8,state="disabled",command=convert_func)
convert_button.grid(row=1,column=3)

root.mainloop()