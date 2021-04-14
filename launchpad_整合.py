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
os.chdir('C://Users//chtu//Desktop')


# 設定變數名稱，不同種類的音檔就用from_XXX   XXX=mp3,WAV,ogg......etc


# song_name = 'Lucid_Dreamer.mp3'
class launchpad(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createwidgets()

	# 多線程
	def threaded_run_1(self, event):
		t = Thread(target=self.song1_start)
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

	def threaded_run_2(self, event):
		t = Thread(target=self.song2_start)
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

	def threaded_run_3(self, event):
		t = Thread(target=self.song3_start)
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

	def threaded_run_4(self, event):
		t = Thread(target=self.song4_start)
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
		# 升key
		self.btnnum1_1_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn01.gif')
		self.btnnum1_1 = tk.Button(self, image=self.btnnum1_1_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1)
		self.btnnum2_1_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn11.gif')
		self.btnnum2_1 = tk.Button(self, image=self.btnnum2_1_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2)
		self.btnnum3_1_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn21.gif')
		self.btnnum3_1 = tk.Button(self, image=self.btnnum3_1_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3)
		self.btnnum4_1_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn31.gif')
		self.btnnum4_1 = tk.Button(self, image=self.btnnum4_1_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4)
		# 降key
		self.btnnum1_lowKey_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn02.gif')
		self.btnnum1_lowKey = tk.Button(self, image=self.btnnum1_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1_lowKey)
		self.btnnum2_lowKey_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn12.gif')
		self.btnnum2_lowKey = tk.Button(self, image=self.btnnum2_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2_lowKey)
		self.btnnum3_lowKey_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn22.gif')
		self.btnnum3_lowKey = tk.Button(self, image=self.btnnum3_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3_lowKey)
		self.btnnum4_lowKey_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn32.gif')
		self.btnnum4_lowKey = tk.Button(self, image=self.btnnum4_lowKey_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4_lowKey)
		# 升速
		self.btnnum1_hiSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn03.gif')
		self.btnnum1_hiSpd = tk.Button(self, image=self.btnnum1_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1_hiSpd)
		self.btnnum2_hiSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn13.gif')
		self.btnnum2_hiSpd = tk.Button(self, image=self.btnnum2_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2_hiSpd)
		self.btnnum3_hiSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn23.gif')
		self.btnnum3_hiSpd = tk.Button(self, image=self.btnnum3_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3_hiSpd)
		self.btnnum4_hiSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn33.gif')
		self.btnnum4_hiSpd = tk.Button(self, image=self.btnnum4_hiSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4_hiSpd)
		# 降速
		self.btnnum1_lowSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn04.gif')
		self.btnnum1_lowSpd = tk.Button(self, image=self.btnnum1_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_1_lowSpd)
		self.btnnum2_lowSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn14.gif')
		self.btnnum2_lowSpd = tk.Button(self, image=self.btnnum2_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_2_lowSpd)
		self.btnnum3_lowSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn24.gif')
		self.btnnum3_lowSpd = tk.Button(self, image=self.btnnum3_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_3_lowSpd)
		self.btnnum4_lowSpd_gif = tk.PhotoImage(file='C://Users//chtu//Desktop//btn//btn34.gif')
		self.btnnum4_lowSpd = tk.Button(self, image=self.btnnum4_lowSpd_gif, height=70, width=80, bd=5, bg='black', command=self.threaded_run_4_lowSpd)


		# 按鍵排版
		self.btnnum1.grid(row=0, column=0, sticky=tk.NE + tk.SW)
		self.btnnum2.grid(row=1, column=0, sticky=tk.NE + tk.SW)
		self.btnnum3.grid(row=2, column=0, sticky=tk.NE + tk.SW)
		self.btnnum4.grid(row=3, column=0, sticky=tk.NE + tk.SW)

		self.btnnum1_1.grid(row=0, column=1, sticky=tk.NE + tk.SW)
		self.btnnum2_1.grid(row=1, column=1, sticky=tk.NE + tk.SW)
		self.btnnum3_1.grid(row=2, column=1, sticky=tk.NE + tk.SW)
		self.btnnum4_1.grid(row=3, column=1, sticky=tk.NE + tk.SW)

		self.btnnum1_lowKey.grid(row=0, column=2, sticky=tk.NE + tk.SW)
		self.btnnum2_lowKey.grid(row=1, column=2, sticky=tk.NE + tk.SW)
		self.btnnum3_lowKey.grid(row=2, column=2, sticky=tk.NE + tk.SW)
		self.btnnum4_lowKey.grid(row=3, column=2, sticky=tk.NE + tk.SW)

		self.btnnum1_hiSpd.grid(row=0, column=3, sticky=tk.NE + tk.SW)
		self.btnnum2_hiSpd.grid(row=1, column=3, sticky=tk.NE + tk.SW)
		self.btnnum3_hiSpd.grid(row=2, column=3, sticky=tk.NE + tk.SW)
		self.btnnum4_hiSpd.grid(row=3, column=3, sticky=tk.NE + tk.SW)

		self.btnnum1_lowSpd.grid(row=0, column=4, sticky=tk.NE + tk.SW)
		self.btnnum2_lowSpd.grid(row=1, column=4, sticky=tk.NE + tk.SW)
		self.btnnum3_lowSpd.grid(row=2, column=4, sticky=tk.NE + tk.SW)
		self.btnnum4_lowSpd.grid(row=3, column=4, sticky=tk.NE + tk.SW)

		# 鍵盤操作
		self.btnnum1_1.bind_all('1', self.threaded_run_1)
		self.btnnum2_1.bind_all('q', self.threaded_run_2)
		self.btnnum3_1.bind_all('a', self.threaded_run_3)
		self.btnnum4_1.bind_all('z', self.threaded_run_4)

		self.btnnum1_lowKey.bind_all('2', self.threaded_run_1_lowKey)
		self.btnnum2_lowKey.bind_all('w', self.threaded_run_2_lowKey)
		self.btnnum3_lowKey.bind_all('s', self.threaded_run_3_lowKey)
		self.btnnum4_lowKey.bind_all('x', self.threaded_run_4_lowKey)

		self.btnnum1_lowKey.bind_all('3', self.threaded_run_1_hiSpd)
		self.btnnum2_lowKey.bind_all('e', self.threaded_run_2_hiSpd)
		self.btnnum3_lowKey.bind_all('d', self.threaded_run_3_hiSpd)
		self.btnnum4_lowKey.bind_all('c', self.threaded_run_4_hiSpd)

		self.btnnum1_lowKey.bind_all('4', self.threaded_run_1_lowSpd)
		self.btnnum2_lowKey.bind_all('r', self.threaded_run_2_lowSpd)
		self.btnnum3_lowKey.bind_all('f', self.threaded_run_3_lowSpd)
		self.btnnum4_lowKey.bind_all('v', self.threaded_run_4_lowSpd)

	def choose_song1(self):
		default_dir = r'C://Users//chtu//Desktop'  # 设置默认打开目录
		global song_name1
		song_name1 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))

	def choose_song2(self):
		default_dir = r'C://Users//chtu//Desktop'  # 设置默认打开目录
		global song_name2
		song_name2 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))

	def choose_song3(self):
		default_dir = r'C://Users//chtu//Desktop'  # 设置默认打开目录
		global song_name3
		song_name3 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))

	def choose_song4(self):
		default_dir = r'C://Users//chtu//Desktop'  # 设置默认打开目录
		global song_name4
		song_name4 = fdl.askopenfilename(title=u"選擇文件", initialdir=(os.path.expanduser(default_dir)))

	# 音訊處理功能
	def song1_start(self):
		sampler = Sampler()
		s1 = Sound.from_file(song_name1)
		s1.pitch_shift = 1
		sampler.play(s1)

	def song1_lowKey(self):
		sampler = Sampler()
		s1 = Sound.from_file(song_name1)
		s1.pitch_shift = -1
		sampler.play(s1)

	def song1_hiSpd(self):
		sampler = Sampler()
		s1 = Sound.from_file(song_name1)
		s1.stretch_factor = 2
		sampler.play(s1)

	def song1_lowSpd(self):
		sampler = Sampler()
		s1 = Sound.from_file(song_name1)
		s1.stretch_factor = 0.5
		sampler.play(s1)

	def song2_start(self):
		sampler = Sampler()
		s2 = Sound.from_file(song_name2)
		s2.pitch_shift = 1
		sampler.play(s2)

	def song2_lowKey(self):
		sampler = Sampler()
		s2 = Sound.from_file(song_name2)
		s2.pitch_shift = -1
		sampler.play(s2)

	def song2_hiSpd(self):
		sampler = Sampler()
		s2 = Sound.from_file(song_name2)
		s2.stretch_factor = 2
		sampler.play(s2)

	def song2_lowSpd(self):
		sampler = Sampler()
		s2 = Sound.from_file(song_name2)
		s2.stretch_factor = 0.5
		sampler.play(s2)

	def song3_start(self):
		sampler = Sampler()
		s3 = Sound.from_file(song_name3)
		s3.pitch_shift = 1
		sampler.play(s3)

	def song3_lowKey(self):
		sampler = Sampler()
		s3 = Sound.from_file(song_name3)
		s3.pitch_shift = -1
		sampler.play(s3)

	def song3_hiSpd(self):
		sampler = Sampler()
		s3 = Sound.from_file(song_name3)
		s3.stretch_factor = 2
		sampler.play(s3)

	def song3_lowSpd(self):
		sampler = Sampler()
		s3 = Sound.from_file(song_name3)
		s3.stretch_factor = 0.5
		sampler.play(s3)

	def song4_start(self):
		sampler = Sampler()
		s4 = Sound.from_file(song_name4)
		s4.pitch_shift = 1
		sampler.play(s4)

	def song4_lowKey(self):
		sampler = Sampler()
		s4 = Sound.from_file(song_name4)
		s4.pitch_shift = -1
		sampler.play(s4)

	def song4_hiSpd(self):
		sampler = Sampler()
		s4 = Sound.from_file(song_name4)
		s4.stretch_factor = 2
		sampler.play(s4)

	def song1_lowSpd(self):
		sampler = Sampler()
		s4 = Sound.from_file(song_name4)
		s4.stretch_factor = 0.5
		sampler.play(s4)


root = Tk()

# 運作
window = launchpad()
window.master.title('Simple Launchpad')
root.iconbitmap('C://Users//chtu//Desktop//btn//1.ico')
window.mainloop()