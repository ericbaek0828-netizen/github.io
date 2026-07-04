---
layout: page
title: "CodingLab & KSEF — High School Research & Teaching"
description: Founded a programming club, designed a deep learning curriculum, and competed in Korea's national science & technology competition
img: assets/img/3.jpg
importance: 3
category: work
related_publications: false
---

## 🏫 Overview

Before university, I ran two parallel tracks: **independent research** and **peer education**. Both came from the same frustration — I kept finding that the structures around me (school curricula, existing clubs) weren't moving fast enough.

---

## 📝 KSEF — Korea Science & Technology Competition (2024)

### The Problem I Noticed

In early 2024, ChatGPT had just arrived and the world was celebrating. I was skeptical.

The model could produce fluent, confident-sounding text while failing basic inferential reasoning. It was **linguistically powerful but epistemically fragile** — it had no reliable way to evaluate the truth of what it was saying.

### The Proposal

I wrote a paper proposing a **Critical Thinking Framework** for LLMs — a structured scaffolding layer to force multi-perspective reasoning before committing to a response.

While developing the idea, I independently arrived at the intuition that an **adversarial training loop** would be necessary: a system where one model generates hypotheses and another challenges them, iterating until a response could survive critique. This is, in essence, what GAN-based training does — and what RLHF achieves in modern alignment research.

> I didn't have the benchmarking methodology to prove it. I won a participation award. But the problem I identified was real and the direction I pointed toward became mainstream.

### What I Learned

The gap between a correct intuition and a publishable result is **methodology and measurement**. This experience is why I now treat experimental design as a first-class engineering concern in J.A.R.V.I.S.

---

## 🏗️ CodingLab — Founding a Programming Club (2025)

### The Situation

My school's existing programming club dissolved. Rather than waiting for a teacher to restart it, I proposed to the faculty that I would found and run **CodingLab (코딩랩)** myself.

### Curriculum Design

The challenge wasn't just knowing the material — it was figuring out _how to transmit it_ to students with no prior ML background.

I drew from:

- **MIT 6.S191** (Introduction to Deep Learning)
- _Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow_
- Additional papers and lectures I had accumulated independently

I restructured these into a **deep learning theory curriculum** and delivered approximately **one semester of lectures** to club members, serving as both instructor and course designer.

### Key Insight

Teaching deep learning to beginners is a different problem from understanding it yourself. You have to find the right analogies, the right sequence, the right level of abstraction — and you only discover what works by watching where people get confused.

> Designing that curriculum made me a better engineer. If I couldn't explain a concept simply, I didn't fully understand it.

---

## 📌 Connection to Current Work

These experiences established the foundations I'm still building on:

| High School                          | University (Now)                                             |
| ------------------------------------ | ------------------------------------------------------------ |
| KSEF: LLM reasoning limits           | J.A.R.V.I.S. Nunchi algorithm (reading implicit context)     |
| KSEF: Adversarial training intuition | MCTS + Tiki-Taka (Friday ↔ Edith adversarial loop)           |
| CodingLab curriculum                 | TA role under Prof. Yang; game jam all-rounder communication |
| "I need better tools"                | Building J.A.R.V.I.S. from scratch                           |
