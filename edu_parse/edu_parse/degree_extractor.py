# encoding:utf-8
import re

degree_str1 = u"(初中|高中|职高|中专|技校|大专|本科|硕士研究生|在职研究生|工程硕士|专业硕士|博士研究生|博士在读|MBA硕士|MBA|EMBA|工商管理硕士|工学学士|访问学者|博士后|研究生|硕士|博士|学士)"
degree_pattern1 = re.compile(degree_str1)

# 抽取学位信息,并将日期按照顺序排列存入list
def degree_extract(str):
    result_list = []
    school_list = degree_pattern1.findall(str)
    for d in school_list:
        # print d
        result_list.append(d)
    return result_list

# 会破坏信息排布的顺序
# 该函数并没有被用到
def remove_duplicate_data(degree_list):
    degree_dic = {}
    for k in degree_list:
        if k not in degree_dic:
            degree_dic.setdefault(k, 0)
        else:
            degree_list.remove(k) #去除第一个k对象
    return degree_list

def process(input_file_path):
    for line in open(input_file_path, 'r'):
        line = line.strip().decode('utf-8')
        print line
        degree_list = degree_extract(line)
        for d in degree_list:
            print d
        print '-------'

def main():
    print 'this is main'
    input_file_path = 'data/samples'
    result_dic = process(input_file_path)

if __name__ == '__main__':
    main()
