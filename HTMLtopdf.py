import requests

req = requests.get('http://permit.mep.gov.cn/permitExt/upanddown.do?method=download&ewmfile=fbfile&datafileid=97c482627f4d4921952a93cc2562ca11')
print(len(req.content))
file_path = 'C:\\Users\何方辉\Downloads\\te.pdf'
with open(file_path, 'wb') as fw:
    fw.write(req.content)
