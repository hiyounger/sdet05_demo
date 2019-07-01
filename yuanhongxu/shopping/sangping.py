#-*- encoding:utf-8 -*-

class sangping_caozuo():
    #录入商品及结束录入商品
    @classmethod
    def sp_spjg(cls):
        try:
            input_user=raw_input("请输入商品价格或按Q结束录入")
            input_data=float(input_user)
            return input_data
        except ValueError:
            if input_user=="Q":
                return "Q"
            print ("输入错误，请输入正确的商品")

    #根据累计商品的列表和折扣返回列表清单,总价
    @classmethod
    def jisuan(cls,spjg_list,disc):
        price_list=[]
        sum_price=0
        for i in range(len(spjg_list)):
            price=[i+1,spjg_list[i],spjg_list[i]*disc]
            price_list.append(price)
            sum_price+=spjg_list[i]*disc
        return price_list,sum_price
    #格式化输出
    @classmethod
    def format(cls,price_list,sum_price):
        out_msg="商品id\t商品原价\t商品折后价\n"
        for i in price_list:
            out_msg+="%s\t\t%s\t\t%s\n"%(i[0],i[1],i[2])
        out_msg+="----------------------------\n"
        out_msg+="商品总价\t%s"%sum_price

        return out_msg



