'''
课程网址：https://class.imooc.com/sc/71/learn
学习时间：20191021 

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
mingzhu.insert(-1,"中华")  #为什么显示在倒数第二而不是倒数第一？  左边是起始，右边是中止处不显示
print(mingzhu)
#删除
mingzhu.pop(-1)
print(mingzhu)
#范围显示
print(mingzhu[1:2]) #从1开始，不显示2
print(mingzhu[::]) #显示all

'''
3-3 字典 
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