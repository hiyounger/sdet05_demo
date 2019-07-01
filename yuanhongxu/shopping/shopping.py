#coding:utf-8
from huiyuan import huiyuan_help
from sangping import sangping_caozuo

def saling():
    #输入手机号，获取折扣
    user_tel=raw_input("请输入你的手机号")
    # disc=huiyuan_help.tel_disc(user_tel)

    #获取积分，得到综合折扣
    disc=huiyuan_help.add_disc(user_tel)
    print(disc)

    #商品录入
    spjg_list = []
    while True:
        shangpin=sangping_caozuo.sp_spjg()
        if shangpin=="Q":
            break
        elif shangpin == None:
            continue
        else:
            spjg_list.append(shangpin)

    price_list,sum_price=sangping_caozuo.jisuan(spjg_list,disc)
    #增加积分
    huiyuan_help.add_jifen(sum_price,user_tel)

    #格式化输出
    print (sangping_caozuo.format(price_list,sum_price))

def huiyuan_guanli():
    while True:
        try:
            choose=input("按1新增会员;按2获取会员信息;按3根据手机号的后四位获取会员信息\n"
                         "按4根据手机号注销会员;按5修改会员信息;退出请按0\n")
            if choose == 0:
                break
            elif choose == 1:
                huiyuan_help.add_huiyuan()
            elif choose == 2:
                huiyuan_help.select_huiyuan()
            elif choose==3:
                select_tel=huiyuan_help.slect_by_tel()
                huiyuan_help.select_huiyuan(select_tel)
            elif choose==4:
                huiyuan_help.del_huiyuan()
            elif choose==5:
                huiyuan_help.update_huiyuan()
            else:
                print ("输入错误，请重新输入")
        except:
            print ("输入错误，请重新输入")


if __name__=="__main__":
    while True:
        try:
            xuanzhe=input("输入1进入销售系统，输入2进入会员管理系统费，输入0退出")
            if xuanzhe==1:
                saling()
            elif xuanzhe==2:
                huiyuan_guanli()
            elif xuanzhe==0:
                break
            else:
                print ("输入错误，请重新输入")
        except:
            print ("输入错误，请重新输入")
