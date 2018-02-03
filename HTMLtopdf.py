import requests

req = requests.get('http://permit.mep.gov.cn/permitExt/upanddown.do?method=download&ewmfile=fbfile&datafileid=97c482627f4d4921952a93cc2562ca11')
print(len(req.content))
file_path = 'C:\\Users\何方辉\Downloads\\te.pdf'
# 此脚本可以在服务器上运行，在本地也可以正常获取到正本PDF，唯一的问题是在重写PDF时，格式会乱，但是
# 这不影响阅读，因为此PDF只有一页
# 明日目标：在写入文件前需要创建文件，把这个函数写出来，改写download_ben文件。然后上传服务器进行检验
with open(file_path, 'wb') as fw:
    fw.write(req.content)
