class Cat:  # 定义一个类Cat
    heigh = 10  # 身高为10cm
    weight = 100  # 体重一百斤
    temper = "暴躁"  # 脾气暴躁

    def __fight(self):  # 定义一个私有方法fight
        print("猫天天打架")
        self._Cat__sleep()  # 调用私有方法sleep

    def __sleep(self):  # 定义一个私有方法sleep
        print("猫天天睡觉")


cat = Cat()  # 实例化类
cat._Cat__fight()  # 调用私有方法fight
cat._Cat__sleep()  # 调用私有方法slepp
