import numpy as np
import matplotlib.pyplot as plt

class SupplyDemandModel:
    def __init__(self, demand_intercept, demand_slope, supply_intercept, supply_slope):
        """
        Initializes the Supply and Demand model with linear functions.
        Demand: Qd = a - bP (a: demand_intercept, b: demand_slope)
        Supply: Qs = c + dP (c: supply_intercept, d: supply_slope)
        """
        self.a = demand_intercept
        self.b = demand_slope
        self.c = supply_intercept
        self.d = supply_slope
        
        # Current supply parameters (can be modified by shifts)
        self.current_c = self.c
        self.current_d = self.d

    def calculate_equilibrium(self):
        """
        Calculates the market equilibrium price (P*) and quantity (Q*).
        Equilibrium condition: Qd = Qs
        a - bP = c + dP
        a - c = (b + d)P
        P* = (a - c) / (b + d)
        """
        if self.b + self.current_d == 0:
            raise ValueError("Slopes are invalid, lines are parallel.")
            
        p_star = (self.a - self.current_c) / (self.b + self.current_d)
        q_star = self.a - self.b * p_star
        return p_star, q_star

    def apply_price_ceiling(self, price_cap):
        """
        Calculates Quantity Demanded (Qd), Quantity Supplied (Qs), and Excess Demand
        under a price ceiling.
        """
        q_d = self.a - self.b * price_cap
        q_s = self.current_c + self.current_d * price_cap
        
        excess_demand = q_d - q_s
        return q_d, q_s, excess_demand

    def shift_supply_curve(self, shift_amount, shift_type='intercept'):
        """
        Shifts the supply curve.
        shift_amount: The amount to shift.
        shift_type: 'intercept' to change the intercept (c), 'slope' to change the slope (d).
        Negative shift_amount for intercept implies a decrease in supply (shift left).
        """
        if shift_type == 'intercept':
            self.current_c += shift_amount
        elif shift_type == 'slope':
            self.current_d += shift_amount
        else:
            raise ValueError("Invalid shift_type. Use 'intercept' or 'slope'.")

    def calculate_deadweight_loss(self, price_cap):
        """
        Calculates the Deadweight Loss (DWL) caused by the price ceiling.
        DWL is the area of the triangle between the supply and demand curves,
        bounded by the quantity supplied at the price cap and the equilibrium quantity.
        """
        p_star, q_star = self.calculate_equilibrium()
        
        # If price cap is above equilibrium, no binding constraint, no DWL
        if price_cap >= p_star:
            return 0.0

        # Quantity supplied at price cap
        q_s_cap = self.current_c + self.current_d * price_cap
        
        # Price on the demand curve at q_s_cap (Willingness to Pay)
        # Qd = a - bP => P = (a - Qd) / b
        p_demand_at_qs = (self.a - q_s_cap) / self.b
        
        # DWL = 0.5 * (P_demand - P_supply) * (Q_star - Q_s_cap)
        # Note: At Q_s_cap, the supply price is the price_cap itself (or lower if we consider the curve)
        # Actually, it's the area between Demand and Supply curves from Q_s_cap to Q_star.
        # Height of triangle at Q_s_cap = P_demand_at_qs - P_supply_at_qs
        # P_supply_at_qs is simply the price_cap (since Qs is determined by price_cap on supply curve)
        # Wait, P_supply_at_qs is the price on the supply curve that corresponds to Q_s_cap.
        # Since Q_s_cap = c + d * price_cap, the price IS price_cap.
        
        height = p_demand_at_qs - price_cap
        base = q_star - q_s_cap
        
        dwl = 0.5 * height * base
        return dwl

    def reset_supply(self):
        """Resets the supply curve to initial parameters."""
        self.current_c = self.c
        self.current_d = self.d
