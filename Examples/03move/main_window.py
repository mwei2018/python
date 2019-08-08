#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QTableWidgetItem
from form.mainform import Ui_MainWindow 
import pandas as pd 
import sys
import logging


class mywindow(QtWidgets.QMainWindow):
    def __init__(self,client):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.client = client
        self.ui.setupUi(self)   
    
        # 绑定点击事件
        self.ui.action_host.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_new.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_star.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_china.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_us.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_act.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_happy.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_sc.triggered.connect(self.onMyToolBarButtonClick)
        self.ui.action_love.triggered.connect(self.onMyToolBarButtonClick)

        self.ui.pushButton.clicked.connect(self.onQueryButtonClick)
        # 初始化加载全部数据
        query = {}
        self.query_db_to_bind_grid(query)
        

    def onMyToolBarButtonClick(self, s):
        """
        工具栏按钮事件
        """
        # 得到触发的button
        sending_button = self.sender()
        print('%s Clicked!' % str(sending_button.objectName()))
        category_key = sending_button.text()
        self.ui.statusbar.showMessage("查询类型为: {0}".format(str(category_key)))
        logging.info("查询类型为: %s", category_key)       
        query = {"category": {"$regex": category_key, "$options": "i"}}        
        self.query_db_to_bind_grid(query)
    
    def onQueryButtonClick(self):
        #获取text文本框里面内容
        keyword = self.ui.textEdit.toPlainText()    
        self.ui.statusbar.showMessage("查询条件为: {0}".format(str(keyword)))   
        query={'$or': [{"name": {"$regex": keyword, "$options": "i"}},{"ename": {"$regex": keyword, "$options": "i"}} ] }
        self.query_db_to_bind_grid(query)
      
        
       
    def query_db_to_bind_grid(self,query):
        """查询数据库并绑定到grid上"""
        movies = self.client.find_match("SyncmovieItem", query)
        df = pd.DataFrame(list(movies)) 
        print(df)      
        self.grid_databind_df(df)


    def grid_databind_df(self,df):
        """  fill table """ 
               
        if df.empty:           
            self.ui.tableWidget.setColumnCount(1)
            self.ui.tableWidget.setRowCount(1)            
            cellinfo=QTableWidgetItem("NoData") 
            self.ui.tableWidget.setItem(0, 0, cellinfo)
            self.ui.statusbar.showMessage("数据共:0条")              
                 
        else:
            part_df=df[['name','ename','area','category','cover']]
            self.ui.tableWidget.setColumnCount(len(part_df.columns))
            self.ui.tableWidget.setRowCount(len(part_df.index))    
            self.ui.statusbar.showMessage("数据共: {0}".format(str(len(part_df.index))))
       
            for i in range(len(part_df.index)):
                for j in range(len(part_df.columns)):
                    self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(part_df.iat[i, j])))

            self.ui.tableWidget.setHorizontalHeaderLabels(part_df.columns)
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.resizeRowsToContents()
            self.ui.tableWidget.doubleClicked.connect(self.on_click_table)
       

    def on_click_table(self, mi):
        rowindex = mi.row()
        columnindex = mi.column()  
        if self.ui.tableWidget.selectionModel().hasSelection():            
            row = self.ui.tableWidget.currentRow()
            name = (self.ui.tableWidget.item(row, 0).text()) 
            url = (self.ui.tableWidget.item(row, 4).text()) 
            print(rowindex) 
        print(rowindex)         



