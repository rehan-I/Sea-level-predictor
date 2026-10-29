import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_full = pd.Series(range(1880, 2051))
    ax.plot(years_full, full.intercept + full.slope * years_full, 'r')

    recent = df[df['Year'] >= 2000]
    recent_fit = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, recent_fit.intercept + recent_fit.slope * years_recent, 'g')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()
