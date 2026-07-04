---
layout: page
title: "CodingLab & KSEF — High School Research & Teaching"
description: Re-founded a programming club, delivered a deep learning curriculum using teacher training materials, and competed in Korea's national science & technology competition
img: assets/img/3.jpg
importance: 3
category: work
related_publications: false
---

## 🏫 Overview

Before university, I ran two parallel tracks: **independent research** and **peer education**. Both came from the same frustration — I kept finding that the structures around me (school curricula, existing clubs) weren't moving fast enough.

---

## 📝 KSEF — 제22회 한국과학기술경진대회 (2024)

### 문제 정의 (The Problem)

2024년, ChatGPT의 등장으로 전 세계가 열광하던 시기, 저는 지역 모델(Llama 등)과 온디바이스 AI를 실험하며 LLM의 한계에 주목했습니다. 모델은 유창하고 자신감 있게 텍스트를 생성했지만, 기본적인 추론 능력과 사실 검증에서는 취약했습니다. 즉, **언어적 능력(Fluency)은 뛰어나지만 논리적 검증(Epistemic verification) 능력은 부족**했습니다.

저는 이러한 LLM의 유창한 거짓말(환각)을 비판적 사고가 거세된 현대의 **'지적 소마(Soma)'**로 인식했습니다. 이를 해결하기 위해서는 단순한 프롬프트 엔지니어링을 넘어, 인간의 비판적 의심을 알고리즘에 강제 주입해야 한다고 판단했습니다.

### 연구 및 구현 (Research & Implementation)

단순한 철학적 지적을 넘어, 이 문제의식을 **수학적 아키텍처(가설 생성-검증 레이어)로 번역**하는 연구를 진행했습니다.

- **가설 생성 파이프라인**: 기존 LLM이 프롬프트를 임베딩하고 1차원적으로 다음 단어를 예측하는 흐름을 인위적으로 끊어냈습니다. 대신 `컨텍스트 분석 → 가능한 논리적 가설 모두 생성 → 각 가설 검증 → 가장 타당한 가설 선택 → 최종 응답 생성`의 비판적 사고(Critical Thinking) 프레임워크를 설계했습니다.
- **선행성 및 하네스 엔지니어링 (Harness Engineering)**: 이 프레임워크는 LLM의 환각을 통제하기 위한 초기 아키텍처 시도로서, 최근 AI 학계와 산업계에서 유행하게 된 **'하네스 엔지니어링(Harness Engineering)'** 개념과 완벽히 동일한 문제의식을 공유합니다. 가설 생성-검증 레이어를 삽입하여 모델이 스스로의 추론을 방어하도록 강제하는 접근법은 이후 LLM 신뢰성 연구의 중요한 방향성이 되었습니다.
- **데이터셋 및 파인튜닝**: 텍스트 분석(50%), 논리적 추론(25%), 문제 해결(25%)로 구성된 **독자적인 한국어 데이터셋(merged-v2)**을 구축하고 Hugging Face에 공개했습니다. 이를 바탕으로 Google Colab 환경에서 Unsloth와 LoRA(rank 16, alpha 16, 4-bit 양자화)를 활용해 **Llama 3.2 3B 모델을 파인튜닝**했습니다.
- **결과**: 비판적 사고가 적용된 모델은 언어 이해, 추론, 요구사항 충족 지표에서 베이스라인 모델(0.466) 대비 **21% 향상된 0.566의 점수를 기록**했습니다.

### 성과 및 한계 (What I Learned)

본 연구로 장려상을 수상하며, 직관적인 아이디어를 학술적 가치로 입증하기 위해서는 **엄밀한 수학적 벤치마킹과 방법론**이 필수적임을 깊이 깨달았습니다. 당시에는 이를 증명할 방법론적 지식이 부족했으나, 이 경험은 현재 J.A.R.V.I.S. 프로젝트에서 실험 설계와 검증(QA)을 최우선 엔지니어링 과제로 삼는 강력한 동기가 되었습니다.

---

## 🏗️ CodingLab — Re-founding a Programming Club (2024)

### The Situation

I stepped up to lead our school's existing programming club. Recognizing the need for deeper technical engagement, I proposed to the faculty that we evolve it into **CodingLab (코딩랩)** with a more structured curriculum.

### Curriculum Design

The challenge wasn't just knowing the material — it was figuring out _how to transmit it_ to students with no prior ML background.

I drew from:

- Existing **Teacher Training Presentations (교원 연수 자료)**
- **MIT 6.S191** (Introduction to Deep Learning) for supplementary reading
- _Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow_

I utilized these materials to deliver a **deep learning theory curriculum**, conducting approximately **one semester of lectures** for club members.

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
