# encoding:utf-8
import re

# date_str1 2010.09
#date_str1 = u"[0-9 年/.]+"
date_str1 = u"[0-9]{4} *[年/.-]+[0-9]{1,2}[月]*"
date_pattern1 = re.compile(date_str1)

# 解决9/1990和09/1992这些case
date_str2 = u"[0-9]{1,2}[月/.-]+19{1}[0-9]{2}[年]*|[0-9]{1,2}[月/.-]+20{1}[0-9]{2}[年]*"
date_pattern2 = re.compile(date_str2)

# 将items（list）所有空元素，过滤掉
def drop_null(items):
    result = []
    for item in items:
        if len(item.strip()) == 0:
            continue
        result.append(item.strip())
    return result

# 抽取日期信息,并将日期按照顺序排列存入list
# str必须保证unicode编码
def date_extract(str):
    result_list = []
    date_list = date_pattern1.findall(str)
    for d in date_list:
        source = d
        d = d.replace("19", " ")
        d = d.replace("20", " ")
        items_tmp = d.split(" ")
        items = drop_null(items_tmp)

        j = 0
        for i in range(0, len(items)):
            k = 0
            pre = ''
            m = j + 2
            if source[j] != items[i][k]:
                while (j < m and j < len(source)):
                    pre += source[j]
                    j = j + 1
            j = j + len(items[i])
            items[i] = pre + items[i]
            # print items[i]
            #str = str.replace(items[i], '') #注释
            result_list.append(items[i])

    result_list.extend(date_pattern2.findall(str))
    return result_list

def get_education_number_from_date(input_str):
    date_size = 0;
    size = len(date_extract(input_str))
    if size % 2 == 0:
        date_size = size / 2
    else:
        date_size = (size + 1) / 2
    return date_size


def process(input_file_path):
    items = []
    items.__sizeof__()
    for line in open(input_file_path, 'r'):
        line = line.strip().decode('utf-8') #一定要
        print line
        # normalize_date(line)
        date_list = date_extract(line)
        for d in date_list:
            print d
        print 'education number: '
        print get_education_number_from_date(line)
        print '-------'


def main():
    print 'this is main'
    input_file_path = 'data/samples'
    result_dic = process(input_file_path)

if __name__ == '__main__':
    main()
