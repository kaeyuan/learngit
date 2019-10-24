'''
课程网址：https://class.imooc.com/sc/71/learn
学习时间：20191021 -1024

2-5 简单判断
'''

ticket = 1 
knifelength = 15
# 当进入火车站时进行安检
# if 判断条件
if ticket  == 1 :
    print("通过车票的检查，进入火车站，安检")
    #判断刀子的长度是否合法，合法则进入候车大厅；反之不合法，等待处理
    if knifelength <= 10 :
        print("通过安检，进入候车大厅")
    else:
        print("刀子的长度不合法，等待处理")
# 当if条件不成立时，即没有车票
else:
    print("兄弟，你还没车票")

'''
2-6 水仙花数字
'''
n = 153
n1 = int(n/100)
n2 = int(n/10%10)
n3 = n%10
result = n1*n1*n1+n2*n2*n2+n3*n3*n3
if n == result :
    print(n,"是1个水仙花数字")
else:
    print(n,"不是1个水仙花数字")

'''
3-2 列表
    保存一系列相同的简单数据，如书籍、名册。不适合复杂信息
    和php中数组极度相似。
    正向索引，反向索引。
    思考：php中相关用法。 php中数组没有反向索引
'''
mingzhu = ["春秋","战国","左传","史记","汉书","三国志","隋唐","五代","十国","元明"]

#追加 
mingzhu.append("民国")
#更改  
mingzhu[3] = "左传后"
print(mingzhu)
#插入  注意：不是[],是()
mingzhu.insert(2,"左传前")
print(mingzhu)
'''.insert()反向是无法插入到列表的最后1个位置，
    正向才可以，insert(10,"朝花夕拾")即可，只要超出列表的索引就默认在最后的位置。

    insert是将一个元素插入到指定元素的位置，也可以理解为插入到指定元素之前的位置。
    从前向后的索引是0-9. 从后向前的索引是-1 - -10 
    其实是插入到索引为9的位置，最后的一个元素后移。插入的元素的位置就变为倒数第二的位置。
    问题地址：https://class.imooc.com/course/qadetail/163316
'''
mingzhu.insert(-1,"中华") 
print(mingzhu)
#删除
mingzhu.pop(-1)
print(mingzhu)
#范围显示
print(mingzhu[1:2]) #从1开始，不显示2
print(mingzhu[::]) #显示all  php中一般for循环处理

'''
3-3 字典 
    保存一个具体事物的不同信息。
    和php中对象极度相似
    key-value
'''
dan = {"name":"dan","age":"22","height":"165","size":"38","sex":"female"}
#更新数值 
##如不存在，视为新增
print(dan["age"])
print(dan)
dan["son"] = "yunxi"  #不存在
print(dan)

#删除数据
dan.pop("son")  #字典是根据key键，列表是根据索引
print(dan)

'''
3-4 编制学籍
    显示时，字典里的非数字对象必须用""包含
'''
stud = []
stud1 ={"name":"li ming","sex":"male","age":"18","father":{"name":"li baba","age":"42"},"mother":{"name":"li mama","age":"41"}}
stud.append(stud1)
print(stud)

stud2 ={"name":"gao yun","sex":"female","age":"18","father":{"name":"gao baba","age":"42"},"mother":{"name":"gao mama","age":"41"}}
stud.append(stud2)
print(stud)

print("name-"+stud[-1]["name"],"\nage-"+stud[-1]["age"])


'''
4-1 while循环
    不定次循环
'''
wh1 = 0
while wh1 < 4 :
    print(wh1*100)
    wh1 = wh1 + 1  #wh1 += 1也可以用；但是 wh1++是不行的
print ("while End")

### 课堂练习
i = 1
j = 3
while i <=10 :
    print (j)  #i=1,j=3;
    j = j * 3
    i = i + 1

### 编程测试 
sum1 = 0 #所有奇数的和
num1 = 1 #奇数
#循环条件
while num1 < 1000 :
    #判断条件
    if num1%2 != 0 :
        # 求和
        sum1 = sum1 + num1
    num1 = num1 + 1  #不能写到if内，不是奇数就不加了？死循环
#打印最终sum1 值        
print(sum1)  #25000

'''
4-2 for循环
    定次循环
'''
mingzhus = ["春秋","战国","左传","史记","汉书","三国志","隋唐","五代","十国","元明"]
for book in mingzhus :
    if book != "三国志" :
        print(book)

# range 左闭右开
for i in range(10,20):
    print(i)

#寻找所有的水仙花数字,3位数
## for循环
for n in range(100,1000):  #此处n，与外部无冲突
    #根据之前课程所学，水仙花的盘点条件
    n1 = int(n/100)
    n2 = int(n/10%10)
    n3 = n%10
    result = n1*n1*n1+n2*n2*n2+n3*n3*n3
    #循环内的数字遍历，符合条件的打印
    if n == result :
        print(n,"是1个水仙花数字")

## while循环
n = 100
while n < 1000 :    #变化
    
    n1 = int(n/100)
    n2 = int(n/10%10)
    n3 = n%10
    result = n1*n1*n1+n2*n2*n2+n3*n3*n3
    
    if n == result :
        print(n,"是1个水仙花数字")
    n=n+1   #变化

'''
4-3 嵌套循环
'''
col1 = ["春秋","战国","左传","史记","汉书"]
col2 = ["唐朝","宋朝","元朝","明朝","清朝"]
col3 = ["唐诗","宋词","元曲","八股","白话"]
row= [col1,col2,col3]
for i in row :
    for j in i :
        print(j+"-",end="")
    print(end="\n")

# 测试
for i in range(1):
    #打印0 
    for j in range(3):
        print('*',end='')
'''参考解析：
本题考察的是对for循环嵌套的应用。range() 函数用于创建一个整数列表，为左闭右开，i的值为0；j的值为0、1、2。内层循环的print中有end=""，星号会在一行显示，输出结果为一行三列的星号。因此A选项正确。'''

'''
4-4 科幻编年史
'''
ke1 = {"书名":"唐书","朝代":"唐朝","艺术":"唐诗"}
ke2 = {"书名":"宋书","朝代":"宋朝","艺术":"宋词"}
ke3 = {"书名":"元书","朝代":"元朝","艺术":"元曲"}
kex=[ke1,ke2,ke3]
name = input("请输入朝代信息")
for ke in kex :
    if ke['朝代'] == name :
        print("书名："+ke['书名'])
        print("朝代："+ke['朝代'])
        print("艺术："+ke['艺术'])


'''
End  最终作业

定义变量：
定义字典变量service_menu    存储货币转换的四种服务
定义一个列表lst
your_money 存储小明的100元钱

定义字典变量service_menu存储货币转换的四种服务：1.人民币转换美元，2.美元转换人民币，3.人民币转换欧元，0.结束程序
sera = {"num":"1","服务":"人民币转换美元","提示":"欢迎使用人民币转化美元服务","ok":"兑换成美元为：14美元",}
serb = {"num":"2","服务":"美元转换人民币","提示":"欢迎使用美元转化人民币服务","ok":"兑换成人民币元为：714人民币",}
serc = {"num":"3","服务":"人民币转换欧元","提示":"欢迎使用人民币转化欧元服务","ok":"兑换成欧元为：12欧元",}
serd = {"num":"0","服务":"结束程序","提示":"感谢您的使用，祝您生活愉快，再见~"}

service_menu=[sera,serb,serc,serd]

'''
print("**********欢迎使用货币转换系统**********")

print('''1.人民币转换美元
欢迎使用人民币转化美元服务
您需要转化 的人民币为：100元
兑换成美元为：14美元''')
print("==================================")

print('''2.美元转换人民币
欢迎使用美元转化人民币服务
您需要转化 的美元为：100元
兑换成美元为：714人民币''')
print("==================================")

print('''3.人民币转换欧元
欢迎使用人民币转化欧元服务
您需要转化 的人民币为：100元
兑换成欧元为：12欧元''')
print("==================================")

print("0.结束程序")
print("感谢您的使用，祝您生活愉快，再见~")
print("==================================")


print("您好，欢迎访问，服务项目如下：")
print("==================================")
service_menu={1:"人民币转换美元",2:"美元转换人民币",3:"人民币转换欧元",0:"结束程序"} #数字做key不用引号，用了是字符串
lst = [1,2,3,0]
for i in lst :
    print(i,'-',service_menu[i])  #i是虚设不用银行，真实存在的value值用引号包含。不支持+连接符
    your_money = 100
    if i == 0 :
        print(service_menu[i])
    elif i == 1:
        print
        pass







print("==================================")




 

for i in service_menu :
    for j in i :
        print(j+":"+i[j])   #为什么[j] 不是['j'] 这是有基础语法的，了解才能广泛运营
    print("========================")


for i in service_menu :
    if i == service_menu['num'] :
        print(service_menu['num'])
        print(service_menu['服务'])
        print(service_menu['提示'])
        print(service_menu['ok'])