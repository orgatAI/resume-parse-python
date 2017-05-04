# -*- coding: utf-8 -*-

import sys
import os

import doc2txt as d2t
import pdf2txt as p2t
import html2text
import eml2txt as e2t
import email

import re
import chardet

import multiprocessing  # 多进程编程

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


# 将所有word文档转换为txt格式,引用封装的doc2txt模块
def handle_docfiles(files):
    for docfile in files:
        if docfile[-4:] == '.DOC':
            doc_file = docfile[:-4] + '.doc'
        else:
            doc_file = docfile
        d2t.convert_doc_to_txt(doc_file)


# 将所有pdf文档转换为txt格式，引用封装的pdf2txt模块
def handle_pdffiles(files):
    for pdffile in files:
        # print pdffile
        pdf2t = pdffile[:-4]  # 以后缀.pdf切词
        if (not os.path.exists(pdf2t + ".txt")):  # 判断是否存在，如果存在就不处理
            # print os.path.exists(pdf2t + ".txt")
            f = open(pdf2t + '.txt', 'w+')  # 以txt格式保存
            f.write(p2t.convert_pdf_to_txt(pdffile))
            f.close()

            # 将所有html文档转换为txt格式


def handle_htmlfiles(files):
    for htmlfile in files:
        html2t = htmlfile[:-5]
        if (not os.path.exists(html2t + ".txt")):  # 判断是否存在，如果存在就不处理
            # print os.path.exists(html2t + ".txt")
            fout = open(html2t + '.txt', 'w')
            fin = open(htmlfile, 'r')
            strfile = fin.read()
            # print chardet.detect(strfile)
            # 文本格式的编码方式统一为utf-8
            if (chardet.detect(strfile)['encoding'] == 'GB2312'):
                str_file = html2text.html2text(strfile.decode("gbk", 'ignore').encode("utf-8", 'ignore'))
            if ((chardet.detect(strfile)['encoding'] == 'utf-8') or (
                        chardet.detect(strfile)['encoding'] == 'UTF-8-SIG')):
                str_file = html2text.html2text(strfile)
            for t in str_file:
                txt = re.sub(r'[# * | -]?', '', t)  # drop #*
                fout.write(txt)
            fout.close()


# 将所有email文档转换为txt格式
def handle_emlfiles(files):
    for emlfile in files:
        email2t = emlfile[:-4]
        if (not os.path.exists(email2t + ".txt")):  # 判断是否存在，如果存在就不处理
            # print email2t[]
            fp = open(emlfile, "r")
            msg = email.message_from_file(fp)  # 创建消息对象
            emltext = 'content:{}'.format(e2t.convert_eml_to_txt(msg))
            fout = open(email2t+'.txt', 'w')

            # print chardet.detect(emltext)
            if (chardet.detect(emltext)['encoding'] == 'GB2312'):
                str_file = html2text.html2text(emltext.decode("gbk", 'ignore').encode("utf-8", 'ignore'))
            if ((chardet.detect(emltext)['encoding'] == 'utf-8') or (
                        chardet.detect(emltext)['encoding'] == 'UTF-8-SIG')):
                str_file = html2text.html2text(emltext)
            for t in str_file:
                txt = re.sub(r'[# * | ]?', '', t)  # drop #*
                fout.write(txt)
            fout.close()


def main():
    pool_size = 8
    pool = multiprocessing.Pool(processes=pool_size)  # 新建进程池，并设置池大小

    path = r'C:\Users\Coraline\Desktop\test\resume\2txt\2txt_packaged\test'
    docfile_list = getalldocfilename(path)  # 获取文件夹内所有文件的名字和路径
    pdffile_list = getallpdffilename(path)
    htmlfile_list = getallhtmlfilename(path)
    emlfile_list = getallemlfilename(path)
    docfilelist = {}
    pdffilelist = {}
    htmlfilelist = {}
    emlfilelist = {}

    for i in range(pool_size):
        docfilelist[i] = []
        pdffilelist[i] = []
        htmlfilelist[i] = []
        emlfilelist[i] = []

    for i in range(len(docfile_list)):
        docfilelist[i % pool_size].append(docfile_list[i])

    for i in range(len(pdffile_list)):
        pdffilelist[i % pool_size].append(pdffile_list[i])

    for i in range(len(htmlfile_list)):
        htmlfilelist[i % pool_size].append(htmlfile_list[i])

    for i in range(len(emlfile_list)):
        emlfilelist[i % pool_size].append(emlfile_list[i])

    for i in xrange(pool_size):
        pool.apply_async(handle_docfiles, (docfilelist[i],))
        pool.apply_async(handle_pdffiles, (pdffilelist[i],))
        pool.apply_async(handle_htmlfiles, (htmlfilelist[i],))
        pool.apply_async(handle_emlfiles, (emlfilelist[i],))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
