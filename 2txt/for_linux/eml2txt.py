# -*- coding:utf8 -*-

import email.utils
import sys
import logging

import chardet
import html2text
import re

reload(sys)
sys.setdefaultencoding("utf-8")


def get_charset(message):
    return message.get_content_charset()


def convert_eml_to_txt(msg):
    try:
        logging.debug('Converting email to txt: ' + str(file))
        for par in msg.walk():
            if not par.is_multipart():  # 这里要判断是否是multipart，是的话，里面的数据是无用的
                charset = get_charset(par)
                if charset == None:
                    mailContent = par.get_payload(decode=True)
                else:
                    mailContent = par.get_payload(decode=True).decode(charset, 'replace')
                    return mailContent

    except Exception, e:
        logging.error('Error in file: ' + file + str(e))
        return ""


# 将所有email文档转换为txt格式
def handle_emlfiles(emlfile):
    fp = open(emlfile, "r")
    msg = email.message_from_file(fp)  # 创建消息对象
    emltext = 'content:{}'.format(convert_eml_to_txt(msg))
    # print chardet.detect(emltext)
    if (chardet.detect(emltext)['encoding'] == 'GB2312'):
        str_file = html2text.html2text(emltext.decode("gbk", 'ignore').encode("utf-8", 'ignore'))
    elif ((chardet.detect(emltext)['encoding'] == 'utf-8') or (
                chardet.detect(emltext)['encoding'] == 'UTF-8-SIG')):
        str_file = html2text.html2text(emltext)
        #print str_file
    return str_file
    # for t in str_file:
    #     txt = re.sub(r'[# * | ]?', '', t)  # drop #*
    # return txt
