# encoding:utf-8
import re
from all_extractor import *
# date_str = u"\d{4} *[年/.-]+\d{1,2}"
# date_str = u"[0-9 年/.]+"
# date_pattern = re.compile(date_str)
#
# str = u'92.1/100  2005年7月  --  2008年7月 2002.92006.12'
#
# date_list = date_pattern.findall(str)
# for d in date_list:
#     print d
# str1 = 'aaa'
# print str1[0:len(str1)/2]  (19|20)[0-9]{2} *[年/.-]+[0-9]{1,2}   (19|20)\d{2} *[年/.-]+\d{1,2}

# str2 = u'计算机科学与技术本科青岛理工学院2006/92010/7' \
#        u'武汉工业职业技术分校大专n2012.92015.6\n\n'
# school_str1 = u"([\u4e00-\u9fa5]+大学|[\u4e00-\u9fa5]+学院|分校|学校+)"
# # school_str1 = u'[\w\u4e00-\u9fa5]+(大学|学院|学校|分校)'
# school_pattern1 = re.compile(school_str1)
# school_list = school_pattern1.findall(str2)
# print type(school_list)
# for d in school_list:
#     print d



# str = '2006/92010/7青岛理工大学计算机科学与技术本科'
# str = '''2002.92006.7
# 湖北大学[武汉]
# 本科[学士]
# 专业：
# 计算机科学与技术专业[电子信息科学类]'''
# str = '''2006.92010.6
# 河北理工大学
# 河北理工大学黄河分校
# 本科[学士]
# 专业：
# 信息与计算科学[数学类]'''

# str = '''2002.92006.7
# 湖北大学[武汉]
# 本科[学士]
# 专业：
# 计算机科学与技术专业[电子信息科学类]
# 2006.92010.6
# 河北理工大学
# 本科[学士]
# 专业：
# 信息与计算科学[数学类]'''
# str = '2005/92009/6中国石油大学（华东）电子信息工程本科'
# str = '1995/7--1999/7：同济大学计算机科学与技术本科'
# str = '''2010年9月-2016年7月 清华大学 核科学与技术（仪表控制、人工智能方向） 博士在读（保送） 学分绩：87.5/100  15%
# 计算机科学与技术本科青岛理工学院2006/92010/7
# 2006.09-2010.07 北京科技大学 自动化 工学学士 学分绩：92.1/100
# '''



#str =u'2005/9--2008/6 北京邮电大学 工商管理 硕士1986/9--1989/7 南昌大学 审计学 大专'

str =u'2006年7月--2009年7月	中央财经大学'
#str = u"2009年9月—2013年6月：新乡学院   土木工程   本科 "
#str = "2007.09 - 2010.06  南京师范大学  课程与教学论  硕士 "
# str = '''青岛理工学院计算机科学与技术本科2006/92010/7
#
# 武汉工业职业技术分校大专n2012.92015.6\n\n"	'''
# #
info_list = info_extract(str)
for info in info_list:
    print 'start_date', info['start_date']
    print 'end_date', info['end_date']
    print 'school', info['school']
    print 'major', info['major']
    print 'degree', info['degree']


# import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
#
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
# s = 'www.runoob.com'
# print s[0:3]

s = '培训展开全部/培训/院校公司性质事业单位公司规模10000人以上职位类别/培训-培训/课程顾问2007年8月--2009年3月对外经济贸易大学2008.04'
print get_education_number_from_date(s)

print "this is a test file"
