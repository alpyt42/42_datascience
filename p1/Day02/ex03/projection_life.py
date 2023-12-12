import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

import numpy as np

def convert_k_m_to_number(value):
    if isinstance(value, str):  # Check if the value is a string
        value = value.strip()  # Trim whitespace
        if re.match(r'^\d+\.?\d*k$', value.lower()):  # Match digit(s) followed by 'k'
            return float(value[:-1]) * 1e3
        elif re.match(r'^\d+\.?\d*m$', value.lower()):  # Match digit(s) followed by 'M'
            return float(value[:-1]) * 1e6
        else:
            return float(value)
    return value

def plot_projection_life(income_1900, life_expectancy_1900):
    # Merge the datasets on the country column
    print('Dataset before merging:')
    print('income_1900:')
    print(income_1900)
    print('life_expectancy_1900:')
    print(life_expectancy_1900)
    merged_data = pd.merge(income_1900, life_expectancy_1900, on='country', )
    print('Dataset after merging:')
    print(merged_data)
    # Filter data for the year 1900 and remove NaN values
    res = merged_data.apply(convert_k_m_to_number).dropna()
    print(pd.concat([
        res[res['country'] == 'Mongolia'],
        res[res['country'] == 'Micronesia, Fed. Sts.'],
        res[res['country'] == 'Denmark']
    ]))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['1900_x'], merged_data['1900_y'])  # Assuming 1900_x is GNP, 1900_y is life expectancy
    plt.xscale('log')

     # Set custom ticks
    tick_values = [300, 1000, 10000]  # You can add more tick values here
    plt.xticks(tick_values, [str(value) for value in tick_values])

    plt.title("Life Expectancy vs GNP in 1900")
    plt.xlabel("GNP (PPP, Inflation Adjusted)")
    plt.ylabel("Life Expectancy (years)")
    plt.show()