# coding:UTF-8
class SalesClient():
    @classmethod
    def get_product_input(cls):
        while True:
            try:
                user_input=raw_input("请输出商品的价格或是Q进行结算：")
                return float(user_input)
            except ValueError:
                if user_input=="Q":
                     return "Q"
                print("输入错误，请重新输入")
    @classmethod
    def calculator_payment(cls,product_list,user_disc):
        payment_list=[]
        total=0
        for i in range(len(product_list)):
            payment_item=[i+1,product_list[i],product_list[i]*user_disc]
            payment_list.append(payment_item)
            total+=product_list[i]*user_disc
        return payment_list,total
    @classmethod
    def format_out_msg(cls,list,total):
        out_msg="商品ID\t原价\t折后价\n"
        for prod in list:
            out_msg+="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
        out_msg+="-------------------\n"
        out_msg+="总价:\t%s"%total
        return  out_msg
