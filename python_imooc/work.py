'''
End  最终作业

定义字典service_menu    存储货币转换的四种服务
定义列表lst
定义变量your_money  存储小明的100元钱

ask:
1-多行语句中如何打印多个变量。
2-为什么定义列表lst？没有实际用处啊

'''

print("**********欢迎使用货币转换系统**********")
#存储货币转换的四种服务
service_menu={1:"人民币转换美元",2:"美元转换人民币",3:"人民币转换欧元",0:"结束程序"} #数字做key不用引号，用了是字符串
lst = [1,2,3,0]
#存储的钱
your_money = 100
for i in lst :
    #打印服务项目
    print(i,'-',service_menu[i])  #i是循环变量

    #输出货币兑换信息
    if i == 1 :
        print('欢迎使用'+service_menu[1]+'服务')
        print('您需要转换的人民币为：',your_money,'元') #+连接符，不能用在数字和字符串之间。 转换str()后即可
        print('兑换成美元为：',your_money/7.14,'$')
        print("==================================")
    elif i == 2:
        print('欢迎使用'+service_menu[2]+'服务')
        print('您需要转换的美元为：'+str(your_money)+'元') 
        print('兑换成人民币为：'+str(your_money*7.14)+'人民币')
        print("==================================")
    elif i == 3:
        print('欢迎使用'+service_menu[3]+'服务')
        print('您需要转换的人民币为：',your_money,'元') 
        print('兑换成欧元为：',your_money*0.12,'€')
        print("==================================")
    else :
        print("感谢您的使用，祝您生活愉快，再见~")
        print("==================================")
 


### 第2种方法制作
print("**********欢迎使用货币转换系统**********")
#存储货币转换的四种服务
service_menu={1:"人民币转换美元",2:"美元转换人民币",3:"人民币转换欧元",0:"结束程序"}
#存储的钱
your_money = 100

for i in service_menu :
    #打印服务项目
    print(i,'-',service_menu[i])
    #输出货币兑换信息
    if i == 1 :
        print('欢迎使用'+service_menu[1]+'服务')
        print('您需要转换的人民币为：',your_money,'元') 
        print('兑换成美元为：',your_money/7.14,'$')
        print("==================================")
    elif i == 2:
        print('欢迎使用'+service_menu[2]+'服务')
        print('您需要转换的美元为：',your_money,'元') 
        print('兑换成人民币为：',your_money*7.14,'人民币')
        print("==================================")
    elif i == 3:
        print('欢迎使用'+service_menu[3]+'服务')
        print('您需要转换的人民币为：',your_money,'元') 
        print('兑换成欧元为：',your_money*0.12,'€')
        print("==================================")
    else :
        print("感谢您的使用，祝您生活愉快，再见~")
        print("==================================")
