# -*- coding: utf-8 -*-
from window import Ui_MainWindow        #导入主窗体类
from attention_window import Attention_MainWindow
from heat_window import Heat_MainWindow
from evaluate_warning_window import Evaluate_Warning_MainWindow
from price_warning_window import Price_Warning_MainWindow
from about_window import About_MainWindow

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication
from mysql import MySQL
from crawl import Crawl
from chart import PlotCanvas        #导入自定义饼图类

import sys
import requests

attention_info=''

def messageDialog(title,message):
    msg_box=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,title,message)
    msg_box.exec()

mycrawl=Crawl()
mysql=MySQL()
sql=mysql.connection_sql()
cur=sql.cursor()

class Main(QMainWindow,Ui_MainWindow):

    #窗体初始化
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)  #初始化窗口

        id_str=mycrawl.get_rankings_json('https://ch.jd.com/hotsale2?cateid=686')
        rankings_list=mycrawl.get_price(id_str)
        #print(rankings_list)
        mysql.insert_ranking(cur,rankings_list,'jd_ranking')

    def close_main(self):
        mysql.close_sql()
        self.close()

    def up(self):
        warningDialog=QtWidgets.QMessageBox.warning(self,'警告','关注商品的预警信息更新后，将以新的信息进行对比并预警！',QtWidgets.QMessageBox.Yes |
                                                    QtWidgets.QMessageBox.No)
        if warningDialog==QtWidgets.QMessageBox.Yes:
            row,column,results=mysql.query_evaluate_info(cur,'attention')
            if row!=0:
                jd_id_str=''
                for i in range(len(results)):
                    jd_id='J_'+results[i][3]+','
                    jd_id_str=jd_id_str+jd_id
                price_url='http://p.3.cn/prices/mgets?type=1&skuIds={id_str}'
                response=requests.get(price_url.format(id_str=jd_id_str))
                price_json=response.json()
                for index,item in enumerate(results):
                    middle_time=mycrawl.get_evaluation(2,item[3])
                    poor_time=mycrawl.get_evaluation(1,item[3])
                    price=price_json[index]['p']
                    up="middle_time='{mi_time}',poor_time='{p_time}',jd_price='{price}'".format(
                        mi_time=middle_time,
                        p_time=poor_time,price=price
                    )
                    mysql.update_attention(cur,'attention',up,results[index][0])
                messageDialog('提示','已更新预警信息！')
            else:
                messageDialog('警告','您并没有关注某件商品！')
    def attention_btn(self):
        sender=self.gridLayout.sender()
        global attention_info

        attention_info=mysql.query_id_info(cur,int(sender.objectName())+1)
        attention.lineEdit.setText(attention_info[0])
        attention.open()

    def show_attention_name(self):
        self.name_list=[]
        row,column,results=mysql.query_evaluate_info(cur,'attention')
        if row!=0:
            for index,i in enumerate(results):
                self.name_list.append('关注商品'+str(index+1)+':\n'+i[1])
            font=QtGui.QFont()
            font.setPointSize(12)
            self.listView.setFont(font)

            self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.listView.setWordWrap(True)
            model=QtCore.QStringListModel()
            model.setStringList(self.name_list)
            self.listView.setModel(model)
        else:
            model=QtCore.QStringListModel()
            model.setStringList(self.name_list)
            self.listView.setModel(model)

    #显示商品分类比例饼图
    def show_classification(self):
        name_all=mysql.query_rankings_name(cur,'jd_ranking')
        name_number=len(name_all)
        number=0
        remove_list=[]
        class_list=[]

        #因为鼠标垫与鼠标名字接近，先移除鼠标垫
        for name in name_all:
            if '鼠标垫' in name:
                remove_list.append(name)
        for r_name in remove_list:
            name_all.remove(r_name)

        for name in name_all:
            if '鼠标' in name:
                number+=1
        mouse_ratio=float('%.1f'%((number/name_number)*100))
        class_list.append(mouse_ratio)

        number=0
        for name in name_all:
            if '键鼠' in name:
                number+=1
        keyboard_ratio=float('%.1f'%((number/name_number)*100))
        class_list.append(keyboard_ratio)

        number=0
        for name in name_all:
            if 'U盘' in name or 'u盘' in name:
                number+=1
        u_ratio=float('%.1f'%((number/name_number)*100))
        class_list.append(u_ratio)

        number=0
        for name in name_all:
            if '硬盘' in name:
                number+=1
        #计算鼠标百分比
        move_ratio=float('%.1f'%((number/name_number)*100))
        class_list.append(move_ratio)

        other_ratio=float('%.1f'%(100-(mouse_ratio+keyboard_ratio+u_ratio+move_ratio)))
        class_list.append(other_ratio)

        pie=PlotCanvas()
        pie.pie_chart(class_list)
        self.horizontalLayout.addWidget(pie)

    def show_top10(self):
        top_10_info=mysql.query_top10_info(cur)
        i=-1
        for n in range(10):
            x=n%2
            if x==0:
                i+=1
            self.widget=QtWidgets.QWidget()
            self.widget.setObjectName("widget"+str(n))
            self.widget.setStyleSheet('QWidget#'+"widget"+str(n)+"{border:2px solid rgb(175,175,175);background-color:rgb(255,255,255);}")

            self.label=QtWidgets.QLabel(self.widget)

            #图片大小设置
            self.label.setGeometry(QtCore.QRect(15, 15, 80, 80))
            self.label.setPixmap(QtGui.QPixmap('img_download/'+str(n)+'.jpg'))

            self.label.setScaledContents(True)
            self.label.setObjectName("img_download"+str(n))
            self.label.setStyleSheet('border:2px solid rgb(175,175,175);')

            self.label_good=QtWidgets.QLabel(self.widget)
            self.label_good.setObjectName("good"+str(n))

            self.label_good.setGeometry(QtCore.QRect(15, 110, 80, 30))
            self.label_good.setStyleSheet("border:2px solid rgb(255,148,61);color:rgb(255,148,61);")
            self.label_good.setAlignment(QtCore.Qt.AlignCenter)
            self.label_good.setText('好评率'+top_10_info[n][2])
            font=QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label_good.setFont(font)

            # 商品名
            self.label_name=QtWidgets.QLabel(self.widget)
            self.label_name.setObjectName("good"+str(n))
            self.label_name.setGeometry(QtCore.QRect(95,30,228,80))
            self.label_name.setText(top_10_info[n][0])
            self.label_name.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.label_name.setWordWrap(True)
            font=QtGui.QFont()
            font.setPointSize(6)
            font.setBold(True)
            font.setWeight(75)
            self.label_name.setFont(font)

            #价格
            self.label_price=QtWidgets.QLabel(self.widget)
            self.label_price.setObjectName("price"+str(n))
            self.label_price.setGeometry(QtCore.QRect(100,40,128,80))
            self.label_price.setStyleSheet("color:rgb(255,0,0);")
            self.label_price.setText('￥'+top_10_info[n][1])
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.label_price.setFont(font)

            self.pushButton=QtWidgets.QPushButton(self.widget)
            self.pushButton.setObjectName(str(n))
            self.pushButton.setGeometry(QtCore.QRect(115, 110, 50, 30))

            font=QtGui.QFont()
            font.setFamily("楷体")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(55)
            self.pushButton.setFont(font)
            self.pushButton.setStyleSheet("background-color:rgb(223,48,51);color:rgb(255,255,255);")
            self.pushButton.setText('关注')

            self.pushButton.clicked.connect(self.attention_btn)

            self.gridLayout.addWidget(self.widget,i,x)

        # 每个商品框体设置
        self.scrollAreaWidgetContents.setMinimumHeight(i*200)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 360, (i * 200)))


class Attention(QMainWindow,Attention_MainWindow):
    def __init__(self):
        super(Attention,self).__init__()
        self.setupUi(self)
        #开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        palette=QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(
            QtGui.QPixmap('img_resources/attention_bg.png')))
        self.centralwidget.setPalette(palette)
        #设置背景色透明，设置按钮背景图及背景图大小
        self.pushButton_yes.setStyleSheet("background-color:rgba(0,0,0,0")
        self.pushButton_yes.setIcon(QtGui.QIcon('img_resources/yes_btn.png'))
        self.pushButton_yes.setIconSize(QtCore.QSize(100,50))

        self.pushButton_no.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.pushButton_no.setIcon(QtGui.QIcon('img_resources/no_btn.png'))
        self.pushButton_no.setIconSize(QtCore.QSize(100,50))

    #显示关注窗体
    def open(self):
        self.show()

    #保存关注商品信息
    def insert_attention_message(self,attention_info):
        #判断数据库是否已经关注该商品
        is_identical=mysql.query_is_name(cur,attention_info[0])
        if is_identical==0:
            middle_time=mycrawl.get_evaluation(2,attention_info[2])
            poor_time=mycrawl.get_evaluation(1,attention_info[2])
            if middle_time !=None and poor_time !=None:
                attention_info=attention_info+(middle_time,poor_time)
                mysql.insert_attention(cur,[attention_info],'attention')
                messageDialog('提示！','已关注'+attention_info[0])
                attention.close()
                main.show_attention_name()
            else:
                print('无法获取评价时间！')
        else:
            messageDialog('警告！','不可以关注相同的商品!')
            attention.close()

#取消关注窗体初始化类
class Cancel_Attention(QMainWindow,Attention_MainWindow):
    def __init__(self):
        super(Cancel_Attention,self).__init__()
        self.setupUi(self)

        self.centralwidget.setAutoFillBackground(True)
        palette=QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(
            QtGui.QPixmap('img_resources/cancel_attention_bg.png')))
        self.centralwidget.setPalette(palette)

        self.pushButton_yes.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.pushButton_yes.setIcon(QtGui.QIcon('img_resources/yes_btn.png'))
        self.pushButton_yes.setIconSize(QtCore.QSize(100,50))

        self.pushButton_no.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.pushButton_no.setIcon(QtGui.QIcon('img_resources/no_btn.png'))
        self.pushButton_no.setIconSize(QtCore.QSize(100,50))

    #显示取消关注的窗体
    def open(self,qModeIndex):
        #在关注商品名称列表中获取单击了哪一个商品的名称
        name=main.name_list[qModeIndex.row()].lstrip('关注商品'+str(qModeIndex.row()+1)+':\n')
        #将商品名称显示在关注窗体的编辑框中
        cancel_attention.lineEdit.setText(name)
        cancel_attention.show()

    #取消关注方法
    def unfollow(self):
        #获取编辑框商品名称
        name=cancel_attention.lineEdit.text()
        mysql.delete_attention(cur,name)
        main.show_attention_name()
        cancel_attention.close()

#热卖榜窗口初始化类
class Heat(QMainWindow,Heat_MainWindow):
    def __init__(self):
        super(Heat,self).__init__()
        self.setupUi(self)

        self.centralwidget.setAutoFillBackground(True)
        palette=QtGui.QPalette()

        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap('img_resources/rankings_bg.png')))
        self.centralwidget.setPalette(palette)
        row,column,results=mysql.query_rankings(cur,'jd_ranking')
        #设置表格内容不可编辑
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setHidden(True)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(column)
        #设置表格头部
        self.tableWidget.setHorizontalHeaderLabels(['排名','商家名称','京东价','京东id','好评率'])
        self.tableWidget.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        for i in range(row):
            for j in range(column):
                temp_data=results[i][j]
                data=QtWidgets.QTableWidgetItem(str(temp_data))
                self.tableWidget.setItem(i,j,data)

    #打开热卖榜窗体
    def open(self):
        self.show()

    #热卖榜窗体双击事件处理方法
    def heat_itemDoubleClicked(self):
        item=self.tableWidget.currentItem()
        if item.column()==1:
            attention.lineEdit.setText(item.text())
            global attention_info
            attention_info=mysql.query_id_info(cur,item.row()+1)
            attention.open()

#评价预警窗体初始化类
class Evaluate_Warning(QMainWindow,Evaluate_Warning_MainWindow):
    def __init__(self):
        super(Evaluate_Warning,self).__init__()
        self.setupUi(self)

    def open_warning(self):
        self.centralwidget.setAutoFillBackground(True)
        palette=QtGui.QPalette()

        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap('img_resources/evaluate_warning_bg.png')))
        self.centralwidget.setPalette(palette)
        warning_list=[]
        row,column,results=mysql.query_evaluate_info(cur,'attention')
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setHidden(True)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(column-4)
        self.tableWidget.setColumnWidth(0,600)
        self.tableWidget.setColumnWidth(1,400)
        self.tableWidget.setColumnWidth(2,140)
        self.tableWidget.setStyleSheet("background-color:rgba(0,0,0,0)")

        if row!=0:
            middle_time=''
            poor_time=''
            for i in range(len(results)):
                new_middle_time=mycrawl.get_evaluation(2,results[i][3])
                new_poor_time=mycrawl.get_evaluation(1,results[i][3])
                if results[i][5]==new_middle_time:
                    middle_time='无'
                else:
                    middle_time='有'
                if results[i][6]==new_poor_time:
                    poor_time='无'
                else:
                    poor_time='有'
                warning_list.append((results[i][1],middle_time,poor_time))
            for i in range(len(results)):
                for j in range(3):
                    temp_data=warning_list[i][j]
                    data=QtWidgets.QTableWidgetItem(str(temp_data))
                    data.setTextAlignment(QtCore.Qt.AlignCenter)
                    evaluate.tableWidget.setItem(i,j,data)
            self.show()
        else:
            messageDialog('警告!','您并没有关注某件商品！')

#价格预警窗体初始化类
class Price_Warning(QMainWindow,Price_Warning_MainWindow):
    def __init__(self):
        super(Price_Warning,self).__init__()
        self.setupUi(self)

    def open_price(self):
        self.centralwidget.setAutoFillBackground(True)
        palette=QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap('img_resources/price_warning_bg.png')))
        self.centralwidget.setPalette(palette)
        price_list=[]
        #查询关注商品信息
        row,column,results=mysql.query_evaluate_info(cur,'attention')

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setHidden(True)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(column-5)
        self.tableWidget.setColumnWidth(0,600)
        self.tableWidget.setColumnWidth(1,140)
        self.tableWidget.setStyleSheet("background-color:rgba(0,0,0,0)")

        #判断是否有关注的商品信息
        if row!=0:
            jd_id_str=''
            for i in range(len(results)):
                jd_id='J_'+results[i][3]+','
                jd_id_str=jd_id_str+jd_id
            price_url='http://p.3.cn/prices/mgets?type=1&skuIds={id_str}'
            response=requests.get(price_url.format(id_str=jd_id_str))
            price_json=response.json()

            change=''
            for index,item in enumerate(price_json):
                new_jd_price=item['p']
                if float(results[index][2])<float(new_jd_price):
                    change='上涨'
                if float(results[index][2])==float(new_jd_price):
                    change='无'
                if float(results[index][2])>float(new_jd_price):
                    change='下浮'
                price_list.append((results[index][1],change))
            for i in range(len(results)):
                for j in range(2):
                    temp_data=price_list[i][j]
                    data=QtWidgets.QTableWidgetItem(str(temp_data))
                    data.setTextAlignment(QtCore.Qt.AlignCenter)
                    price.tableWidget.setItem(i,j,data)
            self.show()
        else:
            messageDialog('警告！','您并没有关注某件商品')

#关于窗体初始化类
class About_Window(QMainWindow,About_MainWindow):
    def __init__(self):
        super(About_Window,self).__init__()
        self.setupUi(self)
        img=QtGui.QPixmap('img_resources/about_bg.png')
        self.label.setPixmap(img)

if __name__ == '__main__':
    # 解决了Qtdesigner设计的界面与实际运行界面不一致的问题
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app=QApplication(sys.argv)      #创建QApplication对象，作为GUI主程序入口
    main=Main()
    main.show()
    main.show_top10()

    #关注窗体对象
    attention=Attention()
    attention.pushButton_yes.clicked.connect(
        lambda :attention.insert_attention_message(attention_info))
    attention.pushButton_no.clicked.connect(attention.close)
    main.show_attention_name()      #显示关注商品名称

    main.show_classification()      #显示商品分类比例饼图

    cancel_attention=Cancel_Attention()
    main.listView.clicked.connect(cancel_attention.open)
    cancel_attention.pushButton_yes.clicked.connect(cancel_attention.unfollow)
    cancel_attention.pushButton_no.clicked.connect(cancel_attention.close)

    #热卖排行榜窗体对象
    heat=Heat()
    #指定热卖榜表格的双击事件处理方法
    heat.tableWidget.itemDoubleClicked.connect(heat.heat_itemDoubleClicked)
    #指定主窗体菜单打开热卖排行榜窗体事件处理方法
    main.action_heat_2.triggered.connect(heat.open)

    evaluate=Evaluate_Warning()
    main.action_evaluate.triggered.connect(evaluate.open_warning)

    price=Price_Warning()
    main.action_price.triggered.connect(price.open_price)

    main.action_up.triggered.connect(main.up)

    about=About_Window()
    main.action_about.triggered.connect(about.show)

    main.action_out_2.triggered.connect(main.close_main)

    sys.exit(app.exec_())       #执行窗体退出


