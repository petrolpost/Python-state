"""
统计学 - 整理与展示演示
频数表、直方图、箱线图、散点图
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("整理与展示 - Python 演示")
print("=" * 60)

np.random.seed(42)
scores = np.random.normal(loc=75, scale=12, size=100)
scores = np.clip(scores, 50, 98).astype(int)

incomes = np.random.lognormal(mean=10.5, sigma=0.5, size=200)
male_heights = np.random.normal(loc=175, scale=6, size=50)
female_heights = np.random.normal(loc=162, scale=5, size=50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

freq_data = pd.cut(scores, bins=[0, 60, 70, 80, 90, 100],
                   labels=['0-59', '60-69', '70-79', '80-89', '90-100'])
freq_table = freq_data.value_counts().sort_index()
freq_table.plot(kind='bar', ax=axes[0, 0], color='steelblue', edgecolor='black')
axes[0, 0].set_title('练习1答案: 成绩频数分布')
axes[0, 0].set_xlabel('分数段')
axes[0, 0].set_ylabel('人数')
for i, v in enumerate(freq_table):
    axes[0, 0].text(i, v + 0.5, str(v), ha='center')

axes[0, 1].hist(scores, bins=15, color='steelblue', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('直方图: 成绩分布（连续视角）')
axes[0, 1].set_xlabel('分数')
axes[0, 1].set_ylabel('人数')
axes[0, 1].axvline(scores.mean(), color='red', linestyle='--', label=f'均值={scores.mean():.1f}')
axes[0, 1].legend()

bp = axes[1, 0].boxplot([scores], patch_artist=True)
bp['boxes'][0].set_facecolor('lightblue')
axes[1, 0].set_title('箱线图: 成绩5数概括')
axes[1, 0].set_ylabel('分数')
q1, median, q3 = np.percentile(scores, [25, 50, 75])
axes[1, 0].text(1.15, q1, f'Q1={q1:.1f}')
axes[1, 0].text(1.15, median, f'中位数={median:.1f}')
axes[1, 0].text(1.15, q3, f'Q3={q3:.1f}')

axes[1, 1].scatter(incomes, np.random.normal(0, 0.1, len(incomes)) + 1,
                   alpha=0.5, s=20, c='steelblue')
axes[1, 1].set_title('散点图: 收入分布（实际应用场景）')
axes[1, 1].set_xlabel('月收入（元）')
axes[1, 1].set_ylabel('')
axes[1, 1].set_yticks([])

plt.tight_layout()
plt.savefig('e:/workspaces/self/Python-state/Inbox/data_display_demo.png',
            dpi=150, bbox_inches='tight')
print("图表已保存到 Inbox/data_display_demo.png")

print("\n" + "=" * 60)
print("练习答案提示")
print("=" * 60)
print("练习1: 总人数=100, 各组频率=3%,5%,6%,4%,2% (频数)")
print("练习2: 分布基本对称（均值≈中位数）")
print("练习3: Q4→直方图或箱线图, Q5→分组箱线图或条形图")
