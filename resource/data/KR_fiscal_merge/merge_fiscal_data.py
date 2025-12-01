import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 파일 경로 설정
expenditure_path = '/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/성질별지출추이_20251201213534.csv'
execution_path = '/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/성질별집행추이_20251201212108.csv'
output_path = '/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/KR_Fiscal_Transfer_15-24.csv'

# 1. 데이터 로드
df_exp = pd.read_csv(expenditure_path) # 지출 (2015-2023)
df_exe = pd.read_csv(execution_path)   # 집행 (2015-2024)

# 2. '이전지출' 관련 항목만 필터링 및 합산 함수
def aggregate_transfers(df, value_col, year_col='회계연도'):
    # 이전지출에 해당하는 항목들 (보전금, 민간이전, 자치단체이전, 해외이전, 출연금 등)
    # 데이터마다 명칭이 조금씩 다를 수 있으므로 '지출성질목명'에 '이전'이나 '출연'이 포함된 것을 기준으로 함
    # 혹은 파일 내용을 기반으로 명시적 필터링
    
    # 지출추이 파일의 경우: '이전지출' 대분류가 명확함 (코드 300)
    if '지출목성질코드' in df.columns:
        mask = df['지출목성질코드'] == 300
    # 집행추이 파일의 경우: '지출성질목명'이 '이전지출'인 경우
    elif '지출성질목명' in df.columns:
        mask = df['지출성질목명'] == '이전지출'
    else:
        return None
        
    df_filtered = df[mask].copy()
    
    # 연도별 합계 계산
    # 지출금액(조원) -> 억 원 단위로 통일 필요 (지출추이는 조원, 집행추이는 억원)
    if value_col == '지출금액(조원)':
        df_filtered['amount_100m'] = df_filtered[value_col] * 10000 # 조원 -> 억원
    elif value_col == '집행합계금액(억원)':
        # 콤마 제거 및 숫자 변환
        df_filtered['amount_100m'] = df_filtered[value_col].astype(str).str.replace(',', '').astype(float)
    
    return df_filtered.groupby(year_col)['amount_100m'].sum().reset_index()

# 3. 연도별 합계 데이터 생성
agg_exp = aggregate_transfers(df_exp, '지출금액(조원)')
agg_exe = aggregate_transfers(df_exe, '집행합계금액(억원)')

# 컬럼명 변경
agg_exp.columns = ['Year', 'Expenditure']
agg_exe.columns = ['Year', 'Execution']

# 4. 데이터 병합 (2015-2023 교집합)
merged = pd.merge(agg_exp, agg_exe, on='Year', how='inner')

# 5. 회귀분석을 통한 보정 계수 산출 (Expenditure = alpha + beta * Execution)
X = merged[['Execution']]
y = merged['Expenditure']

model = LinearRegression()
model.fit(X, y)

r_squared = model.score(X, y)
print(f"R-squared: {r_squared:.4f}")
print(f"Coefficient: {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")

# 6. 2024년 데이터 예측 (보정)
exe_2024 = agg_exe[agg_exe['Year'] == 2024]['Execution'].values[0]
pred_exp_2024 = model.predict([[exe_2024]])[0]

# 7. 최종 데이터셋 생성
final_data = agg_exp.copy()
new_row = pd.DataFrame({'Year': [2024], 'Expenditure': [pred_exp_2024]})
final_data = pd.concat([final_data, new_row], ignore_index=True)

# 단위 환산 (억원 -> 조원) 다시 복구? 아니면 억원 유지? 
# 분석의 편의를 위해 '조원' 단위로 저장 (기존 지출추이 파일 기준)
final_data['Expenditure_Trillion'] = final_data['Expenditure'] / 10000

# 8. CSV 저장
final_data[['Year', 'Expenditure_Trillion']].to_csv(output_path, index=False)

print(f"Successfully created {output_path}")
print(final_data)
