# -*- coding: utf-8 -*-
"""
Stream Sender
author: Reiner New
email: nbxlhc@hotmail.com.com
"""

import sys
import getopt
import logging.handlers
import os
import platform
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication

import manage
from ui.MainWindow import MainWindow

# from pycrunch_trace.client.api import trace


def log(LOGLEVEL):
    levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
    if not os.path.exists("./logs"):
        os.mkdir("logs")
    LOG_FILE = "logs/ffmpeg.log"
    logger = logging.getLogger("myapp")
    hdlr = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*10240, backupCount=400, encoding='utf-8')     # 按大小进行分割
    # hdlr = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='D', interval=1, backupCount=40)  # 按时间进行分割
    logging.basicConfig(level=levels[LOGLEVEL],
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=LOG_FILE,
                        filemode='a+')
    logger.addHandler(hdlr)
    logger.setLevel(LOGLEVEL)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def create_file(filename):
    """
    创建日志文件夹和日志文件
    :param filename:
    :return:
    """
    path = filename[0:filename.rfind("/")]
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename, mode="w", encoding="utf-8")
        fd.close()

# @trace()
def main(argv=None):
    os_platform = platform.system()
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
            log(manage.LOGLEVEL)
            app = QApplication(sys.argv)
            pic = "pic/logo.jpg"
            existPic = os.path.exists(pic)
            if existPic:
                splash = QSplashScreen(QPixmap(pic))
                splash.show()
            ui = MainWindow()
            ui.show()
            if existPic:
                splash.finish(ui)
            sys.exit(app.exec_())

        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
        return 2



if __name__ == "__main__":
    sys.exit(main())
