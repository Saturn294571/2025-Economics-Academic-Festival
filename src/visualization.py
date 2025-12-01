import matplotlib.pyplot as plt
import numpy as np

def plot_is_lm_bp():
    """
    Plot the IS-LM-BP diagram illustrating Fiscal Dominance and Risk Premium Shock.
    """
    # Define grid
    Y = np.linspace(0, 100, 100)
    
    # Define Curves (Linear approximations)
    # IS: r = A - bY
    # LM: r = C + dY
    # BP: r = r_world + theta + eY (Slight slope for imperfect mobility)
    
    # Initial State (0)
    IS_0 = 10 - 0.1 * Y
    LM_0 = 0 + 0.1 * Y
    BP_0 = 5 + 0.0 * Y # Perfect mobility initially, r* = 5
    
    # Shock 1: Fiscal Expansion (IS shifts Right)
    # IS: r = (A+dA) - bY
    IS_1 = 14 - 0.1 * Y
    
    # Shock 2: Monetary Accommodation (Rate Fixed / Fiscal Dominance)
    # LM shifts Right to keep r constant at the new IS intersection?
    # Or simply LM stays fixed and r rises? 
    # Paper says: "LM moves LM0 -> LM1 (abnormally)" to fix rate.
    # Let's say target rate is around 5.
    # Intersection of IS_0 and LM_0 is at Y=50, r=5.
    # Intersection of IS_1 and LM_0 would be at Y=70, r=7.
    # To keep r=5, LM must shift to intersect IS_1 at r=5.
    LM_1 = -2 + 0.1 * Y # Shifts right
    
    # Shock 3: Risk Premium Explosion (BP shifts Up)
    # BP: r = r_world + theta
    BP_1 = 8 + 0.0 * Y # Theta shock = +3
    
    # Plotting
    plt.figure(figsize=(10, 8))
    
    # Draw Curves
    plt.plot(Y, IS_0, 'b-', label='IS0 (Initial)', alpha=0.6)
    plt.plot(Y, IS_1, 'b--', label='IS1 (Fiscal Expansion)', linewidth=2)
    
    plt.plot(Y, LM_0, 'g-', label='LM0', alpha=0.6)
    plt.plot(Y, LM_1, 'g--', label='LM1 (Rate Fixed)', linewidth=2)
    
    plt.plot(Y, BP_0, 'k-', label='BP0 (r*)', alpha=0.6)
    plt.plot(Y, BP_1, 'r-', label='BP1 (r* + Risk)', linewidth=2)
    
    # Mark Equilibrium Points
    # E0: Initial
    plt.plot(50, 5, 'ko', markersize=8)
    plt.text(50, 5.2, '$E_0$', fontsize=12)
    
    # E1: Fiscal Dominance Equilibrium (IS1 meets LM1)
    # IS1 (14 - 0.1Y) = LM1 (-2 + 0.1Y) -> 16 = 0.2Y -> Y = 80. r = 6.
    # Wait, 14 - 8 = 6. -2 + 8 = 6. So r=6.
    # Let's adjust LM1 to make r=5 exactly? 
    # If r=5, IS1: 5 = 14 - 0.1Y -> 0.1Y = 9 -> Y=90.
    # LM1 passing through (90, 5): 5 = C + 9 -> C = -4.
    LM_fixed = -4 + 0.1 * Y
    plt.plot(Y, LM_fixed, 'g--', linewidth=2) # Overwrite LM1
    
    plt.plot(90, 5, 'bo', markersize=8)
    plt.text(90, 5.2, '$E_{Fiscal}$', fontsize=12, color='blue')
    
    # Gap Analysis
    # At E_Fiscal (Y=90, r=5), where is BP1?
    # BP1 is at r=8.
    # Gap = 8 - 5 = 3 (Capital Outflow Pressure)
    plt.annotate('', xy=(90, 8), xytext=(90, 5),
                 arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    plt.text(91, 6.5, 'Capital Outflow\nGap', color='red')
    
    # Styling
    plt.title('IS-LM-BP Model: Fiscal Dominance & Risk Premium Shock', fontsize=16)
    plt.xlabel('National Income (Y)', fontsize=12)
    plt.ylabel('Interest Rate (r)', fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.ylim(0, 12)
    plt.xlim(0, 100)
    
    # Save
    plt.savefig('is_lm_bp_diagram.png')
    print("Diagram saved to is_lm_bp_diagram.png")

if __name__ == "__main__":
    plot_is_lm_bp()
