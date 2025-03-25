from cofig import *
from image2black import *
import tkinter as tk
from tkinter import filedialog

class Level:
    def __init__(self, win):
        '构建GUI界面'
        self.win = win
        
        self.dir_forder = tk.StringVar()
        self.dir_forder.set(DIR_FORDER)
        self.sort_output = tk.StringVar()
        self.sort_output.set(SORT_OUTPUT)
        self.output = tk.StringVar()
        self.output.set(OUTPUT)
        self.pdf_name = tk.StringVar()
        self.pdf_name.set(PDFNAME)
        
        self.black_change = BlackChange(dir_forder = self.dir_forder.get(),
                                        sort_output = self.sort_output.get(),
                                        output = self.output.get(),
                                        pdf_name = self.pdf_name.get()
                                        )
        
    def win_item(self):
        '构建win中按键'
        self.button()
        self.entry()
        
        return self
    
    def button(self):
        '设置按钮'
        button_clear_file = tk.Button(self.win,text='清空文件',command=self.black_change.clear_file)
        button_clear_file.place(x=70,y=130,width=100,height=30)
        
        button_number_sort = tk.Button(self.win,text='文件排序',command=self.black_change.number_sort)
        button_number_sort.place(x=70,y=170,width=100,height=30)
        
        button_clear_file = tk.Button(self.win,text='图像处理',command=self.black_change.black_change)
        button_clear_file.place(x=70,y=210,width=100,height=30)
        
        button_clear_file = tk.Button(self.win,text='载入pdf',command=self.black_change.save2pdf)
        button_clear_file.place(x=70,y=250,width=100,height=30)
        
        return self
    
    def entry(self):
        '设置输入框'
        entry_dir_forder = tk.Entry(self.win, textvariable = self.dir_forder, bd=2)
        entry_dir_forder.place(x=70,y=10,width=100,height=30)
        labal_entry_dir_forder = tk.Label(self.win, text='输入文件夹')
        labal_entry_dir_forder.place(x=0,y=10,width=70,height=30)
        button_entry_dir_forder = tk.Button(self.win,text='...',command=self.select_forder_dir_forder)
        button_entry_dir_forder.place(x=180,y=9,width=30,height=30)
        
        entry_sort_output = tk.Entry(self.win, textvariable = self.sort_output, bd=2)
        entry_sort_output.place(x=70,y=50,width=100,height=30)
        labal_entry_sort_output = tk.Label(self.win, text='排序文件夹')
        labal_entry_sort_output.place(x=0,y=50,width=70,height=30)
        button_entry_sort_output = tk.Button(self.win,text='...',command=self.select_forder_sort_output)
        button_entry_sort_output.place(x=180,y=49,width=30,height=30)
        
        entry_output = tk.Entry(self.win, textvariable = self.output, bd=2)
        entry_output.place(x=70,y=90,width=100,height=30)
        labal_entry_output = tk.Label(self.win, text='输出文件夹')
        labal_entry_output.place(x=0,y=90,width=70,height=30)
        button_entry_output = tk.Button(self.win,text='...',command=self.select_forder_output)
        button_entry_output.place(x=180,y=89,width=30,height=30)
        
        return self
    
    def select_forder_dir_forder(self):
        '选择dir_forder文件夹'
        forder = filedialog.askdirectory()
        self.dir_forder.set(forder)
        
        self.black_change.dir_forder = self.dir_forder.get()
    
    def select_forder_sort_output(self):
        '选择sort_output文件夹'
        forder = filedialog.askdirectory()
        self.sort_output.set(forder)
        
        self.black_change.sort_output = self.sort_output.get()
        
    def select_forder_output(self):
        '选择output文件夹'
        forder = filedialog.askdirectory()
        self.output.set(forder)
        
        self.black_change.output = self.output.get()
    