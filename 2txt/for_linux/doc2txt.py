# -*- coding:utf8 -*-

import os
import sys
import logging
import chardet

reload(sys)
sys.setdefaultencoding("utf-8")


# Load MS Word document,change to txt and return the document object  #import catdoc
def convert_doc_to_txt(file):  # takes in a filename and returns a word document object
    try:
        logging.debug('Converting word to txt: ' + str(file))
        # 后缀名doc切词
        if file[-4:] == '.doc' or file[-4:] =='.DOC':
            doc2t = file[:-4]
        elif file[-5:] == '.docx':
            doc2t = file[:-5]

        text_file='%s.txt'%doc2t
        print type(text_file)#unicode

        os.system("catdoc %s > %s"%(file,text_file))

        with open(text_file, 'r') as fin:
            strfile = fin.read()
            print chardet.detect(strfile)
            if (chardet.detect(strfile)['encoding'] == 'GB2312' ):
                str_file =strfile.decode("gbk", 'ignore').encode("utf-8", 'ignore')
            elif ((chardet.detect(strfile)['encoding'] == 'utf-8') or (
                    chardet.detect(strfile)['encoding'] == 'UTF-8-SIG')or (
                    chardet.detect(strfile)['encoding'] == None)):
                str_file = strfile
            else:
                str_file = strfile
            print str_file
            #os.system('rm %s'%text_file)
        return str_file


    except Exception, e:
        logging.error('Error in file: ' + str(e))
        return ""


# 将word文档转换为txt格式
def handle_docfiles(docfile):

    convert_doc_to_txt(docfile)
