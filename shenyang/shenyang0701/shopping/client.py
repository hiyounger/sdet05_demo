# -*- encoding:utf-8 -*-


class SalesClient():

    # 获取用户对商品信息的输入
    @classmethod
    def get_product_input(cls):
        while True:
            try:
                user_input = raw_input("请输入商品的价格或是Q进行结算:")
                return float(user_input)
            except ValueError:
                #print(user_input)
                if user_input == "Q":
                    return "Q"
                print("输入错误，请重新出入")

    # 依据输入的商品列表，计算商品的结算清单及总价
    @classmethod
    def calculator_payment(cls, prod_list, user_disc):
        payment_list = []
        total = 0
        for i in range(len(prod_list)):
            payment_item = [i + 1, prod_list[i], prod_list[i] * user_disc]
            payment_list.append(payment_item)
            total += prod_list[i] * user_disc
        return payment_list, total

    # TODO 格式化输出内容
    @classmethod
    def format_out_msg(cls, list, total):
        #待完善格式化算法
        out_msg = "商品ID\t原价\t折后价\n"
        for prod in list:
            out_msg += "%s\t%s\t%s\n" % (prod[0], prod[1], prod[2])
        out_msg += "--------------------\n"
        out_msg += "总价:\t%s" % total
        return out_msg