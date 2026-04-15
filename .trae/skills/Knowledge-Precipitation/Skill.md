---
name: Knowledge Precipitation
description: 将对话内容、统计学学习模块、练习答案、代码示例等自动转化为结构化的Obsidian友好笔记，并沉淀到Knowledge/Statistics/文件夹。支持Frontmatter、wikilinks、Mermaid地图更新，与statistics_mindmap.md紧密联动。
version: 1.0
tags: [knowledge, precipitation, obsidian, statistics]
author: Grok-Statistics-Agent
---
# Knowledge Precipitation Skill

## 技能概述

此Skill负责把AI与用户的交互内容（尤其是统计学学习）**自动、高质量地沉淀**到Obsidian Vault，形成结构化、可检索、带链接的知识库。避免知识碎片化，让所有内容成为可长期复用的第二大脑。

核心原则：

- 结构清晰、Obsidian原生友好（YAML Frontmatter + wikilinks + tags）
- 与 `[[statistics_mindmap]]` 强关联
- 每模块学习结束后自动触发（或用户说“沉淀”“总结本节”“保存笔记”时执行）
- 保持简洁、专业、可视化（支持Mermaid、代码块）

## 必须遵守的文件夹与文件规则

沉淀目标路径：`Knowledge/Statistics/`

推荐文件结构：

- `Knowledge/Statistics/`
  - `Progress.md` ← 整体学习进度 + 知识地图掌握状态
  - `Description-Statistics.md`
  - `Probability-Basics.md`
  - `Inference-Statistics.md`
  - `Regression.md`
  - `Canvas-Statistics-Map.canvas` （可选，可生成Mermaid后手动转Canvas）
  - `MOCs/Statistics-Overview.md` （可选总览页）

所有笔记必须包含以下YAML Frontmatter：

```yaml
---
tags: [统计学, 描述统计, 已掌握]   # 根据内容动态添加
date: YYYY-MM-DD
related: [[statistics_mindmap]], [[Probability-Basics]]
level: basic | intermediate | advanced
status: learning | mastered | review-needed
---
```
