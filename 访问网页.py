import requests
url="http://ctf-union.pangolinlabs.cn:50163/"
r=requests.session()
for i in range(332):
    r.get(url)
print(r.get(url).content)