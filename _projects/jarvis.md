---
layout: page
importance: 1
title: "J.A.R.V.I.S. — Multi-Agent Orchestration Prototype"
description: An independent project prototyping an autonomous multi-agent developer pipeline using Docker container sandboxing.
img: assets/img/jarvis_canvas.png
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

## 6. 트러블슈팅 (Troubleshooting)

**문제: Docker 샌드박스 내부의 무한 루프 에러와 I/O 블로킹**
에이전트가 코드를 작성하고 컨테이너에서 실행할 때, 에이전트가 실수로 `while True:` 같은 무한 루프를 만들거나 `input()` 함수를 사용하면 전체 파이프라인이 정지하는 문제가 발생했습니다.

**해결:** 
1. 컨테이너 실행 명령어에 `--memory`와 `--cpus` 제한을 두어 시스템 과부하를 방지했습니다.
2. 실행 시 `timeout` 명령어를 래핑하여 10초 이상 실행 시 프로세스를 강제 종료(SIGKILL)하도록 타임아웃 메커니즘을 구현했습니다.
3. 파이썬 스크립트 실행 전, AST 파서를 통해 `input()` 함수의 사용을 감지하고 차단하는 정적 분석 단계를 추가했습니다.

## 7. 결과물 및 배운 점 (Results & Lessons Learned)

현재 J.A.R.V.I.S.는 **핵심 아키텍처 설계와 오케스트레이션 로직 구현의 초기 단계(WIP)**에 있습니다. 단일 LLM에 모든 문맥을 밀어넣는 기존 방식에서 벗어나, 역할을 쪼개고 검증 샌드박스를 도입하는 것이 오류율을 획기적으로 낮출 수 있다는 점을 실증하고 있습니다.

이 프로젝트를 통해 단순히 프롬프트를 잘 쓰는 법이 아니라, AI를 하나의 컴포넌트로 다루는 **시스템 엔지니어링** 역량을 크게 키울 수 있었습니다. 향후 방향성은 암묵적 맥락을 파악하는 "눈치(Nunchi) 엔진"을 도입하여 인간과 로봇 간의 상호작용 경험을 한 차원 높이는 것입니다.
