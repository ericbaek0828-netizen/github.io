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

During high school, I focused on learning the mathematical and structural foundations of Machine Learning and Deep Learning. I applied this knowledge in two primary ways: establishing a student programming club to teach my peers, and conducting an independent research project for the Korea Science & Engineering Fair (KSEF) to explore LLM reasoning limitations.

---

## 📚 CodingLab: Student Programming Club (2024)

### Background

When our school's previous programming club dissolved, I stepped up to re-establish the group as **CodingLab (코딩랩)**. I wanted to create an environment where members could study deep learning theory beyond basic syntax.

### Curriculum Design & Instruction

As the lead instructor, I designed a semester-long curriculum covering the foundations of neural networks. I prepared lecture slides (80+ pages) and taught topics including:

- **Perceptrons:** Synaptic weights, biases, activation functions (Sigmoid, Tanh, ReLU), cost functions (BCE, MSE), and SGD.
- **CNN (Convolutional Neural Networks):** Convolution operations, kernel/filter sliding, pooling (Max/Average pooling), and dimensional reduction to prevent overfitting.
- **RNN (Recurrent Neural Networks):** Sequence data handling, hidden states, vanishing/exploding gradient problems, LSTM/GRU gated cell architectures, and Attention mechanisms.

The curriculum materials were adapted from **MIT 6.S191** (Introduction to Deep Learning) and standard ML textbooks, translated into accessible language for peers with no prior deep learning background.

---

## 📝 KSEF 2024: Research on LLM Reasonings

### Research Topic

- **Title:** 비판적 사고의 적용을 통한 LLM의 언어 이해 능력 개선 방안 (Improving LLM Language Understanding through the Application of Critical Thinking)
- **Conference:** 22nd Korea Science & Engineering Fair (KSEF 2024)
- **Result:** Awarded Participation Prize (장려상)

### Problem Statement

Large Language Models (LLMs) demonstrate high fluency in natural language generation but frequently suffer from **hallucinations** and logic failures in complex reasoning tasks. I hypothesized that LLMs generate incorrect answers because they predict tokens sequentially without a step-by-step verification process. I proposed a method that mimics human critical thinking—specifically, generating multiple hypotheses and verifying them before generating the final response.

### Implementation Details

- **Dataset (merged-v2):** I curated and cleaned a custom Korean dataset comprising text analysis (50%), logical reasoning (25%), and problem-solving (25%). The dataset was structured in a JSON dictionary format containing instructions, inputs, and outputs.
- **Fine-Tuning:** I fine-tuned a **LLaMA 3.2 3B** model on Google Colab using **Unsloth** for training optimization and **LoRA** (Rank 16, Alpha 16) with 4-bit quantization.
- **Training Config:** Used the AdamW 8-bit optimizer, cosine learning rate scheduler (max LR 2e-4, 5% warm-up), weight decay of 0.01, and gradient accumulation steps set to 4 to optimize memory usage under VRAM constraints.
- **Inference Pipeline:** Modified the text generation process. Instead of immediate token prediction, the model was prompted to generate several potential hypotheses, verify the correctness of each hypothesis using context data, select the most logically sound one, and then formulate the final output.

### Evaluation & Results

I evaluated both the baseline LLaMA 3.2 3B model and my fine-tuned "Critical Thinking" model against a set of complex reasoning prompts (evaluating language suitability, reasoning capability, and requirement fulfillment).

- **Baseline LLaMA 3.2 3B Score:** 0.466 / 1.000
- **Critical Thinking LLM Score:** 0.566 / 1.000

The experiment demonstrated that integrating a hypothesis-generation and verification pipeline could improve reasoning performance and help suppress hallucinated outputs.
