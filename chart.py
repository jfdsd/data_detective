# -*- coding: utf-8 -*-
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib                   #导入图表模块
import matplotlib.pyplot as plt     #导入绘图模块


class PlotCanvas(FigureCanvas):

    def __init__(self,parent=None,width=0,height=0,dpi=100):
        #避免中文乱码
        matplotlib.rcParams['font.sans-serif']=['SimHei']
        matplotlib.rcParams['axes.unicode_minus']=False

        fig=plt.figure(figsize=(width,height),dpi=dpi)
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)

    #显示商品分类饼图
    def pie_chart(self,size):
        label_list=['鼠标','键盘','U盘','移动硬盘','其他']
        plt.pie(size,labels=label_list,labeldistance=1.1,autopct="%1.1f%%",shadow=False,startangle=30,pctdistance=0.6)
        plt.axis("equal")