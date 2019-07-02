# -*- encoding:utf-8 -*-

__str = "[{'discount': 0.95, 'tel': '18812345672', 'id': '1'}, {'discount': 0.9, 'tel': '18812345673', 'id': '2'}, {'discount': 0.9, 'tel': '18812345674', 'id': '3'}, {'discount': 0.8, 'tel': '18812345671', 'id': '4'}, {'discount': 0.8, 'tel': '18811345671', 'id': '5'}]"

__dic = {"resultcode": "200", "reason": "Return Successd!",
       "result": {"province": "浙江", "city": "杭州", "areacode": "0571", "zip": "310000", "company": "移动", "card": ""},
       "error_code": 0}

#1. 获取str中会员的总数
member_counter = __str.count('id')
print member_counter

#2. 获取dic中省份、城市、运营商三个信息
print("省份：%s\t城市: %s\t运营商: %s" % (__dic['result']['province'], __dic['result']['city'], __dic['result']['company']))

#3. 获取str中，所有会员的手机号
member_info_list = __str.split('[{')[-1].split('}]')[0].split('}, {')
for member_info in member_info_list:
       memebr_data = member_info.split(',')[1].split("'")[3]
       print memebr_data.endswith()

