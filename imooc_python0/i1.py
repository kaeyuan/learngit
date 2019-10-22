'''
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
3-3 列表
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
mingzhu.insert(-1,"中华")  #为什么显示在倒数第二而不是倒数第一？
print(mingzhu)
#删除
mingzhu.pop(-1)
print(mingzhu)