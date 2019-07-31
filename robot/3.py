import urllib.request
response = urllib.request.urlopen("https://baidu.com",data=None,timeout=600,cafile=None,capath=None,\
cadefault=False,context=None)
'''
'''
print(response.read().decode('utf-8'))