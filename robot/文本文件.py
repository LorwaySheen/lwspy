import urllib.request
response = urllib.request.urlopen("https://baidu.com")
#print(response.read().decode('utf-8'))

print(type(response))       #<class 'http.client.HTTPResponse'>
