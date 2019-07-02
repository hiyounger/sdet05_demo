#encoding:utf-8
class Saleclient():

    @classmethod
    def get_pro_input(cls):
        while True:
            try:
                shang=raw_input('请输入商品价格或Q进行结算:')
                return float(shang)
            except:
                if shang =='Q':
                    return 'Q'
                print('输入有误，请重新输入')

    @classmethod
    def calculator_payment(cls,pro_list,disc):
        payment_list=[]
        total=0
        for i in range(len(pro_list)):
            payment_item=[i+1,pro_list[i],pro_list[i]*disc]
            payment_list.append(payment_item)
            total+=pro_list[i]*disc
        return payment_list,total

    @classmethod
    def format_out_msg(cls,list,total):
        out_msg='商品ID\t原价\t\t折后价\n'
        for pro in list:
            out_msg+='\t%s\t%s\t%s\n'%(pro[0],pro[1],pro[2])
        out_msg+='-------------\n'
        out_msg+='总价：%s'%total
        return out_msg
