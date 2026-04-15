---
title: Description Statistics
date: 2026-04-15
version: 1.0
author: Grok-Statistics-Agent
tags: [统计学, 描述统计]
related: [[statistics_mindmap]], [[Progress]]
level: basic
status: learning
---

# 描述统计

## 模块定位

- 知识地图位置：主干1 -> 描述统计
- 目标：学会把原始数据整理、概括并可视化表达

## 当前学习状态

- 子模块“数据类型”：已完成验证演练，待正式教学
- 子模块“整理与展示”：未开始
- 子模块“总结指标”：未开始

## 后续沉淀约定

- 每次学习后追加“概念解释 / 例子 / 练习答案 / Python 验证 / 小结”。
- 完成子模块后同步更新 `[[Progress]]`。

## 数据类型：验证演练记录

> [!note]
> 本节用于验证“启动 -> 教学片段 -> 沉淀写入”闭环是否可执行，不代表该子模块已正式完成。

### 概念解释

- 定性数据：描述类别或属性，值本身不表示数量大小，如性别、城市、职业。
- 定量数据：表示数量，可进行算术运算，如身高、体重、月收入。

### 场景例子

- 用户所在城市、职业属于定性数据。
- 用户年龄、订单金额属于定量数据。

### 练习题与答案

- 题目：将“性别、身高、城市、月收入”划分为定性数据和定量数据。
- 答案：
  - 定性数据：性别、城市
  - 定量数据：身高、月收入

### Python 验证

```python
features = {
    "gender": "categorical",
    "height_cm": "numerical",
    "city": "categorical",
    "monthly_income": "numerical",
}

for name, kind in features.items():
    print(f"{name}: {kind}")
```

### 小结

- 数据类型判断是描述统计的起点。
- 后续正式教学仍需补完整的误判场景、练习反馈和可视化衔接。
