#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

class MyFileSelector():
    # 講義資料では，__init__(self)でGUIを設定・表示しましたが，
    # ↓このように関数の中でGUIを表示するという使い方もできます．
    def show_dialog(self):
        root = tk.Tk()
        root.title('File Selector')
        root.geometry("500x150")

        button = tk.Button(root, text='ファイルダイアログを開く', font=('', 20),
                           width=24, height=1, bg='#999999', activebackground="#aaaaaa")
        button.bind('<ButtonPress>', self.file_dialog)
        button.pack(pady=40)

        self.file_name = tk.StringVar()
        self.file_name.set('未選択です')
        label = tk.Label(textvariable=self.file_name, font=('', 12))
        label.pack(pady=0)

        root.mainloop()

    def file_dialog(self, event):
        fTyp = [("All Files", "*.*"),("PNG Files", "*.png")]
        iDir = os.getcwd()
        file_name = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        if len(file_name) == 0:
            self.file_name.set('選択をキャンセルしました')
        else:
            tkinter.messagebox.showinfo('TkinterFileIO',f'{file_name} が選択されました')
            self.file_name.set(file_name)

    def get_filename(self):
        print(f"ファイル名は{self.file_name.get()}")
        return self.file_name.get()

if __name__ == '__main__':
    mycsvselecter = MyCSVSelecter()
    mycsvselecter.show_dialog()
    print(mycsvselecter.get_filename())