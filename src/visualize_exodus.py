import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# [System Instruction]
# This script visualizes 'The Exodus' (Market Perception of Exchange Rate Crisis Factors).
# Data Source: resource/data/exodus_factors.csv (Derived from Market Narrative/Video)

def plot_exodus_factors(filepath):
    """
    Create a Bar Chart for 'The Exodus' factors.
    """
    if not os.path.exists(filepath):
        print(f"Error: Data file not found at {filepath}")
        return

    df = pd.read_csv(filepath)
    
    # Sort by Amount for better visualization
    df = df.sort_values('Amount_USD_Billion', ascending=False)
    
    plt.figure(figsize=(12, 8))
    
    # Create Bar Plot
    sns.set_style("whitegrid")
    ax = sns.barplot(x='Category', y='Amount_USD_Billion', data=df, palette='Reds_r')
    
    # Add Value Labels on top of bars
    for p in ax.patches:
        ax.annotate(f'${int(p.get_height())}B', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=12, fontweight='bold')
    
    plt.title("Market Perception: The 5 Suspects of Exchange Rate Crisis ('The Exodus')", fontsize=16, pad=20)
    plt.ylabel("Estimated Amount (USD Billion)", fontsize=12)
    plt.xlabel("Factors", fontsize=12)
    plt.xticks(rotation=45)
    
    # Add Note about Data Source
    plt.figtext(0.5, 0.01, "Source: Market Narrative & Media Reports (Estimated Values)", 
                ha="center", fontsize=10, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig('the_exodus_chart.png')
    print("\nChart saved to the_exodus_chart.png")

if __name__ == "__main__":
    DATA_PATH = "/home/pluto2477/Documents/2025-Economics-Academic-Festival/resource/data/exodus_factors.csv"
    
    print("--- Visualizing 'The Exodus' ---")
    plot_exodus_factors(DATA_PATH)
