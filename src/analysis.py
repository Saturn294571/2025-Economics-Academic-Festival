import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import os

# [System Instruction]
# This script analyzes the impact of Fiscal Dominance on Exchange Rates using OLS.
# Model: Δln(e_t) = α + β1*Δln(G_t) + β2*Δ(r_t - r*_t) + β3*Δθ_t + ε_t

def load_and_preprocess_data(filepath):
    """
    Load data and prepare variables for regression.
    """
    if not os.path.exists(filepath):
        print(f"Error: Data file not found at {filepath}")
        return None

    df = pd.read_csv(filepath)
    
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Interpolate Fiscal Expenditure (Annual -> Monthly)
    # First, replace 0 or empty strings with NaN if any
    if 'Expenditure_Trillion' in df.columns:
        df['Expenditure_Trillion'] = df['Expenditure_Trillion'].interpolate(method='linear', limit_direction='both')
    
    # Interpolate other missing values if they are small gaps
    df = df.interpolate(method='linear', limit_direction='both')

    # Filter data from 2000 onwards (or available start)
    required_cols = ['Exchange_Rate', 'Expenditure_Trillion', 'KR_3Y_Yield', 'US_10Y_Yield', 'CDS_Premium']
    df_clean = df[required_cols].dropna()
    
    print(f"Data loaded. Valid rows after interpolation and dropping NaNs: {len(df_clean)}")
    
    # Create variables for regression
    # 1. Log Exchange Rate: ln(e)
    df_clean['ln_e'] = np.log(df_clean['Exchange_Rate'])
    
    # 2. Log Government Expenditure: ln(G)
    df_clean['ln_G'] = np.log(df_clean['Expenditure_Trillion'])
    
    # 3. Interest Rate Spread: r - r*
    df_clean['spread'] = df_clean['KR_3Y_Yield'] - df_clean['US_10Y_Yield']
    
    # 4. Risk Premium (CDS): θ (Already in bp, maybe scale it? Keep as is for now)
    df_clean['theta'] = df_clean['CDS_Premium']
    
    # Create Differences (Δ)
    df_clean['d_ln_e'] = df_clean['ln_e'].diff()
    df_clean['d_ln_G'] = df_clean['ln_G'].diff()
    df_clean['d_spread'] = df_clean['spread'].diff()
    df_clean['d_theta'] = df_clean['theta'].diff()
    
    # Drop the first row which will be NaN after differencing
    df_final = df_clean.dropna()
    
    return df_final

def run_ols_regression(df):
    """
    Run OLS Regression: Δln(e) ~ Δln(G) + Δ(r-r*) + Δθ
    """
    print("\n--- Running OLS Regression ---")
    
    # Define Dependent Variable (Y)
    Y = df['d_ln_e']
    
    # Define Independent Variables (X)
    X = df[['d_ln_G', 'd_spread', 'd_theta']]
    X = sm.add_constant(X) # Add intercept (α)
    
    # Fit Model
    model = sm.OLS(Y, X).fit()
    
    # Print Summary
    print(model.summary())
    
    return model

def plot_results(df, model):
    """
    Plot actual vs fitted values and residuals.
    """
    # Predict
    X = df[['d_ln_G', 'd_spread', 'd_theta']]
    X = sm.add_constant(X)
    df['fitted'] = model.predict(X)
    
    plt.figure(figsize=(8, 8))
    plt.scatter(df['d_ln_e'], df['fitted'], alpha=0.6, color='blue', label='Data Points')
    
    # Add 45-degree line for reference
    min_val = min(df['d_ln_e'].min(), df['fitted'].min())
    max_val = max(df['d_ln_e'].max(), df['fitted'].max())
    plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='Perfect Fit (45° Line)')
    
    plt.title('OLS Regression: Actual vs Fitted Δln(Exchange Rate)')
    plt.xlabel('Actual Δln(e)')
    plt.ylabel('Fitted Δln(e)')
    plt.legend()
    plt.grid(True)
    plt.savefig('ols_results.png')
    print("\nScatter plot saved to ols_results.png")

if __name__ == "__main__":
    DATA_PATH = "/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/merged_monthly_data.csv"
    
    print("--- Coder Agent: Starting Analysis ---")
    df = load_and_preprocess_data(DATA_PATH)
    
    if df is not None and not df.empty:
        model = run_ols_regression(df)
        plot_results(df, model)
        
        # Save summary to file for other agents
        with open("ols_summary.txt", "w") as f:
            f.write(model.summary().as_text())
        print("OLS Summary saved to ols_summary.txt")
    else:
        print("Analysis aborted due to insufficient data.")
