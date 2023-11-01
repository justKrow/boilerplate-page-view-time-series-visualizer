import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
data = pd.read_csv('fcc-forum-pageviews.csv')
df = pd.DataFrame(data)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.985))]
df.loc[:, 'date'] = pd.to_datetime(df['date'])


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(20, 5))
    plt.plot(df["date"], df["value"], color = 'r', linewidth = 1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    fig = plt.figure(figsize=(20, 5))
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.loc[:, 'year'] = [d.year for d in df_bar.date]
    df_bar.loc[:, 'month'] = [d.strftime('%b') for d in df_bar.date]
    groupedData = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    ax = groupedData.plot(kind = 'bar')
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    plt.legend(title='Months')
    fig = plt.figure(figsize=(10, 6))
    plt.show()
    df_bar = df_bar.drop(columns=['year', 'month'])

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
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    ax1 = sns.boxplot(data = df_box, x = 'year', y = 'month', ax = axes[0])
    ax1.set(title = 'Year-wise Box Plot (Trend)')

    ax2 = sns.boxplot(data = df_box, x = 'year', y = 'month', ax = axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set(title = 'Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
