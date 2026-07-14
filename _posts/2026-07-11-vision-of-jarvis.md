---
layout: post
title: "The Vision of J.A.R.V.I.S: Moving Beyond Monolithic LLMs"
date: 2026-07-11 15:00:00
description: A reflection on the architecture and philosophy behind my multi-agent orchestration project.
tags: ai multi-agent architecture
categories: research
featured: true
---

As large language models (LLMs) continue to evolve, a fundamental limitation remains: **Context Degradation and Hallucination** during complex, multi-step tasks. While a single monolithic model can write a script or summarize a document, it struggles to maintain strict logic across a sprawling codebase without drifting off-track.

This realization is what birthed my **J.A.R.V.I.S.** (Just A Rather Very Intelligent System) orchestration project. 

### Why Multi-Agent?

The human brain doesn't tackle a complex software project using a single, unified stream of consciousness. We brainstorm, we write code, we critique our own work, and we test it. If one "persona" makes a mistake, another part of our brain catches it.

J.A.R.V.I.S. replicates this by breaking down the developer workflow into distinct agent personas:
- **Friday (The Developer):** Focuses entirely on generating and refactoring code.
- **Edith (The QA Auditor):** Has no writing permissions. Its sole job is to tear down Friday's logic, look for edge cases, and run the code in a secure sandbox.

### The Power of Sandboxing

One of the hardest lessons I learned early on was that AI agents will confidently lie about whether a piece of code works. To enforce absolute truth, I integrated a Docker Sandbox (`python:3.11-slim`). When Edith evaluates Friday's code, it actually *executes* it in an isolated, network-disabled container. 

If the container throws a traceback, Edith issues a `FAIL` verdict, packages the stderr, and sends it back to Friday. This creates a **closed-loop self-correction** cycle that entirely removes human intervention until the code compiles and runs successfully.

### What's Next? (The Nunchi Engine)

Building the technical pipeline is only half the battle. The ultimate goal of J.A.R.V.I.S. isn't just to be a coding tool, but a true collaborator. I am currently researching ways to implement a **Nunchi (눈치) Engine**—a contextual layer that allows the orchestration system to read the implicit urgency and tone of the user's requests, adjusting its verbosity and execution speed accordingly.

The journey of building J.A.R.V.I.S. is just beginning, but it has completely redefined my understanding of how we will interact with software in the future.
