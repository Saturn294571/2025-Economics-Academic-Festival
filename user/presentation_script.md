# Project Cassandra: Presentation Script
## "The Paradox of 2025: Why is the Exchange Rate Soaring?"

---

### Slide 1: Title
*   **Visual:** Project Title, Team Name, Date.
*   **Script:**
    "안녕하십니까. Project Cassandra 팀입니다.
    저희는 오늘 2025년 한국 경제를 뒤흔들고 있는 기이한 현상, '수출 호조 속 환율 폭등'의 미스터리를 풀어보고자 합니다."

---

### Slide 2: System Architecture (AI Collaboration)
*   **Visual:** Diagram showing Brain (Planner), Librarian (Data), and Coder (Analyst) interacting.
*   **Script:**
    "본격적인 분석에 앞서, 저희 프로젝트의 독특한 연구 방식을 소개합니다.
    Project Cassandra는 3명의 AI 에이전트가 협업하는 '멀티 에이전트 시스템'으로 수행되었습니다.
    **Brain**은 경제 이론을 수립하고 전체 연구를 기획했습니다.
    **Librarian**은 한국은행과 미디어에서 방대한 데이터를 채굴했습니다.
    마지막으로 **Coder**는 복잡한 계량 모형을 코딩하고 검증했습니다.
    이 세 에이전트의 유기적인 협업이 이번 연구의 핵심 엔진입니다."

---

### Slide 3: Research Workflow
*   **Visual:** Flowchart (Problem Definition $\rightarrow$ Data Mining $\rightarrow$ VAR Modeling $\rightarrow$ Policy Implication).
*   **Script:**
    "연구는 다음과 같은 4단계 워크플로우로 진행되었습니다.
    먼저 '수출과 환율의 괴리'라는 문제를 정의하고,
    월별 거시경제 데이터를 정밀하게 수집 및 보간했습니다.
    이후 OLS와 VAR 모형을 통해 가설을 다각도로 검증했으며,
    최종적으로 충격 반응 분석을 통해 정책적 시사점을 도출했습니다."

---

### Slide 4: Technical Pipeline
*   **Visual:** Data Pipeline Diagram (Raw Data CSV $\rightarrow$ Python Preprocessing $\rightarrow$ VAR Analysis $\rightarrow$ Visualization).
*   **Script:**
    "기술적으로는 데이터의 수집부터 시각화까지 자동화된 파이프라인을 구축했습니다.
    공공 데이터와 미디어 텍스트가 파이썬 전처리 모듈을 거쳐 분석 가능한 형태로 변환되고,
    이것이 VAR 알고리즘에 입력되어 최종적으로 여러분이 보실 그래프로 출력됩니다.
    이 모든 과정은 데이터의 무결성을 보장하며 투명하게 처리되었습니다."

---

### Slide 5: The Paradox (서론)
*   **Visual:** 
    *   Left: Export Graph (Rising)
    *   Right: Exchange Rate Graph (Soaring to 1,470 KRW)
    *   Text: "교과서의 배신"
*   **Script:**
    "2025년 11월, 대한민국은 반도체 슈퍼사이클로 역대급 수출 실적을 기록하고 있습니다.
    경제학 교과서대로라면, 달러가 유입되니 환율은 떨어져야 정상입니다.
    하지만 현실은 정반대입니다. 원/달러 환율은 1,470원을 돌파하며 외환위기 수준의 공포를 주고 있습니다.
    도대체 왜 이런 '구조적 이탈'이 발생한 것일까요?"

---

### Slide 3: Symptoms & Diagnosis (위기의 징후)
*   **Visual:**
    *   Interest Rate Gap: US 4.0% vs KR 2.5% (1.5%p Gap)
    *   Keywords: "Fiscal Dominance", "Capital Exodus"
*   **Script:**
    "우리는 두 가지 징후에 주목했습니다.
    첫째, 한미 금리 역전이 1.5%p까지 벌어졌음에도 한국은행은 금리를 올리지 못하고 있습니다. 바로 가계부채와 경기 침체 때문입니다.
    둘째, 이로 인해 서학개미와 국민연금, 기업들마저 달러를 찾아 떠나는 '자본 대탈출(Great Exodus)'이 벌어지고 있습니다.
    저희는 이 현상의 근본 원인을 **'재정 우위(Fiscal Dominance)'**로 진단합니다."

---

### Slide 4: Theoretical Framework (이론)
*   **Visual:** Modified IS-LM-BP Model Diagram (Shift of BP Curve)
*   **Script:**
    "기존 IS-LM-BP 모형은 금리차($r-r^*$)만을 강조했습니다.
    하지만 저희는 여기에 **'국가 리스크 프리미엄($\theta$)'**을 도입했습니다.
    정부가 소비쿠폰을 뿌리며 재정을 방만하게 운영할 때, 국가 신뢰도는 추락합니다.
    이때 리스크 프리미엄($\theta$)이 급등하면, BP 곡선 자체가 좌상방으로 이동해버립니다.
    즉, 금리를 조금 올리는 것만으로는 자본 유출을 막을 수 없는 '나쁜 균형'에 빠지는 것입니다."

---

### Slide 5: Market Perception (시장의 인식)
*   **Visual:** `the_exodus_chart.png` (Bar Chart of 5 Factors)
*   **Script:**
    "시장은 무엇을 두려워하고 있을까요?
    데이터를 분석해보니, 사람들은 해외투자 확대, 트럼프 리스크, 국민연금 등을 환율 폭등의 주범으로 지목하고 있었습니다.
    이것이 시장이 느끼는 공포의 크기입니다."

---

### Slide 6: Empirical Evidence (실증 분석 결과)
*   **Visual:** `var_irf_theta_to_e.png` (Impulse Response Function)
*   **Script:**
    "그렇다면 진짜 범인은 누구일까요?
    저희가 VAR 모형으로 충격 반응 분석을 수행한 결과입니다.
    보시다시피, **리스크 프리미엄($\theta$)의 충격**이 발생하자마자 환율은 즉각적이고 폭발적으로 상승합니다.
    단순한 금리차보다, '대한민국 경제에 대한 신뢰 하락'이 환율을 밀어올리는 핵심 동력임이 입증된 것입니다."

---

### Slide 7: Conclusion (결론)
*   **Visual:** Summary Keywords (Fiscal Rule, Independence, Trust)
*   **Script:**
    "결론입니다. 2025년의 위기는 외부 충격이 아닌, 내부의 정책 실패가 만든 '신뢰의 위기'입니다.
    재정 우위로 인해 통화 정책이 무력화된 상황에서, 무분별한 돈 풀기는 독이 될 뿐입니다.
    지금 필요한 것은 소비쿠폰이 아닙니다.
    재정 준칙을 바로 세우고, 한국은행의 독립성을 회복하여 무너진 국가 신뢰($\theta$)를 다시 쌓아 올리는 것만이 유일한 해법입니다.
    감사합니다."
