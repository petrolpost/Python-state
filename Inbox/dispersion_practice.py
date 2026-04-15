"""
统计学 - 离散程度演示
方差、标准差、极差、IQR
"""

import numpy as np
import pandas as pd

print("=" * 60)
print("离散程度指标 - Python 演示")
print("=" * 60)

data1 = np.array([2, 4, 6])
data2 = np.array([1, 3, 5, 7, 9])
data3 = np.array([1, 2, 3, 4, 5, 6, 7, 100])

print("\n数据集对比：")
print(f"data1 = {data1} (紧凑)")
print(f"data2 = {data2} (中等)")
print(f"data3 = {data1} (有极端值)")

print("\n" + "=" * 60)
print("极差 (Range)")
print("=" * 60)
for name, d in [("data1", data1), ("data2", data2), ("data3", data3)]:
    r = np.ptp(d)
    print(f"{name}: 极差 = {r}")

print("\n" + "=" * 60)
print("IQR (四分位距)")
print("=" * 60)
for name, d in [("data1", data1), ("data2", data2), ("data3", data3)]:
    q1, q3 = np.percentile(d, [25, 75])
    iqr = q3 - q1
    print(f"{name}: Q1={q1}, Q3={q3}, IQR={iqr}")

print("\n" + "=" * 60)
print("方差与标准差")
print("=" * 60)
for name, d in [("data1", data1), ("data2", data2), ("data3", data3)]:
    var = np.var(d, ddof=0)
    std = np.std(d, ddof=0)
    print(f"{name}: 方差={var:.4f}, 标准差={std:.4f}")

print("\n" + "=" * 60)
print("对比结论")
print("=" * 60)
print("data1 和 data2 均值都是4，但离散程度不同")
print("标准差越大，数据越分散")
