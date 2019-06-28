# encoding:utf-8
mermber = [
    {'id':1,'tel':'18845871680','zhekou':0.8},
    {'id':2,'tel':'18845095099','zhekou':0.88},
    {'id':1,'tel':'15165206762','zhekou':0.98}
]
tel=input("请输入自己的手机号码：")
print type(tel)
for i in range(len(mermber)):
   for m in mermber[i]:
       if m[i]['tel']==tel:
           print ("您是会员，打%f折"%m[i]['tel'])

