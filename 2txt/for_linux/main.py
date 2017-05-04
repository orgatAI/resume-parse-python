# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import os
import chardet

import doc2txt as d2t
import pdf2txt as p2t
import html2txt as h2t
import eml2txt as e2t

reload(sys)
sys.setdefaultencoding("utf-8")


# 获取一个文件夹内包括子文件夹所有doc文件的名字和路径
def getalldocfilename(path):
    docfilenames = []
    for dirpath, dirnames, filenames in os.walk(path):
        filenames = filter(
            lambda filename: (filename[-4:] == '.doc' or filename[-5:] == '.docx' or filename[-4:] == '.DOC'),
            filenames)
        filenames = map(lambda filename: os.path.join(dirpath, filename), filenames)
        docfilenames.extend(filenames)
        print docfilenames
        return docfilenames


# 获取一个文件夹内包括子文件夹所有pdf文件的名字和路径
def getallpdffilename(path):
    pdffilenames = list()
    for dirpath, dirnames, filenames in os.walk(path):
        filenames = filter(lambda filename: filename[-4:] == '.pdf', filenames)
        filenames = map(lambda filename: os.path.join(dirpath, filename), filenames)
        pdffilenames.extend(filenames)
        return pdffilenames


# 获取一个文件夹内包括子文件夹所有html文件的名字和路径
def getallhtmlfilename(path):
    htmlfilenames = []
    for dirpath, dirnames, filenames in os.walk(path):
        filenames = filter(
            lambda filename: (filename[-5:] == '.html' or filename[-4:] == '.htm'),
            filenames)
        filenames = map(lambda filename: os.path.join(dirpath, filename), filenames)
        htmlfilenames.extend(filenames)
        return htmlfilenames


# 获取一个文件夹内包括子文件夹所有pdf文件的名字和路径
def getallemlfilename(path):
    emlfilenames = list()
    for dirpath, dirnames, filenames in os.walk(path):
        filenames = filter(lambda filename: (filename[-4:] == '.eml' or filename[-4:] == '.mht'), filenames)
        filenames = map(lambda filename: os.path.join(dirpath, filename), filenames)
        emlfilenames.extend(filenames)
        return emlfilenames


def handle_document(filename):
    if (filename[-4:] == '.doc' or filename[-5:] == '.docx' or filename[-4:] == '.DOC'):
        content = d2t.handle_docfiles(filename)
    elif (filename[-4:] == '.pdf'):
        content = p2t.handle_pdffiles(filename)
    elif (filename[-5:] == '.html' or filename[-4:] == '.htm'):
        content = h2t.handle_htmlfiles(filename)
    elif (filename[-4:] == '.eml' or filename[-4:] == '.mht'):
        content = e2t.handle_emlfiles(filename)
    return content


if __name__ == '__main__':
    filename = "/home/coraline/桌面/SharedWithWU/2txt_for_integration/files/王培楠1120.doc"
    print chardet.detect(filename)
    handle_document(filename.decode('utf-8','ignore'))
