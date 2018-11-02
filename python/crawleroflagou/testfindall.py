#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', 'CABA', 'dog', 'cat'])
print(type(s.str.findall("A")))
print(s.str.findall("A"))

d = pd.Series(['3-5年', '1-3年', '5-10年', '1-3年', '不限', '不限', '5-10年', '3-5年', '1-3年'])
pattern = '\d+'
# pattern = "\d+\.?\d*" 可以匹配小数点的正则
ds = d.str.findall(pattern)
print(type(ds))
print(ds)
print(type(ds[1]))
print(ds[1])

