from urllib import request
import chardet


if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com")
    response = request.urlopen(req)
    print("geturl信息:%s" %(response.geturl()))
    print("inf信息:%s" %(response.info()))
    print("getcode信息:%s" %(response.getcode()))
    # html = response.read()
    # chardet = chardet.detect(html)
    # print(chardet)