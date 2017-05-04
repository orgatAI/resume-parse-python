# -*- coding:utf8 -*-

import sys
import logging

import re
import chardet
import html2text

reload(sys)
sys.setdefaultencoding("utf-8")


# 将word文档转换为txt格式
def handle_htmlfiles(htmlfile):
    fin = open(htmlfile, 'r')
    strfile = fin.read()
    #print chardet.detect(strfile)
    # 文本格式的编码方式统一为utf-8
    if (chardet.detect(strfile)['encoding'] == 'GB2312'):
        str_file = html2text.html2text(strfile.decode("gbk", 'ignore').encode("utf-8", 'ignore'))
    if ((chardet.detect(strfile)['encoding'] == 'utf-8') or (
                chardet.detect(strfile)['encoding'] == 'UTF-8-SIG')):
        str_file = html2text.html2text(strfile)
        #print str_file
    return str_file
