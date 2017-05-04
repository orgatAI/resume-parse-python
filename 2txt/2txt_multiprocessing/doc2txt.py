# -*- coding:utf8 -*-

import win32com.client as win32
import sys
import os
import logging

reload(sys)
sys.setdefaultencoding("utf-8")


# Load MS Word document,change to txt and return the document object  #import win32com
def convert_doc_to_txt(file):  # takes in a filename and returns a word document object
    try:
        logging.debug('Converting word to txt: ' + str(file))
        doc2t=""
        # 后缀名doc切词
        if file[-4:] == '.doc':
            doc2t = file[:-4]
        elif file[-5:] == '.docx':
            doc2t = file[:-5]
        if (not os.path.exists(doc2t + ".txt")):  # 判断是否存在，如果存在就不处理
            wordapp = win32.Dispatch('Word.Application')
            wordapp.Visible = False
            wordapp.Documents.Open(file, False, False)
            wordapp.ActiveDocument.SaveAs(doc2t, FileFormat=win32.constants.wdFormatText)
            wordapp.ActiveDocument.Close()
        return wordapp
    except Exception, e:
        logging.error('Error in file: ' + file + str(e))
        return ""
