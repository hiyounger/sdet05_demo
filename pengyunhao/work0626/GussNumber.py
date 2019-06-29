#encoding:utf-8

'''
import random
randomNumber=random.randint(0,100)
print randomNumber
count=0
print ("本游戏为0-100之间的整数")
while 1:

        try :
            count += 1
            userNumber = int(input("请输入数字："))
            print type(userNumber)
            if userNumber<0 or userNumber>100:
                print ("请输入0-100之间的整数")
            elif userNumber==randomNumber :
                if count==1:
                    print ("大佬,你只用了一次就猜对了")
                    break
                else:
                    print ("恭喜，猜对了！,一共猜了%d次"%count)
                    break
            elif userNumber>randomNumber :
                print ("猜大了")
            else:
                print ("猜小了")
        except NameError:
            print ("不能输入字母，请输入0-100之间的整数")
        except SyntaxError:
            print ("不能输入特殊字符，请输入0-100之间的整数")
        except :
            print ("输入错误，请输入0-100之间的整数")

'''
import random
randomNumber=random.randint(0,100)
print randomNumber
count=0
print ("本游戏为0-100之间的整数")
while 1:
    try :
        count += 1
        userNumber=input("请输入数字：")
        if isinstance(userNumber,float):
            print ("不能输入小数，请输入0-100之间的整数")
        else:
            if userNumber<0 or userNumber>100:
                print ("数字太大或太小，请输入0-100之间的整数")
            elif userNumber==randomNumber :
                if count==1:
                    print ("大佬,你只用了一次就猜对了")
                    break
                else:
                    print ("恭喜，猜对了！,一共猜了%d次"%count)
                    break
            elif userNumber==count:
                print ("不能输入字母，请输入0-100之间的整数")
            elif userNumber>randomNumber :
                print ("猜大了")
            else:
                print ("猜小了")
    except NameError:
        print ("不能输入字母，请输入0-100之间的整数")
    except SyntaxError:
        print ("不能输入特殊字符，请输入0-100之间的整数")
    except :
        print ("输入错误，请输入0-100之间的整数")