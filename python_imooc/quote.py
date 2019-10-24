your_money = 100
dollar = 7.14
euro = 0.12
service_menu = {
    '1': {
        'title': '1.人民币转换美元',
        'tips': '欢迎使用人民币转换美元服务',
        'text': '您需要转换的人民币为' + str(your_money) + '元',
        'result': '兑换成美元为' + str(your_money / dollar) + '$'
    },
    '2': {
        'title': '2.美元转换人民币',
        'tips': '欢迎使用美元转换人民币服务',
        'text': '您需要转换的美元为' + str(your_money) + '$',
        'result': '兑换成人民币为' + str(your_money * dollar) + '元'
    },
    '3': {
        'title': '3.人民币转换美元再装换欧元',
        'tips': '欢迎使用人民币转换欧元服务',
        'text': '您需要转换的人民币为' + str(your_money) + '元',
        'result': '兑换成欧元为' + str(your_money * euro) + '€'
    },
    '0': {
        'title': '0.结束程序',
        'tips': '感谢您的使用，祝您生活愉快，再见！'
    }
}
 
lst = ['1', '2', '3', '0']
 
print('**********欢迎使用货币转换服务系统**********')
 
for item in lst:
    service = service_menu[item]
    print(service['title'])
    print(service['tips'])
    if item != '0':
        print(service['text'])
        print(service['result'])
    print('==============================================')