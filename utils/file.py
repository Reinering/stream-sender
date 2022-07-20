# -*- coding: utf-8 -*-

"""
Module implementing.
author: Reiner New
email: nbxlhc@hotmail.com
"""

import chardet
import os


def modifyFileCode(oldfile, newfile, code):
    result = None
    try:
        with open(oldfile, 'r') as f:
            result = f.read()
    except UnicodeDecodeError as e:
        print(e)
        with open(oldfile, 'rb') as f:
            content = f.read()
            result = strJudgeCode(content)
            result = content.decode(encoding=result["encoding"])


    with open(newfile, 'w', encoding=code) as f1:
        f1.write(result)
        f1.flush()

def strJudgeCode(str):
    return chardet.detect(str)

def readFile(path):

    with open(path, 'r') as f:
        f = open(path, 'r')
        filecontent = f.read()

    return filecontent

def WriteFile(str, path):

    with open(path, 'w') as f:
        f.write(str)

def converCode(path):
    file_con = readFile(path)
    result = strJudgeCode(file_con)
    #print(file_con)
    if result['encoding'] == 'utf-8':
        #os.remove(path)
        a_unicode = file_con.decode('utf-8')
        gb2312 = a_unicode.encode('gbk')
        WriteFile(gb2312, path)

def listDirFile(dir):
    list = os.listdir(dir)
    for line in list:
        filepath = os.path.join(dir, line)
        if os.path.isdir(filepath):
            listDirFile(filepath)
        else:
            # print(line)
            converCode(filepath)





if __name__ == '__main__':
    # listDirFile(u'.\TRMD')

    modifyFileCode("../subs/NowOur-stafd.srt", "../subs/1_1", "utf-8")
    modifyFileCode("../subs/The.Suicide.Squad.2021.1080p.HMAX.WEB-DL.DDP5.1.Atmos.H.264-FLUX.srt", "../subs/1_2", "utf-8")