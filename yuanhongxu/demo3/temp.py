#coding:utf-8
import json
temp='注册成功:{"uid":0,"username":"yuan","password":"yuan123","email":"yuan@qq.com"}'

print temp
print type(temp)
print temp.split("成功:")[-1]

return_msg=json.loads(temp.split("成功:")[-1])
print return_msg
print return_msg[u"uid"]