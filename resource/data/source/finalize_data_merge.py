import pandas as pd
import os
import numpy as np

base_path = '/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data'

def load_ecos_wide(path, value_name):
    """Loads ECOS style wide csv and converts to long format (Date, Value)"""
    try:
        # Read first few lines to find header
        with open(path, 'r') as f:
            lines = f.readlines()
        
        # ECOS usually has dates in the first row (or similar)
        # We'll try to read with header=0
        df = pd.read_csv(path)
        
        # Identify date columns (contain '/')
        date_cols = [c for c in df.columns if '/' in c]
        
        if not date_cols:
            # Maybe the header is on a different line?
            # Let's try reading without header and finding the row with dates
            pass
            
        # Melt
        # We assume the first row of data (index 0) contains the values we want
        # or we sum them? Usually there's one row of interest.
        # Let's take the last row if there are multiple, or the first?
        # Usually ECOS downloads have one item per file if filtered.
        # Let's assume the first data row is the one.
        
        # Extract dates and values
        row_idx = 0 # Data usually starts at row 0 of the dataframe (line 2 of csv)
        
        # Check if there are multiple rows. If so, we might need to be careful.
        # For this project, we usually downloaded specific single indicators.
        
        long_data = []
        for col in date_cols:
            val = df.iloc[row_idx][col]
            # Clean value
            if isinstance(val, str):
                val = val.replace(',', '')
            try:
                val = float(val)
            except:
                val = np.nan
            
            long_data.append({'Date': col, value_name: val})
            
        return pd.DataFrame(long_data)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return pd.DataFrame()

def standardize_date(df, freq='M'):
    """Converts ECOS date format to datetime"""
    if df.empty:
        return df
    
    # 2015/Q3 -> 2015-09-30 (Q)
    # 2015/11 -> 2015-11-01 (M)
    
    dates = df['Date'].astype(str)
    new_dates = []
    for d in dates:
        d = d.strip()
        if '/Q' in d: # Quarterly
            y, q = d.split('/Q')
            # End of quarter
            month = int(q) * 3
            # Last day of month... simple approximation: 1st of next month minus 1 day, or just 1st of that month
            # Let's use PeriodIndex
            new_dates.append(pd.Period(f"{y}Q{q}", freq='Q').to_timestamp(how='end'))
        elif '/' in d: # Monthly 2015/11
            y, m = d.split('/')
            new_dates.append(pd.Timestamp(f"{y}-{m}-01"))
        elif '-' in d: # Already YYYY-MM-DD
            new_dates.append(pd.Timestamp(d))
        else:
            new_dates.append(pd.NaT)
            
    df['Date'] = new_dates
    return df

# --- 1. Quarterly Data ---
print("Processing Quarterly Data...")

# GDP (Wide)
df_gdp = load_ecos_wide(os.path.join(base_path, 'KR_GDP_153-253Q.csv'), 'Real_GDP')
df_gdp = standardize_date(df_gdp, 'Q')

# IIP (Long, already processed)
df_iip = pd.read_csv(os.path.join(base_path, 'KR_IIP_Securities_15-24.csv'))
# IIP Date is 2015/Q3 format
df_iip = standardize_date(df_iip, 'Q')

# Merge
# Outer join to keep all dates
df_quarterly = pd.merge(df_gdp, df_iip, on='Date', how='outer')
df_quarterly = df_quarterly.sort_values('Date')

# Save
q_path = os.path.join(base_path, 'merged_quarterly_data.csv')
df_quarterly.to_csv(q_path, index=False)
print(f"Saved {q_path}")


# --- 2. Monthly Data ---
print("Processing Monthly Data...")

# Exchange Rate (Wide)
df_er = load_ecos_wide(os.path.join(base_path, 'EX_rate_1510-2510m.csv'), 'Exchange_Rate')
df_er = standardize_date(df_er, 'M')

# CPI (Wide)
df_cpi = load_ecos_wide(os.path.join(base_path, 'KR_CPI_1510-2510m.csv'), 'CPI')
df_cpi = standardize_date(df_cpi, 'M')

# KR Treasury (Wide)
df_kr_bond = load_ecos_wide(os.path.join(base_path, 'KR_TS_rate_1510-2510m.csv'), 'KR_3Y_Yield')
df_kr_bond = standardize_date(df_kr_bond, 'M')

# US Treasury (Long)
df_us_bond = pd.read_csv(os.path.join(base_path, 'US_TS_rate_1510-2510m.csv'))
df_us_bond.rename(columns={'observation_date': 'Date', 'GS10': 'US_10Y_Yield'}, inplace=True)
df_us_bond['Date'] = pd.to_datetime(df_us_bond['Date'])

# Fiscal (Annual? Check structure)
df_fiscal = pd.read_csv(os.path.join(base_path, 'KR_Fiscal_Transfer_15-24.csv'))
if 'Year' in df_fiscal.columns:
    # Convert Year to Date (End of year or Start? Let's use Start for now, or Coder will handle)
    # Actually, if it's annual total, maybe we should just keep it as annual.
    # But to merge with monthly, we need a Date.
    df_fiscal['Date'] = pd.to_datetime(df_fiscal['Year'].astype(str) + '-01-01')
    # We might want to rename the value column to be clear
    # df_fiscal.rename(columns={'Expenditure_Trillion': 'Fiscal_Expenditure'}, inplace=True)
else:
    # Assume Date exists
    df_fiscal['Date'] = pd.to_datetime(df_fiscal['Date'])
# Rename columns if needed. Assuming 'Expenditure' is the column.
# Let's check column names if possible, but assuming standard from previous steps.

# CDS (Long)
df_cds = pd.read_csv(os.path.join(base_path, 'KR_CDS_Premium_15-24.csv'))
df_cds['Date'] = pd.to_datetime(df_cds['Date'])

# Merge all Monthly
dfs = [df_er, df_cpi, df_kr_bond, df_us_bond, df_fiscal, df_cds]
df_monthly = dfs[0]
for df in dfs[1:]:
    df_monthly = pd.merge(df_monthly, df, on='Date', how='outer')

df_monthly = df_monthly.sort_values('Date')

# Save
m_path = os.path.join(base_path, 'merged_monthly_data.csv')
df_monthly.to_csv(m_path, index=False)
print(f"Saved {m_path}")

print("Sample Quarterly:")
print(df_quarterly.tail())
print("Sample Monthly:")
print(df_monthly.tail())
