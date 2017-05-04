
doc2txt.py: .doc格式文档转换为.txt格式文档，并保存
requirement：win32com库
pdf2txt.py: .pdf格式文档转换为.txt格式文档
requirement：pdfminer库
eml2txt.py：.eml格式文档转换为html格式文档
requirement：email库

html2txt库：html2txt.html2txt()将html格式转换为txt格式

main.py :从简历库中读取简历，得到简历名称，根据文档后缀名（pdf、word、html、email）进行格式分类，对不同格式的文本进行转换，并存储