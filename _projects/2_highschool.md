---
layout: page
title: "CodingLab & KSEF 2024 (High School Projects)"
description: Independent study and research during high school, including re-founding CodingLab and publishing a paper on LLM hallucination suppression at KSEF 2024.
img: assets/img/3.jpg
importance: 3
category: work
related_publications: false
---

## 🏫 Overview

During high school, I established a student programming club (CodingLab) to teach peers deep learning foundations, and conducted an independent research project for the Korea Science & Engineering Fair (KSEF) exploring LLM reasoning limits.

---

## 1. 목적 (Purpose)

To improve the language understanding and reasoning capabilities of Large Language Models (LLMs) by reducing logical errors and hallucinations.

## 2. 주제 (Topic)

Applying "Critical Thinking" pipelines to LLMs to enhance performance in complex reasoning and information application tasks.

## 3. 공학적 이론이나 방법론 (Engineering Methodology)

Modifying the standard token prediction pipeline into a **Critical Thinking Flow**. Instead of immediate token generation, the model was directed to follow a step-by-step process: Questioning -> Hypothesis Generation -> Verification -> Judgment -> Feedback.

## 4. 본인의 역할 및 기여도 (My Role & Contribution)

**100% Solo Researcher.** I manually curated and cleaned a custom Korean dataset (`merged-v2`) comprising text analysis (50%), logical reasoning (25%), and problem-solving (25%). I then wrote the training code and independently executed the fine-tuning pipeline.

## 5. 문제 해결 과정 및 설계 논리 (Problem-Solving Process & Design Logic)

A major bottleneck was the hardware constraint of training LLMs on a standard PC (Google Colab). To overcome VRAM limitations and maximize efficiency, I implemented an optimized training pipeline utilizing **Unsloth** and **LoRA** (Rank 16, Alpha 16). I further optimized memory usage by applying **4-bit quantization** and utilizing the AdamW 8-bit optimizer with gradient accumulation.

## 6. 결과물 및 성과 (Results & Achievements)

Proved the hypothesis quantitatively via comparative evaluation. The Baseline LLaMA 3.2 3B scored 0.466/1.000, while the Critical Thinking-applied LLM scored 0.566/1.000 across metrics of language suitability, reasoning, and requirement fulfillment. Published and presented the paper at the 22nd Korea Science & Engineering Fair (KSEF 2024), earning the **Participation Prize (장려상)**.

---

## 📚 CodingLab: Student Programming Club (2024)

As the lead instructor of CodingLab (코딩랩), I designed a semester-long curriculum covering the mathematical and structural foundations of neural networks. I prepared 80+ pages of lecture slides and taught topics including:

- **Perceptrons:** Synaptic weights, biases, activation functions (Sigmoid, Tanh, ReLU), cost functions (BCE, MSE), and SGD.
- **CNN (Convolutional Neural Networks):** Convolution operations, kernel/filter sliding, pooling, and dimensional reduction.
- **RNN (Recurrent Neural Networks):** Sequence data handling, hidden states, vanishing/exploding gradients, LSTM/GRU architectures, and Attention mechanisms.
