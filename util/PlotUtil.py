#coding=utf-8
import matplotlib.pyplot as plt
from matplotlib import animation  # 动图的核心函数
import sys

class Plot(object):
	"""docstring for Plot"""
	def __init__(self, data,xmax,title):
		# 中文显示
		plt.rcParams['font.sans-serif'] = ['SimHei']
		plt.rcParams['axes.unicode_minus'] = False
		fig, ax = plt.subplots(figsize = (12,6))
		self.fig = fig
		self.ax = ax
		self.data = data
		self.title=title
		self.xmax=xmax

	def showGif(self, save_path, writer = 'imagemagick'):
		plt.cla()
		ani = animation.FuncAnimation(fig = self.fig,
								  func = self.update,
								  frames = len(self.data),
								  init_func = self.init,
								  interval = 0.5,
								  blit = False,
								  repeat = False)
		# 不用imagemagick时，可以保存为html
		ani.save(save_path, writer = writer, fps = 3) #

	def init(self):
		bar = self.ax.barh([], [], color = '#6699CC')
		return bar

	def update(self, i):
		self.ax.cla()
		self.ax.set_xlim([0, self.xmax]) # plt.xlim()
		data = self.data[i]
		x = data[1]
		y = data[2]
		year = data[0]

		bars = []
		for k in range(len(x)):
			tmp = y[k]
			if "v2" in sys.version:
				tmp = y[k].encode("utf-8")
			if tmp in ["中国"]:
				bar = self.ax.barh(k, x[k], color = 'r')
			else:
				bar = self.ax.barh(k, x[k], color = '#6699CC')
			bars.append(bar)

		#添加数据标签
		for rect in bars:
			rect = rect[0]
			w = rect.get_width()
			self.ax.text(w, rect.get_y() + rect.get_height() / 2, '%.1f' % float(w), ha = 'left',va = 'center')

		#设置Y轴刻度线标签
		self.ax.set_title(year)
		self.ax.set_yticks(range(len(y)))
		self.ax.set_yticklabels(y)
		if "v2" in sys.version:
			self.ax.set_xlabel(self.title.decode("utf-8"))
		else:
			self.ax.set_xlabel(self.title)
		return bar
		