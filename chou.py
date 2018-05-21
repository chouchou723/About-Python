# class Student:
# 	def __init__(self,name):
# 		self.name = name
# 	def __str__(self):
# 		return 'Student object (name: %s)' %self.name
# print(Student('chou'))


# class Fib:
# 	def __init__(self):
# 		self.a,self.b = 0,1

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		self.a,self.b = self.b,self.a+self.b
# 		if self.a >100000:
# 			raise StopIteration()
# 		return self.a

# for n in Fib():
# 	print(n)

# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# from enum import Enum, unique

# @unique
# class Weekday(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6

# day1 = Weekday.Mon.value
# print(day1)

# from tt import Hello
# h = Hello()
# h.hello()

# def fn(self,name='world'):
# 	print('Hello, %s' %name)
# def fb(self,name='chou'):
# 	print('fbfb')
# # Hello1 = type('Hello2',(object,),dict(hello=fn))
# # h=Hello1()
# # h.hello()

# Hello = type('Hello',(object,),dict(abc=fn,fbb=fb))
# h = Hello()
# h.fbb()

# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#     	# print(cls)
#         # attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)

# class MyList(list, metaclass=ListMetaclass):
#     pass
# L = MyList()
# # L.add(1)
# print(L)
# d = {'size': 'large', 'quantity': 6}
# il = d.items()
# print(il)

# f = open('/Users/chouchou/Desktop/tte.txt','r')
# f.read()
# f.close()
# with open('/Users/chouchou/Desktop/tte.txt', 'r') as f:
#     # print(f.read(1024))
#     for line in f.readlines():
#     	print(line.strip())

# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')写入

# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world')
# print(f.getvalue())输入string,获取值
# import os
# print(os.name)
# 查看当前目录的绝对路径:
# os.path.abspath('.')
# '/Users/michael'
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# # 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# os.rmdir('/Users/michael/testdir')
# os.path.join('/Users/chouchou/Desktop','test')
# os.mkdir('/Users/chouchou/Desktop/test')
# os.rmdir('/Users/chouchou/Desktop/test')
# os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
# os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')
# # 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
# import pickle
# 对象序列化,把数据存到本地文件
# d = dict(name='bob',age=20,score=99)
# f = open('dump.txt','wb')
# pickle.dump(d,f)
# f.close
# 反序列化,读取文件
# f = open('dump.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)
# json的转换
# import json
# d = dict(name='bob',age=20,score=99)
# f = open('dump.json','w')
# json.dump(d,f)
# f.close()
# f = open('dump.json','r')
# d = json.load(f)
# f.close()
# print(d)

# class Student:
# 	def __init__(self,name,age,score):
# 		self.name = name
# 		self.age= age
# 		self.score = score

# def student2dict(std):
# 	return {
# 		'name':std.name,
# 		'age':std.age,
# 		'score':std.score
# 	}
# s = Student('bob',10,92)
# print(json.dumps(s,default=student2dict))
# print(json.dumps(s,default=lambda obj:obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

# def dict2student(d):
# 	return Student(d['name'], d['age'], d['score'])
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))
# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True)
# print(s)
# from multiprocessing import Process
# import os
# # print('Process (%s) start ...' % os.getpid())
# # pid = os.fork()
# # if pid ==0:
# # 	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# # else:
# # 	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# def run_proc(name):
# 	print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
# 	print('Parent process %s' %os.getpid())
# 	p = Process(target=run_proc,args=('test',))
# 	print('Child process will start')
# 	p.start()
# 	p.join()
# 	print('Child process end.')

# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
# 	print('Run task %s (%s)...' % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds' %(name,(end-start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import subprocess

# # print('$ nslookup www.python.org')
# # r = subprocess.call(['nslookup','www.python.org'])
# # print('Exit code:',r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output)
# print('Exit code:', p.returncode)

# from multiprocessing import Process,Queue
# import os,time,random

# #写数据
# def write(q):
# 	print('Process to write: %s' %os.getpid())
# 	for value in ['A','B','C']:
# 		print('Put %s to queue...' %value)
# 		q.put(value)
# 		time.sleep(random.random())

# def read(q):
# 	print('Process to read %s' %os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue.' %value)

# if __name__=='__main__':
# 	q= Queue()
# 	pw = Process(target=write,args=(q,))
# 	pr = Process(target=read,args=(q,))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()

# import time,threading

# def loop():
# 	print('thread %s is running...' %threading.current_thread().name)
# 	n=0
# 	while n < 5:
# 		n = n+1
# 		print('thread %s >>> %s' % (threading.current_thread().name,n))
# 		time.sleep(1)
# 	print('thread %s ended.' %threading.current_thread().name)

# print('thread %s is running...' %threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' %threading.current_thread().name)

# import time, threading

# # 假定这是你的银行存款:
# balance = 0

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)交替修改balance,会使得balance最后的值不是0


# import time, threading

# # 假定这是你的银行存款:
# balance = 0
# #用了锁,确保线程在运行时,其他线程会等待锁解锁后再运行,不会造成变量共享产生的 共同修改问题
# lock = threading.Lock()
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

# import threading

# # 创建全局ThreadLocal对象:
# local_school = threading.local()

# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# task_master.py
#server
# import random, time, queue
# from multiprocessing.managers import BaseManager

# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()

# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass

# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 8000), authkey=b'abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')
#join
# task_worker.py
# import time, sys, queue
# from multiprocessing.managers import BaseManager

# # 创建类似的QueueManager:
# class QueueManager(BaseManager):
#     pass

# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')

# # 连接到服务器，也就是运行task_master.py的机器:
# server_addr = '127.0.0.1'
# print('Connect to server %s...' % server_addr)
# # 端口和验证码注意保持与task_master.py设置的完全一致:
# m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# # 从网络连接:
# m.connect()
# # 获取Queue的对象:
# task = m.get_task_queue()
# result = m.get_result_queue()
# # 从task队列取任务,并把结果写入result队列:
# for i in range(10):
#     try:
#         n = task.get(timeout=1)
#         print('run task %d * %d...' % (n, n))
#         r = '%d * %d = %d' % (n, n, n*n)
#         time.sleep(1)
#         result.put(r)
#     except Queue.Empty:
#         print('task queue is empty.')
# # 处理结束:
# print('worker exit.')

#正则模块
# >>> import re
# >>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

#常用模块
# >>> from datetime import datetime
# >>> now = datetime.now() # 获取当前datetime
# >>> print(now)
# 2015-05-18 16:28:07.198690
# >>> print(type(now))
# >> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
# >>> print(dt)
# 2015-04-19 12:20:00

# >>> from datetime import datetime
# >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
# >>> dt.timestamp() # 把datetime转换为timestamp
# 1429417200.0
# >>> t = 1429417200.0
# >>> print(datetime.fromtimestamp(t))
# 2015-04-19 12:20:00
# >>> t = 1429417200.0
# >>> print(datetime.fromtimestamp(t)) # 本地时间
# 2015-04-19 12:20:00
# >>> print(datetime.utcfromtimestamp(t)) # UTC时间
# 2015-04-19 04:20:00

# >>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# >>> print(cday)
# 2015-06-01 18:19:59

# >>> now = datetime.now()
# >>> print(now.strftime('%a, %b %d %H:%M'))
# Mon, May 05 16:28

# >>> now = datetime.now()
# >>> now
# datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
# >>> now + timedelta(hours=10)
# datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
# >>> now - timedelta(days=1)
# datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
# >>> now + timedelta(days=2, hours=12)
# datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)

# # 拿到UTC时间，并强制设置时区为UTC+0:00:
# >>> utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# >>> print(utc_dt)
# 2015-05-18 09:05:12.377316+00:00
# # astimezone()将转换时区为北京时间:
# >>> bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# >>> print(bj_dt)
# 2015-05-18 17:05:12.377316+08:00
# # astimezone()将转换时区为东京时间:
# >>> tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# >>> print(tokyo_dt)
# 2015-05-18 18:05:12.377316+09:00
# # astimezone()将bj_dt转换时区为东京时间:
# >>> tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# >>> print(tokyo_dt2)
# 2015-05-18 18:05:12.377316+09:00

# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# p = Point(1,2)
# print(p.x)
# Circle = namedtuple('Circle',['x','y','r'])
# c = Circle(1,2,10)

# from collections import deque
# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)
# deque(['y', 'a', 'b', 'c', 'x'])

# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# >>> from collections import OrderedDict
# >>> d = dict([('a', 1), ('b', 2), ('c', 3)])
# >>> d # dict的Key是无序的
# {'a': 1, 'c': 3, 'b': 2}
# >>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# >>> od # OrderedDict的Key是有序的
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# >>> od = OrderedDict()
# >>> od['z'] = 1
# >>> od['y'] = 2
# >>> od['x'] = 3
# >>> list(od.keys()) # 按照插入的Key的顺序返回
# ['z', 'y', 'x']

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

# from collections import OrderedDict

# class LastUpdatedOrderedDict(OrderedDict):

#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity

#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False) last=false先进先出,去除第一个
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)

# >>> from collections import Counter
# >>> c = Counter()
# >>> for ch in 'programming':
# ...     c[ch] = c[ch] + 1
# ...
# >>> c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})

# from PIL import Image

# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('test.jpg')
# # 获得图像尺寸:
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('thumbnail.jpg', 'jpeg')


#  import requests
# r = requests.get('https://www.douban.com/search',  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'},
# 	params={'q': 'python', 'cat': '1001'})
#  r.json()
#  r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#  upload_files = {'file': open('report.xls', 'rb')}
# >>> r = requests.post(url, files=upload_files)
# #跨请求保持某些参数
# # 创建一个session对象 
# s = requests.Session() 
# # 用session对象发出get请求，设置cookies 
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789') 
# # 用session对象发出另外一个get请求，获取cookies 
# r = s.get("http://httpbin.org/cookies") 
# # 显示结果 
# r.text 
#  '{"cookies": {"sessioncookie": "123456789"}}'

# 我们先来获取CPU的信息：

# import psutil
# a = psutil.cpu_count() # CPU逻辑数量
# 4
# >>> psutil.cpu_count(logical=False) # CPU物理核心
# 2
# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()
# SELECT * FROM classes WHERE grade_id = '1';

# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'

# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''

# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'

# if __name__ == '__main__':
#     app.run()