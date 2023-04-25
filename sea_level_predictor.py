import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('/Users/wenjingli/Desktop/epa-sea-level.csv')


    # Create scatter plot
  plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
  plt.title('Scatter plot')
  plt.xlabel('Year')
  plt.ylabel('CSIRO Adjusted Sea Level')
  plt.show()


    # Create first line of best fit
  slope, intercept,r_value,p_value,std_err = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
  plt.plot(df['Year'], intercept + slope*df['Year'], color='red', label='Best Fit Line')

    # Create second line of best fit
  new_year = range(2000,2050,1)
  plt.plot(new_year, intercept + slope*new_year,   color='red', label='2nd Best Fit Line')
  

    # Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('CSIRO Adjusted Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()