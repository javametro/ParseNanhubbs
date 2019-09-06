import requests

hd = {'User-Agent' : '123'}
r = requests.get("http://www.baidu.com", headers=hd)

print(r.request.headers)

print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.apparent_encoding)
print(r.content)

def getHtmlText(url):
        try:
                r = requests.get(url, timeout=30)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                return r.text
        except:
            return "Something Wrong"


