---
name: Memory Management
description: 管理AI Agent的持久记忆，包括加载长期记忆、用户档案、会话日志记录、精炼更新Persistent-Memory，以及跨会话记忆保持。每次会话开始必须先加载记忆，结束时必须执行沉淀。
version: 1.0
tags: [memory, persistence, obsidian, agent-core]
author: Grok-Statistics-Agent
---
# Memory Management Skill

## 技能概述

此Skill负责让Agent实现**跨会话持久记忆**，以Obsidian Vault作为第二大脑。避免依赖单次聊天上下文，所有关键信息（用户偏好、学习进度、已掌握知识、决策历史）都存储在Memory/文件夹中。

核心原则：

- **读取优先**：每次响应前必须先加载记忆文件。
- **写入保守**：只追加/精炼，不覆盖历史。
- **结构化**：所有输出使用Obsidian友好格式（YAML Frontmatter + wikilinks + Mermaid支持）。
- 与 **statistics_mindmap.md** 紧密联动（尤其是统计学学习时）。

## 文件夹结构（必须严格遵守）

- `Memory/`
  - `Persistent-Memory.md` ← 长期精炼记忆（摘要形式，避免过长）
  - `User-Profile.md` ← 用户背景、学习目标、偏好风格、统计学学习习惯
  - `Session-Logs/` ← 按日期命名的日志文件（如 `2026-04-14-session.md`）
  - `Memory-Index.md` ← 可选的总索引（用Dataview或手动维护）

## 工作流程（Step-by-Step）

### 阶段1：会话开始 - 加载记忆（必须最先执行）

1. 读取根目录 `CLAUDE.md`（系统规则）。
2. 读取根目录 `statistics_mindmap.md`（统计学知识地图）。
3. 读取 `Memory/Persistent-Memory.md`（如果不存在，自动初始化一个基础版本）。
4. 读取 `Memory/User-Profile.md`（如果不存在，询问用户创建或初始化模板）。
5. 读取最新 `Memory/Session-Logs/` 中的1-3个最近文件。
6. 如果涉及统计学，额外读取 `Knowledge/Statistics/Progress.md`。
7. 在响应开头报告（简洁）：
   > 已加载记忆：Persistent-Memory（最后更新日期）、User-Profile关键点、统计学地图已就绪、当前会话日志...
   >

### 阶段2：会话过程中 - 实时记忆维护

- 当用户提供新信息（偏好、目标、练习答案、理解程度）时，立即在内部标记，准备后续沉淀。
- 对于统计学学习：记录“已掌握分支”（例如描述统计-集中趋势）、练习结果、困惑点。
- 使用 [[wikilinks]] 连接到 `[[statistics_mindmap]]` 和相关知识笔记。

### 阶段3：会话结束或用户触发（“总结”“沉淀”“结束本节”“更新记忆”） - 执行沉淀

1. 生成**结构化会话总结**，包含：
   - 关键讨论点
   - 新学知识/练习结果
   - 决策或待办
   - 统计学地图更新建议（哪些主干/分支已掌握）
2. **追加到 Session-Log**：
   - 文件名：`Memory/Session-Logs/YYYY-MM-DD-session.md`
   - 使用 Frontmatter：
     ```yaml
     ---
     date: YYYY-MM-DD
     tags: [session-log, statistics]
     related: [[Persistent-Memory]]
     ---
     ```
