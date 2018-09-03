# 取得每月平均值 以集合的形式返回
def per_mon_avg():
    with open("btc_price.txt", "r",encoding="utf-8") as f:

        lists = f.readlines()
        per_mon = {"01":0,"02":0,"03":0,"04":0}
        per_mon_count = {"01":0,"02":0,"03":0,"04":0}
        i = 0
        for L in lists:
            L = L.split(" ")
            t = L[0].split("-")
            per_mon[t[1]] += float(L[-1]) # 取得每月总价格
            per_mon_count[t[1]] += 1 # 月次数累计
        for S in per_mon:
            per_mon[S] = per_mon[S] / per_mon_count[S] # 月平均值
        return per_mon


per_mon_map = per_mon_avg()

# 由低到高排序
sort_by_month_price = sorted(per_mon_map.values())

# 转换为字典表
revers_per_mon_map = dict()
for mon in per_mon_map:
    revers_per_mon_map[per_mon_map[mon]] = mon

# 将字典表存入文件并输出
for i in sort_by_month_price:
    print("%s月  %s"%(revers_per_mon_map[i],i))
    file = "%s月  %s"%(revers_per_mon_map[i],i)

    with open("btc_price_season1.txt","a") as f:
        f.write(file)
        f.write("\n")