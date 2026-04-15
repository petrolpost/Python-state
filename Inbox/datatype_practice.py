"""
统计学 - 数据类型演示
数据类型判断在数据分析中的基础作用
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("数据类型判断练习")
print("=" * 60)

data = {
    '血液类型': ['A', 'B', 'AB', 'O', 'A', 'B'],
    '教育程度': ['本科', '硕士', '博士', '本科', '高中', '本科'],
    '考试成绩': [85, 92, 78, 88, 95, 73],
    '月薪': [15000, 25000, 35000, 18000, 45000, 12000]
}

df = pd.DataFrame(data)

print("\n数据集预览：")
print(df)

print("\n" + "=" * 60)
print("数据类型检测（pandas自动推断）")
print("=" * 60)
print(df.dtypes)

print("\n" + "=" * 60)
print("数据类型特征总结")
print("=" * 60)

for col in df.columns:
    print(f"\n【{col}】")
    print(f"  - pandas dtype: {df[col].dtype}")
    print(f"  - 唯一值数量: {df[col].nunique()}")
    print(f"  - 唯一值: {df[col].unique()}")

print("\n" + "=" * 60)
print("练习答案提示")
print("=" * 60)
print("血液类型 → 定类（Nominal）- 只有分类，无顺序")
print("教育程度 → 定序（Ordinal）- 有顺序，间距不等")
print("考试成绩 → 定距/定比（Interval/Ratio）- 取决于评分规则")
print("月薪 → 定比（Ratio）- 有绝对零点(0)，可计算比率")
