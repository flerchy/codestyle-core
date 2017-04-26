import urllib
import urllib2
import json
 
#values = {"username":"459118433@qq.com","password":"XXXX"}

values = {"startTime":32434232, "endTime":324354354, "interval":600}
# values = {"username":"1016903103@qq.com","password":"XXXX"}
print values

# format as urlencode,startTime=32434232&endTime=324354354&interval=600
# data = urllib.urlencode(values)

# format as josn
data = json.dumps(values)

# restful api
# url = "http://localhost:9999/lightcontroller/postt"
# restful api
url = "http://localhost:9999/lightcontroller/qsmart"

# i want to post a json to remost
# request.add_header('Content-Type', 'application/json')
# 其中，agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent,例如下面的例子
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
mediaType = 'application/json';
headers = { 'User-Agent' : user_agent, 'Content-Type': mediaType}  

request = urllib2.Request(url, data, headers)

response = urllib2.urlopen(request)
print response.read()