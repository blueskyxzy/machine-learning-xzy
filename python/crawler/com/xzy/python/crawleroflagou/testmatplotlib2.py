#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

d = [1, 2, 6, 5, 4, 8, 4, 2, 4]
print(type(d))
plt.hist(d)
plt.xlabel(u'工资 (千元)')
plt.ylabel(u'频数')
plt.title(u"工资直方图")
plt.savefig('image/test.jpg')
plt.show()
