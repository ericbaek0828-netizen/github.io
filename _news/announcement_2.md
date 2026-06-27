---
layout: post
title: AI Agent Framework, Multi-Agent & PKM
date: 2026-06-27 19:06:00 +0900
description: J.a.r.v.i.s. is back to the game!
inline: false
related_posts: true
---

I am excited to share my current plans for Build **J.A.R.V.I.S.** and my study tracks in AI agents, reinforcement learning, and knowledge systems. This roadmap outlines my main milestones.
I spent 3 days to make this Framework in My Obsidian Vault

<img src="/github.io/assets/img/jarvis_architecture.png" style="width: 100%; max-width: 800px; display: block; margin: 20px auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />

#### Overview
The diagram above illustrates the core cognitive and decision-making architecture of **J.A.R.V.I.S.** I envision. It is organized into three main conceptual sections:

1. **7 Layers**
   * **Layer 1~7:** Ambient Awareness, Proactive Engine, World Model, Personality & EQ, Long-Term Memory, Tool Forge, Social Interface
2. **Bi-directional Communication**
   * Rather than a fixed, one-way flow, each layer and tier is organically interconnected through real-time feedback loops for exchanging goals, commands, and action results. 
3. **MCTS & Decision-Making Pipeline (Execution Pipeline)**
   * The right side of the diagram depicts the pipeline for resolving complex tasks. It follows a structured process: **Decomposition -> Deliberation -> MCTS (Tree Search) -> Verification**, ensuring optimal action selection through iterative refinement.

---

### 1. J.A.R.V.I.S. Core (Multi-Agent Orchestration)
* **Goal:** Build a robust orchestration layer capable of coordinating specialized sub-agents with high correctness.
* **Key Tasks:**
  * Implement **MCTS (Monte Carlo Tree Search)** for complex problem decomposition and path planning.
  * Implement self-correcting prompt.

### 2. Reinforcement Learning & Investing
* **Goal:** Apply RL models to dynamic environments
* **Key Tasks:**
  * Design trading envi for RL agent training.

### 3. Personal Knowledge Management (PKM)
* **Goal:** Build an auto-linking local knowledge graph to manage research references and coding logs.
* **Key Tasks:**
  * Create a local Markdown parser to discover semantic connections between research notes.
  * Build a graph visualization dashboard for active study tracks.

---
#### Preferences
1. Oh my ClaudeCode(Harness Engineering)
2. RSI Lab
3. Hermes Agent
4. Jarvis Wikipedia
5. Dwarkesh Patel Youtube( Richard Sutton, Dario Amodei)
6. [The Equation That Beat Wall Street](https://www.youtube.com/watch?v=A5w-dEgIU1M)
etc.