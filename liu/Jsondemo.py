#  encoding=utf-8
str = "[{'discount': 0.95, 'tel': '18812345672', 'id': '1'}, {'discount': 0.9, 'tel': '18812345673', 'id': '2'}, {'discount': 0.9, 'tel': '18812345674', 'id': '3'}, {'discount': 0.8, 'tel': '18812345671', 'id': '4'}, {'discount': 0.8, 'tel': '18811345671', 'id': '5'}]"

dic = {"resultcode": "200", "reason": "Return Successd!",
       "result": {"province": "浙江", "city": "杭州", "areacode": "0571", "zip": "310000", "company": "移动", "card": ""},
       "error_code": 0}

#1
member_count=str.count('id')
print member_count

#2
print('省份:%s\n城市:%s\n运营商:%s\n'%(dic['result']['province'],dic['result']['city'],dic['result']['company']))

#3
member_tel=str.split('[{')[-1].split('}]')[0].split('}, {')
print member_tel
for mem in member_tel:
       tel = mem.split(",")[1].split('\'')[3]
       print tel