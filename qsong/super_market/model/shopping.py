# -*- encoding:utf-8 -*-
from tyj.super_market.db import mysql












# class get_members():
#     @classmethod
#     def get_member_by_tel(cls, tel):
#         get_member_by_tel = []
#         get_add_newmember = []
#         for member in mysql.members:
#             if int(member['tel']) != int(tel):
#                 get_member = {"return_code": 508, "return_msg": "add member failed, exists"}
#                 return get_member
#             elif int(member['tel']) == int(tel) and len(member['tel']) == 11:
#                 get_member_by_tel.append(member)
#                 get_member = {
#                     "return_code": 200,
#                     "return_msg": "add member success",
#                     "member": get_member_by_tel}
#                 return get_member
#         get_add_newmember = get_add_newmember.append(get_member)
#         return get_add_newmember
