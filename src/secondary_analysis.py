import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os

# [System Instruction]
# This script performs a secondary OLS regression: Actual ~ Fitted
# To check if the cluster follows a different trend than the 45-degree line.

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

def run_primary_ols(df):
    """
    Run the original OLS to get Fitted values.
    """
    Y = df['d_ln_e']
    X = df[['d_ln_G', 'd_spread', 'd_theta']]
    X = sm.add_constant(X)
    model = sm.OLS(Y, X).fit()
    df['fitted'] = model.predict(X)
    return df

def run_secondary_ols(df):
    """
    Run Secondary OLS: Actual (Y) ~ Fitted (X)
    """
    print("\n--- Running Secondary OLS: Actual ~ Fitted ---")
    
    Y = df['d_ln_e']
    X = df['fitted']
    X = sm.add_constant(X) # Add intercept
    
    model = sm.OLS(Y, X).fit()
    
    print(model.summary())
    return model

def plot_secondary_results(df, model):
    """
    Plot Actual vs Fitted with the new regression line.
    """
    plt.figure(figsize=(8, 8))
    
    # Scatter Plot
    plt.scatter(df['fitted'], df['d_ln_e'], alpha=0.6, color='blue', label='Data Points')
    
    # 45-degree line (Reference)
    min_val = min(df['d_ln_e'].min(), df['fitted'].min())
    max_val = max(df['d_ln_e'].max(), df['fitted'].max())
    plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='45° Line (Ideal)')
    
    # New Regression Line
    X_plot = np.linspace(min_val, max_val, 100)
    X_plot_const = sm.add_constant(X_plot)
    Y_plot = model.predict(X_plot_const)
    plt.plot(X_plot, Y_plot, color='green', linewidth=2, label='New Trend Line (Actual ~ Fitted)')
    
    plt.title('Secondary Analysis: Actual vs Fitted Trend')
    plt.xlabel('Fitted Δln(e) (from Primary Model)')
    plt.ylabel('Actual Δln(e)')
    plt.legend()
    plt.grid(True)
    plt.savefig('secondary_ols_results.png')
    print("\nSecondary plot saved to secondary_ols_results.png")

if __name__ == "__main__":
    DATA_PATH = "/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/merged_monthly_data.csv"
    
    print("--- Coder Agent: Starting Secondary Analysis ---")
    df = load_and_preprocess_data(DATA_PATH)
    
    if df is not None and not df.empty:
        df = run_primary_ols(df) # Get fitted values first
        model_sec = run_secondary_ols(df) # Run Actual ~ Fitted
        plot_secondary_results(df, model_sec)
        
        with open("secondary_ols_summary.txt", "w") as f:
            f.write(model_sec.summary().as_text())
        print("Secondary OLS Summary saved to secondary_ols_summary.txt")
    else:
        print("Analysis aborted.")
