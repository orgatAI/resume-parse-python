# -*- coding:utf8 -*-
from cStringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import sys
import logging

reload(sys)
sys.setdefaultencoding("utf-8")


def convert_pdf_to_txt(path):
    try:
        logging.debug('Converting pdf to txt: ' + str(path))
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                      check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        # print chardet.detect(text)
        # print text
        return text
    except Exception, e:
        logging.error('Error in file: ' + path + str(e))
        return ""


# 将pdf文档转换为txt格式
def handle_pdffiles(pdffile):
    # print pdffile
    # pdf2t = pdffile[:-4]  # 以后缀.pdf切词
    convert_pdf_to_txt(pdffile)

    # print os.path.exists(pdf2t + ".txt")
    #  f = open(pdf2t + '.txt', 'w+')  # 以txt格式保存
    #  f.write(convert_pdf_to_txt(pdffile))
    #  f.close()
