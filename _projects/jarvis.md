---
layout: page
importance: 1
title: "J.A.R.V.I.S. — Multi-Agent Orchestration Prototype"
description: An independent project prototyping an autonomous multi-agent developer pipeline using Docker container sandboxing.
img: assets/img/jarvis_canvas.png
importance: 1
category: work
related_publications: false
---

## 🧠 Overview

**J.A.R.V.I.S.** (Just A Rather Very Intelligent System) is an independent, ongoing architectural design project aimed at building an autonomous collaborator. It prototypes a multi-agent orchestration architecture to handle complex developer tasks.

---

## 1. 목적 (Purpose)

To resolve chronic limitations of current Large Language Models (LLMs)—specifically **Hallucination** (fabricating facts or executing incorrect logic) and **Context Degradation / Loss of Focus** in complex, multi-step tasks. Ultimately, the project strives to achieve end-to-end task automation to eliminate repetitive, tedious developer workflows.

## 2. 주제 (Topic)

**Autonomous Multi-Agent Orchestration Prototype.** Building a closed-loop system where multiple AI agents collaborate, generate code, execute it in a safe sandbox, and self-correct based on execution feedback.

## 3. 공학적 이론이나 방법론 (Engineering Methodology)

**Persona-based Multi-Agent Orchestration.** Instead of relying on a single monolithic model which frequently suffers from context degradation, the system assigns narrow, hyper-focused roles to specific agents. By enforcing strict boundaries, agents can collaborate and cross-verify each other's outputs efficiently.

## 4. 본인의 역할 및 기여도 (My Role & Contribution)

**Sole Architect.** Conceptualized the core orchestration pipeline and designed the prompt-based agent state machine routing.

## 5. 문제 해결 과정 및 설계 논리 (Problem-Solving Process & Design Logic)

To effectively suppress hallucinations, I designed a **Self-Correction Loop** involving two primary agents:

- **Friday (Developer Agent):** Generates and refines code implementations.
- **Edith (QA Auditor Agent):** Reviews generated code, checks for potential bugs, and issues a `PASS` or `FAIL` verdict.

When Edith issues a `FAIL` verdict, Friday must revise the code based on the specific critique without manual human intervention. To guarantee safety during this autonomous execution, I integrated a **Docker Sandbox** (`python:3.11-slim`), running scripts in an isolated, network-disabled container with strict memory limits and infinite-loop freeze gateways.

## 6. 결과물 및 성과 (Results & Achievements)

Currently in the **core architecture design and orchestration logic planning phase (WIP)**. The theoretical foundation is laid for a fully autonomous developer agent pipeline. Future directions include exploring a "Nunchi (눈치) Engine"—adapting agent communication tones based on implicit contextual cues for enhanced human-robot interaction.
