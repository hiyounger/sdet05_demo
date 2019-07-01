#encoding:utf-8
class scilt():
    pay_list = []
    @classmethod
    def input_price(cls):
        while True:
            try:
                price = raw_input("请输入商品的价格或者输入Q退出")
                return float(price)
            except:
                if price == "Q":
                    return "Q"
                print('输入错误，请重新输入')

    # 将价格导入支付账单中，并计算折扣后的价格
    @classmethod
    def pay_list_cal(slef,shop_list, disc):
        sum = 0
        for i in range(len(shop_list)):
            temp = [i + 1, shop_list[i], shop_list[i] * disc]
            scilt.pay_list.append(temp)
            sum += shop_list[i] * disc
        pay_lists = [scilt.pay_list, sum]
        return pay_lists
    # 输出格式
    @classmethod
    def out_way(cls,new_pay_list):
        msg = "商品ID\t单价\t折扣价格\n"
        for i in new_pay_list[0]:
            msg += "%s\t\t%s\t%s\n" % (i[0], i[1], i[2])
        msg += "-----------------\n"
        msg += "总价:\t%s" % new_pay_list[1]
        return msg
