# 定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
# TongLao类里面有2个方法see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
# fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
# 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
# 加入模块化改造
# 希望各位同学在此基础上可以添加自己的“freestyle”哦

class TongLao:  # 定义一个童姥类
    # power = 1000
    # hp=200
    def __init__(self, hp, power, dihp=10000, dipower=24):  # 定义一个init私有方法可以传入参数
        self.h = hp
        self.pow = power
        self.dh = dihp
        self.dp = dipower

    def see_people(self, name="WYZ"):  # 定义一个see_people方法设定一个name参数
        if name == "WYZ":  # 如果参数name等于”WYZ“则输出”师弟！！！“
            print("师弟！！！！")
        elif name == "LQS":
            print("贱人")
        elif name == "DCQ":
            print("叛徒，我杀了你")
        else:
            print("这是谁我不认识")

    def fight_zms(self):  # 定义一个方法fight_zms
        bigh = self.h * 10  # 设定一个变量bigh为童姥开大后hp乘十
        print("我使用天山折梅手hp乘十了：{}".format(bigh))
        bigpow = self.pow / 2  # 设定一个变量bigpow为童姥开大后攻击力除二
        print("但是我攻击力除二：{}".format(bigpow))
        if bigh - self.dp < self.dh - self.pow:  # 如果童姥hp小与敌人则为输
            print("童姥输")
        elif bigh - self.dp > self.dh - self.pow:  # 如果童姥hp大于敌人则为胜利
            print("敌人输")
        else:  # hp一样则平局
            print("平局")


class XuZhu(TongLao):  # 定义一个XuZhu类继承TongLao类
    def read(self):
        print("罪过罪过")


tl = TongLao(50, 22)

tl.see_people("WYZ")
tl.fight_zms()
xz = XuZhu(70, 22)
xz.read()
xz.read()
