from abc import abstractmethod


# 动物园类要求有“名字”属性和“添加动物”的方法
# “添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能
class Zoo(object):
    def __init__(self, name):
        self.name = name

    def add_animal(self, obj):
        # class_name = obj.__class__.__name__
        if hasattr(self, obj.__class__.__name__):
            if obj in self.obj.__class__.__name__:
                print('该动物已存在')
            else:
                self.obj.__class__.__name__[obj] = obj
                print('该动物已添加成功')
        else:
            setattr(self, obj.__class__.__name__, {obj: obj})
            print('该动物已添加成功')


# 动物类不允许被实例化
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性
# 是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”
class Animal(Zoo):
    size = {
        '小': 1,
        '中': 2,
        '大': 3,
    }
    is_meat = {
        '食肉': True,
        '食草': False,
        '杂食': False,
    }
    character = {
        '凶猛': True,
        '温顺': False,
    }

    @abstractmethod
    def __init__(self, size, is_meat, character):
        self.size = Animal.size[size]
        self.body = Animal.is_meat[is_meat]
        self.character = Animal.character[character]

        # 判断是否为凶猛动物
        if self.size >= 2 and self.is_meat == True and self.character == True:
            self.is_fierce = True
        else:
            self.is_fierce = False


# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性
# 其中“叫声”作为类属性，猫类继承自动物类
class Cat(Animal):
    def __init__(self, name, is_meat, size, character):
        super().__init__(size, is_meat, character)
        self.meow = "喵"
        self.name = name
        # 适合作为宠物
        self.is_pet = 'Y'


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(have_cat)
    # 再添加一次查看是否报错
    z.add_animal(cat1)
    have_cat = getattr(z, 'Cat')
    print(have_cat)


