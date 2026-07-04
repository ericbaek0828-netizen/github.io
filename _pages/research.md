---
layout: page
title: research
permalink: /research/
description: My research interests and ongoing directions.
nav: true
nav_order: 2
---

## Research Interests

My work sits at the intersection of **multi-agent AI systems** and **human-AI interaction**. I'm interested in building agents that don't just process language — they read context, infer intent, and respond with social awareness.

---

### 🤖 Multi-Agent Orchestration

How do you coordinate multiple specialized AI agents to solve complex tasks with high correctness? My primary vehicle for this question is [**J.A.R.V.I.S.**](/projects/1_jarvis/), which implements:

- **MCTS-based planning** for task decomposition before execution
- **Tiki-Taka loops** (Friday ↔ Edith) for adversarial code generation and critique
- **Infinite-loop detection** with state serialization for graceful failure handling
- **Docker sandbox execution** for safe, isolated code runs

The key insight: orchestration is not just about routing messages between agents. It's about designing the *decision architecture* — when to escalate, when to retry, when to stop.

---

### 👁️ Nunchi (눈치) — Social Context Modeling

Named after the Korean concept of "reading the room," the Nunchi algorithm is J.A.R.V.I.S.'s social perception layer. Most AI responds to *what you say*. Nunchi is designed to respond to *what the situation means*.

Current focus areas:

- **Implicit feedback loops**: Inferring user state (energy, mood, engagement) from behavioral patterns rather than explicit ratings
- **Humor weight filtering**: Deciding response tone (serious, playful, ironic) based on aggregated social signals
- **Sub-linguistic signal processing**: Micro-expressions, involuntary eye contact patterns, and other signals humans can't consciously suppress

This is an active research direction with **Prof. Seong-jun Park** (Department Head, Sungkyul University), who has proposed a formal collaboration on applying this model to human-robot interaction.

---

### 🧠 Reinforcement Learning

I'm exploring RL as a decision-making framework beyond games:

- Agent training in dynamic, adversarial environments
- Reward shaping for multi-objective optimization
- Applications to financial decision-making and resource allocation

---

### 📚 Personal Knowledge Management (PKM)

How do you build systems that help researchers manage, connect, and retrieve knowledge at scale?

- Auto-linking knowledge graphs from local Markdown notes
- Semantic connection discovery across research references
- Integration with AI agents for context-aware information retrieval

---

## Research Philosophy

> A clear instinct isn't enough. You need the tools to test it.

I learned this the hard way at KSEF in 2024 — I identified a real problem (LLM reasoning fragility) and pointed in the right direction (adversarial training), but lacked the benchmarking methodology to prove it. That gap between intuition and evidence is what I'm closing now.

Every system I build is designed to be **testable, measurable, and falsifiable**. If I can't set up an experiment to prove myself wrong, I don't trust the result.
