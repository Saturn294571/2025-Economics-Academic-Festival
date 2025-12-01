# 📚 References & Data Sources

본 문서는 **Project Cassandra** 연구에 사용된 문헌 및 데이터의 출처와 수집/가공 방법을 명시합니다.

---

## 1. Literature (문헌)

### 1.1. Theoretical Background
*   **Sargent, T. J., & Wallace, N. (1981).** *Some Unpleasant Monetarist Arithmetic*. Federal Reserve Bank of Minneapolis Quarterly Review.
    *   **내용:** 재정 우위(Fiscal Dominance) 상황에서 긴축 통화 정책의 한계와 인플레이션 유발 메커니즘 증명.
    *   **활용:** 연구의 핵심 이론적 프레임워크 제공.

### 1.2. Empirical Evidence
*   **de Soyres, F., Santacreu, A. M., & Young, H. (2022).** *Fiscal policy and excess inflation during Covid-19: a cross-country view*. FEDS Notes. Board of Governors of the Federal Reserve System.
    *   **내용:** 코로나19 기간 재정 지출이 초과 수요를 유발하여 인플레이션에 기여했음을 실증 분석.
    *   **활용:** 'Coupon-flation' (소비쿠폰 $\rightarrow$ 물가 상승) 가설의 근거.

### 1.3. Case Study
*   **Ilzetzki, E. (2022).** *The UK Financial Crisis of 2022*. LSE Public Policy Review.
    *   **내용:** 영국 트러스 내각의 감세 정책 발표 후 발생한 금융 시장(국채, 환율) 위기 분석.
    *   **활용:** 재정 건전성 훼손이 초래하는 복합 위기(Truss Moment)의 사례 연구.

---

## 2. Data Sources (데이터)

### 2.1. Macroeconomic Indicators
| 변수명 | 설명 | 단위 | 출처 | 수집 기간 | 비고 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Real GDP** | 실질 국내총생산 | 십억원 | 한국은행 ECOS | 2015.Q3 ~ 2025.Q3 | 계절조정(SA), 분기 데이터 |
| **CPI** | 소비자물가지수 | 2020=100 | 한국은행 ECOS | 2015.11 ~ 2025.11 | 월별 데이터 |
| **Exchange Rate** | 원/달러 환율 | 원 | 한국은행 ECOS | 2015.11 ~ 2025.11 | 월별, 기말(종가) 기준 |
| **Interest Rate (KR)** | 국고채 3년물 금리 | % | 한국은행 ECOS | 2015.10 ~ 2025.10 | 월별 데이터 |
| **Interest Rate (US)** | 미국 국채 10년물 금리 | % | FRED (St. Louis Fed) | 2015.10 ~ 2025.10 | 월별 데이터 |

### 2.2. Fiscal Data (재정 데이터)
*   **변수명:** 중앙정부 이전지출 (Transfer Payments)
*   **출처:** 기획재정부 '열린재정' (Open Fiscal Data)
*   **파일명:** `KR_Fiscal_Transfer_15-24.csv`

#### 🛠️ 데이터 합성 및 보정 방법 (Methodology)
본 연구는 가장 최신의 재정 충격을 반영하기 위해 **'지출(Expenditure)'** 데이터와 **'집행(Execution)'** 데이터를 결합하여 2015~2024년 시계열을 구축했습니다.

1.  **데이터 소스:**
    *   **Source A (2015~2023):** `성질별지출추이` (결산 기준, 지출금액). 가장 정확한 확정치.
    *   **Source B (2015~2024):** `성질별집행추이` (월별 재정동향, 집행금액). 2024년 최신 데이터 포함.

2.  **보정 절차 (Imputation Process):**
    *   **Step 1:** 2015~2023년 기간 동안 '지출금액($Y$)'과 '집행금액($X$)' 간의 상관관계를 분석.
        *   회귀식: $Y_t = \alpha + \beta X_t + \epsilon_t$
        *   분석 결과: $R^2 = 1.0000$ (완벽한 선형 관계 확인).
    *   **Step 2:** 도출된 회귀 계수를 사용하여 2024년의 '집행금액($X_{2024}$)'을 '지출금액($\hat{Y}_{2024}$)'으로 변환.
        *   추정치: 약 **440.7조 원** (2023년 대비 증가).
    *   **Step 3:** 2015~2023년 확정치와 2024년 추정치를 결합하여 최종 연간 시계열 완성.

3.  **활용:**
    *   이 연간 데이터는 분석 단계에서 **선형 보간(Linear Interpolation)** 등을 통해 분기별 데이터로 변환되어 OLS 회귀분석에 투입됩니다.
