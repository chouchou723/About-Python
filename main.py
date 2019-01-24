from bottle import route, run, error,abort,redirect
from bottle import static_file, request, template, view

images_path = './images'
assets_path = './assets'
static_path = './views/static'

@error(404)
def miss(code):
    #错误页面，一般来说，可以在网站制定一个404的HTML页面，然后用return template('404')去访问404这个页面
    return '没找到页面！'
@route('/error')
def nofound():
    #引发404错误
    abort(404)

@route('/page')
def page():
    #当访问/page的时候，跳转到首页
    redirect('/')




#定义上传路径
save_path = './upload'

#文件上传的HTML模板，这里没有额外去写html模板了，直接写在这里，方便点吧
@route('/upload')
def upload():
    return '''
        <html>
            <head>
            </head>
            <body>
                <form action"/upload" method="post" enctype="multipart/form-data">
                    <input type="file" name="data" />
                    <input type="submit" value="Upload" />
                </form>
            </body>
        </html>
    '''
#文件上传，overwrite=True为覆盖原有的文件，
#如果不加这参数，当服务器已存在同名文件时，将返回“IOError: File exists.”错误
@route('/upload', method = 'POST')
def do_upload():
    upload   = request.files.get('data')
    import os.path
    name, ext = os.path.splitext(upload.filename)  #用os.path.splitext方法把文件名和后缀相分离
    upload.filename = ''.join(('123',ext))        #修改文件名
    upload.save(save_path,overwrite=True)  #把文件保存到save_path路径下
    return u'上传成功  原文件名是：%s  文件后缀名是：%s \n 修改后的文件名是：%s' %(name,ext,''.join(('123',ext)))

@route('/vue')
def my_vue():
    return template('index.html')

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,root=static_path)


# @route('images/<filename:re:.*\.JPG>')
# def server_static(filename):
#     return static_file(filename,root=images_path)
@route('/assets/<filename:re:.*\.css|.*\.js|.*\.jpg|.*\.png|>')
def server_static(filename):
    return static_file(filename,root=assets_path)
@route('/assets/<filename:re:.*\.ttf|.*\.otf|.*\.eot|.*\.woff|.*\.svg|.*\.map>')
def server_staticR(filename):
    """定义/assets/字体资源路径"""
    return static_file(filename, root=assets_path)

@route('/')
def index():
    return template('index')

@route('/hello/:name')
def hello(name='World'):
    return '<b>Hello %s!</b>' % name

@route('/login')
def login():
    return template('login')
    #  return '''
    #     <html>
    #     <head>
    #     </head>
    #     <body>
    #     <form action="/login" method="post">
    #         Username: <input name="username" type="text" />
    #         Password: <input name="password" type="password" />
    #         <input value="Login" type="submit" />
    #     </form>
    #     </body>
    #     </html>
    # '''
@route('/login',method='POST')
def doLogin():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return '<p>账号:%s</p><p>密码:%s</p>' %(username,password)

@route('/info')
@view('info')
def info123():
    name = '戴儒锋'
    age = '30'
    blog = 'www.linuxyw.com'
    qq = '63780668'
    book = ['python','linux','php']
    price = {'pc':4000,'phone':2000,'bike':600}
    data = {'tname':name,'tage':age,'tblog':blog, 'tqq': qq,'tbook':book,'tprice':price}
    return data
# def info():
    # '''这里默认是GET方法，id,name,age将从url里获取，然后返回到网页内容中'''
    # id = request.query.id
    # name = request.query.name
    # age = request.query.age
    # return "id=%s,name=%s,age=%s" % (id,name,age)
run(host='localhost', port=8180,debug=True)