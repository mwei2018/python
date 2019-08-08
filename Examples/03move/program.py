#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import gflags
import logging
import db_util
from PyQt5 import QtWidgets
from main_window import mywindow  

Flags = gflags.FLAGS
gflags.DEFINE_boolean("debug", True, "whether debug")

def main(argv):
    Flags(argv)
    #配置logging格式
    log_format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt="%a, %d %b %Y %H:%M:%S",
        filename="logger.log",
        filemode="w",
    )

    logging.warning(Flags.debug)
    #实例化db处理类
    client = db_util.MongoDBManager(lazy_connection=True) 

   #启动主窗体
    logging.info('启动主窗体')
    app =QtWidgets.QApplication([])
    application = mywindow(client) 
    application.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main(sys.argv)
