import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
pageview_filepath  = 'fcc-forum-pageviews.csv'
df = pd.read_csv(pageview_filepath, parse_dates=['date'], index_col='date')

# Clean data
# Filter out the top 2.5% and bottom 2.5% of the dataset 
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():

    fig, ax = plt.subplots(figsize=(20, 10))
    plt.plot(df, label='lineplots', color='r', linewidth=1.0)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy() 
    df_bar['year'] = df_bar.index.year 
    df_bar['month'] = df_bar.index.month 
    # Group the data by year and month and calculate the average page views 
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack() 
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 7)) 
    df_grouped.plot(kind='bar', ax=ax, cmap='tab20') 
    # Set the title and labels 
    ax.set_title('Average Daily Page Views per Month (Grouped by Year)') 
    ax.set_xlabel('Years') 
    ax.set_ylabel('Average Page Views') 
    # Customize the legend 
    ax.legend(title='Months', labels=[ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    #df_box['month_num'] = df_box['date'].dt.month 
    #df_box = df_box.sort_values('month_num')

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5)) 
    # Year-wise Box Plot (Trend) 
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], orientation='vertical') 
    axes[0].set_title('Year-wise Box Plot (Trend)') 
    axes[0].set_xlabel('Year') 
    axes[0].set_ylabel('Page Views') 
    # Month-wise Box Plot (Seasonality) 
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=['Jan','Feb','Mar','Apr','May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']) 
    axes[1].set_title('Month-wise Box Plot (Seasonality)') 
    axes[1].set_xlabel('Month') 
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
