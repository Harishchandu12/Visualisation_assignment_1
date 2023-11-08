# import library
import matplotlib.pyplot as plt
import pandas as pd
import inspect
import os.path


# get current dir
def get_file_path():
    """
    This function returns the current path directory
    """
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    return path

# link for kaggle dataset : https://www.kaggle.com/datasets/shariful07/nice-work-thanks-for-share
# read csv
input_path = str(get_file_path())+r"\University_Students_Monthly_Expenses.csv"

# add csv file to dataframe
df_monthly_expenses = pd.read_csv(input_path)

# sum of monthly expenses as avg_expenses per year
df_agg_expenses = df_monthly_expenses.groupby(
    ['Study_year'])['Monthly_expenses_$'].mean().astype(int).reset_index(name='avg_expenses')

x = df_agg_expenses['Study_year']
y = df_agg_expenses['avg_expenses']


# Create a bar graph
plt.bar(x, y, align='center', alpha=0.7, color='b')

plt.xticks(x)

# Add labels and title
plt.xlabel('Study Year', fontsize=12)
plt.ylabel('Average Expenses', fontsize=12)
plt.title('Student Average Expenses by Study Year', fontsize=15)

# To display the plot
plt.show()
