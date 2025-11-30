# 📨 To. Coder (지시 사항 및 진행 현황)

이 파일은 **Project Cassandra**의 **Coder(계량경제학자)**가 작업을 기록하고 소통하는 채널입니다.

## 📋 Current Task (현재 작업)
> **Status:** `Ready to Code` (분석 파이프라인 설계 및 데이터 대기 중)

### 1. 계량 분석 파이프라인 구축 (Econometric Pipeline)
*   **Target:** `src/analysis.py` (예정)
*   **Methodology:**
    *   **OLS Regression:** $\ln(e_t) = \beta_0 + \beta_1 \ln(G_t) + \beta_2 (r_t - r^*_t) + \beta_3 \ln(Y_t) + \epsilon_t$
    *   **VAR Model:** 충격반응함수(Impulse Response Function) 도출.
*   **Action:** Librarian이 제공할 데이터셋(.csv) 대기 중. 데이터 입수 즉시 단위근 검정(ADF) 및 회귀분석 수행 예정.

### 2. IS-LM-BP 시각화 (Visualization)
*   **Target:** `src/visualization.py` (예정)
*   **Goal:** 재정 우위(Fiscal Dominance) 상황에서의 균형 이동 시각화.
    *   **IS Curve:** 우측 이동 (확장 재정)
    *   **LM Curve:** 고정 (금리 동결)
    *   **BP Curve:** 하방 위치 (자본 유출 압력)
*   **Action:** `matplotlib`를 활용한 정적/동적 그래프 코드 설계.

---

## 📝 History (완료된 작업)

### [Step 1] 목표 설정 및 역할 파악
*   **Date:** 2025-12-01
*   **Details:**
    *   `RULES.md`, `coder.md`, `user/paper.md` 분석 완료.
    *   핵심 임무 정의: "재정 우위가 환율에 미치는 영향"을 통계적으로 입증.
    *   분석 방법론 확정: OLS 및 VAR 모형 활용.
