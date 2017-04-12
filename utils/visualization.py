'''
Some functions are used to visualize data. 
Note: We use date as index to access rows of dataframe. Date is arranged in chronological order.
'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


def normalize_data(df):
    """Normalize data before plotting to scale all stock prices"""
    return df/df.ix[0,:]


def plot_data(df, title="Stock prices", save_figure=False, file_name="./default.png"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    if save_figure:
        plt.savefig(file_name)
    plt.show()


def plot_selected(df, columns, start_index, end_index, save_figure=False, file_name="./default.png"):
    """Plot the desired columns over index values in the given range."""
    df_selected = df.ix[start_index: end_index, columns]
    return plot_data(df_selected, title='Selected stock prices', save_figure=save_figure, file_name=file_name)

def plot_hist(df, save_figure=False, file_name="./default.png"):
    df['Daily_return'].hist(bins=20)
    mean = df['Daily_return'].mean()
    std = df['Daily_return'].std()
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    if save_figure:
        plt.savefig(file_name)
    plt.show()


def risk_reward_portfolio(ticker_1, ticker_2, norm_data, save_figure=False,  file_name="./default.png"):
    spaced_samples = np.linspace(0, 1, 100, endpoint=False)
    portfolio = pd.DataFrame({
    'reward': pd.Series([(r*norm_data[ticker_1] + (1-r)*norm_data[ticker_2]).pct_change().mean() for r in spaced_samples], index=spaced_samples),
    'risk': pd.Series([(r*norm_data[ticker_1] + (1-r)*norm_data[ticker_2]).pct_change().std() for r in spaced_samples], index=spaced_samples)
})

    ax = portfolio.plot(secondary_y='risk')
    ax.set_xlabel('Percent of portfolio in ' + str(ticker_1))
    ax.set_ylabel('Mean of daily percent change')
    ax.right_ax.set_ylabel('Standard deviation of daily percent change')
    plt.title(str(ticker_1) + ' vs. ' + str(ticker_2) + ' : Reward and Risk')
    if save_figure:
        plt.savefig(file_name)
    plt.show()

def optimal_portfolio(ticker_1, ticker_2, norm_data, save_figure=False,  file_name="./default.png"):
    spaced_samples = np.linspace(0, 1, 100, endpoint=False)
    portfolio = pd.DataFrame({
    'reward': pd.Series([(r*norm_data[ticker_1] + (1-r)*norm_data[ticker_2]).pct_change().mean() for r in spaced_samples], index=spaced_samples),
    'risk': pd.Series([(r*norm_data[ticker_1] + (1-r)*norm_data[ticker_2]).pct_change().std() for r in spaced_samples], index=spaced_samples)
})
    reward_over_risk = portfolio.reward/portfolio.risk
    reward_over_risk.plot()
    max_port = reward_over_risk.argmax()
    plt.xlabel('Percent of portfolio in ' + str(ticker_1) + ' | Portfolio: ' + str(max_port))
    plt.ylabel('Reward/Risk')
    if save_figure:
        plt.savefig(file_name)
    plt.show()

def plot_stock_data(df):
    plt.figure(figsize=(12,15)) 
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1, sharex=ax1)
    ax1.plot(df.index, df['Adj_close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])
    plt.show()