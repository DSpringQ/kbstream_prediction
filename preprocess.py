#coding=utf-8
import sys, os
import json

dataset_path = os.path.join(os.path.abspath('.'), 'data', 'dataset')
shopinfo_path = os.path.join(dataset_path, 'shop_info.txt')
userpay_path = os.path.join(dataset_path, 'user_pay.txt')
sta_path = os.path.join(dataset_path, 'pay.json')

dic = {}
cities_dic = {}
cate1_dic = {}
cate2_dic = {}
cate3_dic = {}

def get_shopinfos():
    with open(shopinfo_path) as f:
        for line in f:
            line_sp = line.rstrip().split(',')
            dic[line_sp[0]] = {}
            if line_sp[1] not in cities_dic:
                cities_dic[line_sp[1]] = 0
            cities_dic[line_sp[1]] += 1
            if line_sp[7] not in cate1_dic:
                cate1_dic[line_sp[7]] = 0
            cate1_dic[line_sp[7]] += 1
            if line_sp[8] not in cate2_dic:
                cate2_dic[line_sp[8]] = 0
            cate2_dic[line_sp[8]] += 1
            if line_sp[9] not in cate3_dic:
                cate3_dic[line_sp[9]] = 0
            cate3_dic[line_sp[9]] += 1
    print "number of cities:", len(cities_dic)
    print "types of cate1", len(cate1_dic)
    print "types of cate2", len(cate2_dic)
    print "types of cate3", len(cate3_dic)

def save_userpay_info():
    total_userpay_num = 69674110
    i = 0
    with open(userpay_path) as f:
        for line in f:
            i += 1
            if i%100000 == 0:
                print i, '-->>', total_userpay_num
            now_shop = line.rstrip().split(',')[1]
            now_date = line.rstrip().split(',')[2].split()[0]
            if now_date not in dic[now_shop]:
                dic[now_shop][now_date] = 0
            dic[now_shop][now_date] += 1

    with open(sta_path, 'w') as f:
        json.dump(dic, f)

def get_userpay_info(shop, date=""):
    with open(sta_path) as f:
        dic = json.load(f)
        if date == "":
            print "Deal numbers of shop {} are:".format(shop)
            for k, v in dic[shop].iteritems():
                print k, v
        else:
            print "Deal number of shop {} on day {} is {}.".format(shop, date, dic[shop][date])
        return dic[shop]

def visualize_dealnumbers_for_one_shop(shop):
    dic = get_userpay_info(shop)
    sorted_dic_list = sorted(dic.iteritems(), key=lambda x:x[0])
    dates = []
    deal_nums = []
    for date, deal_num in sorted_dic_list:
        dates.append(date)
        deal_nums.append(deal_num)
    print dates
    print deal_nums
    from matplotlib import pyplot as plt
    from matplotlib.dates import MonthLocator,DateFormatter
    import datetime

    fig, ax = plt.subplots()
    ax.plot_date(dates, deal_nums, '-')

    # format the ticks
    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%Y%m'))
    ax.autoscale_view()

    # format the coords message box
    def price(x):
        return  x
    ax.fmt_xdata = DateFormatter(u'%Y-%m-%d')
    ax.fmt_ydata = price
    ax.grid(True)

    fig.autofmt_xdate()
    plt.show()

    # pyplot.plot(range(len(deal_nums)), deal_nums)
    # # pyplot.xticks(range(len(deal_nums)), dates, rotation=45)
    # pyplot.show()

visualize_dealnumbers_for_one_shop('344')