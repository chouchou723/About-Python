#-*-coding:utf-8-*-
import requests
from lxml import html
url='http://www.zyzw.com/sjmhxs/sjmhxs' #需要爬数据的网址
number = 1
L = [x+1 for x in range(10)]
add = '.htm'
for i in L: 
	if i<10:
		i = '00%d' %i
	elif i<100:
		i = '0%d' %i
	page=requests.Session().get(url+str(i)+add);
	page.encoding = 'gb2312'
	tree=html.fromstring(page.text)
	result=tree.xpath('//font[@style="font-size: 10.5pt; line-height: 16pt"]/text()')
print(result)	
# def f(x):
# 	return x.decode('gb2312','strict')
# r = list(map(f, result))
