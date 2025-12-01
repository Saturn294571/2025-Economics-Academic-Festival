import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt
import os

# [System Instruction]
# This script performs VAR (Vector Autoregression) Analysis.
# Variables: Δln(e), Δln(G), Δ(r-r*), Δθ

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
    
    # Create Differences (Δ)
    df_clean['d_ln_e'] = df_clean['ln_e'].diff()
    df_clean['d_ln_G'] = df_clean['ln_G'].diff()
    df_clean['d_spread'] = df_clean['spread'].diff()
    df_clean['d_theta'] = df_clean['theta'].diff()
    
    return df_clean.dropna()

def run_var_analysis(df):
    """
    Run VAR Model.
    """
    print("\n--- Running VAR Analysis ---")
    
    # Select variables for the system
    # Order matters for Cholesky decomposition in IRF, but for basic VAR estimation it's symmetric.
    # Let's put policy variables first, then market variables.
    # G -> Spread -> Theta -> Exchange Rate (Hypothesized ordering)
    data = df[['d_ln_G', 'd_spread', 'd_theta', 'd_ln_e']]
    
    model = VAR(data)
    
    # Select optimal lag order based on AIC
    lag_order_results = model.select_order(maxlags=10)
    print(lag_order_results.summary())
    
    optimal_lag = lag_order_results.aic
    print(f"\nSelected Lag Order (AIC): {optimal_lag}")
    
    # Fit model
    results = model.fit(optimal_lag)
    print(results.summary())
    
    return results

def plot_irf(results):
    """
    Plot Impulse Response Functions.
    """
    irf = results.irf(10) # 10 periods
    
    plt.figure(figsize=(10, 10))
    irf.plot(orth=True, impulse='d_theta', response='d_ln_e')
    plt.title('Impulse Response: Shock to Risk Premium (θ) -> Exchange Rate (e)')
    plt.grid(True)
    plt.savefig('var_irf_theta_to_e.png')
    print("\nIRF plot saved to var_irf_theta_to_e.png")
    
    # Also plot G -> e
    plt.figure(figsize=(10, 10))
    irf.plot(orth=True, impulse='d_ln_G', response='d_ln_e')
    plt.title('Impulse Response: Shock to Gov Expenditure (G) -> Exchange Rate (e)')
    plt.grid(True)
    plt.savefig('var_irf_G_to_e.png')
    print("IRF plot saved to var_irf_G_to_e.png")

def plot_time_series(df):
    """
    Plot time series of the differenced variables used in VAR.
    """
    plt.figure(figsize=(12, 10))
    
    variables = ['d_ln_e', 'd_ln_G', 'd_spread', 'd_theta']
    titles = ['Exchange Rate Change (Δln e)', 'Gov Expenditure Change (Δln G)', 
              'Interest Rate Spread Change (Δ(r-r*))', 'Risk Premium Change (Δθ)']
    colors = ['blue', 'green', 'orange', 'red']
    
    for i, (var, title, color) in enumerate(zip(variables, titles, colors)):
        plt.subplot(4, 1, i+1)
        plt.plot(df.index, df[var], label=var, color=color, linewidth=1.5)
        plt.title(title)
        plt.legend(loc='upper right')
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('var_time_series.png')
    print("\nTime series plot saved to var_time_series.png")

if __name__ == "__main__":
    DATA_PATH = "/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/merged_monthly_data.csv"
    
    print("--- Coder Agent: Starting VAR Analysis ---")
    df = load_and_preprocess_data(DATA_PATH)
    
    if df is not None and not df.empty:
        plot_time_series(df) # Plot time series first
        results = run_var_analysis(df)
        plot_irf(results)
        
        with open("var_summary.txt", "w") as f:
            f.write(str(results.summary()))
        print("VAR Summary saved to var_summary.txt")
    else:
        print("Analysis aborted.")
