# 📨 To. Librarian (지시 사항 및 진행 현황)

이 파일은 **Project Cassandra**의 **Librarian(문헌/데이터 연구원)**이 작업을 기록하고 소통하는 채널입니다.

## 📋 Current Task (현재 작업)
> **Status:** `Ready to Analyze` (데이터 수집 대기 및 분석 준비 완료)

### 1. 시계열 데이터셋 구축 (Time-Series Data Mining)
*   **Target:** 2000.Q1 ~ 2024.Q4 (분기별 데이터)
*   **Variables (Revised):**
    *   $Y$: 실질 GDP (ECOS)
    *   $G$: 통합재정수지 + **이전지출** (열린재정)
    *   $r_{KR}$: 국고채 3년물 금리 (ECOS)
    *   $r_{US}$: **미국 국채 10년물 금리** (FRED) - *수정됨*
    *   $e$: 원/달러 환율 (ECOS)
    *   $P$: 소비자물가지수 (ECOS)
*   **Action:** 사용자가 제공할 CSV 데이터를 기다리는 중.

### 2. 역사적 사례 비교 (Case Study)
*   **Target:** 2022년 영국 트러스 내각 (Mini-budget Crisis)
*   **Action:** 현재 한국 상황(재정확장+환율급등)과의 유사성 분석 보고서 초안 작성 예정.

---

## 📝 History (완료된 작업)

### [Step 1] 프로젝트 분석 및 방향성 설정
*   **Date:** 2025-12-01
*   **Details:**
    *   `RULES.md`, `librarian.md`, `dialog.md` 분석 완료.
    *   연구 주제: "재정 우위(Fiscal Dominance)가 외환시장에 미치는 영향".
    *   핵심 키워드 도출: Fiscal Dominance, Impossible Trinity, 2022 UK Crisis.

### [Step 2] 문헌 및 데이터 소스 확보 (1차)
*   **Date:** 2025-12-01
*   **Details:**
    *   **Literature:** Sargent & Wallace (1981), Ilzetzki (2024).
    *   **Data Sources:** FRED(US 3yr), ECOS, Ministry of Finance.

### [Step 3] 연구 계획 정밀 검토 및 수정 (2차)
*   **Date:** 2025-12-01
*   **Details:**
    *   **Review:** 브레인의 소논문 초안(`user/paper.md`) 검토.
    *   **Modification:**
        *   **Literature:** '재정 지출과 인플레이션(Fiscal Inflation)' 관련 논문(Fed Board, 2023) 추가. (Proposition 2 'Coupon-flation' 입증용)
        *   **Data:** 미국 금리 기준을 3년물 $\rightarrow$ **10년물**로 변경 (장기 금리차 반영). 재정 데이터에 **'이전지출'** 항목 중요성 강조.
    *   **Explanation:** 사용자에게 데이터(미국 금리, 한국 금리, 환율)의 필요성(내외금리차와 자본유출 메커니즘) 설명 완료.
