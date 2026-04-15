"""
统计学 - 形状指标演示
偏度、峰度
"""

import numpy as np
from scipy import stats

print("=" * 60)
print("形状指标 - Python 演示")
print("=" * 60)

np.random.seed(42)

left_skewed = np.random.exponential(scale=2, size=1000)
right_skewed = -np.random.exponential(scale=2, size=1000) + 10
symmetric = np.random.normal(loc=5, scale=1, size=1000)

normal_dist = np.random.normal(loc=5, scale=1, size=1000)
leptokurtic = np.random.normal(loc=5, scale=0.5, size=1000)
platykurtic = np.random.normal(loc=5, scale=2, size=1000)

print("\n" + "=" * 60)
print("偏度 (Skewness)")
print("=" * 60)

for name, data in [("左偏分布", left_skewed),
                    ("右偏分布", right_skewed),
                    ("对称分布", symmetric)]:
    skew = stats.skew(data)
    mean = np.mean(data)
    median = np.median(data)
    print(f"\n{name}:")
    print(f"  均值 = {mean:.2f}, 中位数 = {median:.2f}")
    print(f"  偏度 = {skew:.2f} ({'偏左' if skew < 0 else '偏右' if skew > 0 else '对称'})")

print("\n" + "=" * 60)
print("峰度 (Kurtosis)")
print("=" * 60)

for name, data in [("尖峰分布", leptokurtic),
                    ("正态分布", normal_dist),
                    ("平峰分布", platykurtic)]:
    kurtosis = stats.kurtosis(data)
    print(f"{name}: 峰度 = {kurtosis:.2f}")

print("\n" + "=" * 60)
print("手算练习验证")
print("=" * 60)

data1 = np.array([1, 2, 3, 4, 5, 10])
data2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for name, data in [("数据集A", data1), ("数据集B", data2)]:
    print(f"\n{name}: {data}")
    print(f"  均值={np.mean(data):.2f}, 中位数={np.median(data):.2f}")
    print(f"  偏度={stats.skew(data):.2f}")
