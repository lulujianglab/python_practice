while True:
    print("*********欢迎使用转换器***********")
    print("T 温度转换")
    print("L 长度转换")
    print("C 货币转换")

    type = input("请选择转换器：")

    # 温度转换
    if type == "T":
        temperature = input("请输入温度(示例：1C或2F)：")
        if temperature[-1] == "C":
            temperature = temperature[0:-1]
            temperatureC = float(temperature)
            temperatureF = (9/5) * temperatureC+32
            print("华氏温度为：%.2fF" % temperatureF)
        elif temperature[-1] == "F":
            temperature = temperature[0:-1]
            temperatureF = float(temperature)
            temperatureC = (temperatureF - 32) / (9 / 5)
            print("摄氏温度为：%.2fC" % temperatureC)

    # 长度转换
    elif type == "L":
        length = input("请输入长度(示例：1in或2cm)：")
        if length[-1] == "n":
            length = length[0:-2]
            lengthIN = float(length)
            lengthCM = lengthIN * 30.48
            print("厘米为：%.2fcm" % lengthCM)
        elif length[-1] == "m":
            length = length[0:-2]
            lengthCM = float(length)
            lengthIN = lengthCM / 30.48
            print("英尺为：%.2fin" % lengthIN)

    # 货币转换
    elif type == "C":
        money = input("请输入多少钱(示例：1￥或2$)：")
        if money[-1] == "$":
            money = money[0:-1]
            moneyM = float(money)
            moneyR = moneyM * 6.8724
            print("人民币为：%.2f元" % moneyR)
        elif money[-1] == "￥":
            money = money[0:-1]
            moneyR = float(money)
            moneyM = moneyR / 6.8724
            print("美元为：%.2f美元" % moneyM)
