# encoding:utf-8
from date_extractor import *
from school_name_extractor import *
from major_extractor import *
from degree_extractor import *

import re

space_pattern = re.compile('\s')


def init_info_dic():
    result = {}
    result['start_date'] = ''
    result['end_date'] = ''
    result['school'] = ''
    result['major'] = ''
    result['degree'] = ''
    return result


# PS: 解析的格式是utf-8
def info_extract(input_str):
    result = []
    if len(input_str.strip()) == 0:
        return result
    #input_str_src = space_pattern.sub('', input_str)
    #info_list = split_source_info(input_str_src)
    info_list = split_source_info(input_str)

    for input_str in info_list:
        date_list = date_extract(input_str)
        # for d in date_list:
        # print d
        school_list = school_name_extract(input_str.decode('utf-8'))
        # for d in school_list:
        # print d
        major_list = major_extract(input_str)
        # for d in major_list:
        # print d
        degree_list = degree_extract(input_str.decode('utf-8'))
        # for d in degree_list:
        # print d

        for i in range(0, len(degree_list)):
            tmp = init_info_dic()
            j = i * 2
            if j < len(date_list):
                tmp['start_date'] = date_list[j]
            j += 1
            if j < len(date_list):
                tmp['end_date'] = date_list[j]

            if i < len(school_list):
                tmp['school'] = school_list[i]

            if i < len(major_list):
                tmp['major'] = major_list[i]

            if i < len(degree_list):
                tmp['degree'] = degree_list[i]

            if tmp['end_date'] == '' and (input_str.__contains__("至今") or input_str.__contains__("致今")):
                tmp['end_date'] = '1970/01/01'

            result.append(tmp)
    return result


def split_source_info(input_str):
    info_list = []
    degree_list = degree_extract(input_str.decode('utf-8'))
    if len(degree_list) == 1:
        info_list.append(input_str)
        return info_list
    else:
        # 以日期开头进行切分，假如不是以日期切分，则直接扔出给后台处理。（能正确切分的话，正确率会非常高）
        date_list = date_extract(input_str)
        index = input_str.find(date_list[0])
        tmp_pos = []
        if index != -1 and index < 2:
            pos = 0
            for i in range(1, len(date_list)):
                index = input_str.find(date_list[i])
                if index - pos > 20:
                    pos = index
                    tmp_pos.append(index)
        k = 0
        for i in tmp_pos:
            info_list.append(input_str[k:i])
            k = i
        if k < len(input_str):
            info_list.append(input_str[k:len(input_str)])

    return info_list


def process(input_file_path):
    items = []
    items.__sizeof__()
    for line in open(input_file_path, 'r'):
        line = line.strip()
        print line
        info_list = info_extract(line)
        for info in info_list:
            print info['start_date']
            print info['end_date']
            print info['school']
            print info['major']
            print info['degree']
        print '-------'


def main():
    print 'this is main'
    input_file_path = 'data/2.txt'
    result_dic = process(input_file_path)


if __name__ == '__main__':
    main()
