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
    *   Text: "교과서의 배신: $NX \uparrow \Rightarrow e \downarrow$ ?"
*   **Script:**
    "2025년 11월, 대한민국 경제는 기이한 현상을 목격하고 있습니다.
    반도체 슈퍼사이클에 힘입어 수출은 역대 최고치를 경신하고 있습니다.
    경제학 원론에서 우리는 배웠습니다. 수출이 늘어나면 달러 공급이 증가하여 환율은 하락해야 한다고 말입니다.
    하지만 지금의 현실은 정반대입니다. 원/달러 환율은 1,470원을 돌파하며 외환위기 수준의 공포를 주고 있습니다.
    수출 호조와 환율 폭등이 공존하는 이 '구조적 이탈(Structural Divergence)', 도대체 왜 발생한 것일까요?
    저희는 이 미스터리의 해답을 교과서 밖의 현실, 바로 '정책의 실패'에서 찾았습니다."

---

### Slide 6: Symptoms & Diagnosis (위기의 징후)
*   **Visual:**
    *   Interest Rate Gap: US 4.0% vs KR 2.5% (1.5%p Gap)
    *   Keywords: "Fiscal Dominance (재정 우위)", "Capital Exodus (자본 대탈출)"
*   **Script:**
    "우리는 두 가지 결정적인 징후에 주목했습니다.
    첫째, '재정 우위(Fiscal Dominance)'입니다. 현재 한미 금리차는 1.5%p까지 벌어졌습니다.
    정상적이라면 한국은행은 금리를 올려 자본 유출을 막아야 합니다. 하지만 가계부채와 경기 침체라는 족쇄 때문에 금리를 동결할 수밖에 없는 상황입니다. 즉, 재정 정책의 부작용이 통화 정책을 무력화시킨 것입니다.
    둘째, 이로 인한 '자본 대탈출(Great Exodus)'입니다.
    금리 매력도 잃고, 국가 신뢰도 잃은 한국 시장에서 서학개미, 국민연금, 심지어 기업들마저 달러를 찾아 떠나고 있습니다. 이는 단순한 투자가 아닌, 자산 가치를 지키기 위한 '생존형 탈출'입니다."

---

### Slide 7: Theoretical Framework (이론)
*   **Visual:** Modified IS-LM-BP Model Diagram (Shift of BP Curve)
*   **Script:**
    "이 현상을 이론적으로 규명하기 위해, 저희는 기존 IS-LM-BP 모형을 수정했습니다.
    핵심은 **'국가 리스크 프리미엄($\theta$)'**의 도입입니다.
    메커니즘은 다음과 같습니다.
    1. 정부가 소비쿠폰을 발행하며 확장 재정을 펼치면 IS 곡선이 우측으로 이동합니다.
    2. 하지만 한국은행이 금리를 동결(LM 고정)하면서, 시장에는 '정부가 물가를 잡을 의지가 없다'는 시그널을 줍니다.
    3. 이는 국가 신뢰도 하락으로 이어져 리스크 프리미엄($\theta$)이 급등합니다.
    4. 결과적으로 BP 곡선 자체가 좌상방으로 강력하게 이동해버립니다.
    이제는 금리를 조금 올리는 것만으로는 균형을 회복할 수 없는, 이른바 **'나쁜 균형(Bad Equilibrium)'**에 빠지게 된 것입니다."

---

### Slide 8: Market Perception (시장의 인식)
*   **Visual:** `the_exodus_chart.png` (Bar Chart of 5 Factors)
*   **Script:**
    "그렇다면 시장 참여자들은 무엇을 가장 두려워하고 있을까요?
    저희가 미디어와 시장 데이터를 분석해본 결과, '환율 붕괴 5적'이 도출되었습니다.
    가장 큰 요인은 '해외투자 확대'와 '트럼프 리스크'였습니다.
    특히 국민연금의 해외 투자 확대와 기업들의 달러 보유 성향(Lagging)은, 한국 경제의 펀더멘털에 대한 불신이 얼마나 심각한지를 보여주는 지표입니다.
    시장은 이미 한국 원화보다 달러를 더 신뢰하고 있는 것입니다."

---

### Slide 9: Empirical Evidence (실증 분석 결과)
*   **Visual:** `var_irf_theta_to_e.png` (Impulse Response Function)
*   **Script:**
    "이제 우리의 가설을 데이터로 검증해 보겠습니다.
    저희는 VAR(벡터 자기회귀) 모형을 구축하고, **충격 반응 분석(Impulse Response Analysis)**을 수행했습니다.
    이 그래프는 '리스크 프리미엄($\theta$)'에 충격이 가해졌을 때 환율($e$)이 어떻게 반응하는지를 보여줍니다.
    보시다시피, 리스크 충격 직후 환율은 **즉각적이고 폭발적으로 상승**하며, 그 효과는 장기간 지속됩니다.
    반면, 단순한 재정 지출 자체는 환율에 유의미한 영향을 주지 못했습니다.
    즉, 돈을 썼다는 사실보다, 그로 인해 **'국가 신뢰가 무너졌다'**는 사실이 환율 폭등의 진짜 주범임이 입증된 것입니다."

---

### Slide 10: Conclusion (결론)
*   **Visual:** Summary Keywords (Fiscal Rule, Independence, Trust)
*   **Script:**
    "결론입니다. 2025년의 위기는 외부 충격이 아닌, 내부의 정책 실패가 자초한 **'신뢰의 위기'**입니다.
    재정 우위로 인해 통화 정책의 독립성이 훼손된 상황에서, 섣부른 부양책은 독이 될 뿐입니다.
    저희 Project Cassandra 팀은 다음의 세 가지를 제언합니다.
    첫째, **재정 준칙(Fiscal Rule)**을 법제화하여 무분별한 포퓰리즘 지출을 통제해야 합니다.
    둘째, **중앙은행의 독립성**을 회복하여, 물가 안정을 위한 금리 정상화를 추진해야 합니다.
    셋째, 노동·연금 개혁을 통해 잠재성장률을 높여, 무너진 **국가 신뢰($\theta$)**를 다시 쌓아 올려야 합니다.
    신뢰를 잃은 화폐에 미래는 없습니다.
    경청해 주셔서 감사합니다."
