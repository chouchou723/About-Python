import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","123456","TESTDB" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# sql="""CREATE TABLE EMPLOYEE(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT
# )
# # """
# sql="""CREATE TABLE DEPART(
#     ID INT NOT NULL,
#     DEP_NAME CHAR(20),
#     MEMBER INT
# )
# # """
# SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) \
#     VALUES('C','Chou',20,'M',12000)"
sql = "INSERT INTO DEPART(DEP_NAME,MEMBER) \
    VALUES('Sale',20)"
# 用了"""可以不用加\ 来做换行
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    # SQL 插入语句 方便替换变量
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
# SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE +1 WHERE SEX = '%s'" %('M')
# SQL 删除语句
# sql="DELETE FROM DEPART WHERE MEMBER = '%d'" %(20)
try:
    # 执行sql语句
    cursor.execute(sql)
     # 提交到数据库执行
    db.commit()
# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
except:
     # 如果发生错误则回滚
    # db.rollback()
    print("error")
# print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()
