# coding:utf-8

str = "[{'discount': 0.95, 'tel': '18812345672', 'id': '1'}, {'discount': 0.9, 'tel': '18812345673', 'id': '2'}, {'discount': 0.9, 'tel': '18812345674', 'id': '3'}, {'discount': 0.8, 'tel': '18812345671', 'id': '4'}, {'discount': 0.8, 'tel': '18811345671', 'id': '5'}]"

dic = {"resultcode": "200", "reason": "Return Successd!",
       "result": {"province": "浙江", "city": "杭州", "areacode": "0571", "zip": "310000", "company": "移动", "card": ""},
       "error_code": 0}


# str_list=list(str)
# print (len(str_list))
print str.count("id")



print (dic["result"]["province"])
print (dic["result"]["city"])
print (dic["result"]["company"])

member_list=str.split("[{")[-1].split("}]")[0].split("}, {")
for str in member_list:
       member_data=str.split(",")[1].split("'")[3]
       print member_data





