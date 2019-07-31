import urllib.request
response = urllib.request.urlopen("https://baidu.com")
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))