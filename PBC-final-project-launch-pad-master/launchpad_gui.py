import os
import pydub
from pydub import AudioSegment
from pydub.playback import play

# 看你的音檔位置在哪裡，然後指定位置
os.chdir("C://Users//chtu//Desktop")

# 設定變數名稱，不同種類的音檔就用from_XXX   XXX=mp3,WAV,ogg......etc
song1_raw = AudioSegment.from_mp3("C://Users//chtu//Desktop//AF.mp3")
song2 = AudioSegment.from_mp3("C://Users//chtu//Desktop//Japanese_drum1.mp3")
song3 = AudioSegment.from_mp3("C://Users//chtu//Desktop//guitar.mp3")

# 播放
ten_seconds = 10 * 1000
song1 = song1_raw[:ten_seconds]

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

class launchpad(tk.Frame):

    def __init__(self):

        tk.Frame.__init__(self)
        self.grid()
        self.createwidgets()


        # 視窗
    def createwidgets(self):
        # 字型
        f1 = tkFont.Font(size=40, family='Tw Cen MT')
        # 三個按鍵
        self.btnnum1 = tk.Button(self, text='vocal', fg='white', height=3, width=15, bd=20, command=self.song1_start, font=f1,
                                 bg='black', activebackground='yellow')
        self.btnnum2 = tk.Button(self, text='drum', fg='white', height=3, width=15, bd=20, command=self.song2_start, font=f1,
                                 bg='black', activebackground='yellow')
        self.btnnum3 = tk.Button(self, text='guitar', fg='white', height=3, width=15, bd=20, command=self.song3_start, font=f1,
                                 bg='black', activebackground='yellow')
        # 按鍵排版
        self.btnnum1.grid(row=0, column=0, sticky=tk.NE + tk.SW)
        self.btnnum2.grid(row=0, column=1, sticky=tk.NE + tk.SW)
        self.btnnum3.grid(row=0, column=2, sticky=tk.NE + tk.SW)
        # 鍵盤操作
        self.btnnum1.bind_all('a', self.song1_start)
        self.btnnum2.bind_all('s', self.song2_start)
        self.btnnum3.bind_all('d', self.song3_start)

    def song1_start(self):
        play(song1)


    def song2_start(self):
        play(song2)


    def song3_start(self):
        play(song3)

root = Tk()

# 運作
window = launchpad()
window.master.title('Simple Launchpad')
root.iconbitmap('1.ico')
window.mainloop()
