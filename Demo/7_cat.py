class Cat(object): # object 基类
    def __init__(self,name,mood,hungry,energy):#__init__ 一旦创建立刻调用
        self.name = name
        self.__mood = mood,
        self.__hungry = hungry,
        self.__energy = energy
        self.age = 1

alice = Cat('alice',100,0,100)

print(alice.name)
#print(alice.__mood) # 私有变量

