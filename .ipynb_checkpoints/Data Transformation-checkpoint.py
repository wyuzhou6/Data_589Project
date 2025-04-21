# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 09:44:47 2025

@author: Wyuzh
"""

import pandas as pd

# 读取原始 Tab 分隔的文件
df = pd.read_csv("0014081-250402121839773.csv", delimiter="\t")

# 保存为标准的逗号分隔 CSV 文件
df.to_csv("dataset.csv", index=False)