import os
import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog as fdl
from aupyom import Sampler, Sound
from ipywidgets import interact, FloatSlider
from pydub import AudioSegment
from pydub.playback import play

class launchpad(tk.Frame):
	
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createwidgets()
	#視窗
	def createwidgets(self):
		#字型
		f1 = tkFont.Font(size = 20, family = 'Ink Free') 
		#按鍵
		self.btnnum1 = tk.Button(self,text = 'choose_sound',height = 1, width = 20, command = self.choose_song,font = f1)
		#按鍵排版
		self.btnnum1.grid(row = 0, column = 0,sticky = tk.NE + tk.SW)
	def choose_song(self):
		default_dir = r"D://USER//desktop"  # 设置默认打开目录
		song_name = fdl.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
		sampler = Sampler()
		s1 = Sound.from_file(song_name)
		sampler.play(s1)	

#運作			
window = launchpad()
window.master.title('launchpad')
window.mainloop()