---
layout: page
title: "J.A.R.V.I.S. — Multi-Agent Orchestration Prototype"
description: An independent project prototyping an autonomous multi-agent developer pipeline using Docker container sandboxing.
img: assets/img/jarvis_canvas.png
importance: 1
category: work
related_publications: false
---

## 🧠 Project Overview

**J.A.R.V.I.S.** (Just A Rather Very Intelligent System) is an independent development project where I prototype a multi-agent orchestration architecture. The goal is to build an autonomous collaborator that can break down tasks, generate code, execute it in a safe sandbox, and self-correct based on execution feedback.

---

## 🏛️ System Architecture

The core pipeline operates as a closed-loop multi-agent workflow:

```
[User Goal]
     ↓
[Harley (PM) — Task Decomposition & PRD]
     ↓
Loop (Self-Correction):
  [Friday (Generator) — Code Implementation]
     ↓
  [Docker Sandbox — Execution & Test Run]
     ↓
  [Edith (QA Auditor) — Code Review & Verdict]
     ↓ (FAIL -> Retry with critique | PASS -> Ship)
[Final Output]
```

### Agent Roles

- **Harley (Product Manager):** Decomposes user goals into actionable sub-tasks and defines the criteria for completion.
- **Friday (Developer Agent):** Generates and refines code implementations based on the requirements.
- **Edith (QA Auditor):** Reviews generated code, checks for potential bugs, and issues a `PASS` or `FAIL` verdict.

### Key Engineering Elements

- **Automated Self-Correction Loop:** Friday and Edith engage in a direct critique-correction cycle. If Edith finds an issue, Friday revises the code using the feedback without requiring manual human intervention.
- **Docker Sandboxing:** To safely execute generated code during testing, the runtime runs scripts in an isolated, network-disabled Docker container (`python:3.11-slim` with memory limits).
- **Execution Safeguards:** Implemented an Infinite Loop Freeze Gateway that pauses the process and serializes the sprint state if the same execution error repeats consecutively, preventing infinite execution loops.

---

## 🛠️ Technical Stack

- **Runtime:** Node.js (TypeScript) + Jarvis CLI
- **Agent Integration:** Prompt-based agent state machine routing
- **Sandbox Environment:** Docker API client for container management
- **Development Tooling:** Obsidian for personal knowledge management and architecture planning

---

## 💡 Future Directions: Social Context Modeling

In addition to the core code execution pipeline, I am interested in exploring how AI agents can interact more naturally with humans. I have conceptualized a **Nunchi (눈치) Engine**—a theoretical model designed to adapt agent communication tones based on implicit contextual cues (such as dry/short messaging patterns or response latency).

During the 2026 Department Game Jam, I had the opportunity to present a high-level abstraction of this context-weighting idea (incorporating HRI/non-verbal signals) to Department Head Prof. Seong-jun Park, discussing its theoretical application in human-robot interaction.
