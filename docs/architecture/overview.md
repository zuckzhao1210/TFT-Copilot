# TFT Agent OS - System Overview

## 目标
构建一个能够：
- 读取游戏画面
- 理解局势
- 做出决策
- 执行操作
- 自我进化

的 Agent 系统

---

## 系统结构

Perception → State → LLM → Action → Feedback → Memory → Evolution

---

## 模块划分

1. Perception（视觉识别）
2. State Representation（状态建模）
3. LLM Decision（决策）
4. Action Execution（操作）
5. Memory（记忆）
6. Evolution（自我优化）

---

## 核心难点

- 状态压缩（视觉 → token）
- 决策稳定性
- 长期记忆
- 自我训练闭环

## ideas