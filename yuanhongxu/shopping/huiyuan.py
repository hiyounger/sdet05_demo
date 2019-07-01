#-*- encoding:utf-8 -*-

# 会员信息表
huiyuan=[
    {"id":1,"tel":"13512345678","disc":0.8,"status":"inactive","jifen":100},
    {"id":2,"tel":"13512345679","disc":0.9,"status":"active","jifen":3000}
]

class huiyuan_help():
    # 通过电话号码返回折扣
    @classmethod
    def tel_disc(cls,user_tel):
        for i in huiyuan:
            if i['tel']==user_tel:
                return i['disc']
        return 1.0



    # 增加会员
    @classmethod
    def add_huiyuan(cls):
        tel=raw_input("请输入会员电话")
        disc=input("请输入折扣")
        id=len(huiyuan)+1
        huiyuan_dict={"id":id,"tel":tel,"disc":disc,"status":"active","jifen":0}
        huiyuan.append(huiyuan_dict)

    #获取所有会员列表
    @classmethod
    def select_huiyuan(cls,huiyuan=huiyuan):
        huiyuan_format="会员id\t会员电话\t\t会员折扣\t\t积分\n"
        for i in huiyuan:
            if i["status"]=="active":
                huiyuan_format+="%s\t\t%s\t%s\t\t\t%s\n"%(i["id"],i["tel"],i["disc"],i["jifen"])
        print (huiyuan_format)

    #根据手机号后四位获取会员信息
    @classmethod
    def slect_by_tel(cls):
        tel_list=[]
        tel=raw_input("请输入手机号后四位")
        tel_list_four=list(tel)
        for i in huiyuan:
            if tel_list_four[0]==i["tel"][-4] and tel_list_four[1]==i["tel"][-3] and tel_list_four[2]==i["tel"][-2] and tel_list_four[3]==i["tel"][-1]:
                tel_list.append(i)
        return tel_list


    #根据手机号注销会员（保留）
    @classmethod
    def del_huiyuan(cls):
        # print huiyuan
        tel_del=raw_input("请输入要删除的手机号")
        for i in huiyuan:
            if i["tel"]==tel_del:
                i["status"]="inactive"
        # print huiyuan

    #修改会员信息（手机号，折扣）
    @classmethod
    def update_huiyuan(cls):
        tel_update = raw_input("请输入要修改的会员手机号")
        for i in huiyuan:
            if i["tel"] == tel_update and i["status"] == "inactive":
                print ("此会员已注销")
                return None
        choose_update = input("请输入要修改的内容：按1修改手机号，按2修改折扣信息")
        if choose_update == 1:
            new_tel = raw_input("请输入新手机号")
            for i in huiyuan:
                if i["tel"] == tel_update:
                    i["tel"] = new_tel
        if choose_update == 2:
            new_disc = input("请输入新折扣")
            for i in huiyuan:
                if i["tel"] == tel_update:
                    i["disc"] = new_disc

    #会员可积累购物积分（1元=1积分，1000积分可以打98折，3000积分打95折，5000积分打九折）
    @classmethod
    def add_jifen(cls,sum_price,user_tel):
        for i in huiyuan:
            if i["tel"]==user_tel:
                i["jifen"]+=sum_price
    #
    @classmethod
    def add_disc(cls,user_tel):
        for i in huiyuan:
            if i["tel"]==user_tel:
                if i["status"]=="inactive":
                    return 1.0
                elif i["jifen"] >= 5000:
                    return i["disc"] * 0.90
                elif i["jifen"] >= 3000:
                    return i["disc"] * 0.95
                elif i["jifen"] >= 1000:
                    return i["disc"] * 0.98
                else:
                    return i["disc"]
        return 1.0
