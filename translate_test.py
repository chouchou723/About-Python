from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    Request_URL = "http://fanyi.baidu.com/v2transapi"
    Form_Data = {}
    Form_Data['query'] = 'jack'
    Form_Data['from'] = 'en'
    Form_Data['to'] = 'zh'
    Form_Data['transtype'] = 'realtime'
    Form_Data['simple_means_flag'] = '3'
    Form_Data['sign'] = '143778.447123'
    Form_Data['token'] = '2a168a8c49aa7b45ab69a459e6358225'
    # Form_Data['doctype'] = 'json'
    # Form_Data['version'] = '2.1'
    # Form_Data['keyfrom'] = 'fanyi.web'
    # Form_Data['action'] = 'FY_BY_REALTIME'
    # Form_Data['typoResult'] = 'false'
    
    data = parse.urlencode(Form_Data).encode('utf-8')

    response = request.urlopen(Request_URL,data)

    html = response.read().decode('utf-8')

    translate_results = json.loads(html)

    # translate_results = translate_results['translateResult'][0][0]['tgt']

    print("翻译的结果是：%s" % translate_results)
