#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import matplotlib

# mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# # # plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  #（此条可能只适用于mac）
# mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

zhfont1 = matplotlib.font_manager.FontProperties(fname='/Users/xzy/Downloads/simhei.ttf')

d = [1, 2, 6, 5, 4, 8, 4, 2, 4]
print(type(d))
plt.hist(d)
plt.xlabel(u'工资 (千元)', fontproperties=zhfont1)
plt.ylabel(u'频数', fontproperties=zhfont1)
plt.title(u"工资直方图", fontproperties=zhfont1)
plt.savefig('image/test.jpg')
plt.show()
