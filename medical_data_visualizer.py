import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('/Users/wenjingli/Desktop/DESK/medical_examination.csv')

df['BMI'] = df['weight']/((df['height']/100)**2)

# Add 'overweight' column
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
#df['value'] = df.apply(lambda row:0 if row['gluc']==1 or row['cholesterol']==1 else 1,axis = 1)

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x==1 else 1)

df['gluc']= df['gluc'].apply(lambda x:0 if x==1 else 1)
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df,id_vals = 'cardio',value_vals = ['active','alco','cholesterol','gluc','overweight','smoke'])




    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    

    # Draw the catplot with 'sns.catplot()'
  g = sns.catplot(df_cat,x='variable',hue='value',kind='count',col='cardio',height = 4,aspect=1)
  g.set_xlabels('Categorical Features')
  g.set_ylables('Total')
  plt.tight_layout()
  plt.show()

    # Get the figure for the output
  fig = g


    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo']<=df['ap_hi']) & 
             (df['height']>=df['height'].quantile(0.025)) &
             (df['height']<=df['height'].quantile(0.975)) &
             (df['weight']<=df['weight'].quantile(0.975)) &
             (df['weight']>=df['weight'].quantile(0.025))]

    # Calculate the correlation matrix
    corr = df_heat.corr()
  

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr,type = bool))



    # Set up the matplotlib figure
    fig = sns.heatmap(corr,annot = True, fmt = '.1f', mask = mask)

    # Draw the heatmap with 'sns.heatmap()'
    plt.show()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
