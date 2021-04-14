import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.filedialog as fdl
from aupyom import Sampler, Sound
from ipywidgets import interact, FloatSlider
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

# 看你的音檔位置在哪裡，然後指定位置
os.chdir('/Users/yan/Documents/GitHub/PBC-final-project-launch-pad')


# 設定變數名稱，不同種類的音檔就用from_XXX   XXX=mp3,WAV,ogg......etc


# song_name = 'Lucid_Dreamer.mp3'
class launchpad(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createwidgets()

    # 多線程
    # song1
    def threaded_run_1_origin(self, event):
        t = Thread(target=self.song1_origin)
        t.daemon = True
        t.start()

    def threaded_run_1_hikey(self, event):
        t = Thread(target=self.song1_hikey)
        t.daemon = True
        t.start()

    def threaded_run_1_lowKey(self, event):
        t = Thread(target=self.song1_lowKey)
        t.daemon = True
        t.start()

    def threaded_run_1_hiSpd(self, event):
        t = Thread(target=self.song1_hiSpd)
        t.daemon = True
        t.start()

    def threaded_run_1_lowSpd(self, event):
        t = Thread(target=self.song1_lowSpd)
        t.daemon = True
        t.start()

    # song2
    def threaded_run_2_origin(self, event):
        t = Thread(target=self.song2_origin)
        t.daemon = True
        t.start()

    def threaded_run_2_hikey(self, event):
        t = Thread(target=self.song2_hikey)
        t.daemon = True
        t.start()

    def threaded_run_2_lowKey(self, event):
        t = Thread(target=self.song2_lowKey)
        t.daemon = True
        t.start()

    def threaded_run_2_hiSpd(self, event):
        t = Thread(target=self.song2_hiSpd)
        t.daemon = True
        t.start()

    def threaded_run_2_lowSpd(self, event):
        t = Thread(target=self.song2_lowSpd)
        t.daemon = True
        t.start()

    # song3
    def threaded_run_3_origin(self, event):
        t = Thread(target=self.song3_origin)
        t.daemon = True
        t.start()

    def threaded_run_3_hikey(self, event):
        t = Thread(target=self.song3_hikey)
        t.daemon = True
        t.start()

    def threaded_run_3_lowKey(self, event):
        t = Thread(target=self.song3_lowKey)
        t.daemon = True
        t.start()

    def threaded_run_3_hiSpd(self, event):
        t = Thread(target=self.song3_hiSpd)
        t.daemon = True
        t.start()

    def threaded_run_3_lowSpd(self, event):
        t = Thread(target=self.song3_lowSpd)
        t.daemon = True
        t.start()

    # song4
    def threaded_run_4_origin(self, event):
        t = Thread(target=self.song4_origin)
        t.daemon = True
        t.start()

    def threaded_run_4_hikey(self, event):
        t = Thread(target=self.song4_hikey)
        t.daemon = True
        t.start()

    def threaded_run_4_lowKey(self, event):
        t = Thread(target=self.song4_lowKey)
        t.daemon = True
        t.start()

    def threaded_run_4_hiSpd(self, event):
        t = Thread(target=self.song4_hiSpd)
        t.daemon = True
        t.start()

    def threaded_run_4_lowSpd(self, event):
        t = Thread(target=self.song4_lowSpd)
        t.daemon = True
        t.start()

    # 視窗
    def createwidgets(self):
        # 字型
        f1 = tkFont.Font(size=18, family='Tw Cen MT')

        # 四個輸入歌曲按鍵
        self.btnnum1 = tk.Button(self, text='choose1', fg='white', height=2, width=10, bd=10, command=self.choose_song1, font=f1, bg='black', activebackground='gray')
        self.btnnum2 = tk.Button(self, text='choose2', fg='white', height=2, width=10, bd=10, command=self.choose_song2, font=f1, bg='black', activebackground='gray')
        self.btnnum3 = tk.Button(self, text='choose3', fg='white', height=2, width=10, bd=10, command=self.choose_song3, font=f1, bg='black', activebackground='gray')
        self.btnnum4 = tk.Button(self, text='choose4', fg='white', height=2, width=10, bd=10, command=self.choose_song4, font=f1, bg='black', activebackground='gray')

        # 原音
        self.btnnum1_origin_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn0_1.gif')
        self.btnnum1_origin_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn0_1c.gif')
        self.btnnum1_origin = tk.Button(self, image=self.btnnum1_origin_gif, height=70, width=80, bd=5, bg='black',
                                        command=self.threaded_run_1_origin)
        self.btnnum2_origin_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn1_1.gif')
        self.btnnum2_origin_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn1_1c.gif')
        self.btnnum2_origin = tk.Button(self, image=self.btnnum2_origin_gif, height=70, width=80, bd=5, bg='black',
                                        command=self.threaded_run_2_origin)
        self.btnnum3_origin_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn2_1.gif')
        self.btnnum3_origin_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn2_1c.gif')
        self.btnnum3_origin = tk.Button(self, image=self.btnnum3_origin_gif, height=70, width=80, bd=5, bg='black',
                                        command=self.threaded_run_3_origin)
        self.btnnum4_origin_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn3_1.gif')
        self.btnnum4_origin_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn3_1c.gif')
        self.btnnum4_origin = tk.Button(self, image=self.btnnum4_origin_gif, height=70, width=80, bd=5, bg='black',
                                        command=self.threaded_run_4_origin)
        # 升key
        self.btnnum1_hikey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn01.gif')
        self.btnnum1_hikey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn01c.gif')
        self.btnnum1_hikey = tk.Button(self, image=self.btnnum1_hikey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1_hikey)
        self.btnnum2_hikey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn11.gif')
        self.btnnum2_hikey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn11c.gif')
        self.btnnum2_hikey = tk.Button(self, image=self.btnnum2_hikey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2_hikey)
        self.btnnum3_hikey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn21.gif')
        self.btnnum3_hikey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn21c.gif')
        self.btnnum3_hikey = tk.Button(self, image=self.btnnum3_hikey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3_hikey)
        self.btnnum4_hikey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn31.gif')
        self.btnnum4_hikey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn31c.gif')
        self.btnnum4_hikey = tk.Button(self, image=self.btnnum4_hikey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4_hikey)

        # 降key
        self.btnnum1_lowKey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn02.gif')
        self.btnnum1_lowKey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn02c.gif')
        self.btnnum1_lowKey = tk.Button(self, image=self.btnnum1_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1_lowKey)
        self.btnnum2_lowKey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn12.gif')
        self.btnnum2_lowKey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn12c.gif')
        self.btnnum2_lowKey = tk.Button(self, image=self.btnnum2_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2_lowKey)
        self.btnnum3_lowKey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn22.gif')
        self.btnnum3_lowKey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn22c.gif')
        self.btnnum3_lowKey = tk.Button(self, image=self.btnnum3_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3_lowKey)
        self.btnnum4_lowKey_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn32.gif')
        self.btnnum4_lowKey_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn32c.gif')
        self.btnnum4_lowKey = tk.Button(self, image=self.btnnum4_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4_lowKey)

        # 升速
        self.btnnum1_hiSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn03.gif')
        self.btnnum1_hiSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn03c.gif')
        self.btnnum1_hiSpd = tk.Button(self, image=self.btnnum1_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1_hiSpd)
        self.btnnum2_hiSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn13.gif')
        self.btnnum2_hiSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn13c.gif')
        self.btnnum2_hiSpd = tk.Button(self, image=self.btnnum2_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2_hiSpd)
        self.btnnum3_hiSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn23.gif')
        self.btnnum3_hiSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn23c.gif')
        self.btnnum3_hiSpd = tk.Button(self, image=self.btnnum3_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3_hiSpd)
        self.btnnum4_hiSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn33.gif')
        self.btnnum4_hiSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn33c.gif')
        self.btnnum4_hiSpd = tk.Button(self, image=self.btnnum4_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4_hiSpd)

        # 降速
        self.btnnum1_lowSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn04.gif')
        self.btnnum1_lowSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn04c.gif')
        self.btnnum1_lowSpd = tk.Button(self, image=self.btnnum1_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1_lowSpd)
        self.btnnum2_lowSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn14.gif')
        self.btnnum2_lowSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn14c.gif')
        self.btnnum2_lowSpd = tk.Button(self, image=self.btnnum2_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2_lowSpd)
        self.btnnum3_lowSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn24.gif')
        self.btnnum3_lowSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn24c.gif')
        self.btnnum3_lowSpd = tk.Button(self, image=self.btnnum3_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3_lowSpd)
        self.btnnum4_lowSpd_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn34.gif')
        self.btnnum4_lowSpd_change_gif = tk.PhotoImage(file='/Users/yan/Documents/Downloads/launchpad_icon/btn/btn34c.gif')
        self.btnnum4_lowSpd = tk.Button(self, image=self.btnnum4_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4_lowSpd)




        # 按鍵排版
        self.btnnum1.grid(row=0, column=0, sticky=tk.NE + tk.SW)
        self.btnnum2.grid(row=1, column=0, sticky=tk.NE + tk.SW)
        self.btnnum3.grid(row=2, column=0, sticky=tk.NE + tk.SW)
        self.btnnum4.grid(row=3, column=0, sticky=tk.NE + tk.SW)

        self.btnnum1_origin.grid(row=0, column=1, sticky=tk.NE + tk.SW)
        self.btnnum2_origin.grid(row=1, column=1, sticky=tk.NE + tk.SW)
        self.btnnum3_origin.grid(row=2, column=1, sticky=tk.NE + tk.SW)
        self.btnnum4_origin.grid(row=3, column=1, sticky=tk.NE + tk.SW)

        self.btnnum1_hikey.grid(row=0, column=2, sticky=tk.NE + tk.SW)
        self.btnnum2_hikey.grid(row=1, column=2, sticky=tk.NE + tk.SW)
        self.btnnum3_hikey.grid(row=2, column=2, sticky=tk.NE + tk.SW)
        self.btnnum4_hikey.grid(row=3, column=2, sticky=tk.NE + tk.SW)

        self.btnnum1_lowKey.grid(row=0, column=3, sticky=tk.NE + tk.SW)
        self.btnnum2_lowKey.grid(row=1, column=3, sticky=tk.NE + tk.SW)
        self.btnnum3_lowKey.grid(row=2, column=3, sticky=tk.NE + tk.SW)
        self.btnnum4_lowKey.grid(row=3, column=3, sticky=tk.NE + tk.SW)

        self.btnnum1_hiSpd.grid(row=0, column=4, sticky=tk.NE + tk.SW)
        self.btnnum2_hiSpd.grid(row=1, column=4, sticky=tk.NE + tk.SW)
        self.btnnum3_hiSpd.grid(row=2, column=4, sticky=tk.NE + tk.SW)
        self.btnnum4_hiSpd.grid(row=3, column=4, sticky=tk.NE + tk.SW)

        self.btnnum1_lowSpd.grid(row=0, column=5, sticky=tk.NE + tk.SW)
        self.btnnum2_lowSpd.grid(row=1, column=5, sticky=tk.NE + tk.SW)
        self.btnnum3_lowSpd.grid(row=2, column=5, sticky=tk.NE + tk.SW)
        self.btnnum4_lowSpd.grid(row=3, column=5, sticky=tk.NE + tk.SW)

        # 鍵盤操作
        self.btnnum1_origin.bind_all('1', self.threaded_run_1_origin)
        self.btnnum2_origin.bind_all('q', self.threaded_run_2_origin)
        self.btnnum3_origin.bind_all('a', self.threaded_run_3_origin)
        self.btnnum4_origin.bind_all('z', self.threaded_run_4_origin)

        self.btnnum1_hikey.bind_all('2', self.threaded_run_1_hikey)
        self.btnnum2_hikey.bind_all('w', self.threaded_run_2_hikey)
        self.btnnum3_hikey.bind_all('s', self.threaded_run_3_hikey)
        self.btnnum4_hikey.bind_all('x', self.threaded_run_4_hikey)

        self.btnnum1_lowKey.bind_all('3', self.threaded_run_1_lowKey)
        self.btnnum2_lowKey.bind_all('e', self.threaded_run_2_lowKey)
        self.btnnum3_lowKey.bind_all('d', self.threaded_run_3_lowKey)
        self.btnnum4_lowKey.bind_all('c', self.threaded_run_4_lowKey)

        self.btnnum1_hiSpd.bind_all('4', self.threaded_run_1_hiSpd)
        self.btnnum2_hiSpd.bind_all('r', self.threaded_run_2_hiSpd)
        self.btnnum3_hiSpd.bind_all('f', self.threaded_run_3_hiSpd)
        self.btnnum4_hiSpd.bind_all('v', self.threaded_run_4_hiSpd)

        self.btnnum1_lowSpd.bind_all('5', self.threaded_run_1_lowSpd)
        self.btnnum2_lowSpd.bind_all('t', self.threaded_run_2_lowSpd)
        self.btnnum3_lowSpd.bind_all('g', self.threaded_run_3_lowSpd)
        self.btnnum4_lowSpd.bind_all('b', self.threaded_run_4_lowSpd)

    # 選擇歌曲
    def choose_song1(self):
        default_dir = r'/Users/yan/Documents/GitHub/PBC-final-project-launch-pad'  # 设置默认打开目录
        self.btnnum1.configure(bg="yellow")
        global song_name1
        song_name1 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))


    def choose_song2(self):
        default_dir = r'/Users/yan/Documents/GitHub/PBC-final-project-launch-pad'  # 设置默认打开目录
        self.btnnum2.configure(bg="yellow")
        global song_name2
        song_name2 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))

    def choose_song3(self):
        default_dir = r'/Users/yan/Documents/GitHub/PBC-final-project-launch-pad'  # 设置默认打开目录
        self.btnnum3.configure(bg="yellow")
        global song_name3
        song_name3 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))

    def choose_song4(self):
        default_dir = r'/Users/yan/Documents/GitHub/PBC-final-project-launch-pad'  # 设置默认打开目录
        self.btnnum4.configure(bg="yellow")
        global song_name4
        song_name4 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))

    # 音訊處理功能
    # song1
    def song1_origin(self):
        self.btnnum1_origin.configure(image = self.btnnum1_origin_change_gif)
        sampler = Sampler()
        s1 = Sound.from_file(song_name1)
        sampler.play(s1)
        self.btnnum1_origin.configure(image=self.btnnum1_origin_gif)

    def song1_hikey(self):
        self.btnnum1_hikey.configure(image = self.btnnum1_hikey_change_gif)
        sampler = Sampler()
        s1 = Sound.from_file(song_name1)
        s1.pitch_shift = 1
        sampler.play(s1)
        self.btnnum1_hikey.configure(image=self.btnnum1_hikey_gif)

    def song1_lowKey(self):
        self.btnnum1_lowKey.configure(image = self.btnnum1_lowKey_change_gif)
        sampler = Sampler()
        s1 = Sound.from_file(song_name1)
        s1.pitch_shift = -1
        sampler.play(s1)
        self.btnnum1_lowKey.configure(image=self.btnnum1_lowKey_gif)

    def song1_hiSpd(self):
        self.btnnum1_hiSpd.configure(image = self.btnnum1_hiSpd_change_gif)
        sampler = Sampler()
        s1 = Sound.from_file(song_name1)
        s1.stretch_factor = 2
        sampler.play(s1)
        self.btnnum1_hiSpd.configure(image=self.btnnum1_hiSpd_gif)

    def song1_lowSpd(self):
        self.btnnum1_lowSpd.configure(image = self.btnnum1_lowSpd_change_gif)
        sampler = Sampler()
        s1 = Sound.from_file(song_name1)
        s1.stretch_factor = 0.5
        sampler.play(s1)
        self.btnnum1_lowSpd.configure(image=self.btnnum1_lowSpd_gif)

    # song2
    def song2_origin(self):
        self.btnnum2_origin.configure(image = self.btnnum2_origin_change_gif)
        sampler = Sampler()
        s2 = Sound.from_file(song_name2)
        sampler.play(s2)
        self.btnnum2_origin.configure(image=self.btnnum2_origin_gif)

    def song2_hikey(self):
        self.btnnum2_hikey.configure(image = self.btnnum2_hikey_change_gif)
        sampler = Sampler()
        s2 = Sound.from_file(song_name2)
        s2.pitch_shift = 1
        sampler.play(s2)
        self.btnnum2_hikey.configure(image=self.btnnum2_hikey_gif)

    def song2_lowKey(self):
        self.btnnum2_lowKey.configure(image = self.btnnum2_lowKey_change_gif)
        sampler = Sampler()
        s2 = Sound.from_file(song_name2)
        s2.pitch_shift = -1
        sampler.play(s2)
        self.btnnum2_lowKey.configure(image=self.btnnum2_lowKey_gif)

    def song2_hiSpd(self):
        self.btnnum2_hiSpd.configure(image = self.btnnum2_hiSpd_change_gif)
        sampler = Sampler()
        s2 = Sound.from_file(song_name2)
        s2.stretch_factor = 2
        sampler.play(s2)
        self.btnnum2_hiSpd.configure(image=self.btnnum2_hiSpd_gif)

    def song2_lowSpd(self):
        self.btnnum2_lowSpd.configure(image = self.btnnum2_lowSpd_change_gif)
        sampler = Sampler()
        s2 = Sound.from_file(song_name2)
        s2.stretch_factor = 0.5
        sampler.play(s2)
        self.btnnum2_lowSpd.configure(image=self.btnnum2_lowSpd_gif)

    # song3
    def song3_origin(self):
        self.btnnum3_origin.configure(image = self.btnnum3_origin_change_gif)
        sampler = Sampler()
        s3 = Sound.from_file(song_name3)
        sampler.play(s3)
        self.btnnum3_origin.configure(image=self.btnnum3_origin_gif)

    def song3_hikey(self):
        self.btnnum3_hikey.configure(image = self.btnnum3_hikey_change_gif)
        sampler = Sampler()
        s3 = Sound.from_file(song_name3)
        s3.pitch_shift = 1
        sampler.play(s3)
        self.btnnum3_hikey.configure(image=self.btnnum3_hikey_gif)

    def song3_lowKey(self):
        self.btnnum3_lowKey.configure(image = self.btnnum3_lowKey_change_gif)
        sampler = Sampler()
        s3 = Sound.from_file(song_name3)
        s3.pitch_shift = -1
        sampler.play(s3)
        self.btnnum3_lowKey.configure(image=self.btnnum3_lowKey_gif)

    def song3_hiSpd(self):
        self.btnnum3_hiSpd.configure(image = self.btnnum3_hiSpd_change_gif)
        sampler = Sampler()
        s3 = Sound.from_file(song_name3)
        s3.stretch_factor = 2
        sampler.play(s3)
        self.btnnum3_hiSpd.configure(image=self.btnnum3_hiSpd_gif)

    def song3_lowSpd(self):
        self.btnnum3_lowSpd.configure(image = self.btnnum3_lowSpd_change_gif)
        sampler = Sampler()
        s3 = Sound.from_file(song_name3)
        s3.stretch_factor = 0.5
        sampler.play(s3)
        self.btnnum3_lowSpd.configure(image=self.btnnum3_lowSpd_gif)

    # song 4
    def song4_origin(self):
        self.btnnum4_origin.configure(image = self.btnnum4_origin_change_gif)
        sampler = Sampler()
        s4 = Sound.from_file(song_name4)
        sampler.play(s4)
        self.btnnum4_origin.configure(image=self.btnnum4_origin_gif)

    def song4_hikey(self):
        self.btnnum4_hikey.configure(image = self.btnnum4_hikey_change_gif)
        sampler = Sampler()
        s4 = Sound.from_file(song_name4)
        s4.pitch_shift = 1
        sampler.play(s4)
        self.btnnum4_hikey.configure(image=self.btnnum4_hikey_gif)

    def song4_lowKey(self):
        self.btnnum4_lowKey.configure(image = self.btnnum4_lowKey_change_gif)
        sampler = Sampler()
        s4 = Sound.from_file(song_name4)
        s4.pitch_shift = -1
        sampler.play(s4)
        self.btnnum4_lowKey.configure(image=self.btnnum4_lowKey_gif)

    def song4_hiSpd(self):
        self.btnnum4_hiSpd.configure(image = self.btnnum4_hiSpd_change_gif)
        sampler = Sampler()
        s4 = Sound.from_file(song_name4)
        s4.stretch_factor = 2
        sampler.play(s4)
        self.btnnum4_hiSpd.configure(image=self.btnnum4_hiSpd_gif)

    def song4_lowSpd(self):
        self.btnnum4_lowSpd.configure(image = self.btnnum4_lowSpd_change_gif)
        sampler = Sampler()
        s4 = Sound.from_file(song_name4)
        s4.stretch_factor = 0.5
        sampler.play(s4)
        self.btnnum4_lowSpd.configure(image=self.btnnum4_lowSpd_gif)


root = Tk()

# 運作
window = launchpad()
window.master.title('Simple Launchpad')
root.iconbitmap('/Users/yan/Documents/Downloads/launchpad_icon/btn/1.ico')
window.mainloop()