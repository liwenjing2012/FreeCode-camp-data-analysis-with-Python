import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/Users/wenjingli/Desktop/fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])

# Clean data
df = df[(df['value']>= df['value'].quantile(0.025)) & 
        (df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylable('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    year_month_formatter = mdates.DateFormatter("%Y-%m")
    half_year_locator = mdates.MonthLocator(interval=6)
    ax.xaxis.set_major_locator(half_year_locator) 
    ax.xaxis.set_major_formatter(year_month_formatter)
    ax.plot(df['date'], df['value'])
    





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()
    monthly_mean = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()
    fig = sns.catplot(monthly_mean,x='year',y= 'value',hue = 'month',kind='bar')
  

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
