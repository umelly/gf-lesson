# -*- coding:utf-8 -*-

"""面向对象编程"""

class Human(object):
    
    def say(self):
        print "第一句话"
        pass

    def work(self):
        pass

    @property
    def gender(self):
        pass

class Girl(Human):
    @property
    def gender(self):
        return "female"

    def say(self):
        super(Girl, self).say()
        return "我要口红"

    def work(self):
        return "化妆"

class Boy(Human):
    @property
    def gender(self):
        return "male"

    def say(self):
        return "我要玩游戏"

    def work(self):
        return "赚钱"

boy = Boy()
girl = Girl()

print boy.say()
print girl.say()

