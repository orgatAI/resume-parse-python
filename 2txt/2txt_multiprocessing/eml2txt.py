# -*- coding:utf8 -*-
# import email
import email.utils
import os
import sys
import logging

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
