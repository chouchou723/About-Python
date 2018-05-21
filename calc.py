# name = input('please enter your name: ')
# print('hello,',name)
# print('''line1
# line2
# line3''')
# s = input('please enter your age:')
# age = int(s)
# if age > 18:
# 	print('adult')
# else:
# 	print('teenageer')
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)
# s2 = 'Hello, \'Adam\''
# s2 = 1024 * 768
# print(s2)
# a = -2100
# if a>=0:
# 	print(a)
# else:
# 	print(-a)
# %d	整数    %03d 3位整数 补0
# %f	浮点数 %.1f 1位小数
# %s	字符串
# %x	十六进制整数   用%来转义%
# s1 = 72
# s2 = 85
# r = ((85-72)/72)*100
# print('%.1f%%'   % r)
# print ('%03d-%02d' % (3, 1))
# classmates = []
# classmates.append('Adam')
# classmates.insert(1, 'Jack')
# print (classmates)
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
# def square(x):
# 	a = x/100
# 	return a*a
# def main():
# 	height=float(input('请输入身高(cm):'))
# 	weight=float(input('请输入体重(kg):'))
# 	bmi = weight/square(height)
# 	if bmi<18.5:
# 		print('您太轻了')
# 	elif bmi>18.5 and bmi<25:
# 		print('体重正常')
# 	elif bmi>=25 and bmi<28:
# 		print('您过重了')
# 	elif bmi>=28 and bmi<32:
# 		print('您肥胖了')
# 	else:
# 		print('您严重肥胖了')
# main()

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# L  = ['b','L','A']
# for x in L:
# 	print ('hello'+x)

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#         break #立即结束while,打印end
#     print(n)
# print('end')
# s = set([1, 2, 3])
# print (s.1)
# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# def quadratic(a,b,c):
#     if a==0:
#         return ('a cannot be 0')
#     elif (b*b-4*a*c)<0:
#         return ('无解')
#     else:
#         x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
#         x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
#         return x1,x2

# print ('求ax*x+bx+c的两个根')
# j=float(input('please enter a '))
# m=float(input('please enter b '))
# x=float(input('please enter c '))
# print (quadratic(j,m,x))

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# def move(n,a,b,c):
#     if n == 1:
#         print(a,'->',c)
#     else:
#         move(n-1,a,c,b) #将前n-1个盘子从x移动到y上
#         move(1,a,b,c) #将最底下的最后一个盘子从x移动到z上
#         move(n-1,b,a,c)  #将y上的n-1个盘子移动到z上
#     x = (2**n)-1
#     return x

# x = move(70,"a","b","c")
# print("move steps :", x)


# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L1 if isinstance(x, (str))] 列表生成式的一般格式:[要生成的元素 for 变量名 in 可迭代对象 if判断语句]
# print(L2)