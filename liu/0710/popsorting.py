# encoding:utf-8
s = [6,8,10,1,7,3,9]
s = list(s)
for i in range(len(s)):
    for a in range(len(s)-1):
        if s[a] > s[a+1]:
            n = s[a]
            s[a] = s[a+1]
            s[a+1]= n
print(s)

# @class sorting:
#     def lisorting_list(self,list):
#         for i in range(len(s) - 1):
#             for a in range(len(s) - 1 - i):
#                 if s[a] > s[a + 1]:
#                     temp = s[a]
#                     s[a] = s[a + 1]
#                     s[a + 1] = temp
#             print(s)
#
#     def lisorting_list2(self,desc,asc):
#         sort = input()
#         for i in range(len(s) - 1):
#             for a in range(len(s) - 1 - i):
#                 if s[a] > s[a + 1] and sort =='desc':
#                     temp = s[a]
#                     s[a] = s[a + 1]
#                     s[a + 1] = temp
#                 elif s[a] < s[a + 1] and sort =='asc':
#                     temp = s[a]
#                     s[a] = s[a + 1]
#                     s[a + 1] = temp
#             return s
#
#
#
#
# try:
#     type(s) == list
# except:
#     print('400')
# s=list(s)
# try:
#     for i in list(s):
#         i = int(i)
# except:
#     print(list(s))















