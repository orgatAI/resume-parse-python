# encoding:utf-8
from major_extractor import *

import re

input_encode = 'utf-8'

#|[\u4e00-\u9fa5]中专+|[\u4e00-\u9fa5]+大专
school_str1 = u"([\u4e00-\u9fa5]+大学|[\u4e00-\u9fa5]+学院|[\u4e00-\u9fa5]+分校|[\u4e00-\u9fa5]+学校|[\u4e00-\u9fa5]+电大)"
#school_str1 = u"[\u4e00-\u9fa5]+(大学|学院|分校|学校|电大)"
school_pattern1 = re.compile(school_str1)

stop_words = {}

#stop_words[u"至今"] = 0

#stop_words = {u"至今": "", u"月": "", u"本科": "", u"研究生": "", u"硕士": "", u"硕士研究生": ""}
stop_words[u"至今"] = 0
stop_words[u"月"] = 0
stop_words[u'年'] = 0
stop_words[u'日'] = 0

#消除学校前面的专业
# # 构建专业知识库
# major_set = set([v.strip() for v in open('major_dic', 'r')])


# 将items（list）所有空元素，过滤掉
def drop_null(items):
    result = []
    for item in items:
        if len(item.strip()) == 0:
            continue
        result.append(item.strip())
    return result

# items 是学校,当学校名字中含有以stop_words开头时,将stop_wrods替换成空.
def drop_stop_words(items):
    result = []
    for item in items:
        if len(item.strip()) == 0:
            continue
        for sw in stop_words:
            if item.startswith(sw):
                item = item.replace(sw, "")
        result.append(item.strip())
    return result

# 抽取日期信息,并将日期按照顺序排列存入list
def school_name_extract(str):
    result_list = []
    school_list = school_pattern1.findall(str)
    for d in school_list:
        # print d
        result_list.append(d)
    result_list = drop_null(result_list)
    result_list = drop_stop_words(result_list)
    return result_list

def get_education_number_from_school_name(input_str):
    date_size = 0
    size = len(school_name_extract(input_str))
    return size

def process(input_file_path):
    for line in open(input_file_path, 'r'):
        line = line.strip().decode(input_encode)
        print line
        school_list = school_name_extract(line)

        for d in school_list:
            print d

        print 'education number: '
        print get_education_number_from_school_name(line)
        print '-------'

def main():
    print 'this is main'
    input_file_path = 'data/samples'
    result_dic = process(input_file_path)

if __name__ == '__main__':
    main()
