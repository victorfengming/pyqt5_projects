#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 1606030113

class MyList(list):
    name = "字符串列表"

    # 重写父类insert方法
    def insert(self, index, obj):
        self.check_type(obj)
        super().insert(index,obj)

    # 重写父类的append方法
    def append(self, obj):
        print("重构方法被调用")
        self.check_type(obj)
        super().append(obj)

    # 定义检查类型成员方法
    def check_type(self,obj):

        if str(obj) == obj:
            # 如果类型为字符串,返回真
            return True
        else:
            # 如果类型不正确,抛出异常,终止程序
            raise Exception("参数类型错误")

    # 定义输出成员方法
    def out_content(self):
        for i in self:
            print(i)


# 实例化对象
ml = MyList()

# 这行程序执行会报错
# ml.append(12)
ml.append("2312")
ml.append("1sdfgh2")
ml.append("12asfdh")

# 调用对象的成员方法,打印全部内容
ml.out_content()