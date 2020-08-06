from urllib import request,parse
import json

def fanyi(keyword):
    base_url = 'https://fanyi.baidu.com/sug'

    #构建请求对象
    data = {
        'kw': keyword
    }
    data = parse.urlencode(data)

    #模拟浏览器
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=headers)
    res = request.urlopen(req)

    #获取json字符串
    str_json = res.read().decode('utf-8')
    # 把json转换成字典
    myjson = json.loads(str_json)
    info = myjson['data'][0]['v']
    print(info)

if __name__ == '__main__':
    while True:
        keyword = input('亲，请输入你要翻译的单词：')
        if keyword == 'q':
            break
        fanyi(keyword)