import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os

# [System Instruction]
# This script performs Heteroscedasticity Test.
# Plot: Fitted Values (X) vs Residuals (Y)

def load_and_preprocess_data(filepath):
    """
    Load data and prepare variables (Same as analysis.py).
    """
    if not os.path.exists(filepath):
        print(f"Error: Data file not found at {filepath}")
        return None

    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    if 'Expenditure_Trillion' in df.columns:
        df['Expenditure_Trillion'] = df['Expenditure_Trillion'].interpolate(method='linear', limit_direction='both')
    df = df.interpolate(method='linear', limit_direction='both')

    required_cols = ['Exchange_Rate', 'Expenditure_Trillion', 'KR_3Y_Yield', 'US_10Y_Yield', 'CDS_Premium']
    df_clean = df[required_cols].dropna()
    
    df_clean['ln_e'] = np.log(df_clean['Exchange_Rate'])
    df_clean['ln_G'] = np.log(df_clean['Expenditure_Trillion'])
    df_clean['spread'] = df_clean['KR_3Y_Yield'] - df_clean['US_10Y_Yield']
    df_clean['theta'] = df_clean['CDS_Premium']
    
    df_clean['d_ln_e'] = df_clean['ln_e'].diff()
    df_clean['d_ln_G'] = df_clean['ln_G'].diff()
    df_clean['d_spread'] = df_clean['spread'].diff()
    df_clean['d_theta'] = df_clean['theta'].diff()
    
    return df_clean.dropna()

def run_ols_and_get_residuals(df):
    """
    Run OLS and calculate residuals.
    """
    Y = df['d_ln_e']
    X = df[['d_ln_G', 'd_spread', 'd_theta']]
    X = sm.add_constant(X)
    model = sm.OLS(Y, X).fit()
    
    df['fitted'] = model.predict(X)
    df['residual'] = model.resid
    
    return df

def plot_residuals(df):
    """
    Plot Fitted Values vs Residuals to check for Heteroscedasticity.
    """
    plt.figure(figsize=(10, 6))
    
    plt.scatter(df['fitted'], df['residual'], alpha=0.6, color='purple')
    plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
    
    plt.title('Heteroscedasticity Check: Fitted Values vs Residuals')
    plt.xlabel('Fitted Values (Predicted Δln(e))')
    plt.ylabel('Residuals (Error)')
    plt.grid(True, alpha=0.3)
    
    plt.savefig('heteroscedasticity_check.png')
    print("\nResidual plot saved to heteroscedasticity_check.png")

if __name__ == "__main__":
    DATA_PATH = "/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/merged_monthly_data.csv"
    
    print("--- Coder Agent: Starting Heteroscedasticity Check ---")
    df = load_and_preprocess_data(DATA_PATH)
    
    if df is not None and not df.empty:
        df = run_ols_and_get_residuals(df)
        plot_residuals(df)
    else:
        print("Analysis aborted.")
